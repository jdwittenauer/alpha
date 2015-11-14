import urllib2
import Quandl
import pandas as pd
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy import sql
from zipfile import ZipFile


# TODO - finish update data function
# TODO - expand to bring in other data sets on the list


def load_sql_data(engine, table=None, query=None, index=None, date_columns=None):
    """
    Retrieves data from a SQL database and loads the data into a data frame.
    """
    if query is not None:
        data = pd.read_sql(query, engine, index_col=index, parse_dates=date_columns)
    else:
        data = pd.read_sql('SELECT * FROM ' + table, engine, index_col=index, parse_dates=date_columns)

    print('SQL data loaded successfully.')

    return data


def save_sql_data(engine, data, table, exists='append', index=True, index_label=None):
    """
    Writes data from a data frame to a SQL database table.
    """
    data.to_sql(table, engine, schema=None, if_exists=exists,
                index=index, index_label=index_label, chunksize=10000)

    print('SQL data written successfully.')


def test_api_calls(api_key):
    """
    Test function with examples of calls using the Quandl API via python wrapper.
    """
    data = Quandl.get('WIKI/AAPL', authtoken=api_key)
    data_new = Quandl.get('WIKI/AAPL', rows=5, sort_order='desc', authtoken=api_key)
    data_range = Quandl.get('WIKI/AAPL', trim_start='2015-01-01', trim_end='2015-01-01', authtoken=api_key)
    data_multiple = Quandl.get(['WIKI/AAPL', 'WIKI/MSFT'], authtoken=api_key)


def get_dataset_codes(directory, dataset, api_key):
    """
    Retrieve the unique list of codes for the provided data set.
    """
    # retrieve the zip file
    codes_url = 'https://www.quandl.com/api/v3/databases/{0}/codes?api_key={1}'.format(dataset, api_key)
    response = urllib2.urlopen(codes_url)
    output = open(directory + '{0}_codes.zip'.format(dataset), 'wb')
    output.write(response.read())
    output.close()

    # unzip and load the csv into pandas
    z = ZipFile(directory + '{0}_codes.zip'.format(dataset))
    codes = pd.read_csv(z.open('{0}-datasets-codes.csv'.format(dataset)))

    # convert to a list
    code_list = codes.iloc[:, 0].tolist()

    print('Code retrieval successful.')
    return code_list


def create_dataset_table(engine):
    """
    Creates a table to track the names and status of data sets being fetched online.
    """
    dataset_list = ['WIKI', 'RAYMOND', 'FRED', 'FED', 'USTREASURY', 'DOE']
    dataset_table = pd.DataFrame(dataset_list, columns=['Dataset'])
    dataset_table['Last Updated'] = datetime(1900, 1, 1)

    save_sql_data(engine, dataset_table, 'DATASETS', exists='replace', index=False)

    print('Dataset table creation complete.')


def create_dataset_code_table(engine, directory, dataset, api_key):
    """
    Map the list of codes contained in a data set to a data frame to be used
    """
    update_dataset = sql.text(
        'UPDATE DATASETS '
        'SET [Last Updated] = :updated '
        'WHERE [Dataset] = :dataset')
    conn = engine.connect()

    # retrieve the most updated list from the remote server
    code_list = get_dataset_codes(directory, dataset, api_key)

    # strip off the data set name
    code_offset = len(dataset) + 1
    code_list_stripped = code_list.map(lambda x: x[code_offset:])

    # create a new frame with the dataset, codes, and placeholder columns for metadata
    code_table = pd.DataFrame(code_list_stripped, columns=['Code'])
    code_table['API Code'] = code_list
    code_table['Start Date'] = datetime(1900, 1, 1)
    code_table['End Date'] = datetime(1900, 1, 1)
    code_table['Last Updated'] = datetime(1900, 1, 1)
    code_table = code_table[['Code', 'API Code', 'Start Date', 'End Date', 'Last Updated']]

    save_sql_data(engine, code_table, dataset + '_CODES', exists='replace', index=False)

    # update the dataset table to show that the code table was created
    conn.execute(update_dataset, updated=datetime.now(), dataset=dataset)

    print('Code table creation complete.')


def load_historical_data(engine, dataset, api_key):
    """
    Creates a new data table for the provided data set and loads historical data for each code into the table.
    """
    update_code = sql.text(
        'UPDATE ' + dataset + '_CODES '
        'SET [Start Date] = :start, [End Date] = :end, [Last Updated] = :updated '
        'WHERE Code = :code')
    conn = engine.connect()

    # retrieve the current code table
    code_table = load_sql_data(engine, dataset + '_CODES', date_columns=['Start Date', 'End Date', 'Last Updated'])

    # fetch the first code's data to create the data frame
    data = Quandl.get(code_table['API Code'].iloc[0], rows=1, authtoken=api_key)
    data['Code'] = code_table['Code'].iloc[0]
    data['Date'] = data['Date'].convert_objects(convert_dates='coerce')
    data = data.iloc[0:0]

    # iterate over each code and append the returned data
    for row in code_table.iterrows():
        code_data = Quandl.get(row['API Code'], authtoken=api_key)
        code_data['Code'] = row['Code']
        code_data['Date'] = code_data['Date'].convert_objects(convert_dates='coerce')
        data = pd.concat([data, code_data])

        # update the code table
        min_date = min(code_data['Date'])
        max_date = max(code_data['Date'])
        current_date = datetime.now()
        conn.execute(update_code, start=min_date, end=max_date, updated=current_date, code=row['Code'])

    # move the code column to the beginning
    columns = data.columns.tolist()
    columns = [columns[-1]] + columns[:-1]
    data = data[columns]

    save_sql_data(engine, data, dataset, exists='replace', index=False)

    print('Historical data loaded successfully.')


def update_dataset_codes(engine, directory, dataset, api_key):
    """
    Updates the list of codes for a data set and pulls in historical data for new codes.
    """
    select_code = sql.text('SELECT 1 FROM ' + dataset + '_CODES WHERE [Code] = :code')
    insert_code = sql.text('INSERT INTO ' + dataset + '_CODES VALUES (:code, :api_code, :start, :end, :updated)')
    update_dataset = sql.text(
        'UPDATE DATASETS '
        'SET [Last Updated] = :updated '
        'WHERE [Dataset] = :dataset')
    conn = engine.connect()

    # retrieve the most updated list from the remote server
    code_list = get_dataset_codes(directory, dataset, api_key)
    code_offset = len(dataset) + 1

    # iterate over each code and check its status in the database
    for api_code in code_list:
        code = api_code[code_offset:]
        result = conn.execute(select_code, code=code)

        # if there was no result then the code is new and must be inserted
        if len(result) == 0:
            init_date = datetime(1900, 1, 1)
            conn.execute(insert_code, code=code, api_code=api_code, start=init_date, end=init_date, updated=init_date)

    # update the dataset table to reflect the fact that the code table was refreshed
    conn.execute(update_dataset, updated=datetime.now(), dataset=dataset)

    print('Code table updated successfully.')


def update_dataset_data(engine, dataset, api_key):
    """
    Updates data for each code in the data set, retrieving new entries since the last update.
    """
    update_code = sql.text(
        'UPDATE ' + dataset + '_CODES '
        'SET [Start Date] = :start, [End Date] = :end, [Last Updated] = :updated '
        'WHERE Code = :code')
    conn = engine.connect()

    # retrieve the current code table
    code_table = load_sql_data(engine, dataset + '_CODES', date_columns=['Start Date', 'End Date', 'Last Updated'])

    # fetch the first code's data to create the data frame
    data = Quandl.get(code_table['API Code'].iloc[0], rows=1, authtoken=api_key)
    data['Code'] = code_table['Code'].iloc[0]
    data['Date'] = data['Date'].convert_objects(convert_dates='coerce')
    data = data.iloc[0:0]

    # iterate over each code and append the returned data
    for row in code_table.iterrows():
        if row['Last Updated'] == datetime(1900, 1, 1):
            # this is a new code so we need to pull all historical data
            code_data = Quandl.get(row['API Code'], authtoken=api_key)
            code_data['Code'] = row['Code']
            code_data['Date'] = code_data['Date'].convert_objects(convert_dates='coerce')
            data = pd.concat([data, code_data])

            # update the code table
            min_date = min(code_data['Date'])
            max_date = max(code_data['Date'])
            current_date = datetime.now()
            conn.execute(update_code, start=min_date, end=max_date, updated=current_date, code=row['Code'])
        else:
            # incremental update from the current end date for the code
            print('TODO')

    # move the code column to the beginning
    columns = data.columns.tolist()
    columns = [columns[-1]] + columns[:-1]
    data = data[columns]

    save_sql_data(engine, data, dataset, exists='append', index=False)

    print('Code data updated successfully.')


def main():
    print('Fetching data...')

    directory = 'C:\\Users\\John\\Documents\\Data\\Alpha\\'
    db_connection = 'sqlite:///C:\\Users\\John\\Documents\\Data\\Alpha\\alpha.sqlite'
    api_key = 'SkQK_ZNrZn4cjfXxjJmb'

    engine = create_engine(db_connection)

    # initial load
    create_dataset_table(engine)
    create_dataset_code_table(engine, directory, 'WIKI', api_key)
    load_historical_data(engine, 'WIKI', api_key)

    # incremental updates
    update_dataset_codes(engine, directory, 'WIKI', api_key)
    update_dataset_data(engine, 'WIKI', api_key)

    print('Fetch complete.')


if __name__ == "__main__":
    main()

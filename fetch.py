import urllib2
import Quandl
import pandas as pd
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy import sql
from zipfile import ZipFile


# TODO - modify historical load to populate code table
# TODO - finish update codes function
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


def create_dataset_table(engine):
    """
    Creates a table to track the names and status of data sets being fetched online.
    """
    dataset_list = ['WIKI', 'RAYMOND', 'FRED', 'FED', 'USTREASURY', 'DOE']
    dataset_table = pd.DataFrame(dataset_list, columns=['Dataset'])
    dataset_table['Codes'] = 0
    dataset_table['Last Updated'] = datetime(1900, 1, 1)

    save_sql_data(engine, dataset_table, 'DATASETS', exists='replace', index=False)

    print('Dataset table construction complete.')

    return dataset_table


def get_database_codes(directory, dataset, api_key):
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

    print('Code retrieval complete.')

    return code_list


def create_dataset_code_table(engine, dataset, code_list):
    """
    Map the list of codes contained in a data set to a data frame to be used
    """
    # strip off the data set name
    code_offset = len(dataset) + 1
    code_list = code_list.map(lambda x: x[code_offset:])

    # create a new frame with the dataset, codes, and placeholder columns for metadata
    code_table = pd.DataFrame(code_list, columns=['Code'])
    code_table['Dataset'] = dataset
    code_table['Start Date'] = datetime(1900, 1, 1)
    code_table['End Date'] = datetime(1900, 1, 1)
    code_table['Last Updated'] = datetime(1900, 1, 1)
    code_table = code_table[['Dataset', 'Code', 'Start Date', 'End Date', 'Last Updated']]

    save_sql_data(engine, code_table, dataset + '_CODES', exists='replace', index=False)

    print('Code table construction complete.')

    return code_table


def load_historical_data(engine, dataset, code_list, api_key):
    """
    Creates a new data table for the provided data set and loads historical data for each code into the table.
    """
    # fetch the first code's data to create the data frame
    code_offset = len(dataset) + 1
    data = Quandl.get(code_list[0], rows=1, authtoken=api_key)
    data['Code'] = code_list[0][code_offset:]
    data = data.iloc[0:0]
    
    update_statement = sql.text(
        'UPDATE ' + dataset + '_CODES '
        'SET [Start Date] = :start, [End Date] = :end, [Last Updated] = :updated '
        'WHERE Dataset = :dataset')
    conn = engine.connect()

    # iterate over each code and append the returned data
    for code in code_list:
        code_data = Quandl.get(code, authtoken=api_key)
        code_data['Code'] = code[code_offset:]
        data = pd.concat([data, code_data])

        # update the code table
        min_date = min(code_data['Date'])
        max_date = max(code_data['Date'])
        current_date = datetime.now()
        conn.execute(update_statement, start=min_date, end=max_date, updated=current_date)

    # move the code column to the beginning
    columns = data.columns.tolist()
    columns = [columns[-1]] + columns[:-1]
    data = data[columns]
    data['Date'] = data['Date'].convert_objects(convert_dates='coerce')

    save_sql_data(engine, data, dataset, exists='replace', index=False)

    print('Historical data loaded successfully.')

    return data


def update_dataset_codes():
    """
    Updates the list of codes for a data set and pulls in historical data for new codes.
    """
    print('TODO')


def update_dataset_data():
    """
    Updates data for each code in the data set, retrieving new entries since the last update.
    """
    print('TODO')


def main():
    print('Fetching data...')

    directory = 'C:\\Users\\John\\Documents\\Data\\Alpha\\'
    db_connection = 'sqlite:///C:\\Users\\John\\Documents\\Data\\Alpha\\alpha.sqlite'
    api_key = 'SkQK_ZNrZn4cjfXxjJmb'

    engine = create_engine(db_connection)

    dataset_table = create_dataset_table(engine)
    code_list = get_database_codes(directory, 'WIKI', api_key)
    code_table = create_dataset_code_table(engine, 'WIKI', code_list)
    data = load_historical_data(engine, 'WIKI', code_list, api_key)

    print('Fetch complete.')


if __name__ == "__main__":
    main()

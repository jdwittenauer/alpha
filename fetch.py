import urllib2
import Quandl
import sqlite3
import pandas as pd
from zipfile import ZipFile


def load_sql_data(connection, table=None, query=None, index=None, date_columns=None):
    if query is not None:
        data = pd.read_sql(query, connection, index_col=index, parse_dates=date_columns)
    else:
        data = pd.read_sql('SELECT * FROM ' + table, connection, index_col=index, parse_dates=date_columns)

    print('SQL data loaded successfully.')

    return data


def save_sql_data(connection, data, table, exists='append', index=True, index_label=None):
    data.to_sql(table, connection, if_exists=exists, index=index, index_label=index_label, chunksize=10000)
    print('SQL data written successfully.')


def get_database_codes(directory, dataset, api_key):
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

    return codes, code_list


def fetch_historical_data(dataset, code_list, api_key):
    # fetch the first code's data to create the data frame
    code_offset = len(dataset) + 1
    data = Quandl.get(code_list[0], rows=1, authtoken=api_key)
    data['Code'] = code_list[0][code_offset:]
    data = data.iloc[0:0]

    # iterate over each code and append the returned data
    for code in code_list:
        code_data = Quandl.get(code, authtoken=api_key)
        code_data['Code'] = code[code_offset:]
        data = pd.concat([data, code_data])

    # move the code column to the beginning
    columns = data.columns.tolist()
    columns = [columns[-1]] + columns[:-1]
    data = data[columns]

    print('Historical data loaded successfully.')

    return data


def fetch_updated_data():
    print('TODO')


def main():
    print('Fetching data...')

    directory = 'C:\\Users\\John\\Documents\\Data\\Alpha\\'
    database_file = 'C:\\Users\\John\\Documents\\Data\\Alpha\\alpha.sqlite'
    conn = sqlite3.connect(database_file)

    # this is a unique key per Quandl account
    api_key = 'SkQK_ZNrZn4cjfXxjJmb'

    # API usage examples
    data = Quandl.get('WIKI/AAPL', authtoken=api_key)
    data_new = Quandl.get('WIKI/AAPL', rows=5, sort_order='desc', authtoken=api_key)
    data_range = Quandl.get('WIKI/AAPL', trim_start='2015-01-01', trim_end='2015-01-01', authtoken=api_key)
    data_multiple = Quandl.get(['WIKI/AAPL', 'WIKI/MSFT'], authtoken=api_key)

    # retrieve the unique list of codes
    codes, code_list = get_database_codes(directory, 'WIKI', api_key)
    save_sql_data(conn, codes, 'WIKI_CODES', exists='replace')

    # fetch data for the codes and save to the database
    historical_data = fetch_historical_data('WIKI', code_list, api_key)
    save_sql_data(conn, historical_data, 'WIKI', exists='replace')

    # read the data back into a data frame
    frame = load_sql_data(conn, table='WIKI')
    frame.head()

    conn.close()

    print('Fetch complete.')


if __name__ == "__main__":
    main()

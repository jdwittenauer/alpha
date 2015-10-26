import urllib2
import Quandl
import pandas as pd
from zipfile import ZipFile


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
    codes.to_csv(directory + '{0}_codes.csv'.format(dataset))

    # convert to a list
    code_list = codes.iloc[:, 0].tolist()

    return code_list


def fetch_historical_data(directory, dataset, code_list, api_key):
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

    # write file to disk
    data.to_csv(directory + '{0}_data.csv'.format(dataset))

    return data


def main():
    print('Fetching data...')

    directory = 'C:\\Users\\John\\Documents\\Data\\Alpha\\'

    # this is a unique key per Quandl account
    api_key = 'SkQK_ZNrZn4cjfXxjJmb'

    # API usage examples
    data = Quandl.get('WIKI/AAPL', authtoken=api_key)
    data_new = Quandl.get('WIKI/AAPL', rows=5, sort_order='desc', authtoken=api_key)
    data_range = Quandl.get('WIKI/AAPL', trim_start='2015-01-01', trim_end='2015-01-01', authtoken=api_key)
    data_multiple = Quandl.get(['WIKI/AAPL', 'WIKI/MSFT'], authtoken=api_key)

    code_list = get_database_codes(directory, 'WIKI', api_key)
    historical_data = fetch_historical_data(directory, 'WIKI', code_list[0:3], api_key)

    print('Fetch complete.')


if __name__ == "__main__":
    main()

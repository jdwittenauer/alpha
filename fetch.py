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


def main():
    print('Fetching data...')

    directory = 'C:\\Users\\John\\Documents\\Data\\Alpha\\'

    # this is a unique key per Quandl account
    api_key = 'SkQK_ZNrZn4cjfXxjJmb'

    data = Quandl.get('WIKI/AAPL', authtoken=api_key)
    data_new = Quandl.get('WIKI/AAPL', rows=5, sort_order='desc', authtoken=api_key)
    data_range = Quandl.get('WIKI/AAPL', trim_start='2015-01-01', trim_end='2015-01-01', authtoken=api_key)
    data_multiple = Quandl.get(['WIKI/AAPL', 'WIKI/MSFT'], authtoken=api_key)

    code_url = 'https://www.quandl.com/api/v3/databases/WIKI/codes?api_key=' + api_key
    code_list = get_database_codes(directory, 'WIKI', api_key)

    print('Fetch complete.')


if __name__ == "__main__":
    main()

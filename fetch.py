import Quandl


def main():
    print('Fetching data...')

    directory = 'C:\\Users\\John\\Documents\\Data\\Alpha\\'

    # this is a unique key per Quandl account
    api_key = 'SkQK_ZNrZn4cjfXxjJmb'

    data = Quandl.get('WIKI/AAPL', authtoken=api_key)
    data_new = Quandl.get('WIKI/AAPL', rows=5, sort_order='desc', authtoken=api_key)
    data_range = Quandl.get('WIKI/AAPL', trim_start='2015-01-01', trim_end='2015-01-01', authtoken=api_key)
    data_multiple = Quandl.get(['WIKI/AAPL', 'WIKI/MSFT'], authtoken=api_key)

    # doesn't work
    codes = Quandl.get('databases/WIKI/codes', authtoken=api_key)

    print('Fetch complete.')


if __name__ == "__main__":
    main()

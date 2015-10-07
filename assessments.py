def calc_price_earnings_ratio(price_per_share, earnings_per_share):
    return float(price_per_share) / float(earnings_per_share)


def calc_market_capitalization(price_per_share, shares_outstanding):
    return price_per_share * shares_outstanding


def calc_stockholder_equity(total_assets, total_liabilities):
    return total_assets - total_liabilities


def calculate_book_value(stockholder_equity, goodwill, intangible_assets, other_long_term_assets):
    return stockholder_equity - goodwill - intangible_assets - other_long_term_assets


def calc_operating_income(revenue, cost_of_goods_sold, operating_expenses):
    return revenue - cost_of_goods_sold - operating_expenses


def calc_EBIT(operating_income, non_operating_income):
    return operating_income + non_operating_income


def calc_debt(short_term_debt, long_term_debt):
    return short_term_debt + long_term_debt


def calc_excess_cash(total_cash, current_liabilities, current_assets):
    return total_cash - max(current_liabilities - current_assets, 0)


def calc_enterprise_value(market_capitalization, debt, excess_cash):
    return max(market_capitalization + debt - excess_cash, 1)


def calc_earnings_yield(EBIT, depreciation, capital_expenditures, enterprise_value):
    return float(EBIT + (depreciation - capital_expenditures)) / float(enterprise_value)


def calc_net_fixed_assets(plant_performance_equipment, accumulated_depreciation):
    return plant_performance_equipment - accumulated_depreciation


def calc_working_capital(current_assets, current_liabilities, excess_cash):
    return max(current_assets - current_liabilities - excess_cash, 0)


def calc_return_on_capital(operating_income, net_fixed_assets, working_capital):
    return float(operating_income) / float(net_fixed_assets + working_capital)


def calc_return_on_assets(net_income, total_assets):
    return float(net_income) / float(total_assets)


def calc_return_on_equity(net_income, stockholder_equity):
    return float(net_income) / float(stockholder_equity)


def calc_free_cash_flow(operating_cash_flow, capital_expenditures, depreciation):
    return operating_cash_flow - min(capital_expenditures, depreciation)


def calc_free_cash_flow_yield(free_cash_flow, shares_outstanding, price_per_share):
    return (float(free_cash_flow) / float(shares_outstanding)) / price_per_share


def calc_NCAV_per_share(current_assets, total_liabilities, shares_outstanding):
    return float(max(current_assets - total_liabilities, 1)) / float(shares_outstanding)


def calc_NCAV_ratio(price_per_share, NCAV_per_share):
    return float(price_per_share) / float(NCAV_per_share)


def main():
    # TODO
    # Add growth
    # Add other ratios/metrics

    print('Analysis for Apple (2014)...')

    # Market
    price_per_share = 110.78

    # Income Statement
    revenue = 182795
    cost_of_goods_sold = 112258
    operating_expenses = 18034
    non_operating_income = 1364
    net_income = 39510
    earnings_per_share = 6.45
    shares_outstanding = 6123

    # Balance Sheet
    total_cash = 25077
    current_assets = 68531
    plant_performance_equipment = 39015
    accumulated_depreciation = 18391
    goodwill = 4616
    intangible_assets = 4179
    other_long_term_assets = 5146
    total_assets = 231839
    short_term_debt = 6308
    current_liabilities = 63448
    long_term_debt = 28987
    total_liabilities = 120292

    # Cash Flow
    depreciation = 7946
    operating_cash_flow = 59713
    capital_expenditures = 9813

    price_earnings_ratio = calc_price_earnings_ratio(price_per_share, earnings_per_share)
    print('Price/Earnings Ratio = ' + str(price_earnings_ratio))

    market_capitalization = calc_market_capitalization(price_per_share, shares_outstanding)
    print('Market Capitalization = ' + str(market_capitalization))

    stockholder_equity = calc_stockholder_equity(total_assets, total_liabilities)
    print('Stockholder Equity = ' + str(stockholder_equity))

    book_value = calculate_book_value(stockholder_equity, goodwill, intangible_assets, other_long_term_assets)
    print('Book Value = ' + str(book_value))

    operating_income = calc_operating_income(revenue, cost_of_goods_sold, operating_expenses)
    EBIT = calc_EBIT(operating_income, non_operating_income)
    print('EBIT = ' + str(EBIT))

    debt = calc_debt(short_term_debt, long_term_debt)
    excess_cash = calc_excess_cash(total_cash, current_liabilities, current_assets)
    enterprise_value = calc_enterprise_value(market_capitalization, debt, excess_cash)
    print('Enterprise Value = ' + str(enterprise_value))

    earnings_yield = calc_earnings_yield(EBIT, depreciation, capital_expenditures, enterprise_value)
    print('Earnings Yield = ' + str(earnings_yield))

    net_fixed_assets = calc_net_fixed_assets(plant_performance_equipment, accumulated_depreciation)
    print('Net Fixed Assets = ' + str(net_fixed_assets))

    working_capital = calc_working_capital(current_assets, current_liabilities, excess_cash)
    print('Working Capital = ' + str(working_capital))

    return_on_capital = calc_return_on_capital(operating_income, net_fixed_assets, working_capital)
    print('Return On Capital = ' + str(return_on_capital))

    return_on_assets = calc_return_on_assets(net_income, total_assets)
    print('Return On Assets = ' + str(return_on_assets))

    return_on_equity = calc_return_on_equity(net_income, stockholder_equity)
    print('Return On Equity = ' + str(return_on_equity))

    free_cash_flow = calc_free_cash_flow(operating_cash_flow, capital_expenditures, depreciation)
    print('Free Cash Flow = ' + str(free_cash_flow))

    free_cash_flow_yield = calc_free_cash_flow_yield(free_cash_flow, shares_outstanding, price_per_share)
    print('Free Cash Flow Yield = ' + str(free_cash_flow_yield))

    NCAV_per_share = calc_NCAV_per_share(current_assets, total_liabilities, shares_outstanding)
    print('NCAV Per Share = ' + str(NCAV_per_share))

    NCAV_ratio = calc_NCAV_ratio(price_per_share, NCAV_per_share)
    print('NCAV Ratio = ' + str(NCAV_ratio))

    print('Analysis complete.')


if __name__ == "__main__":
    main()

def calc_market_capitalization(price_per_share, total_shares_outstanding):
    return price_per_share * total_shares_outstanding


def calc_stockholder_equity(total_assets, total_liabilities):
    return total_assets - total_liabilities


def calc_book_value(stockholder_equity, goodwill, intangible_assets, other_long_term_assets):
    return stockholder_equity - goodwill - intangible_assets - other_long_term_assets


def calc_operating_income(revenue, cost_of_goods_sold, operating_expenses):
    return revenue - cost_of_goods_sold - operating_expenses


def calc_EBIT(operating_income, non_operating_income):
    return operating_income + non_operating_income


def calc_earnings(EBIT, depreciation, capital_expenditures):
    return EBIT + (depreciation - capital_expenditures)


def calc_debt(short_term_debt, long_term_debt):
    return short_term_debt + long_term_debt


def calc_preferred_value(total_shares_outstanding, basic_shares_outstanding, price_per_share):
    return (total_shares_outstanding - basic_shares_outstanding) * price_per_share


def calc_excess_cash(total_cash, current_liabilities, current_assets):
    return total_cash - max(current_liabilities - current_assets, 0)


def calc_enterprise_value(market_capitalization, debt, preferred_shares_value, excess_cash):
    return max(market_capitalization + debt + preferred_shares_value - excess_cash, 1)


def calc_earnings_yield(earnings, enterprise_value):
    return float(earnings) / float(enterprise_value)


def calc_net_fixed_assets(total_assets, current_assets, goodwill, intangible_assets, other_long_term_assets):
    return total_assets - current_assets - goodwill - intangible_assets - other_long_term_assets


def calc_working_capital(current_assets, current_liabilities, short_term_debt, excess_cash):
    return max(current_assets - (current_liabilities - short_term_debt) - excess_cash, 0)


def calc_invested_capital(stockholder_equity, debt):
    return stockholder_equity + debt


def calc_return_on_equity(net_income, stockholder_equity):
    return float(net_income) / float(stockholder_equity)


def calc_return_on_assets(net_income, total_assets):
    return float(net_income) / float(total_assets)


def calc_return_on_capital(earnings, net_fixed_assets, working_capital):
    return float(earnings) / float(net_fixed_assets + working_capital)


def calc_return_on_invested_capital(earnings, invested_capital):
    return float(earnings) / float(invested_capital)


def calc_free_cash_flow(operating_cash_flow, capital_expenditures, depreciation):
    return operating_cash_flow - min(capital_expenditures, depreciation)


def calc_free_cash_flow_yield(free_cash_flow, enterprise_value):
    return float(free_cash_flow) / float(enterprise_value)


def calc_cash_return_on_capital(free_cash_flow, net_fixed_assets, working_capital):
    return float(free_cash_flow) / float(net_fixed_assets + working_capital)


def calc_cash_return_on_invested_capital(free_cash_flow, invested_capital):
    return float(free_cash_flow) / float(invested_capital)


def calc_dividend_yield(dividends_paid, total_shares_outstanding, price_per_share):
    return (float(dividends_paid) / float(total_shares_outstanding)) / price_per_share


def calc_price_earnings_ratio(price_per_share, earnings_per_share):
    return float(price_per_share) / float(earnings_per_share)


def calc_annual_growth_rate(starting_value, final_value, n_years):
    return ((float(final_value) / float(starting_value)) ** (float(1) / n_years)) - 1


def calc_price_earnings_to_growth_ratio(price_earnings_ratio, annual_growth_rate):
    return float(price_earnings_ratio) / (float(annual_growth_rate) * 100)


def calc_price_to_book_ratio(market_capitalization, book_value):
    return float(market_capitalization) / float(book_value)


def calc_NCAV_per_share(current_assets, total_liabilities, total_shares_outstanding):
    return float(max(current_assets - total_liabilities, 1)) / float(total_shares_outstanding)


def calc_NCAV_ratio(price_per_share, NCAV_per_share):
    return float(price_per_share) / float(NCAV_per_share)


def calc_bond_equity_earnings_yield_ratio(ten_year_treasury_yield, earnings_yield):
    return float(ten_year_treasury_yield) / float(earnings_yield)


def calc_owner_earnings():
    print('TODO')


def main():
    print('Analysis for Apple (2014)...')

    # Market
    beginning_net_income = 25922
    ending_net_income = 39510
    n_years = 3
    price_per_share = 110.78
    ten_year_treasury_yield = 0.0222
    institutional_ownership_ratio = 0.59

    # Income Statement
    revenue = 182795
    cost_of_goods_sold = 112258
    operating_expenses = 18034
    interest_expense = 384
    non_operating_income = 1364
    net_income = 39510
    earnings_per_share = 6.45
    basic_shares_outstanding = 6086
    total_shares_outstanding = 6123

    # Balance Sheet
    total_cash = 25077
    receivables = 17460
    inventories = 2111
    deferred_income_taxes = 4318
    other_current_assets = 19565
    current_assets = 68531
    plant_performance_equipment = 39015
    accumulated_depreciation = 18391
    equity_investment = 130162
    goodwill = 4616
    intangible_assets = 4179
    other_long_term_assets = 5146
    non_current_assets = 163308
    total_assets = 231839
    short_term_debt = 6308
    accounts_payable = 30196
    current_liabilities = 63448
    long_term_debt = 28987
    non_current_liabilities = 56844
    total_liabilities = 120292

    # Cash Flow
    depreciation = 7946
    stock_repurchased = 35253
    dividends_paid = 11126
    operating_cash_flow = 59713
    capital_expenditures = 9813

    market_capitalization = calc_market_capitalization(price_per_share, total_shares_outstanding)
    print('Market Capitalization = ' + str(market_capitalization))

    stockholder_equity = calc_stockholder_equity(total_assets, total_liabilities)
    print('Stockholder Equity = ' + str(stockholder_equity))

    book_value = calc_book_value(stockholder_equity, goodwill, intangible_assets, other_long_term_assets)
    print('Book Value = ' + str(book_value))

    operating_income = calc_operating_income(revenue, cost_of_goods_sold, operating_expenses)
    print('Operating Income = ' + str(operating_income))

    EBIT = calc_EBIT(operating_income, non_operating_income)
    print('EBIT = ' + str(EBIT))

    earnings = calc_earnings(EBIT, depreciation, capital_expenditures)
    print('Earnings = ' + str(earnings))

    debt = calc_debt(short_term_debt, long_term_debt)
    print('Debt = ' + str(debt))

    preferred_value = calc_preferred_value(total_shares_outstanding, basic_shares_outstanding, price_per_share)
    print('Preferred Value = ' + str(preferred_value))

    excess_cash = calc_excess_cash(total_cash, current_liabilities, current_assets)
    print('Excess Cash = ' + str(excess_cash))

    enterprise_value = calc_enterprise_value(market_capitalization, debt, preferred_value, excess_cash)
    print('Enterprise Value = ' + str(enterprise_value))

    earnings_yield = calc_earnings_yield(earnings, enterprise_value)
    print('Earnings Yield = ' + str(earnings_yield))

    net_fixed_assets = calc_net_fixed_assets(total_assets, current_assets, goodwill, intangible_assets, other_long_term_assets)
    print('Net Fixed Assets = ' + str(net_fixed_assets))

    working_capital = calc_working_capital(current_assets, current_liabilities, short_term_debt, excess_cash)
    print('Working Capital = ' + str(working_capital))

    invested_capital = calc_invested_capital(stockholder_equity, debt)
    print('Invested Capital = ' + str(invested_capital))

    return_on_equity = calc_return_on_equity(net_income, stockholder_equity)
    print('Return On Equity = ' + str(return_on_equity))

    return_on_assets = calc_return_on_assets(net_income, total_assets)
    print('Return On Assets = ' + str(return_on_assets))

    return_on_capital = calc_return_on_capital(earnings, net_fixed_assets, working_capital)
    print('Return On Capital = ' + str(return_on_capital))

    return_on_invested_capital = calc_return_on_invested_capital(earnings, invested_capital)
    print('Return On Invested Capital = ' + str(return_on_invested_capital))

    free_cash_flow = calc_free_cash_flow(operating_cash_flow, capital_expenditures, depreciation)
    print('Free Cash Flow = ' + str(free_cash_flow))

    free_cash_flow_yield = calc_free_cash_flow_yield(free_cash_flow, enterprise_value)
    print('Free Cash Flow Yield = ' + str(free_cash_flow_yield))

    cash_return_on_capital = calc_cash_return_on_capital(free_cash_flow, net_fixed_assets, working_capital)
    print('Cash Return On Capital = ' + str(cash_return_on_capital))

    cash_return_on_invested_capital = calc_cash_return_on_invested_capital(free_cash_flow, invested_capital)
    print('Cash Return On Invested Capital = ' + str(cash_return_on_invested_capital))

    dividend_yield = calc_dividend_yield(dividends_paid, total_shares_outstanding, price_per_share)
    print('Dividend Yield = ' + str(dividend_yield))

    price_earnings_ratio = calc_price_earnings_ratio(price_per_share, earnings_per_share)
    print('Price/Earnings Ratio = ' + str(price_earnings_ratio))

    annual_growth_rate = calc_annual_growth_rate(beginning_net_income, ending_net_income, n_years)
    print('Annual Growth Rate = ' + str(annual_growth_rate))

    price_earnings_to_growth_ratio = calc_price_earnings_to_growth_ratio(price_earnings_ratio, annual_growth_rate)
    print('Price/Earnings To Growth Ratio = ' + str(price_earnings_to_growth_ratio))

    price_to_book_ratio = calc_price_to_book_ratio(market_capitalization, book_value)
    print('Price To Book Ratio = ' + str(price_to_book_ratio))

    NCAV_per_share = calc_NCAV_per_share(current_assets, total_liabilities, total_shares_outstanding)
    NCAV_ratio = calc_NCAV_ratio(price_per_share, NCAV_per_share)
    print('Net Current Asset Value Ratio = ' + str(NCAV_ratio))

    bond_equity_earnings_yield_ratio = calc_bond_equity_earnings_yield_ratio(ten_year_treasury_yield, earnings_yield)
    print('Bond Equity Earnings Yield Ratio = ' + str(bond_equity_earnings_yield_ratio))

    print('Institutional Ownership Ratio = ' + str(institutional_ownership_ratio))

    print('Analysis complete.')


if __name__ == "__main__":
    main()

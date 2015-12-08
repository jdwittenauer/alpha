def calc_market_capitalization(price_per_share, total_shares_outstanding):
    """
    Market capitalization is the total market value of all of the shares outstanding.  It is based on
    the current stock price.  Total shares should be the diluted amount (includes preferred shares).
    """
    return price_per_share * total_shares_outstanding


def calc_stockholder_equity(total_assets, total_liabilities):
    """
    Stockholder's equity is the capital received from investors in exchange for stock (paid-in capital),
    donated capital and retained earnings.  Stockholders' equity represents the equity stake currently held
    on the books by a firm's equity investors.
    """
    return total_assets - total_liabilities


def calc_book_value(stockholder_equity, goodwill, intangible_assets, other_long_term_assets):
    """
    Book value is the net asset value of a company, calculated by total assets minus intangible assets
    (patents, goodwill) and liabilities.
    """
    return stockholder_equity - goodwill - intangible_assets - other_long_term_assets


def calc_operating_income(revenue, cost_of_goods_sold, operating_expenses):
    """
    Operating income is the amount of profit realized from a business's operations after taking out
    cost of goods sold and operating expenses.
    """
    return revenue - cost_of_goods_sold - operating_expenses


def calc_EBIT(operating_income, non_operating_income):
    """
    Earnings before interest and taxes (EBIT) is a measure of earnings that includes depreciation but
    excludes other variable deductions.
    """
    return operating_income + non_operating_income


def calc_earnings(EBIT, depreciation, capital_expenditures):
    """
    Earnings as calculated here is based on EBIT but also deducts capital expenditures above and beyond
    the depreciation cost.

    This calculation is part of Greenblat's magic formula.
    """
    return EBIT + (depreciation - capital_expenditures)


def calc_debt(short_term_debt, long_term_debt):
    """
    Debt is a measure of the amount of money a company has borrowed.
    """
    return short_term_debt + long_term_debt


def calc_preferred_value(total_shares_outstanding, basic_shares_outstanding, price_per_share):
    """
    Preferred value is the total dollar value of all of a company's outstanding preferred shares if they
    were exercised at once.  It is based on the current stock price.
    """
    return (total_shares_outstanding - basic_shares_outstanding) * price_per_share


def calc_excess_cash(total_cash, current_liabilities, current_assets):
    """
    Excess cash is a measure of the company's cash on hand that exceeds the delta between a company's current
    assets and current liabilities.

    This calculation is part of Greenblat's magic formula.
    """
    return total_cash - max(current_liabilities - current_assets, 0)


def calc_enterprise_value(market_capitalization, debt, preferred_shares_value, excess_cash):
    """
    Enterprise value calculates and adjusted market capitalization for a company that penalizes outstanding
    debt and preferred shares but provides a bonus for excess cash on hand.

    This calculation is part of Greenblat's magic formula.
    """
    return max(market_capitalization + debt + preferred_shares_value - excess_cash, 1)


def calc_earnings_yield(earnings, enterprise_value):
    """
    Earnings yield is a percentage representing real earnings relative to the value of the company.  It
    approximates the amount earned per dollar invested in the company.

    This calculation is part of Greenblat's magic formula.
    """
    return float(earnings) / float(enterprise_value)


def calc_net_fixed_assets(total_assets, current_assets, goodwill, intangible_assets, other_long_term_assets):
    """
    Net fixed assets is the value of all tangible assets (land, buildings, equipment etc.) less
    accumulated depreciation.

    This calculation is part of Greenblat's magic formula.
    """
    return total_assets - current_assets - goodwill - intangible_assets - other_long_term_assets


def calc_working_capital(current_assets, current_liabilities, short_term_debt, excess_cash):
    """
    Working capital as calculated here is the difference between a company's current assets and current
    liabilities, excluding short-term debt, and after removing excess cash.

    This calculation is part of Greenblat's magic formula.
    """
    return max(current_assets - (current_liabilities - short_term_debt) - excess_cash, 0)


def calc_invested_capital(stockholder_equity, debt):
    """
    Invested capital is calculated as total assets less total liabilites excluding debt.
    """
    return stockholder_equity + debt


def calc_return_on_equity(net_income, stockholder_equity):
    """
    Return on equity is the ratio of net income generated per dollar of stockholder equity.
    """
    return float(net_income) / float(stockholder_equity)


def calc_return_on_assets(net_income, total_assets):
    """
    Return on assets is the ratio of net income generated per dollar of total assets.
    """
    return float(net_income) / float(total_assets)


def calc_return_on_capital(earnings, net_fixed_assets, working_capital):
    """
    Return on capital is the ratio of earnings relative to a company's invested capital.  It's a measure
    of efficiency at allocating capital toward profitable investment.
    """
    return float(earnings) / float(net_fixed_assets + working_capital)


def calc_return_on_invested_capital(earnings, invested_capital):
    """
    Return on invested capital is an alternate definition of return on capital that uses as the
    denominator the calculation of invested capital above.
    """
    return float(earnings) / float(invested_capital)


def calc_free_cash_flow(operating_cash_flow, capital_expenditures, depreciation):
    """
    Free cash flow (FCF) represents the cash that a company is able to generate after laying out the money
    required to maintain or expand its asset base. Free cash flow is important because it allows a company
    to pursue opportunities that enhance shareholder value. Without cash, it's tough to develop new products,
    make acquisitions, pay dividends and reduce debt.
    """
    return operating_cash_flow - min(capital_expenditures, depreciation)


def calc_free_cash_flow_yield(free_cash_flow, enterprise_value):
    """
    Free cash flow yield is a percentage representing real cash flow relative to the value of the company.
    It is similar to earnings yield but uses actual cash flow instead of reported earnings.
    """
    return float(free_cash_flow) / float(enterprise_value)


def calc_cash_return_on_capital(free_cash_flow, net_fixed_assets, working_capital):
    """
    Cash return on capital is the ratio of free cash flow relative to a company's invested capital.  It is
    similar to return on capital but uses actual cash flow instead of reported earnings.
    """
    return float(free_cash_flow) / float(net_fixed_assets + working_capital)


def calc_cash_return_on_invested_capital(free_cash_flow, invested_capital):
    """
    Cash return on invested capital is an alternate definition of cash return on capital that uses as the
    denominator the calculation of invested capital above.  It is similar to return on invested capital but
    uses actual cash flow instead of reported earnings.
    """
    return float(free_cash_flow) / float(invested_capital)


def calc_dividend_yield(dividends_paid, total_shares_outstanding, price_per_share):
    """
    Dividend yield indicates how much a company pays out in dividends each year relative to its share price.
    """
    return (float(dividends_paid) / float(total_shares_outstanding)) / price_per_share


def calc_price_to_earnings_ratio(price_per_share, earnings_per_share):
    """
    The price/earnings (P/E) ratio measures the current share price relative to per-share earnings.
    """
    return float(price_per_share) / float(earnings_per_share)


def calc_annual_growth_rate(starting_value, final_value, n_years):
    """
    Calculates the annual compound growth rate required to reach the final value from the starting
    value over a period of n years.
    """
    return ((float(final_value) / float(starting_value)) ** (float(1) / n_years)) - 1


def calc_price_earnings_to_growth_ratio(price_earnings_ratio, annual_growth_rate):
    """
    The price/earnings to growth (PEG) ratio measures the price/earnings ratio relative to the annual
    earnings growth rate of the company.  The PEG ratio is used to determine a stock's value while
    taking the company's earnings growth into account.  However, it does not distinguish between more
    desirable types of growth (such as sales or margin growth) vs. less desirable types of growth
    (such as growth from acquisitions or share buybacks).
    """
    return float(price_earnings_ratio) / (float(annual_growth_rate) * 100)


def calc_price_to_free_cash_flow_ratio(market_capitalization, free_cash_flow):
    """
    The price/free cash flow ratio measures the current share price relative to real cash flow.  It is
    similar to the price/earnings ratio but uses actual cash flow instead of reported earnings.
    """
    return float(market_capitalization) / float(free_cash_flow)


def calc_price_to_book_ratio(market_capitalization, book_value):
    """
    The price to book (P/B) ratio is a ratio used to compare a stock's market value to its book value.
    """
    return float(market_capitalization) / float(book_value)


def calc_current_ratio(current_assets, current_liabilities):
    """
    The current ratio is a liquidity ratio that measures a company's ability to pay short-term and
    long-term obligations. To gauge this ability, the current ratio considers the total assets of a
    company (both liquid and illiquid) relative to that company's total liabilities.
    """
    return float(current_assets) / float(current_liabilities)


def calc_quick_ratio(current_assets, inventories, current_liabilities):
    """
    The quick ratio is an indicator of a company's short-term liquidity. The quick ratio measures a
    company's ability to meet its short-term obligations with its most liquid assets.
    """
    return float(current_assets - inventories) / float(current_liabilities)


def calc_debt_ratio(debt, total_assets):
    """
    The debt ratio measures the extent of a company's or consumer's leverage. The debt ratio is defined
    as the ratio of total debt to total assets.
    """
    return float(debt) / float(total_assets)


def calc_debt_to_equity_ratio(total_liabilities, stockholder_equity):
    """
    The debt to equity ratio is a debt ratio used to measure a company's financial leverage,
    calculated by dividing a company's total liabilities by its stockholders' equity.
    """
    return float(total_liabilities) / float(stockholder_equity)


def calc_current_liability_coverage_ratio(operating_cash_flow, dividends_paid, current_liabilities):
    """
    The current liability coverage ratio measures a company's ability to pay its debts based on cash
    generated from operations.
    """
    return float(operating_cash_flow - dividends_paid) / float(current_liabilities)


def calc_operating_cash_flow_ratio(operating_cash_flow, revenue):
    """
    The operating cash flow ratio measures a company's ability to turn revenue from sales into cash.
    """
    return float(operating_cash_flow) / float(revenue)


def calc_cash_investing_inflows(sales_of_investments, other_investing_activities):
    """
    Cash investing inflows are positive cash flows from the investment section of the cash flow statement.
    """
    return sales_of_investments + other_investing_activities


def calc_cash_financing_inflows(debt_issued, common_stock_issued):
    """
    Cash financing inflows are positive cash flows from the financing section of the cash flow statement.
    """
    return debt_issued + common_stock_issued


def calc_cash_generating_power_ratio(operating_cash_flow, cash_investing_inflows, cash_financing_inflows):
    """
    The cash generating power ratio measures the proportion of a company's positive cash flow that comes
    from operating the business vs. cash from investments or financing activities.
    """
    return float(operating_cash_flow) / float(operating_cash_flow + cash_investing_inflows + cash_financing_inflows)


def calc_bond_equity_earnings_yield_ratio(ten_year_treasury_yield, earnings_yield):
    """
    The bond equity earnings yield (BEER) ratio measures the earnings yield of a business relative to current
    returns from a ten-year treasury note.  A BEER of 1 would indicate equal levels of perceived risk between
    the bond market and the equity. BEER ratios greater than 1 imply that the equity may be overvalued, while
    numbers less than 1 mean it may be undervalued.
    """
    return float(ten_year_treasury_yield) / float(earnings_yield)


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
    sales_of_investments = 208111
    other_investing_activities = 16
    debt_issued = 18266
    common_stock_issued = 730
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

    price_earnings_ratio = calc_price_to_earnings_ratio(price_per_share, earnings_per_share)
    print('Price/Earnings Ratio = ' + str(price_earnings_ratio))

    annual_growth_rate = calc_annual_growth_rate(beginning_net_income, ending_net_income, n_years)
    print('Annual Growth Rate = ' + str(annual_growth_rate))

    price_earnings_to_growth_ratio = calc_price_earnings_to_growth_ratio(price_earnings_ratio, annual_growth_rate)
    print('Price/Earnings To Growth Ratio = ' + str(price_earnings_to_growth_ratio))

    price_to_free_cash_flow_ratio = calc_price_to_free_cash_flow_ratio(market_capitalization, free_cash_flow)
    print('Price To Free Cash Flow Ratio = ' + str(price_to_free_cash_flow_ratio))

    price_to_book_ratio = calc_price_to_book_ratio(market_capitalization, book_value)
    print('Price To Book Ratio = ' + str(price_to_book_ratio))

    current_ratio = calc_current_ratio(current_assets, current_liabilities)
    print('Current Ratio = ' + str(current_ratio))

    quick_ratio = calc_quick_ratio(current_assets, inventories, current_liabilities)
    print('Quick Ratio = ' + str(quick_ratio))

    debt_ratio = calc_debt_ratio(debt, total_assets)
    print('Debt Ratio = ' + str(debt_ratio))

    debt_to_equity_ratio = calc_debt_to_equity_ratio(total_liabilities, stockholder_equity)
    print('Debt To Equity Ratio = ' + str(debt_to_equity_ratio))

    current_liability_coverage_ratio = calc_current_liability_coverage_ratio(operating_cash_flow, dividends_paid, current_liabilities)
    print('Current Liability Coverage Ratio = ' + str(current_liability_coverage_ratio))

    operating_cash_flow_ratio = calc_operating_cash_flow_ratio(operating_cash_flow, revenue)
    print('Operating Cash Flow Ratio = ' + str(operating_cash_flow_ratio))

    cash_investing_inflows = calc_cash_investing_inflows(sales_of_investments, other_investing_activities)
    cash_financing_inflows = calc_cash_financing_inflows(debt_issued, common_stock_issued)
    cash_generating_power_ratio = calc_cash_generating_power_ratio(operating_cash_flow, cash_investing_inflows, cash_financing_inflows)
    print('Cash Generating Power Ratio = ' + str(cash_generating_power_ratio))

    bond_equity_earnings_yield_ratio = calc_bond_equity_earnings_yield_ratio(ten_year_treasury_yield, earnings_yield)
    print('Bond Equity Earnings Yield Ratio = ' + str(bond_equity_earnings_yield_ratio))

    print('Analysis complete.')


if __name__ == "__main__":
    main()

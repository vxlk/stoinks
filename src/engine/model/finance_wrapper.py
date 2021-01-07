import yfinance as yf
from util.logger import *

class yfinance_data():
    def __init__(self, ticker = None):

        self.hist_periods = ['1d', '5d', '1mo', '3mo', '6mo', 'ytd', '1y', '2y', '5y', '10y']
        self.hist_intervals = ['1m', '2m', '5m', '15m', '30m', '60m', '90m', '1h', '1d', '5d', '1wk', '1mo', '3mo']
        # -- begin data -- #
        self.info = None

        self.history = None
        self.today = None

        self.actions = None
        self.dividends = None
        self.splits = None
        self.quarterly_financials = None
        self.major_holders = None
        self.institutional_holders = None
        self.balance_sheet = None
        self.quarterly_balance_sheet = None
        self.cashflow = None
        self.quarterly_cashflow = None
        self.earnings = None
        self.quarterly_earnings = None
        self.sustainability = None
        self.recommendations = None
        self.calendar = None
        self.isin = None
        self.options = None
        self.options_chain = []
        # -- end data   -- #

        if ticker != None:
            self.fill_in_data_from_ticker(ticker)
    
    def fill_in_data_from_ticker(self, ticker):
        # get stock info
        self.info = ticker.info
        # get historical market data
        self.history = ticker.history(period="max")
        self.today = ticker.history(period="1d", interval="5m")
        # show actions (dividends, splits)
        self.actions = ticker.actions
        # show dividends
        self.dividends = ticker.dividends
        # show splits
        self.splits = ticker.splits
        # show financials
        self.financials = ticker.financials
        self.quarterly_financials = ticker.quarterly_financials
        # show major holders
        self.major_holders = ticker.major_holders
        # show institutional holders
        self.institutional_holders = ticker.institutional_holders
        # show balance sheet
        self.balance_sheets = ticker.balance_sheet
        self.quarterly_balance_sheet = ticker.quarterly_balance_sheet
        # show cashflow
        self.cashflow = ticker.cashflow
        self.quarterly_cashflow = ticker.quarterly_cashflow
        # show earnings
        self.earnings = ticker.earnings
        self.quarterly_earnings = ticker.quarterly_earnings
        # show sustainability
        self.sustainability = ticker.sustainability
        # show analysts recommendations
        self.recommendations = ticker.recommendations
        # show next event (earnings, etc)
        self.calendar = ticker.calendar
        # show ISIN code - *experimental*
        # ISIN = International Securities Identification Number
        self.isin = ticker.isin
        # show options expirations
        self.options = ticker.options 

        for option in self.options:
            # get option chain for specific expiration
            #opt = ticker.option_chain('YYYY-MM-DD')
            self.options_chain.append(ticker.option_chain(option))
            # data available via: opt.calls, opt.puts

    def history(self, date_string):
        # todo
        return None

    def price(self):
        return self.info['regularMarketPrice']

# a wrapper around the yahoo finance module
class yfinance_module():
    def __init__(self, list_stock_abbreviations):
        self.yfinance_tickers = {}
        self.yfinance_ticker_data = {}
        for stock in list_stock_abbreviations:
            self.add_ticker(stock)

    def add_ticker(self, str_stock_abbreviation):
        if not str_stock_abbreviation in self.yfinance_tickers:
            self.yfinance_tickers[str_stock_abbreviation] = yf.Ticker(str_stock_abbreviation)
            self.create_data(str_stock_abbreviation)

    def create_data(self, str_stock_abbreviation):
        logger.Log("Scraping stock data for: " + str_stock_abbreviation)
        self.yfinance_ticker_data[str_stock_abbreviation] = yfinance_data(self.yfinance_tickers[str_stock_abbreviation])

    def update_data(self):
        for stock_name in self.yfinance_tickers.keys():
            self.create_data(stock_name)

    def info(self, str_stock_abbreviation):
        return self.yfinance_ticker_data[str_stock_abbreviation].info

    def history(self, str_stock_abbreviation):
        hist = self.yfinance_ticker_data[str_stock_abbreviation].history
        # eventually format here
        return hist
    def today(self, str_stock_abbreviation):
        hist = self.yfinance_ticker_data[str_stock_abbreviation].today
        return hist

    def price(self, str_stock_abbreviation):
        return self.yfinance_ticker_data[str_stock_abbreviation].price()
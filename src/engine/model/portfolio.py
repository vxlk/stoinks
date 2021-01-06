from model.finance_wrapper import *

# Portfolio keeps track of the stocks we are watching and
# is able to retrieve data about them
class Portfolio():
    def __init__(self):
        self.stock_name_list = []
        self.stock_name_list.append("TSLA")
        #self.stock_name_list.append("AAPL")
        self.yfinance_wrapper = yfinance_module(self.stock_name_list)

    def update(self):
        self.yfinance_wrapper.update_data()

    def stocks(self):
        return self.stock_name_list
import statsmodels.tsa.stattools as ts
from algo.result import Result
from util.logger import *

# https://www.quantstart.com/articles/Basics-of-Statistical-Mean-Reversion-Testing/

# mean reversion is following the strategy based on statistical phenomenon that
# a time series set of values will return to its mean value

# we can determine mean and then do regression to the mean to come up with 
# numerical deviations, a negative deviation converging towards the mean
# can be used to predict a rise in price to the actual historical mean

class MeanReversionDataSet_ADFuller():
    def __init__(self, data, data_str_name):
        self.data_name = data_str_name
        self.adfuller_data = ts.adfuller(data)

    # will eventually return a result class
    def GetResult(self):
        print(self.adfuller_data)

class MeanReversion():
    def __init__(self):
        self.data = []

    def Calculate(self, data_name_str, data):
        calc_data = MeanReversionDataSet_ADFuller(data, data_name_str)
        calc_data.GetResult()
        self.data.append(calc_data)


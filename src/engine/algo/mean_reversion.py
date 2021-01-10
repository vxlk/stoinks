import statsmodels.tsa.stattools as ts
from numpy import cumsum, log, polyfit, sqrt, std, subtract
from numpy.random import randn

from algo.result import *
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

        #data
        self.calc_test_stat = self.adfuller_data[0] # the result, to test this should be MORE NEGATIVE than any of the critical values
        self.p_value = self.adfuller_data[1] # p-value (lower # = greater statistical relevance)
        self.num_values = self.adfuller_data[3] # total number of points read
        self.critical_values = self.adfuller_data[4] # critical values at 1,10,5%

    def __str__(self):
        return \
        "Mean Reversion Data\n" + \
        "Calculated Result: " + str(self.calc_test_stat) + \
        "P-Value: " + str(self.p_value) + \
        "Number of values given: " + str(self.num_values) + \
        "Critical Values " + str(self.critical_values)

    # will eventually return a result class
    def GetResult(self):
        print(self.__str__())
        res = self.Calculate()
        print(res.__str__())
        return res

    def Calculate(self):
        res = Result("Mean Reversion Result", False, "Mean Reversion failed on " + self.data_name)
        for crit_value_key in self.critical_values.keys():
            value = self.critical_values[crit_value_key]
            if value > self.calc_test_stat:
                res = Result("Mean Reversion Result",
                            True, 
                            "Mean Reversion passed on " + self.data_name,
                            self.calc_test_stat,
                            "Calculated Result",
                            value,
                            crit_value_key)
        return res

# Used to calculate how close a set of data is to a random
# walk
# https://www.quantstart.com/articles/Basics-of-Statistical-Mean-Reversion-Testing/
class MeanReversionDataSet_Hurst():
    def __init__(self, data, data_str_name):
        self.data_name = data_str_name
        #data
        self.hurst_result = self.RunHurst(data)

    def RunHurst(self, ts):
        # Create the range of lag values
        lags = range(2, 100)

        # Calculate the array of the variances of the lagged differences
        tau = [sqrt(std(subtract(ts[lag:], ts[:-lag]))) for lag in lags]
        print(tau)
        print(lags)
        # Use a linear fit to estimate the Hurst Exponent
        poly = polyfit(log(lags), log(tau), 1)

        # Return the Hurst exponent from the polyfit output
        return poly[0]*2.0

    def GetResult(self):
        print(self.__str__())
        res = self.Calculate()
        print(res.__str__())
        return res

    def Calculate(self):
        # decide if: reverting, trending, about to walk
        # todo: verify if H is statistically significant
        # https://en.wikipedia.org/wiki/Confidence_interval
        walk = 0.5
        reverting = 0.0
        trending = 1.0

        walk_res = abs(self.hurst_result - walk)
        revert_res = abs(self.hurst_result - reverting)
        trending_res = abs(self.hurst_result - trending)

        if (walk_res < revert_res and walk_res < trending_res):
            return Result("Hurst Mean Reversion", 
                        True, 
                        self.data_name + " had a walk value: " + walk_res,
                        self.hurst_result,
                        "Calculated Hurst Result",
                        walk,
                        "Statistical Walk Value")
        if (revert_res < walk_res and revert_res < trending_res):
            return Result("Hurst Mean Reversion", 
                        True, 
                        self.data_name + " had a revert value: " + revert_res,
                        self.hurst_result,
                        "Calculated Hurst Result",
                        revert,
                        "Statistical Revert Value")

        if (trending_res < walk_res and trending_res < revert_res):
            return Result("Hurst Mean Reversion", 
                        True, 
                        self.data_name + " had a trending value: " + trending_res,
                        self.hurst_result,
                        "Calculated Hurst Result",
                        trending,
                        "Statistical Trending Value")

    def __str__(self):
        return \
        "Mean Reversion Data - Hurst\n" + \
        "Calculated Result: " + str(self.hurst_result)

class MeanReversion():
    def __init__(self):
        self.data = []

    def Calculate(self, data_name_str, data):
        calc_data_fuller = MeanReversionDataSet_ADFuller(data, data_name_str)
        calc_data_fuller.GetResult()
        self.data.append(calc_data_fuller)

        calc_data_hurst = MeanReversionDataSet_Hurst(data, data_name_str)
        calc_data_hurst.GetResult()
        self.data.append(calc_data_hurst)


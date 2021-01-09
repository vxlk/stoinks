from algo.mean_reversion import *

# container for all of our algorithms

class AlgorithmContainer():
    def __init__(self):
        self.algos = {}
        self.algos["Mean Reversion"] = MeanReversion()

    def Calculate(self, data_str_name, data):
        for algo_key in self.algos.keys():
            self.algos[algo_key].Calculate(data_str_name, data)

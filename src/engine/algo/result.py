
# a simple results class
# every algorithm follows the same process to abstract processing:
# Result = Process(data)
# Result will either be positive or negative
# Result will contain a reason as to why it is positive or negative
# Result will carry the numeric value and name of variable and comparison it used

class Result():
    def __init__(bool_positive, str_reason, result_num, str_result_num_name, compared_num, str_compared_num_name):
        self.result = bool_positive
        self.reason = str_reason
        self.result_number = result_num
        self.result_number_name = str_result_num_name
        self.result_comparator = compared_num
        self.result_comparator_name = str_compared_num_name

    def Value(self):
        return self.result == True

# a simple results class
# every algorithm follows the same process to abstract processing:
# Result = Process(data)
# Result will either be positive or negative
# Result will contain a reason as to why it is positive or negative
# Result will carry the numeric value and name of variable and comparison it used

class Result():
    def __init__(self, str_result_name, bool_positive, str_reason, result_num = None, str_result_num_name = None, compared_num = None, str_compared_num_name = None):
        self.result_name = str_result_name
        self.result = bool_positive
        self.reason = str_reason
        self.result_number = result_num
        self.result_number_name = str_result_num_name
        self.result_comparator = compared_num
        self.result_comparator_name = str_compared_num_name

    def Value(self):
        return self.result == True

    def __str__(self):
        return \
        "Result For " + self.result_name + "\n" + \
        "Result: " + str(self.result) + \
        "Reason: " + str(self.reason) + \
        "Result Number: " + str(self.result_number) + \
        "Result Name: " + str(self.result_number_name) + \
        "Compared To: " + str(self.result_comparator) + \
        "Compared To Var: " + str(self.result_comparator_name)

# bad_value = Result("Result", False, "This is invalid", 0, "Crap", 0, "Crap")
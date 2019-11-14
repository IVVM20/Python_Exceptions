
def number_in_list(number):
    my_list = [1, 2, 3, 4]
    assert (number in my_list), "Number {} not in {}".format(number,
                                                             my_list.__repr__())
    return "Number {} is in list.".format(number)

"""
Output:

Traceback (most recent call last):
  File "/project/Python_Exceptions/asserting_using_AssertionError.py", line 2, in <module>
    assert (5 in list1), "5 not in list1"
AssertionError: 5 not in list1
"""


def is_dict(variable):
    assert (type(variable) is dict), "Variable {} is " \
                                     "not dict".format(variable.__repr__())
    return "Variable type is dict."


print(number_in_list(13))
"""
Output:

Traceback (most recent call last):
  File "/project/Python_Exceptions/asserting_using_AssertionError.py", line 24, in <module>
    print(number_in_list(13))
  File "/project/Python_Exceptions/asserting_using_AssertionError.py", line 5, in number_in_list
    my_list.__repr__())
AssertionError: Number 13 not in [1, 2, 3, 4]
"""
print(is_dict(13))
"""
Output:

Traceback (most recent call last):
  File "/project/Python_Exceptions/asserting_using_AssertionError.py", line 35, in <module>
    print(is_dict(13))
  File "/project/Python_Exceptions/asserting_using_AssertionError.py", line 20, in is_dict
    "not dict".format(variable.__repr__())
AssertionError: Variable 13 is not dict
"""
class LowerThanTen(object):
    def __init__(self, number):
        self.number = number

    def raise_if_higher(self):
        if self.number > 10:
            raise Exception('The number should not be bigger than 10. '
                            'The value was: {}'.format(self.number))
        else:
            print("Value is lower than 10. The value was: {}".format(self.number))

my_test_instance = LowerThanTen(3)
my_test_instance.raise_if_higher()

my_test_instance2 = LowerThanTen(13)
my_test_instance2.raise_if_higher()


"""
Output:

Value is lower than 10. The value was: 3
Traceback (most recent call last):
  File "/project/Python_Exceptions/raise_exception.py", line 16, in <module>
    my_test_instance2.raise_if_higher()
  File "/project/Python_Exceptions/raise_exception.py", line 8, in raise_if_higher
    'The value was: {}'.format(self.number))
Exception: The number should not be bigger than 10. The value was: 13
"""
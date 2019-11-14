class Error(Exception):
    """Base class for other exceptions"""
    pass


class ValueTooLargeError(Error):
    """Raised when the input value is too large"""
    pass


class ValueTooSmallError(Error):
    """Raised when the input value is too small"""
    pass


class InvalidInputError(Error):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return repr(self.msg)


class LowerOrHigherThanTen(object):
    """
    Class used to verify if number is lower or higher than 10 and raise proper
    custom exception.
    """
    def __init__(self, number):
        self.number = number

    def raise_if_higher(self):
        """
        Method verifies if number is higher than 10 and raises exception if true
        :return:
        """
        if self.number > 10:
            raise ValueTooLargeError('The number should not be bigger than 10. '
                                     'The value was: {}'.format(self.number))
        else:
            print("Value is lower than 10. The value was: {}".format(self.number))

    def raise_if_lower(self):
        """
        Method verifies if number is lower than 10 and raises exception if true

        :return:
        """
        if self.number < 10:
            raise ValueTooSmallError('The number should be bigger than 10. '
                                     'The value was: {}'.format(self.number))
        else:
            print("Value is higher than 10. The value was: {}".format(self.number))


if __name__ == "__main__":
    my_test_instance = LowerOrHigherThanTen(13)
    my_test_instance.raise_if_lower()

"""
Output when input is 3 -> LowerOrHigherThanTen(3):

Traceback (most recent call last):
  File "/project/Python_Exceptions/raise_custom_exception.py", line 36, in <module>
    my_test_instance.raise_if_lower()
  File "/project/Python_Exceptions/raise_custom_exception.py", line 30, in raise_if_lower
    'The value was: {}'.format(self.number))
__main__.ValueTooSmallError: The number should be bigger than 10. The value was: 3


Output when input is 13 -> LowerOrHigherThanTen(13):
Value is higher than 10. The value was: 13

"""

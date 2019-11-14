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
        self.number = number if self._is_number(number) else int(number)

    @staticmethod
    def _is_number(number):
        try:
            if type(number) != int:
                raise InvalidInputError("'number' value argument is not integer! "
                                        "Inserted value is {}. Will attempt to "
                                        "convert to integer!".format(number))
        except InvalidInputError as e:
            print("Invalid input entered; {}".format(e))

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
    my_test_instance = LowerOrHigherThanTen(3)
    my_test_instance.raise_if_lower()

"""
Output when input is "13a"  -> LowerOrHigherThanTen("13a"):

Invalid input entered; "'number' value argument is not integer! Inserted value is 13a. Will attempt to convert to integer!"
Traceback (most recent call last):
  File "/project/Python_Exceptions/raise_custom_exception.py", line 67, in <module>
    my_test_instance = LowerOrHigherThanTen("13a")
  File "/project/Python_Exceptions/raise_custom_exception.py", line 30, in __init__
    self.number = number if self._is_number(number) else int(number)
ValueError: invalid literal for int() with base 10: '13a'


Output when input is "13"  -> LowerOrHigherThanTen("13"):

Invalid input entered; "'number' value argument is not integer! Inserted value is 13. Will attempt to convert to integer!"
Value is higher than 10. The value was: 13


Output when input is "3"  -> LowerOrHigherThanTen("3"):

Invalid input entered; "'number' value argument is not integer! Inserted value is 3. Will attempt to convert to integer!"
Traceback (most recent call last):
  File "/project/Python_Exceptions/raise_try_except_custom_exception.py", line 68, in <module>
    my_test_instance.raise_if_lower()
  File "/project/Python_Exceptions/raise_try_except_custom_exception.py", line 61, in raise_if_lower
    'The value was: {}'.format(self.number))
__main__.ValueTooSmallError: The number should be bigger than 10. The value was: 3


Output when input is 13  -> LowerOrHigherThanTen(13):

Value is higher than 10. The value was: 13


Output when input is 3  -> LowerOrHigherThanTen(3):

Traceback (most recent call last):
  File "/project/Python_Exceptions/raise_try_except_custom_exception.py", line 68, in <module>
    my_test_instance.raise_if_lower()
  File "/project/Python_Exceptions/raise_try_except_custom_exception.py", line 61, in raise_if_lower
    'The value was: {}'.format(self.number))
__main__.ValueTooSmallError: The number should be bigger than 10. The value was: 3
"""

# Python Exception and Error Handling
The main goal of the repository is to give examples on how to increase the code robustness and implement good exception/error handling procedures which guard against potential failures which may cause your program to exit its run in an uncontrolled fashion.
The code is written using Python 3, but most of it can be also run in Python 2 with little or no modifications required.

## Preparing for Failure
A good rule of thumb is to always prepare for failure in one of the components you have designed. This being said, you should start exercising failure scenarios in your design. The more failure scenarios you cover, the easier it will be to find why your program is missbehaving, thus reducing your Mean Time to Recover (__*MTTR*__).
Recovery from a problem has the following steps:
1. __*Detect*__ the problem
2. __*Identify*__ the root cause
3. __*Determine*__ and __*Deploy*__ the solution.

This repository will give examples of error handling, which if done good, generally speaking handles the first two steps in the recovery procedure above.  

## Syntax Errors and Runtime Errors
In Python programs, many problems can go wrong, abbruptly called erros.
These errors can be of two types:
1. Syntax errors: errors caused by not following the proper structure/syntax of the python language; these errors are caught when interpreting the code
2. Runtime Errors: these exceptions occur at run-time; even though your code is bullet-proof syntactically speaking, there are exceptions at runtime from a functional perspective.

## Examples of Syntax Errors and Runtime Errors

1.__Syntax Errors__
```
my_list = [1, 2, 3]
for item in my_list:
print(item)
```
__Output:__
```
  File "<ipython-input-23-30fcf0822ade>", line 3
    print(value)
        ^
IndentationError: expected an indented block
```
__Explanation:__ The arrow indicates where the parser ran into the syntax error. In this example, the code block was not indented properly.

2.__Runtime Errors__
```
a = 2
b = 0
print(a/b)
```
__Output:__
```
Traceback (most recent call last):
  File "main.py", line 3, in <module>
    print(a/b)
ZeroDivisionError: integer division or modulo by zero
```
__Explanation:__ We have ran into an exception error and this type of error occurs whenever syntactically correct Python core results in an error. We can see in the last line of the message what type of exception error we encountered. In this case we encountered a ZeroDivisionError because we tried to calculate 2/0.


## Runtime Error/Exception Handling.
It becomes obvious that the we must employ tactics for detecting and identifying the cause of the run-time errors; The syntacting errors being mostly easy to repair.
Python comes shipped already with various built-in exceptions and also leaves the user the possibility of creating self-defined exceptions.
Built-in Exception Classes:

| Exception Class  | Event  |
|---|---|
|Exception  |Base class for all exceptions  |
|ArithmeticError  |Raised when numeric calculations fails   |
|FloatingPointError   |Raised when a floating point calculation fails   |
|ZeroDivisionError   |Raised when division or modulo by zero takes place for all numeric types   |
|AssertionError   |Raised when Assert statement fails   |
|OverflowError   |Raised when result of an arithmetic operation is too large to be represented   |
|ImportError   |Raised when the imported module is not found   |
|IndexError   |Raised when index of a sequence is out of range   |
|KeyboardInterrupt   |Raised when the user interrupts program execution, generally by pressing Ctrl+c   |
|IndentationError   |Raised when there is incorrect indentation   |
|SyntaxError   |Raised by parser when syntax error is encountered   |
|KeyError   |Raised when the specified key is not found in the dictionary   |
|NameError   |Raised when an identifier is not found in the local or global namespace   |
|TypeError   |Raised when a function or operation is applied to an object of incorrect type   |
|ValueError   |Raised when a function gets argument of correct type but improper value   |
|IOError   |Raised when an input/ output operation fails   |
|RuntimeError   |Raised when a generated error does not fall into any category   |

You can find more information here:
* [Python3 Exceptions](https://docs.python.org/3/library/exceptions.html) - Python3 Error/Exception Handling
* [Python2 Exceptions](https://docs.python.org/2/library/exceptions.html) - Python2 Error/Exception Handling


## Raising an Exception
You can use "raise" to throw an exception __if__ a condition occurs. 
__Note:__ You can generally use your custom exception here to better complement the statement and handle the error. 
```
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
```
__Output:__
```
Value is lower than 10. The value was: 3
Traceback (most recent call last):
  File "/project/Python_Exceptions/raise_exception.py", line 16, in <module>
    my_test_instance2.raise_if_higher()
  File "/project/Python_Exceptions/raise_exception.py", line 8, in raise_if_higher
    'The value was: {}'.format(self.number))
Exception: The number should not be bigger than 10. The value was: 13
```

## Asserting with AssertionError Exception
This should be used when a certain condition is met. If our condition is True, than the program continues its run. Otherwise, if our condition is False, than an AssertionError exception is trown.

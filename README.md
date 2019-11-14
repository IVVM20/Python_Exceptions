# Python_Exceptions
The main goal of the repository is to give examples on how to increase the code robustness and implement good exception/error handling procedures which guard against potential failures which may cause your program to exit its run in an uncontrolled fashion.

## Preparing for Failure
A good rule of thumb is to always prepare for failure in one of the components you have designed. This being said, you should start exercising failure scenarios in your design. The more failure scenarios you cover, the easier it will be to find why your program is missbehaving, thus reducing your Mean Time to Recover (*MTTR*).
Recovery from a problem has the following steps:
1. *Detect* the problem
2. *Identify* the root cause
3. *Determine* and *Deploy* the solution.

This repository will give examples of error handling, which if done good, generally speaking handles the first two steps in the recovery procedure above.  

## Detecting the problem
In Python programs, many problems can go wrong, abbruptly called erros.
These errors can be of two types:
1. Syntax errors: errors caused by not following the proper structure/syntax of the python language; these errors are caught when interpreting the code
2. Runtime Errors: these exceptions occur at run-time; even though your code is bullet-proof syntactically speaking, there are exceptions at runtime from a functional perspective.

### Examples of Syntax Errors and Runtime Errors
"""

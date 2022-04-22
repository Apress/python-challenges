# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


import time
from functools import wraps


def check_argument_is_positive_integer(unary_func):
    def helper(n):
        if type(n) == int and n > 0:
            return unary_func(n)
        else:
            raise ValueError("n must be positive and of type int")

    return helper


def factorial(n):
    if n <= 0:
        raise ValueError("n must be >= 1")

    # rekursiver Abbruch
    if n == 1:
        return 1

    # rekursiver Abstieg
    return n * factorial(n - 1)


# factorial = check_argument_is_positive_integer(factorial)


@check_argument_is_positive_integer
def factorial(n):
    # rekursiver Abbruch
    if n == 1:
        return 1

    # rekursiver Abstieg
    return n * factorial(n - 1)


print(factorial(5))


# print(factorial(-5))


def check_arguments_are_positive_integers(binary_func):
    def helper(param1, param2):
        if type(param1) == int and param1 > 0 and \
            type(param2) == int and param2 > 0:
            return binary_func(param1, param2)
        else:
            raise ValueError("both params must be positive and of type int")

    return helper


@check_arguments_are_positive_integers
def add(value1, value2):
    return value1 + value2


@check_arguments_are_positive_integers
def subtract(value1, value2):
    return value1 - value2


def audit_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before calling " + func.__name__)
        result = func(*args, **kwargs)
        print("After calling " + func.__name__)
        return result

    return wrapper


def check_arguments_are_positive_integers(binary_func):
    @wraps(binary_func)
    def helper(param1, param2):
        if type(param1) == int and param1 > 0 and \
           type(param2) == int and param2 > 0:
            return binary_func(param1, param2)
        else:
            raise ValueError("both params must be positive and of type     int")

    return helper


@audit_decorator
@check_arguments_are_positive_integers
def add(value1, value2):
    return value1 + value2


print("add", add(2, 7))


def timed_execution(func):
    @wraps(func)
    def timed_execute(*args, **kwargs):
        start_time = time.process_time()
        result = func(*args, **kwargs)
        end_time = time.process_time()
        run_time = end_time - start_time
        print(f"'{func.__name__}' took {run_time * 1000:.2f} ms")
        return result

    return timed_execute

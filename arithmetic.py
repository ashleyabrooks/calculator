def add(num1, num2):
    """Return the sum of two numbers"""
    # total = 0
    # for i in args:
    #     total += i
    # return total
    return round((num1 + num2), 2)


def subtract(num1, num2):
    """Return the difference of two numbers"""
    return round((num1 - num2), 2)


def multiply(num1, num2):
    """Return the product of two numbers"""
    return round((num1 * num2), 2)


def divide(num1, num2):
    """Return the quotient of two numbers as a float"""
    return round((float(num1) / float(num2)), 2)


def square(num):
    """Return the square of a number"""
    return round((num ** 2), 2)


def cube(num):
    """Return the cube of a number"""
    return round((num ** 3), 2)


def power(num, exponent):
    """Return num raised to the power of exponent"""
    return round((num ** exponent), 2)


def mod(num1, num2):
    """Return remainder of num1 divided by num2"""
    return round((num1 % num2), 2)

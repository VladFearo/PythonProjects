def temperature_converter(c):
    """
    converts degrees from celsius to fahrenheit.
    :param c: degrees in Celsius
    :return: degrees in Fahrenheit
    """
    return c/(5/9)+32


def factorial_print():
    """
    prints all the factorials from 0! to 60!
    :return: None
    """
    f, n = 1, 0
    for _ in range(61):
        print(n, "! = ", f)
        n += 1
        f = f*n


def square_cube():
    """
    prints an array of a number running from 0 to 9 the square of that number and the cube of that number.
    :return: None
    """
    i = 0
    while i <= 9:
        print(i, i**2, i**3)
        i += 1


def GCD(x, y):
    """
    Calculates the greatest common denominator
    :param x: Integer
    :param y: Integer
    :return: Greatest common denominator of the two integers.
    """
    while y:
        x, y = y, x % y

    return x


def fibonacci_rec(n):
    """
    Calculates the n figure in the fibonacci sequence recursively
    :param n: a positive integer
    :return: the nth figure in the fibonacci sequence
    """
    if n <= 1:
        return n
    else:
        return fibonacci_rec(n-1)+fibonacci_rec(n-2)


def fibonacci_non_rec(n):
    """
    Calculates the n figure in the fibonacci sequence non recursively
    :param n: a positive integer
    :return: the nth figure in the fibonacci sequence
    """
    a0 = 0
    a1 = 1
    an = a0 + a1
    a_next = an + a1
    index = 3
    while index <= n:
        an, a_next = a_next, an + a_next
        index += 1
    return an


def is_perfect_number(n):
    """
    Checks if a given number is a perfect number.
    :param n: an integer.
    :return: True if the number is perfect and False otherwise.
    """
    sum = 0
    for x in range(1, n):
        if n%x == 0:
            sum += x
    return sum == n


"""for n in range(10000):
    if is_perfect_number(n):
        print(n)"""


def num_delete(n, x):
    """
    Removes a number x out of a number n. (e.x. n = 1221 x = 2 -> new number = 11).
    :param n: a positive integer
    :param x: a positive integer
    :return: a positive integer without x in n
    """
    n_string = str(n)
    for _ in n_string:
        n_string = n_string.replace(str(x), '')

    return int(n_string)





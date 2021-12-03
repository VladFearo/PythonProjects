import random


def random_binary(n):
    """
    Prints n random numbers in binary format
    :param n: a positive integer
    :return: None
    """
    for _ in range(n):
        print(bin(random.randint(0, 255)))


def list_of_integers(n):
    """
    creats a list of numbers that make the number n
    :param n: a real number
    :return: a list of integers
    """
    string_n = str(n)
    string_n = string_n.replace('.', '')
    print(string_n)
    return list(string_n)


def square_root(n):
    """
    calculates the square root of an integer that has a whole square root
    :param n: an integer that a has a whole square root
    :return: the square root of the number
    """
    subtractor = 1
    counter = 0
    while n > 0:
        n = n - subtractor
        counter += 1
        subtractor += 2
    return counter


def non_negative_list():
    """
    makes a list of non negative real numbers from user input.
    when the users enters an invalid number the program stops.
    :return: a list of non negative numbers
    """
    arr = []
    while True:
        x = float(input("Enter positive number:"))
        if x > 0:
            arr.append(x)
        else:
            break
    return arr


def min_sum_max(arr):
    return [min(arr), sum(arr), max(arr)]


def list_combination(A, B):
    x = []
    for _ in range(len(A)):
        x += ([A[_]]*B[_])

    return x


def random_list():
    x = []
    for _ in range(100):
        x += random.sample(range(1, 11),10)
    return x


print(len(random_list()))

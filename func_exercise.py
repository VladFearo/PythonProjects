def lesser_of_two_evens(a, b):
    """
    if a and b are even returns the lowest of the two if a or b are not even returns the larger
    :param a: integer
    :param b: integer
    :return: integer
    """
    if a > b:
        lesser = b
        bigger = a
    else:
        lesser = a
        bigger = b
    if a % 2 == 0 and b % 2 == 0:
        return lesser
    else:
        return bigger


def animal_crackers(text):
    """
    returns true if the first letter of both words is the same letter
    :param text: two word string
    :return: boolean
    """
    split_text = text.split()
    if split_text[0][0] == split_text[1][0]:
        return True
    else:
        return False


def makes_twenty(n1, n2):
    """
    returns true if n1+n2 is 20 or if n1 or n2 is 20 otherwise returns false
    :param n1: a number
    :param n2: a number
    :return: boolean
    """
    return n1 == 20 or n2 == 20 or n1 + n2 == 20


def old_macdonald(name):
    """
    makes the first and 4th letter uppercase
    :param name: a string
    :return: a string with the 1st and 4th letter in uppercase
    """
    first = name[:3]
    last = name[3:]
    return first.capitalize() + last.capitalize()


def master_yoda(text):
    """
    returns the texted in reverse order (e.g. I love python -> python love I)
    :param text: string
    :return: reversed order string
    """
    temp = text.split()
    return " ".join(temp[::-1])


def almost_there(n):
    """
    checks if the number n is in a 10 range difference from 100 or 200
    :param n: a number
    :return: boolean
    """
    return abs(n - 100) <= 10 or abs(n - 200) <= 10


def has_33(nums):
    """
    checks if a list of numbers contains a 3 after a 3 (e.g. [1,2,3,3] -> True, [1,2,3,4,3] -> False)
    :param nums: a list of numbers
    :return: boolean
    """
    flag = False
    for i in range(len(nums) - 1):
        if nums[i] == 3:
            flag = True
        else:
            flag = False
        if flag:
            if nums[i + 1] == 3:
                return flag
    return flag


def paper_doll(text):
    """
    takes a string and returns the string with every letter 3 times (e.g. python -> pppyyyttthhhooonnn)
    :param text: a string
    :return: a string
    """
    new_string = ''
    for letter in text:
        new_string += letter * 3
    return new_string


def blackjack(a, b, c):
    """
    takes 3 numbers and returns the sum of them if it is under 21 or the word 'BUST' if it is over 21
    :param a: an integer between 1 and 11
    :param b: an integer between 1 and 11
    :param c: an integer between 1 and 11
    :return: a number or the word 'BUST'
    """
    bj_sum = sum((a, b, c))
    if bj_sum > 21:
        if 11 in [a, b, c]:
            return bj_sum - 10
        else:
            return 'BUST'
    else:
        return bj_sum


def summer_69(arr):
    """
    gets an array of numbers and calculates its sum until it sees the number 6 and stops counting until it sees the
    number 9 then continues counting
     :param arr: an array of numbers
     :return: a number
    """
    sum_of_nums = 0
    flag = False
    for i in arr:
        if not flag:
            if i == 6:
                flag = True
            else:
                sum_of_nums += i
        if i == 9:
            flag = False

    return sum_of_nums


def spy_game(nums):
    """
    gets a list of numbers and returns True if the list contains the series '007' in order
    (e.g. [1,0,0,7] -> True [7,0,0] -> False)
    :param nums: an array of numbers
    :return: boolean
    """
    FZFlag = False  # first zero flag
    SZFlag = False  # second zero flag
    for i in nums:
        if i == 0 and not FZFlag:
            FZFlag = True
        elif i == 0 and FZFlag:
            SZFlag = True
        if i == 7 and FZFlag and SZFlag:
            return True
    return False


def is_prime(n):
    """
    calculates if a number is prime
    :param n: a number
    :return: boolean
    """
    from math import sqrt
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def count_primes(num):
    """
    calculates how many prime numbers are in a number
    :param num: a number
    :return: the number of primes in the number given
    """
    counter = 0
    for i in range(num):
        if is_prime(i):
            counter += 1
    return counter



def integral(a, b, f):
    """
    calculates an integral for a function from a to b
    :param a: integer
    :param b: integer
    :param f: function
    :return: float of the solution of the integral
    """
    fsum = 0
    for k in range(0, 1000):
        fsum += f(a + k * (b - a) / 1000)
    return fsum * ((b - a) / 1000)


def fibo_build(a, b):
    """
    creates a function that returns a fibonacci number based on n
    :param a: a positive integer
    :param b: a possitve integer
    :return: a function that calculates a fibonacci number depending on n
    """
    def fibonacci(n):
        """
        calculates a fibonacci number depending on the choice of the user:
        n == 0 calculates fibonacci sequence for Aa
        n == 1 for Ab
        n != 0 and n != 1 for An
        :param n: a positive integer
        :return: a fibonacci number based on n
        """
        def calc(x):
            """
                Calculates the x figure in the fibonacci sequence non recursively
                :param x: a positive integer
                :return: the nth figure in the fibonacci sequence
                """
            a0 = 0
            a1 = 1
            an = a0 + a1
            a_next = an + a1
            index = 3
            while index <= x:
                an, a_next = a_next, an + a_next
                index += 1
            return an
        if n == 0:
            return calc(a)
        elif n == 1:
            return calc(b)
        else:
            return calc(n)
    return fibonacci


def smooth(f):
    def g(n):
        return (f(n-1)+f(n)+(n-1))/3
    return g

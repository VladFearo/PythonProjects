def splitNumbers(string):
    return list(map(int, string.split(',')))


def onlyEvenStr(iter):
    return ','.join(str(x) for x in iter if x % 2 == 0)

print(onlyEvenStr([1,2,3,4]))

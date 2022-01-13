from _operator import add

rates = {('dollar', 'nis'): 3.11, ('euro', 'nis'): 3.56, ('nis', 'dollar'): 0.32, ('nis', 'euro'): 0.28,
         ('dollar', 'euro'): 0.87, ('euro', 'dollar'): 1.14}


class Euro:
    def __init__(self, amount):
        self._amount = amount

    def amount(self):
        return self._amount * rates[('euro', 'nis')]

    def get_amount(self):
        return self._amount

    def __str__(self):
        return f'{self._amount}€'

    def __repr__(self):
        return f'Euro({self._amount})'

    def __add__(self, other):
        return self.amount() + other.amount()

    def add(self, other):
        return self.amount() + other.amount()


class Dollar:
    def __init__(self, amount):
        self._amount = amount

    def amount(self):
        return float(self._amount) * rates[('dollar', 'nis')]

    def get_amount(self):
        return self._amount

    def __str__(self):
        return f'{self._amount}$'

    def __repr__(self):
        return f'Dollar({self._amount})'

    def __add__(self, other):
        return self.amount() + other.amount()

    def add(self, other):
        return self.amount() + other.amount()


class Shekel:
    def __init__(self, amount):
        self._amount = amount

    def amount(self):
        return self._amount

    def get_amount(self):
        return self._amount

    def __str__(self):
        return f'{self._amount}₪'

    def __repr__(self):
        return f'Shekel({self._amount})'

    def __add__(self, other):
        return self.amount() + other.amount()


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def op_detect(operator):
    if operator in ['+', 'add', 'Add', 'ADD']:
        return add
    elif operator in ['-', 'sub', 'Sub', 'SUB']:
        return sub
    else:
        print("Wrong operator entered.")


def apply(operator, obj, other):
    op = op_detect(operator)
    if type(obj) is Euro:
        if type(other) is Euro:
            return Euro(op(obj.get_amount(), other.get_amount()))
        elif type(other) is Dollar:
            return Euro(op(obj.get_amount(), other.get_amount() * rates[('dollar', 'euro')]))
        elif type(other) is Shekel:
            return Euro(op(obj.get_amount(), other.get_amount() * rates[('nis', 'euro')]))
    elif type(obj) is Dollar:
        if type(other) is Euro:
            return Dollar(op(obj.get_amount(), other.get_amount() * rates[('euro', 'dollar')]))
        elif type(other) is Dollar:
            return Dollar(op(obj.get_amount(), other.get_amount()))
        elif type(other) is Shekel:
            return Dollar(op(obj.get_amount(), other.get_amount() * rates[('nis', 'euro')]))
    elif type(obj) is Shekel:
        if type(other) is Euro:
            return Shekel(op(obj.get_amount(), other.get_amount() * rates[('euro', 'nis')]))
        elif type(other) is Dollar:
            return Shekel(op(obj.get_amount(), other.get_amount() * rates[('dollar', 'nis')]))
        elif type(other) is Shekel:
            return Shekel(op(obj.get_amount(), other.get_amount()))


def coerce_apply(operator, obj, other):
    op = op_detect(operator)
    return Shekel(op(obj.amount(), other.amount()))



class Student:
    def __init__(self, first_name, last_name):
        self._first_name, self._last_name = first_name, last_name
        self._grades = []

    def __add__(self, grade):
        if isinstance(grade, (int, float)):
            if grade > 0:
                self._grades.append(grade)
        else:
            print('Error, bad input.')

    def __str__(self):
        return f'Name: {self._first_name}'

    def __eq__(self, other):
        if self._first_name == other.get_first_name():
            if self._last_name == other.get_last_name():
                return True
        return False

    def __len__(self):
        return len(self._grades)

    def average(self):
        sum = 0
        nums = len(self)
        for grade in self._grades:
            sum += grade
        return sum/nums

    def get_first_name(self):
        return self._first_name

    def get_last_name(self):
        return self._last_name

    def get_grades(self):
        return self._grades

    def set_first_name(self, first_name):
        if isinstance(first_name, str):
            self._first_name = first_name

    def set_last_name(self, last_name):
        if isinstance(last_name, str):
            self._last_name = last_name
        else:
            print("Error")


Vlad = Student("Vlad", "Shevtsov")
Vlad+100
Vlad+50
x = Vlad
print(Vlad==x)
sum = 0
print(len(Vlad))
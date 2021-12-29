class Course:
    def __init__(self, name):
        if isinstance(name, str):
            self.name = name
            self.grade = 101
        else:
            raise TypeError("A name must be a string")

    def __str__(self):
        return f'Course name: {self.name} \nGrade: {self.grade}'

    def __repr__(self):
        return f'Course("{self.name}")'

    def setGrade(self, grade):
        """
        a function that sets a grade for a course.
        :param grade: a number between 0 and 100
        :return: None
        """
        if 0 <= grade <= 100:
            self.grade = grade


class Student:
    def __init__(self, name, ID):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError("A name must be a string")
        if isinstance(ID, int):
            self._ID = ID
        else:
            raise TypeError("An ID must be a number")
        self.courses = []

    def getID(self):
        """
        a function that returns the ID of a student
        :return: a number that represents the student ID
        """
        return self._ID

    def addCourse(self, course):
        """
        a function that adds a course to a list of courses for the student only if the course grade is valid
        :param course: a course object from the Course class
        :return: None
        """
        if 0 <= int(course.grade) <= 100 and course not in self.courses:
            self.courses.append(course)
        elif course in self.courses:
            index = self.courses.index(course)
            self.courses[index].setGrade()

    def get_average(self):
        """
        Calculates the average of a student.
        :return: float number the average of the student.
        """
        return sum(list(map(lambda x: x.grade, self.courses))) / len(self.courses)

    def is_studying(self, course_name):
        """
        Checks if the student has a course by the name given and returns its grade
        :param course_name: A string that represents a course name.
        :return: a number that is the grade of a course
        """
        return list(filter(lambda course: course.name == course_name, self.courses))[0].grade

    def __str__(self):
        return f'Name: {self.name} \nID: {self.getID()}\ncourses: {self.courses}'

    def __repr__(self):
        return f'Student("{self.name}", {self.getID()})'


name = input("Enter a file name:")

students = []
try:
    with open(name, 'r') as file:
        for line in file:
            info = line.strip().split('\t')
            temp = (Student(info[0], int(info[1])))
            info.pop(0)
            info.pop(0)
            info = info[0].split(";")
            for course in info:
                tempCourse = Course(course.split("#")[0])
                tempCourse.setGrade(int(course.split("#")[1]))
                temp.addCourse(tempCourse)
            students.append(temp)
except FileNotFoundError:
    print("The file is not found")

while True:
    n = int(input("Please choose an option:\n1. Calculate an average for a student\n2. Calculate an average for a "
                  "course\n3. calculate an average for all students\n4.Exit\n"))
    if n == 1:
        student_name = input("Enter a students name:\n")


        def find_student(student):
            """
            Gets a student and checks if its name is the same as the name provided by the user.
            :param student: Student class object
            :return: True if the student has the name provided and False otherwise
            """
            return True if student.name == student_name else False


        print(students)
        print(list(filter(find_student, students))[0].get_average())
    elif n == 2:
        course_name = input("Enter a course name:\n")
        courses_l = list(map(lambda student: student.is_studying(course_name), students))
        print(sum(courses_l)/len(courses_l))
    elif n == 3:
        IDS = list(map(lambda student: student.getID(), students))
        AVERAGES = list(map(lambda student: student.get_average(), students))
        MIX = list(map(lambda a, b: f'{a} {b}\n', IDS, AVERAGES))
        file_name = input("Enter a file name to write into:\n")
        with open(file_name, 'w') as file:
            file.writelines(MIX)

    elif n == 4:
        print("Good bye.")
        break

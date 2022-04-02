import math
class Line():

    def __init__(self, coor1, coor2):
        """
        constructor for the class line
        :param coor1: a tuple repressanting a point (x, y)
        :param coor2: a tuple repressanting a point (x, y)
        """
        self.coor1, self.coor2 = coor1, coor2

    def distance(self):
        """
        calculates the distance between two points
        :return: a number that is the distance between two points
        """
        return math.sqrt((self.coor2[0]-self.coor1[0]) ** 2 + (self.coor2[1] - self.coor1[1]) ** 2)

    def slope(self):
        """
        calculates the slope between two points
        :return: a number that is the slope between two points
        """
        return (self.coor2[1] - self.coor1[1]) / (self.coor2[0] - self.coor1[0])


coordinate1 = (3, 2)
coordinate2 = (8, 10)

li = Line(coordinate1, coordinate2)
print(li.distance())
print(li.slope())
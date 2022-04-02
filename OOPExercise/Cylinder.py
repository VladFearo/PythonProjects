import math


class Cylinder:
    pi = math.pi

    def __init__(self, height=1, radius=1):
        """
        constructor for the cylinder class
        :param height: float number the height of the cylinder
        :param radius: float number the radius of the cylinder
        """
        self.height, self.radius = height, radius

    def volume(self):
        """
        calculates the volume of the cylinder
        :return: the volume of the cylinder (pi * r * r * h)
        """
        return self.pi * self.radius * self.radius * self.height

    def surface_area(self):
        """
        calculates the surface area of the cylinder
        :return: the surface area of the cylinder (2 * pi * r * r + 2 * pi * r * h)
        """
        return 2 * self.pi * self.radius * self.radius + 2 * self.pi * self.radius * self.height


c = Cylinder(2, 3)

print(c.volume())
print(c.surface_area())
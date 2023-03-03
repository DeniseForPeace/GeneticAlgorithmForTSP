import math
import random


class City:
    def __init__(self, name, x=None, y=None):
        self.name = name
        self.x = None
        self.y = None

        if x is not None:
            self.x = x
        else:
            self.x = int(random.random() * 200)
        if y is not None:
            self.y = y
        else:
            self.y = int(random.random() * 200)

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def calculate_distance_to(self, city):
        x_distance = abs(self.get_x() - city.get_x())
        y_distance = abs(self.get_y() - city.get_y())
        distance = math.sqrt((x_distance * x_distance) + (y_distance * y_distance))
        return distance

    def __repr__(self):
        return str(self.name)
        # + "(" + str(self.getX()) + "," + str(self.getY()) + ")")

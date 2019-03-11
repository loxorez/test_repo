import math


class Room():
    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b

    def perimeter(self):
        return 2 * (self.side_a + self.side_b)

    def square(self):
        return self.side_a * self.side_b


class Points():
    def __init__(self, x_point, y_point):
        self.x_point = x_point
        self.y_point = y_point

    def coordinates_distance(self):
        return math.sqrt(self.x_point**2 + self.y_point**2)

    def remote_point_distance(self, remote_point):
        return math.sqrt((remote_point.x_point - self.x_point)**2 + (remote_point.y_point - self.y_point)**2)


a = Points(-5, 12)
b = Points(3, 15)
print(a.coordinates_distance())
print(b.coordinates_distance())
print(a.remote_point_distance(b))

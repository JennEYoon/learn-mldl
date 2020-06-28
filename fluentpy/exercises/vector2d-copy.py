""" Copy of book code, with my comments.  """

from math import hypot

class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        # x, y values passed in when class constructor is called  

    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)
        # returns x, y as real numbers?  
    
    def __abs__(self):
        return hypot(self.x, self.y)
        # absolute value of point (x, y)?

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

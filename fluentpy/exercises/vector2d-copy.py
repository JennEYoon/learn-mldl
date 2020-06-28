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
        # absolute value of point (x, y) distance from (0, 0) origin 

    def __bool__(self):
        return bool(abs(self))
        # true if positive?  
    
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)
        # pass in other, allows setting of 2nd private variable  
        # add two numbers 
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
        # vector multiplied by scaler number.  
        # scaler is a passed in private variable  

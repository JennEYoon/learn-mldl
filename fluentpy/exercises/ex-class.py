"""filename: ex-class.py  
Python practice using class 
Date June  5, 2020 update  -- edit 6/20/2020  
    * First pass, has numerous errors.
"""

def MyClass:  
    """Main Class, no parameters passed in, not inherit"""
    # Declare constants shared by all instances of class.
    self.name = 'MyClass'
    # Create an instance upon call.  
    def __init__(self):  
    # Init only has self as a parameter.    
    # No external parameters passed to self om the first example.  
    self.greeting = 'Hello there'
    return self.greeting

def SubClass(MyClass):  
    """Inherited from base class, MyClass"""
    # placeholder - blank for now
    return pass


# Create an instance of MyClass object.  
# No parameters passed on first call.  
my_deck = MyClass()

# Testing:  
# Expect creating of MyClass instance with definitions for
# MyClass.name, self.greeting, and self.name.  
print(my_deck)
print(my_deck.name)
print(MyClass.name)
print(my_deck.greeting)


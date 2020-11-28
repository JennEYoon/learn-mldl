"""filename: ex-class-v4.py  
Python practice using class 
Date Update: June  18, 2020 - edited 6/20/2020  
"""
# Previous mistake, tried to use "def" instead of "class".  

class MyClass:  
    """Main Class, no parameters passed in, not inherit. 
    Notice no "()" at "class MyClass:" title.  
    When there is no class inheritance, no parenthesis.  
    """

    # Declare constants shared by all instances of class.
    name = 'MyClass'

    # Create an instance upon call to class constructor.  
    def __init__(self):  
        # Init only has self as a parameter.    
        # No external parameters are passed in to self.  
        self.greeting = 'Hello there'
        return self.greeting  # Error: should return 'None' instead of string. 

class SubClass(MyClass):  
    """Inherited from main class, MyClass"""
    # placeholder - blank for now

# Create an instance of MyClass object.  
# No parameters passed on first call.  
# Need () here, "MyClass()".  This calls an action, class constructor.  
my_deck = MyClass()

# Testing:  
# Expect creating of MyClass instance with definitions for
# MyClass.name, self.greeting, and self.name.  
print(my_deck)
print(my_deck.name)
print(MyClass.name)
print(my_deck.greeting)
print(MyClass.greeting)  # expect error, not exist 


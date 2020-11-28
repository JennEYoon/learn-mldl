"""filename: ex-class-v6.py  
Python practice using class 
Date Update: June  18, 2020  -- edit 6/20/2020  
"""

# "class" keyword is used to create a class object.  
# "def" keyword is used to define a function object. 

class MyClass:  
    """Main Class, no parameters passed in, not inherit"""
    # Notice there is no () in class definition without inheritance. 

    # Declare constants shared by all instances of class.
    name = 'MyClass'

    # Create an instance upon call.  
    def __init__(self):  
        # Init only has self as a parameter.    
        # No external parameters passed to self.  
        self.greeting = 'Hello there'
        return None

class SubClass(MyClass):  
    """Subordinate class, inherit from MyClass"""
    
    # Create a sub-class instance, with private variable.  
    def __init__(self): 
        print("SubClass init")
        self.greeting = 'I am SubClass. What is your name'
        return None

# Create an instance of MyClass object.  
# No parameters passed on first call, but () added to MyClass to denote action.  
my_deck = MyClass()

# Testing:  
# Expect creating of MyClass instance with definitions for
# MyClass.name, self.greeting, and self.name.  
print(my_deck)    # expect memory object
print(my_deck.name)    # expect 'MyClass' 
print(MyClass.name)    # expect 'MyClass'
print(my_deck.greeting)    # expect 'Hello there'
print(MyClass.greeting)  # expect error, no attribute 'greeting' 

# Create an instance of SubClass, inherits from MyClass. 
your_deck = SubClass()  # expect 'SubClass init' 

print(your_deck.greeting)    # expect 'I am SubClass. What is your name' 
print(your_deck.name)    # expect inherited 'MyClass' 
print(SubClass.name)    # expect inherited 'MyClass' 
print(my_deck.greeting)    # expect unchanged 'Hello there' 

# Everything passed as expected.  

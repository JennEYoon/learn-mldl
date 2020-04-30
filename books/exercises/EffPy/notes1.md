# Effective Python, my notes 

Date: March 9, 2020 


## Chapter 1:  

#### Imports  
 * Ordering of imports, standard library first then third-party modules, then my own modules. 
   Alpahbetize within each sub-sections.  
 * Absolute path instead of relative path.  If relative path is needed, use explicit.  
   ```
   from . import foo  
   from .foo import *  
   # from current folder, import foo module. Useful if there are multiple "foo" modules.  
   ```
   
 * Importing from parent doesn't work, but can import from sub directory.  
   ```from sub import bar ```
   
 * To run from parent, define PATH to parent variable first. Or run something in the parent folder to add it to Python path.   
   ```
   from .. import foo  
   from ..foo import bar  
   # These should work but doesn't.  
   # Try running python from parent directory, then try ..foo from inside a sub/bar module.  
   ``` 
   
 * Add how to set PATH from within python session, save a PATH to variable.    
 
## Chapter 3 Functions  
   
Date: March 10, 2020  

 * Item 19: Returning tuples from function call, use no more than 3 items.  
   It gets confusing and prone to error when 4 or more items are returned.  
   Use Class or pack the tuple into a named variable.  
   
 * Item 20: Prefer raising Error to returning **None**    
   Example uses floating print type divide by zero. None can mean numerator is zero or denomiator is zero.  
   - Example best practice with input data types, output data type, and correct docstring:  
   ``` python  
   def careful_divide(a: float, b: float) -> float:
       """Divides a by b. 
       
       Raises:
           ValueError: When the inputs cannot be divided [by zero]. 
       """
       try:
           return a/b
       except ZeroDivisionError as e:
           raise ValueError('Invalid inputs')
   ```
   
    - Also, example uses print statement string formatting that is new to Python 3.6+.  I need to practice more of these.  
    ```
    print(f'Min: {minimum}, Max: {maximum}')
    print(f'Shortest: {shortest:>4.0%}')
    
    ```

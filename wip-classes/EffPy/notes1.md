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
   
   

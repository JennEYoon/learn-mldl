# Effective Python, my notes 

Date: March 9, 2020 


## Chapter 1:  

#### Imports  
 * Ordering of imports, standard library first then third-party modules, then my own modules. 
   Alpahbetize within each sub-sections.  
 * Absolute path instead of relative path.  If relative path is needed, use explicit.  
   ```
   from . import foo  
   from current folder, import foo module. Useful if there are multiple "foo" modules.  
   ```
   
 * Importing from parent doesn't work, but can import from sub directory.  
   ```from sub import bar ```
 
## Chapter 3 Functions  
   
   

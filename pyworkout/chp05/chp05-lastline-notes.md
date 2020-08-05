# Notes on Chapter 5 -- Files  

  * July 30, 2020 TH 6:30 PM  
     - Need test files to test code.  
     - First attempt at solution below.  Check with StackOverflow or documentation for syntax.  
  
  ```python  
  fpath = ''  
  fname = ''  
  fobj = with open(fpath&fname, 'rb')
  line_one = fobj.readln()  
  print(line_one)
  
  # First attempt.  Need test files to be able to read it.  Use binary file format.  
  
  ### Second attempt notes:  
  
  with open('text.csv', 'rb') as f:  
      lines = f.readlines()  # read everything into memory at once  
      first = lines[0] 
      last = lines[-1]  
      but this takes a long time for large files.  
      
 with open('text.csv', 'rb') as f2:  
     last = f2.seek(2, 1)  # goto end of file, read last line  
     first = f2.seek(0, 1)  # goto beginning of file, read first line.  
  
  ```  
    

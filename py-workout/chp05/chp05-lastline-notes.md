# Notes on Chapter 5 -- Files  

#### July 30, 2020 TH 6:30 PM  
     - Need test files to test code.  
     - First attempt at solution below.  Check with StackOverflow or documentation for syntax.  
  
  ```python  
  fpath = ''  
  fname = ''  
  fobj = with open(fpath&fname, 'rb')
  line_one = fobj.readln()  
  print(line_one)
  
  # First attempt.  Need test files to be able to read it.  Use binary file format.  
  
#### Commands:  
  
  f = open('filename.ext')  
  with open('filename', 'r') as f:  # context block, auto cloase file at the end of block.  
  
  f.read(1)  # read one byte  
  f.readline(1)  # read one line in text file ??
  f.readlines()  # read all lines into memory  
  # readlines(2)  # read first 2 lines into memory ??
  
  lines = f.readlines()  
  first = lines[0]
  last = lines[-1]
  
   ```fseek(offset, whence=0)``` First parameter how many to move, second start from where.  
  f.seek(2, 0)  # move pointer from front of file to 2 bytes forward. 
  f.seek(-2, 2) # move point from back of file, to 2 bytes backward 
  f.seek(0, 1)  # move pointer from current location, to 2 bytes forward.
  
  
#### Second attempt notes:  
  
  with open('text.csv', 'rb') as f:  
      lines = f.readlines()  # read everything into memory at once  
      first = lines[0] 
      last = lines[-1]  
      but this takes a long time for large files.  
      print(first, last)
      
      
 with open('text.csv', 'rb') as f:  
     f.seek(-2, 2)  # move pointer to the end of file, jump back 2 items 
     last = f.read(1)  # read 1 byte.  Does not check for EOL tag.  
     print(last)
     f.seek(0, 1)  # goto beginning of file, read first byte.  
     first = f.read(1)  # read 1 byte  
     print(first)  
     
 ```  
    

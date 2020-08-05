# Chapter 5 exercises, read first and last lines.  
Stack Overflow answers.  
https://stackoverflow.com/questions/3346430/what-is-the-most-efficient-way-to-get-first-and-last-line-of-a-text-file/3346788 

### For small files, can read in whole file to memory, then use indexing in "readlines()" with S. 

```python
with open("myfile.txt") as f:
    lines = f.readlines()
    first_row = lines[0]
    print first_row
    last_row = lines[-1]
    print last_row
```    
use ```f.readlines()[-1]``` insead of new variable.  
0 = First Line, 1 = Second Line, -1 = Last Line, -2 = Line Before Last Line..    
Can also use "reversed"  
  
### For large files, this won't work. Takes too long.  
Read files in binary mode, then use seek to quickly go to the end of file (need estimated max size).  
Use "readline()" WITHOUT S, which read only one line into memory at a time.  

### Here's a modified version of SilentGhost's answer that will do what you want. 
No need for an upper bound for line length here. Offs is multiplied by 2 after each try.  

```python  
with open(fname, 'rb') as fh:
    first = next(fh)
    offs = -100
    while True:
        fh.seek(offs, 2)
        lines = fh.readlines()
        if len(lines)>1:
            last = lines[-1]
            break
        offs *= 2
    print first
    print last
```
    
### To read both the first and final line of a file you could...

>open the file, ...
>... read the first line using built-in readline(), ...  
>... seek (move the cursor) to the end of the file, ...  
>... step backwards until you encounter EOL (line break) and ...  
>... read the last line from there.  

```python
def readlastline(f):
    f.seek(-2, 2)              # Jump to the second last byte.
    while f.read(1) != b"\n":  # Until EOL is found ...
        f.seek(-2, 1)          # ... jump back, over the read byte plus one more.
    return f.read()            # Read all data from this point on.
    
with open(file, "rb") as f:
    first = f.readline()
    last = readlastline(f)
```

 * Jump to the second last byte directly to prevent trailing newline characters to cause empty lines to be returned.  
 * The current offset is pushed ahead by one every time a byte is read so the stepping backwards is done two bytes at a time,   
   past the recently read byte and the byte to read next.

The ```whence``` parameter passed to ```fseek(offset, whence=0)``` indicates that fseek should seek to a position offset bytes relative to...
Second parameter, where to start from, first parameter, how many to move forward/backward.  

 * 0 or os.SEEK_SET = The beginning of the file.
 * 1 or os.SEEK_CUR = The current position.
 * 2 or os.SEEK_END = The end of the file.  
 
As would be expected as the default behavior of most applications, including ```print``` and ```echo```, is to append ***one*** to every line written and has no effect on lines missing trailing newline character.

# Chapter 5 exercises, read first and last lines.  
# Stack Overflow answers.  
# https://stackoverflow.com/questions/3346430/what-is-the-most-efficient-way-to-get-first-and-last-line-of-a-text-file/3346788 

### For small files, can read in whole file to memory, then use indexing in "readlines()" with S. 

with open("myfile.txt") as f:
    lines = f.readlines()
    first_row = lines[0]
    print first_row
    last_row = lines[-1]
    print last_row
    
# use f.readlines()[-1] insead of new variable. 0 = First Line, 1 = Second Line, -1 = Last Line, -2 = Line Before Last Line..    
# Cam also use "reversed"  
  
### For large files, this won't work. Takes too long.  
# Read files in binary mode, then use seek to quickly go to the end of file (need estimated max size). 

# Here's a modified version of SilentGhost's answer that will do what you want. 
# No need for an upper bound for line length here. Offs is increased by 2 after each try.  

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

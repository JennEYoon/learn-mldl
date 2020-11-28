
# Python file to test reading files.  
# Chp 5 last line exercises, Python Workbook. 
# Date: 8/5/2020  

f = open('demofile.txt', 'rt')
blob = f.read() 
print(blob)  
f.close()
# Printed whole file with correct line spacing, 
# and without \n tags

f = open('demofile.txt')
lines = f.readlines() # read all lines into memory
print(lines)  
# printed lines as a list with "" around string and \n at end of each line 

first_line = lines[0]
last_line = lines[-1] 
print(first_line, last_line)
# printed each line without "" but added 1 space between items.

print(first_line)
print(last_line)
# gets rid of extra space? Yes.
f.close()

f = open('demofile.txt')
line_a = f.read(1)  # read one character
print(line_a) 
f.close()

f = open('demofile.txt')
line_b = f.readlines(-2)  # unexpected behavior
print(line_b)
f.close()

# f.readlines()  does not take number as a passed parameter
# f.readlines()[-2] works.  Index into iterable lines object.  
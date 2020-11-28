# Python file to test reading files.  
# Chp 5 last line exercises, Python Workbook. 
# Date: 8/5/2020  

f = open('demofile.txt', 'rt')
blob = f.read() 
print(blob)  
lines = f.readlines() # all lines 
print(lines)  
first_line = lines[0]
last_line = lines[-1] 

line_a = f.read(1)
print(line_a) 

line_b = f.readline(2)  # first 2 lines? Or error? 

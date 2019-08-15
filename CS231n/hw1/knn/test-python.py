import numpy as np
import pandas as pd
lista = [1, 2, 3, 4]
listb = ['A', 'B', 'C', 'D']
listc = ['Elsa', 'Dan', 'Peter', 'Jennifer']
df = pd.DataFrame(zip(lista, listb, listc))  # Make sure to copy the ending "))". Or you will get an error.
print(df)
#  Should print a dataframe, 1st columne is auto-index number, starts with zero.
# row1: 0,  1, 'A', 'Elsa'
# row2: 1,  2, 'B', 'Dan'
# row3: 2,  3, 'C', 'Peter'
# row4: 3,  4, 'D', 'Jennifer'

arr = np.array([lista, listb, listc])
print(arr)
# Should create a 2-D array.  But each row is now a list item.

arr2 = arr.transpose()
print(arr2)
# Should create a 2-D array with each list as a column.
# Note that lista is now a string type ['1', '2', '3', '4'].
# Numpy array needs a single data type unlike a Pandas dataframe.

# If you don't create an account at CodeShare, any edits will be gone after 24 hours.
# This file is on my account for CodeShare.io -- Jennifer Yoon
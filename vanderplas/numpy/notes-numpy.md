# Reading notes on Numpy chapter, VanderPlas.  

#### 1. Broadcasting  

* Broadcasting is stretching the source data to fill in the destination shape.   
A = np.array([0, 1, 2])  
B = 5  

A + B is same as [0, 1, 2] + [5, 5, 5] = [5, 6, 7]  
B is stretched from [5] to [5, 5, 5]  

#### 1. Masks, Fancy Indexing  

mylist = ["Mary", "Tom", "Harry", "Moe"]  
ind = [1, 2]  
A = np.array(mylist)  # Convert list type to ndarray type.  
B = np.array(A[ind])  
B = ["Tom", "Harry"]  

```oython 
  import numpy as np
  mylist = ["Mary", "Tom", "Harry", "Moe"]
  A = np.array(mylist)
  ind = [1, 2]
  B = np.array(A[ind])
  print(B)
  #(output)
  >>>['Tom' 'Harry']
```

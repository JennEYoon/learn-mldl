# Numpy, Python Data Science Handbook.  

### To Do. ~ More practive with ufuncs. 9/1/2019.  

 * (x, newaxis) column  or (newaxis, y) row vector.
  
 * Boolean and masks

 * Sorting.  Fancy Indexing.

### Tasks 9/29/2019  

Currently doing ufunc, broadcasting, fancy indexing. 
Remaining Boolean Masks, Sorting. Pages 60 to 96.  
To Post - Writeup on datasciY.com this week.  
Do not try to directly edit Jupyter Notebooks.  Even though JSON formatting, directly editing seems to corrupt file.
VanderPlas 2.05 boxed image broadcasting example is correct in the notebook.  Numpy.ndarray is reshaped to allow broadcasting rules to work.  Note: When none of the dimension is 1, and the dimensions do not match, error is returned.  Broadcasting only stretches the smaller dimension if that dimension is 1.  (5, 3) + (3, 3) will produce an error.  (5, 3) + (3, 1) will be broadcast.  

### Notes - Andrew Ng DL.AI  

Andrew Ng -- don't use (5, )  Rank 1 ndarray.
Always fully specify dimension  (5, 1) or (1, 5) for Rank 2 ndarray.  
   [[5],  
    [1]]  
    column 2D array  
  
  or [[1], [5]]  row 2D array  
  
Transpose of A is same as A for rank 1 ndarray.  
  
  

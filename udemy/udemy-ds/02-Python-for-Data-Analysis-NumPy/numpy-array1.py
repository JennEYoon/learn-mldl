"""
Udemy - PyDSML - Section 5 Numpy: Numpy arrays
JY 2/19/2019 9am started.
(Udemy class 2/6/2019 bought, June 2016 class recorded Python 3.5.)

Also Quickstart tutorial, Numpy, SciPy.org,
    https://docs.scipy.org/doc/numpy/user/quickstart.html
ndarray is the main object inside numpy library.
.items are attributes of the object.
ndarray.ndim -- axis, dimensions

"""
import numpy as np

# "cast" to 2d array.  np.array is an alias of np.ndarray.
my_mat = [[1, 2, 3], [4, 5, 6], [10, 11, 12]]
my_mat
np.array(my_mat)
my_matarr = np.array(my_mat)  # saves ndarray object to new variable.
my_matarr
type(my_matarr)
my_matarr.ndimar
my_mat3 = [[[0, 1], [11, 12]], [[20, 30], [0, 0]], [[42, 44], [43, 44]]]
m3 = np.array(my_mat3)
m3
m3.ndim
m3.shape
"""
array([[[ 0,  1],
        [11, 12]],

       [[20, 30],
        [ 0,  0]],

       [[42, 44],
        [43, 44]]])
3D array has 3 brackets at start and end!
Think of 2-valued elements as lines start and stop on x, y, z coordinates.
First row of 1st dimension is a line that starts at 0 and ends at 1 in x-axis.
Then first rows of y and z axis are first observations.
Second row of 1st dimension is 2nd line that start at 11 and goes to 12 in x-axis.
Second rows of 2nd and 3rd dimensions are 2nd observations in y and z axis.
np.arange(num) and np.reshape(row, col, depth) useful.
"""

m2 = np.arange(24).reshape(4, 2, 3)
m2
m2.ndim
m2.shape
m2.size

"""  ndarray attributes output & memo

m2 = np.arange(24).reshape(4, 2, 3)
>>> m2
array([[[ 0,  1,  2],
        [ 3,  4,  5]],

       [[ 6,  7,  8],
        [ 9, 10, 11]],

       [[12, 13, 14],
        [15, 16, 17]],

       [[18, 19, 20],
        [21, 22, 23]]])
>>> m2.ndim
3
>>> m2.shape
(4, 2, 3)  # 4 groups, 2 rows, 3 columns
>>> m2.size
24

m2 = np.arange(48).reshape(2, 4, 2, 3)
array([[[[ 0,  1,  2],
         [ 3,  4,  5]],

        [[ 6,  7,  8],
         [ 9, 10, 11]],

        [[12, 13, 14],
         [15, 16, 17]],

        [[18, 19, 20],
         [21, 22, 23]]],


       [[[24, 25, 26],
         [27, 28, 29]],

        [[30, 31, 32],
         [33, 34, 35]],

        [[36, 37, 38],
         [39, 40, 41]],

        [[42, 43, 44],
         [45, 46, 47]]]])
>>> m2.ndim
4  # Dimension is 3rd item from right. 4-dim not 2.
   # Think of it as 2 units of film with (x, y, z, and time) dimensions.
   # Withink each 4D file item, there are 2 observations.
   # Each observation has 3 features, such as start, duration, end.
>>> m2.shape
(2, 4, 2, 3)
   # Shape is 2 groups, 4 dimensions, 2 observations, 3 features per observation.
>>> m2.size
48

"""

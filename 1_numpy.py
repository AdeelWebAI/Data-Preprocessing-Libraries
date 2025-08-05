import numpy as np

# arr1 = np.array([1,2,3,4])     one dimentional array

# arr1 = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])   two dimentional array (4 
# columns and 3 rows)

#===========  numpy function ============== 

# arr1 = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])

# print(arr1.shape)    #shape of the array (3, 4)

# print(arr1.ndim)     #umber of dimentions (2)

# print(arr1.size)     #number of elements in array (12)

# print(arr1.dtype)    #data types of elements in array (int64)

# ========= Generation special arrays ============


# arr = np.zeros((3,3))  # creates matrix of 3 x 3 of zeros

# arr = np.ones((3,3))  # creates matrix of 3 x 3 of zeros

# arr = np.eye(5,k=2, dtype=int)    # https://youtu.be/wEvdhmThxx0?si=iDtRO9Go8IQzuSmL

# arr = np.identity(5, dtype=int)# https://youtu.be/wEvdhmThxx0?si=iDtRO9Go8IQzuSmL

# arr = np.full((4,4),6)

# arr = np.arange(1,10,2)   #  [1 3 5 7 9]

# print(arr)
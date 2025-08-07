# import numpy as np

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


            # . NumPy Operations


# ============ mathematical operations ===============


# arr = np.array([1,2,3,4])  

# print(arr + 2)
# print(arr - 2)
# print(arr * 2)
# print(arr ** 2)
# print(arr / 2)
# print(arr // 2)


# ======== matrix operations ============


# A = np.array([[10,2,3,4], [5,6,7,8]])
# B = np.array([[3,10,11,12],[13,14,15,16]])
# print(A +B)
# print(A - B)
# print(A * B)
# print(A ** B)
# print(A / B)
# print(A // B)
# arr = np.array([[1,2,3,4], [5,6,7,8]])  
# print(arr.T)


# =========== Statistical Functions ================

# arr = np.array([1, 2, 3, 4, 5,6,7,8,9,10,11]) 

# print(np.mean(arr)) # Mean
# print(np.median(arr)) # Median
# print(np.std(arr)) # Standard Deviation
# print(np.var(arr)) # Variance 
# print(np.sum(arr)) # Sum
# print(np.min(arr)) # Minimum Value
# print(np.max(arr)) # Maximum Value


# ========== Indexing and Slicing ==============

# arr = np.array([10,20,30,40,50,60])

# print(arr[1])
# print(arr[1:4])
# print(arr[:3])
# print(arr[-1])


# ========= Slicing in multi dimentional array ===========

# mat = np.array([[10,20,30],
#                 [40,50,60,],
#                 [70,80,90]])
# print(mat[1,2])  # first row and second column (60)
# print(mat[0:2, 1:3])  # first two rows and last two columns
# print(mat[0:2,1:]) 


# ========= Random Numbers ============

# print(np.random.rand(3,3))# 3x3 matrix of random numbers (0 to 1)
# print(np.random.randn(3,3)) # 3x3 matrix of normally distributed random numbers
# np.random.seed()
# print(np.random.randint(1,100,(3,3)))  # 3x3 random integers from 1 to 100

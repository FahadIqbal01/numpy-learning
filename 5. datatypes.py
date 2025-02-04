# Data types in python: string, integer, float, boolean, complex
# Data types in NumPy
# i for integer
# b for boolean
# u for unsigned
# f for float
# c for complex float
# m for timedelta
# M for datetime
# O for object
# S for string
# U for unicode string
# V - memory

# Checking data type of numpy array - dtype
import numpy as np
sharad = np.array(
    [1, 2, 3, 4]
)
print(sharad.dtype)

# Checking data type of numpy array - string
sharad = np.array(
    ['apple', 'banana', 'cherry']
)
print(sharad.dtype)

# Creating array with a defined datatype
sharad = np.array(
    [1, 2, 3, 4], dtype= 'S'
)
print(sharad)
print(sharad.dtype)

# Now we will create an array with data type of 4 byte integer
sharad = np.array(
    [1, 2, 3, 4], dtype='i4'
)
print(sharad)
print(sharad.dtype)

# If a type is given in which the elements can't be casted then numpy will raise error. What if a value can't be converted?
# sharad = np.array(
#     ['a', '2', '3'], dtype= 'i'
# )
# print(sharad.dtype)

# Converting data type on an existing array - astype()
sharad = np.array(
    [1.1, 2.1, 3.1]
)
sharad1 = sharad.astype(int)
print(sharad1)
print(sharad1.dtype)

# Converting data type from integer to boolean
sharad = np.array(
    [1, 0, -3]
)
sharad1 = sharad.astype(bool)
print(sharad1)
print(sharad1.dtype)
# Products: use prod() function
# Here we will find the product of elements of the below array
import numpy as np
sharad = np.array([1, 2, 3, 4])
sharadnew = np.prod(a= sharad)
print(sharadnew)

# Here we will find the product of 2 different arrays
sharad1 = np.array([1, 2, 3, 4])
sharad2 = np.array([5, 6, 7, 8])
sharadnew = np.prod([sharad1, sharad2])
print(sharadnew)

# Product over an axis
sharad1 = np.array([1, 2, 3, 4])
sharad2 = np.array([5, 6, 7, 8])
sharadnew = np.prod([sharad1, sharad2], axis= 1)
print(sharadnew)

# Cummulative product
sharad = np.array([5, 6, 7, 8])
sharadnew = np.cumprod(a= sharad)
print(sharadnew)
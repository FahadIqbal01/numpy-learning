# Summation: Difference-> addition happens between 2 arguments whereas summation happens over n elements.

# Adding two arrays
import numpy as np
sharad1 = np.array([1, 2, 3])
sharad2 = np.array([1, 2, 3])
sharadnew = np.add(sharad1, sharad2)
print(sharadnew)

# Sum the values in 2 arrays
sharad1 = np.array([1, 2, 3])
sharad2 = np.array([1, 2, 3])
sharadnew = np.sum([sharad1, sharad2])
print(sharadnew)

# Summation over an axis. If you specify axis=1, numpy will sum the number in each group.
sharad1 = np.array([1, 2, 3])
sharad2 = np.array([1, 2, 3])
sharadnew = np.sum([sharad1, sharad2], axis= 1)
print(sharadnew)

# Cummulative Sum: means partially adding the elements in the array
sharad = np.cumsum([1, 2, 3, 4])
print(sharad)

# Searching array - you can search for an array for a certain value and return the indexes that got match by using where()

import numpy as np
sharad = np.array(
    [1, 2, 3, 4, 5, 4, 4]
)
sharadnew = np.where(sharad == 4)
print(sharadnew)

# We will find the indexes where values are even
sharad = np.array(
    [1, 2, 3, 4, 5, 6, 7, 8]
)
sharad1 = np.where(sharad % 2 == 0)
print(sharad1)

# We will find the indexes where values are odd
sharad = np.array(
    [1, 2, 3, 4, 5, 6, 7, 8]
)
sharad1 = np.where(sharad % 2 == 1)
print(sharad1)

# SearchSorted() - perform binary search in array
# We will now find the index where the value 7 should be inserted
sharad = np.array(
    [6, 7, 8, 9]
)
sharad1 = np.searchsorted(a= sharad, v= 7)
print(sharad1)

# We will search from right side
sharad = np.array(
    [6, 7, 8, 9]
)
sharad1 = np.searchsorted(a= sharad, v= 7, side= 'right')
print(sharad1)

# How to search multiple values
sharad = np.array(
    [1, 3, 5, 7]
)
sharad1 = np.searchsorted(sharad, [2, 4, 6])
print(sharad1)

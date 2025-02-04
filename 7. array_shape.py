# Shape of an array - Number of elements in each dimensions.
# Now we will try to get the shape of an array

import numpy as np
sharad = np.array(
    [
        [1, 2, 3, 4],
        [5, 6, 7, 8]
    ]
)
print(sharad.shape)

# Now we will create a 5-D array using ndmin
sharad = np.array(
    [1, 2, 3, 4, 5], ndmin= 5
)
print(sharad)
print(sharad.shape)
# sort() - the numpy ndarray function and this will sort a specified array

import numpy as np
sharad = np.array(
    [3, 2, 0, 1]
)
print(np.sort(sharad))

# Sort the array alphabetically
sharad = np.array(
    ["banana", "cherry", "apple"]
)
print(np.sort(sharad))

# Sort the boolean array
sharad = np.array(
    [True, False, True]
)
print(np.sort(sharad))

# Sorting the 2-D array
sharad = np.array(
    [
        [3, 2, 4],
        [5, 0, 1]
    ]
)
print(np.sort(sharad))

# Iterating Arrays - means going through the elements one by one.
# Like for loop.

import numpy as np

# Iterate the elements of 1-D
sharad = np.array(
    [1, 2, 3]
)
for i in sharad:
    print(i)

# Iterate the elements of 2-D
sharad = np.array(
    [
        [1, 2, 3],
        [4, 5, 6]
    ]
)
for i in sharad:
    print(i)

# Iterate on each scalar of the 2-D
sharad = np.array(
    [
        [1, 2, 3],
        [4, 5, 6]
    ]
)
for i in sharad:
    for j in i:
        print(j)

# Iterate on each elements of 3-D array
sharad = np.array(
    [
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
            [10, 11, 12]
        ]
    ]
)
for i in sharad:
    for j in i:
        for k in j:
            print(k)

# Iterating arrays using nditer() function.
# Now we will iterate on each scalar element
sharad = np.array(
    [
        [
            [1, 2],
            [3, 4],
            [5, 6],
            [7, 8]
        ]
    ]
)
for i in np.nditer(sharad):
    print(i)

# Now we will iterate with deifferent step sizes
sharad = np.array(
    [
        [1, 2, 3, 4],
        [5, 6, 7, 8]
    ]
)
for i in np.nditer(sharad[:, ::2]):
    print(i)
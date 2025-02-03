# 1-D Array indexing is same as accessing array element. Start with 0.
import numpy as np

sharad = np.array([1, 2, 3, 4])
print(sharad[0])

# We can geet the third and fourth elements by adding them
sharad = np.array([1, 2, 3, 4])
print(sharad[2] + sharad[3])

# Accessing the 2-D. It is like a rows and columns.
sharad = np.array(
    [
        [1, 2, 3, 4, 5], 
        [6, 7, 8, 9, 10]
    ])
print("2nd element in first row", sharad[0, 1])
print("5th element in second row", sharad[1, 4])

# Accessing the 3-D, same as accessing
sharad = np.array(
    [
        [
            [1, 2, 3],
            [4, 5, 6]
        ],
        [
            [7, 8, 9],
            [10, 11, 12]
        ]
    ]
)
print(sharad[0, 1, 2])
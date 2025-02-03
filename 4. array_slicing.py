# Slicing array - Slicing in python means taking elements from one given to another index.
# [start: end], [start, end, step]

# Now we will slice elements from 1 to 5
import numpy as np
sharad = np.array(
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
)
print(sharad[1: 5])

# Now we will slice from index 4 to the end value
sharad = np.array(
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
)
print(sharad[4:])

# Now we will slice elements from starting to index 4
sharad =  np.array(
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
)
print(sharad[:4])

# Negative Slicing - Index 3 to end
sharad =  np.array(
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
)
print(sharad[-6: -1])

# Step: we will use step value to determine the step of the slicing.
# Return every other value from index 1 to 9
sharad =  np.array(
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
)
print(sharad[1::2])

# Now return every other number from the entire array
sharad =  np.array(
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
)
print(sharad[::2])

# Slicing 2-D array
sharad =  np.array(
    [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10]
    ]
)
print(sharad[1, 1:4])
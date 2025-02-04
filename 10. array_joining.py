# Joining the numpy arrays - here for this we will pass concatenate()

import numpy as np
sharad = np.array(
    [1, 2, 3]
)
sharad1 = np.array(
    [4, 5, 6]
)
sharad2 = np.concatenate((sharad, sharad1))
print("Shape:", sharad2.shape)
print("Concatenate 1-D array:\n", sharad2)

# Joining of 2-D arrays along with rows (axis=0)
sharad = np.array(
    [
        [1, 2], [3, 4]
    ]
)
sharad1 = np.array(
    [
        [5, 6], [7, 8]
    ]
)
sharad2 = np.concatenate((sharad, sharad1), axis= 1)
print("Concatenate 2-D array:\n", sharad2)

# Joining array using the stack()
sharad = np.array(
    [1, 2, 3]
)
sharad1 = np.array(
    [4, 5, 6]
)
sharad2 = np.stack((sharad, sharad1), axis= 1)
print("Stacking:\n", sharad2)

# Stacking along with rows: hstack()
sharad = np.array(
    [1, 2, 3]
)
sharad1 = np.array(
    [4, 5, 6]
)
sharad2 = np.hstack((sharad, sharad1))
print("Stacking:\n", sharad2)

# Stacking along with columns: vstack()
sharad = np.array(
    [1, 2, 3]
)
sharad1 = np.array(
    [4, 5, 6]
)
sharad2 = np.vstack((sharad, sharad1))
print(sharad2)

# Stacking along with height(depth): dstack()
sharad = np.array(
    [1, 2, 3]
)
sharad1 = np.array(
    [4, 5, 6]
)
sharad2 = np.dstack((sharad, sharad1))
print(sharad2)

sharad = np.array(
    [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
)

sharad1 = np.array(
    [[[9, 10], [11, 12]], [[13, 14], [15, 16]]]
)
sharad2 = np.concatenate((sharad, sharad1), axis= 2)
print("Concatenation:\n", sharad2)
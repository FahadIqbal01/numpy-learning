# Reshaping means changing the shape of an array like adding or removing the elements.
import numpy as np

# Reshaping from 1-D to 2-D
sharad = np.array(
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
)
sharad1 = sharad.reshape(4, 3)
print(sharad1)

# Reshaping from 1-D to 3-D
sharad = np.array(
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
)
sharad1 = sharad.reshape(2, 2, 3)
print(sharad1)

# Unknown dimension - you are only allowed to have one unknown dimension. Pass -1
sharad = np.array(
    [1, 2, 3, 4, 5, 6, 7, 8]
)
sharad1 = sharad.reshape(2, 2, -1)
print(sharad1)

# Flattening the array by converting the mutidimensional array into 1-D
sharad = np.array(
    [
        [1, 2, 3],
        [4, 5, 6]
    ]
)
sharad1 = sharad.reshape(-1)
print(sharad1)

# There are alot of functions for changing the shapes of an array like flatten, ravel and also rearranging the elements rot90, flip, fliplr, flipud. They all are actually comes under advanced NumPy.
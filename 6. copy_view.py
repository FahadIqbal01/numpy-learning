# Difference between numpy array copy and view
# We will make a copy, change in original array, and display both.

import numpy as np
sharad = np.array(
    [1, 2, 3, 4, 5]
)
sharad1 = sharad.copy()
sharad[0] = 12

print(sharad)
print(sharad1)

# Now we will make a view, change in original array and display both.
sharad = np.array(
    [1, 2, 3, 4, 5]
)
sharad1 = sharad.view()
sharad[0] = 21

print(sharad)
print(sharad1)
# Finding LCM
# Here we will find the LCM of the 2 numbers

import numpy as np
sharad1 = 4
sharad2 = 6
sharadnew = np.lcm(sharad1, sharad2)
print(sharadnew)

# Finding LCM in the array
sharad = np.array([3, 6, 9])
sharadnew = np.lcm.reduce(sharad)
print(sharadnew)

# Here we will find the LCM of an array where it contains integers 1 to 10
sharad = np.arange(1, 11)
sharadnew = np.lcm.reduce(sharad)
print(sharadnew)
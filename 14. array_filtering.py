# Getting some elements out of an existing array and creating a new array is called filtering.
# A boolen index list is a list of boolean corresponding to indexes in the array. (True and False)
# Create an array from the element on index 0 to 2

import numpy as np
sharad = np.array(
    [41, 42, 43, 44]
)
sharad1 = [True, False, True, False]
finalSharad = sharad[sharad1]
print(finalSharad)

# We will create a filter array that will return only values higher than 42
sharad = np.array(
    [41, 42, 43, 44]
)
filter = []
for element in sharad:
    if element > 42:
        filter.append(True)
    else:
        filter.append(False)
filtered_array = sharad[filter]
print(filtered_array)
print(filter)

# Create a filter array that will return only even elements from the original array
sharad = np.array(
    [1, 2, 3, 4, 5, 6, 7]
)
filter = []
for element in sharad:
    if element % 2 == 0:
        filter.append(True)
    else:
        filter.append(False)
filtered_array = sharad[filter]
print(filter)
print(filtered_array)

# We will also create filter directly from array
sharad = np.array(
    [41, 42, 43, 44]
)
sharad1 = sharad > 42
sharad2 = sharad[sharad1]
print(sharad2)
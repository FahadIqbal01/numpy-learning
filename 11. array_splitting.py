# Splitting arrays in numpy - it is Reverse of Joining, breaking the array
# array_split()

# Split array in 3 parts
import numpy as np
sharad = np.array(
    [1, 2, 3, 4, 5, 6]
)
sharadnew = np.array_split(ary= sharad, indices_or_sections= 3)
print(sharadnew, type(sharadnew))

# Now we will split this array in 4 parts
sharad = np.array(
    [1, 2, 3, 4, 5, 6]
)
sharadnew = np.array_split(ary= sharad, indices_or_sections= 4)
print("\n")
print(sharadnew)

# Splitting the 2-D array
sharad = np.array(
    [
        [1, 2], 
        [3, 4], 
        [5, 6], 
        [7, 8], 
        [9, 10], 
        [11, 12]
    ]
)
sharadnew = np.array_split(ary= sharad, indices_or_sections= 3)
print('\n')
print(sharad.shape, sharad.ndim)
print(sharadnew[0], sharadnew[0].shape)

# Splitting the 2-D array in 3 2-D arrays
sharad = np.array(
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8 ,9],
        [10, 11, 12],
        [13, 14, 15],
        [16, 17, 18]
    ]
)
sharadnew = np.array_split(ary= sharad, indices_or_sections= 3)
print('\n')
print(sharad.shape, sharad.ndim)
print(sharadnew)

# Splitting the 2=D array into 3 2-D arrays along with axis
sharad = np.array(
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8 ,9],
        [10, 11, 12],
        [13, 14, 15],
        [16, 17, 18]
    ]
)
sharadnew = np.array_split(ary= sharad, indices_or_sections= 3, axis= 1)
print(sharadnew)

# Alternate solutions is using hsplit() or opposite hstack()
sharad = np.array(
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8 ,9],
        [10, 11, 12],
        [13, 14, 15],
        [16, 17, 18]
    ]
)
sharadnew = np.hsplit(ary= sharad, indices_or_sections= 3)
print(sharadnew)
# Permutations refers to arrangement of elements
# NumPy random module provides 2 methods: shuffle() and permutation()

# We will randomly shuffle elements for the array
import numpy as np
sharad = np.array(
    [1, 2, 3, 4, 5]
)
np.random.shuffle(x= sharad)
print(sharad)

# We will generate the permutation of elements for the array
sharad = np.array(
    [1, 2, 3, 4, 5]
)
print(np.random.permutation(sharad))
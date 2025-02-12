# ufunc - universal function and they are actually numpy functions that operates on the ndarray objects.
# ufunc also takes additional arguments - where, dtype and out
# Vectorization - Converting the iterative statements into a vector based statement.

# Example without ufunc, here we will use python inbuilt zip()
x = [1, 2, 3, 4]
y = [5, 6, 7, 8]
z = []

for i, j in zip(x, y):
    z.append(i + j)

print(z)

# With ufunc, we will now use add() function
import numpy as np

x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = np.add(x, y)

print(z)
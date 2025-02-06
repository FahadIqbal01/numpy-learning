# Random meaning something that can't be predicted logically
# Now we will generate a random number from 0 to 100
import numpy as np
sharad = np.random.randint(0, 100)
print(sharad)

# You can also generate float via rand() from 0 to 1
sharad = np.random.rand()
print(sharad)

# You can also generate Random array
# We will generate a 1-D array containing 5 random integers from 0 to 100
sharad = np.random.randint(0, 100, size=5)
print(sharad)

# We will generate a 2-D array with 3 rows each containing 5 random ints from 0 to 100
sharad = np.random.randint(0, 100, size=(3, 5))
print(sharad)

# We will generate a 1-D array containing 5 random floats from 0 to 1
sharad = np.random.rand(5)
print(sharad)

# We will generate a 2-D array with 3 rows each containing 5 random floats from 0 to 100
sharad = np.random.rand(3, 5)
print(sharad)

# We will generate random numbers from an array
# choice()
sharad = np.random.choice([3, 5, 7, 9, 1, 4, 6])
print(sharad)

# We will generate random numbers from a 2-D array
sharad = np.random.choice([3, 5, 7, 9, 1, 4, 6], size=(4, 5))
print(sharad)
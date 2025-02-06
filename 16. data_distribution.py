# Data distribution is a list of all possible value and how often each value occurs.
# Such lists are important when working with statistics and data science

# Random Distribution : Probabilty Function

# Now we will generate 1-D array with 100 values where each value has to be 3 5 7 9
# The probability for the value 3 is set to be 0.1
# The probability for the value 5 is set to be 0.3
# The probability for the value 7 is set to be 0.6
# The probability for the value 9 is set to be 0
# The sum of all probabilities should be "1"

import numpy as np
sharad = np.random.choice(a=[3, 5, 7, 9], size= 100, p=[0.1, 0.3, 0.6, 0.0])
print(sharad)

# Now we will generate 21-D array with 3 rows each with 5 values where each value has to be 3 5 7 9
sharad = np.random.choice(a=[3, 5, 7, 9], size=(3, 5), p=[0.1, 0.3, 0.6, 0.0])
print(sharad)
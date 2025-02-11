# Poisson distribution - it estimates how many times an event can happen
# Param - lam(number of occurences or rate), size

# Generate a random 1*10 distribution for the occurence of 2

import numpy as np
sharad = np.random.poisson(lam= 2, size= 10)
print(sharad)

# Visualization of poisson distribution
import matplotlib.pyplot as pypl
import seaborn as sb

sb.displot(data= np.random.poisson(lam= 2, size= 1000))
pypl.show()
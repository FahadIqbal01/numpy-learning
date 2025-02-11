# Exponential Distribution: It is used for describing the time till next event that is like failure or success
# Parameters - scale(inverse of rate(see lam poisson dist)) and size

# Here we will draw a sample for exponential distribution with 2.0 scale and size (2, 3)

import numpy as np
sharad = np.random.exponential(scale= 2.0, size= (2, 3))
print(sharad)

# Visualization of Exponential Distribution
import matplotlib.pyplot as pypl
import seaborn as sb
sb.displot(data=np.random.exponential(size= 1000), kind='kde')
pypl.show()
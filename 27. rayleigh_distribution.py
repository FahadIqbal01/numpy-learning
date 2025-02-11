# Rayleigh Distribution - It is used in Signal Processing
# Parameters - scale(standard deviation, how flat the distribution is) and size

# Sample for RL with scale of 2.0 with size (2, 3)
import numpy as np
sharad = np.random.rayleigh(scale= 2, size= (2, 3))
print(sharad)

# Visualization of Rayleigh Distribution
import matplotlib.pyplot as pypl
import seaborn as sb

sb.displot(data= np.random.rayleigh(size= 1000), kind='kde')
pypl.show()
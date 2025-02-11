# Logistic Distribution - Describe growth it is basically important in regression and machine learning
# Params - loc(mean 0), scale(standard deviation 1) and size

import numpy as np
sharad = np.random.logistic(loc= 1, scale= 2, size= (2, 3))
print(sharad)

# Visualization of Logistic Distribution
import matplotlib.pyplot as pypl
import seaborn as sb

sb.displot(np.random.logistic(size= 1000), kind='kde')
pypl.show()
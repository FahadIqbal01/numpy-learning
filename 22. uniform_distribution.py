# Uniform Distribution - It is only made for probability
# Params - a(lower bound 0.0), b(upper bound 1.0) and size

import numpy as np
sharad = np.random.uniform(size= (2,3))
print(sharad)

# Visualization of Uniform Distribution
import matplotlib.pyplot as pypl
import seaborn as sb

sb.distplot(a= np.random.uniform(size= 1000), hist= False)
pypl.show()
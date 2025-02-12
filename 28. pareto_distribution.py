# Pareto Distribution : 80:20 ratio. (20% Factors Cause 80% Outcome)
# Parameters - a(scale) and size

# Sample for Pareto Distribution with shape 2 and size 2*3
import numpy as np
sharad = np.random.pareto(a= 2.0, size= (2,3))
print(sharad)

# Visualization of Pareto Distribution
import matplotlib.pyplot as pypl
import seaborn as sb
sb.displot(data= np.random.pareto(a= 2.0, size= 1000), kind='hist')
pypl.show()
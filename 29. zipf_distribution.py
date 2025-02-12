# Zipf Distribution - It's definition is like... Common word in English has occurs nearly 1/5 times as of the most hindi words
# Parameters - a(dist param) and size

# Sample for Zipf Distribution with a as 2 with size 2*3
import numpy as np
sharad = np.random.zipf(a= 2, size=(2, 3))
print(sharad)

# Visualization of Zipf Distribution
import matplotlib.pyplot as pypl
import seaborn as sb
sharad = np.random.zipf(a= 2, size= 1000)
sb.displot(data= sharad[sharad < 10], kind='hist')
pypl.show()
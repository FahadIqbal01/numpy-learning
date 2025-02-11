# Binomial Distribution - Discrete Distribution - Binary Output
# param - n(number of trials), p(probabilities) and size(shape - returned array)

# Given 10 trial for a coin which will generate 10 data points
import numpy as np
sharad = np.random.binomial(n= 10, p= 0.5, size= 10)
print(sharad)

# Visualization of Binomial Distribution
import matplotlib.pyplot as pypl
import seaborn as sb

sharad = np.random.binomial(n= 10, p= 0.5, size= 1000)
sb.displot(data= sharad, kind= 'hist')
pypl.show()

# Difference between normal and binomial distributions - normal (continuous) and binomial (discrete)
import numpy as np
import matplotlib.pyplot as pypl
import seaborn as sb

sb.displot(data= np.random.normal(loc= 50, scale= 5, size= 1000), kind= 'kde')
sb.displot(data= np.random.binomial(n= 100, p= 0.5, size= 1000), kind= 'kde')
pypl.show()
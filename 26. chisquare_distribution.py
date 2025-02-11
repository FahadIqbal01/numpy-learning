# Chi Square Distribution - It is basically used as a basis to verify the hypothesis
# Params - df(Degree of Freedom) and size

# Sample for chi quared distribution with df 2 and size (2, 3)
import numpy as np
sharad = np.random.chisquare(df= 2.0, size=(2, 3))
print(sharad)

# Visualization of Chi Square
import matplotlib.pyplot as pypl
import seaborn as sb
sb.displot(data= np.random.chisquare(df= 1, size= 1000), kind='kde')
pypl.show()
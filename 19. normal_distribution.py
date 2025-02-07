# Normal (Gaussian) Distribution - very important.
# random.normal() method - loc(mean), scale(standard deviation), size

# We are generating a random normal distribution of size 2 * 3
import numpy as np
sharad = np.random.normal(size= (2, 3))
print(sharad)

# We are generating a random normal distribution of size 2 * 3 with mean at 1 and standard deviation of 2.
sharad = np.random.normal(loc= 1, scale= 2, size=(2, 3))
print(sharad)

# Visualization of Normal Distribution
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(data= np.random.normal(size= 1000), kind='kde')
plt.show()

# The curve of normal ditribution is also called as bell curve
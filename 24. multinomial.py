# Multinomial Distribution - It is a generalization of binomial distribution.
# Params - n(number of outcomes), pvals(list of possibilities) and size

# Draw out a sample for dice roll
import numpy as np
sharad = np.random.multinomial(n= 6, pvals= [1/6, 1/6, 1/6, 1/6, 1/6, 1/6])
print(sharad)
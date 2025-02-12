# Finding GCD (Greatest Common Denominator) or HCF (Highest Common Factor)
# We will find the HCF of the below 2 numbers.

import numpy as np
sharad1 = 6
sharad2 = 9
sharadnew = np.gcd(sharad1, sharad2)
print(sharadnew)

# Finding the HCF/GCD of an array
sharad1 = np.array([20, 8, 32, 16, 36])
sharadnew = np.gcd.reduce(sharad1)
print(sharadnew)
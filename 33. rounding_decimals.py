# Rounding Decimals: there are 5 ways of rounding off the decimal in numpy.
# truncation, fix, rounding, floor, ceil

# Truncation: trunc() and fix()
# Here we are truncating the below array, these commands remove the decimals and return the float number closest to zero
import numpy as np
sharad = np.trunc([-3.1666, 3.6667])
print(sharad)

# fix() example
import numpy as np
sharad = np.fix([-3.1666, 3.6667])
print(sharad)

# Rounding: the around() function increments preceding digit or decimal by nearest to 1: if n > 5 =1 or n < 5 =0
sharad = np.around(-3.1666, decimals= 2)
print(sharad)

# Floor: round off decimals to the lower integer
sharad = np.floor([-3.166,  3.666])
print(sharad)

# Ceiling: round off to the upper integer
sharad = np.ceil([-3.166, 3.666])
print(sharad)
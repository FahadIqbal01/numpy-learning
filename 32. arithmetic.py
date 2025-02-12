# Arithmetic Operators - +, -, *, /
# Arguments of frompyfunc(): function, inputs and outputs

# Here now we will use add()
import numpy as np
sharad1 = np.array([1, 2, 3, 4, 5])
sharad2 = np.array([6, 7, 8, 9, 10])
sharadnew = np.add(sharad1, sharad2)
print(sharadnew)

# Subtracting the value
sharad1 = np.array([1, 2, 3, 4, 5])
sharad2 = np.array([6, 7, 8, 9, 10])
sharadnew = np.subtract(sharad1, sharad2)
print(sharadnew)

# Multiplying the value
sharad1 = np.array([1, 2, 3, 4, 5])
sharad2 = np.array([6, 7, 8, 9, 10])
sharadnew = np.multiply(sharad1, sharad2)
print(sharadnew)

# Dividing the value
sharad1 = np.array([1, 2, 3, 4, 5])
sharad2 = np.array([6, 7, 8, 9, 10])
sharadnew = np.divide(sharad1, sharad2)
print(sharadnew)

# power() function raises the value from the first array to the power of the values of the 2nd array and return the new array.
sharad1 = np.array([10, 20, 30, 40, 50, 60])
sharad2 = np.array([3, 5, 6, 8, 2, 33])
sharadnew = np.power(sharad1, sharad2)
print(sharadnew)

# Remainder - mod() and remainder() functions return the remainder of the first array corresponding to the second array
sharad1 = np.array([10, 20, 30, 40, 50, 60])
sharad2 = np.array([3, 7, 9, 8, 2, 33])
# sharadnew = np.mod(sharad1, sharad2)
sharadnew = np.remainder(sharad1, sharad2)
print(sharadnew)

# Quotient and mod(remainder)
# divmod() function return both quotient and mod
sharad1 = np.array([10, 20, 30, 40, 50, 60])
sharad2 = np.array([3, 7, 9, 8, 2, 33])
sharadnew = np.divmod(sharad1, sharad2)
print(sharadnew)

# absolute() and abs() - do the same function but here we should use absolute() to avoid confusion with inbuilt function math.abs()
sharad = np.array([-1, -2, -3, -4, -5])
sharadnew = np.absolute(sharad)
print(sharadnew)
# To create your own ufunction, you have to define a python function, like you do in normal function in python, then you add it to the numpy function with frompyfunc() method.
# Arguments of frompyfunc(): function, inputs and outputs

# Create our own ufunc for addition
import numpy as np

def my_add(x, y):
    return x + y

my_add = np.frompyfunc(my_add, 2, 1)

print(my_add([1, 2, 3, 4], [5, 6, 7, 8]))
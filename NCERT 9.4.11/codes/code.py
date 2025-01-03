#importing required libraries
import matplotlib.pyplot as plt
import math
from ctypes import *

#loading the shared obect file
vals = CDLL('./vals.so')

#assigning the C functions in Python
x_val = vals.x_val
y_val = vals.y_val

#setting the result type of the C-Python functions
x_val.restype = c_float
y_val.restype = c_float

#setting initial coordinates as the point given in the question
x = 0.0
y = 1.0
plt.plot(x,y,'ro')

#initialising h
h = 0.1

#iterating to generate more points on the curve using finite differences and plotting each indivdual point
for i in range(100):
    y = y_val(c_float(x), c_float(y), c_float(h))
    x = x_val(c_float(x), c_float(h))
    plt.plot(x,y,'ro')

#setting up the labels and grid for the plot
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Approximate Plot')
plt.grid(True)

#saving the generated plot
plt.savefig('../figs/fig.pdf')

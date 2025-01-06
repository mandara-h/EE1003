#importing required libraries
import matplotlib.pyplot as plt
import math
from ctypes import *

#loading the shared obect file
vals = CDLL('./vals.so')

#assigning the C functions in Python
x_func = vals.x
y_func = vals.y
y_act = vals.y_val

#setting the result type of the C-Python functions
x_func.restype = c_float
y_func.restype = c_float
y_act.restype = c_float

#setting initial coordinates as the point given in the question
x = 1.0
y = 0.0
plt.plot(x,y,'ro', label='Simulation Plot')
plt.plot(x,y,'bo', label='Theoretical Plot')

#initialising h
h = 0.1

#iterating to generate more points on the curve using finite differences and plotting each indivdual point
for i in range(100):
    y = y_func(c_float(x), c_float(y), c_float(h)) #y-coordinate of simulation plot
    y_val = y_act(c_float(x)) #y-coordinate of theoretical plot
    x = x_func(c_float(x), c_float(h)) #x-coordinate of simulation plot and theoretical plot
    plt.plot(x,y,'ro') #plotting simulation curve
    plt.plot(x,y_val,'bo') #plotting theoretical curve

#setting up the labels and grid for the plot
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)

#adding a legend
plt.legend()

#saving the generated plot
plt.savefig('../figs/fig.pdf')

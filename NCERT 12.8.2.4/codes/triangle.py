#importing required libraries
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from ctypes import *

#loading the shared obect file
vals = CDLL('./functions.so')

# Store triangle vertices
triangle_vertices = []

#assigning the C functions in Python
x_func = vals.x
y_funcAB = vals.yAB
y_funcBC = vals.yBC
y_funcCA = vals.yCA
y_actAB = vals.y_valAB
y_actBC = vals.y_valBC
y_actCA = vals.y_valCA

#setting the result type of the C-Python functions
x_func.restype = c_float
y_funcAB.restype = c_float
y_actAB.restype = c_float
y_funcBC.restype = c_float
y_actBC.restype = c_float
y_funcCA.restype = c_float
y_actCA.restype = c_float

#plotting line AB
x = -1
y = 0
h = 0.02
triangle_vertices.append((x, y))  # Add first vertex
for i in range(100):
    y = y_funcAB(c_float(y), c_float(h)) #y-coordinate of simulation plot
    y_val = y_actAB(c_float(x)) #y-coordinate of theoretical plot
    x = x_func(c_float(x), c_float(h)) #x-coordinate of simulation plot and theoretical plot
    plt.plot(x,y,'ro') #plotting simulation curve
    plt.plot(x,y_val,'bo') #plotting theoretical curve

#plotting line BC
x = 1
y = 3
h = 0.02
triangle_vertices.append((x, y))  # Add second vertex
plt.plot(x,y,'ro', label='Simulation Plot')
plt.plot(x,y,'bo', label='Theoretical Plot')
for i in range(100):
    y = y_funcBC(c_float(y), c_float(h)) #y-coordinate of simulation plot
    y_val = y_actBC(c_float(x)) #y-coordinate of theoretical plot
    x = x_func(c_float(x), c_float(h)) #x-coordinate of simulation plot and theoretical plot
    plt.plot(x,y,'ro') #plotting simulation curve
    plt.plot(x,y_val,'bo') #plotting theoretical curve

#plotting line CA
x = -1
y = 0
h = 0.04
triangle_vertices.append((3,2)) #close the loop
for i in range(100):
    y = y_funcCA(c_float(y), c_float(h)) #y-coordinate of simulation plot
    y_val = y_actCA(c_float(x)) #y-coordinate of theoretical plot
    x = x_func(c_float(x), c_float(h)) #x-coordinate of simulation plot and theoretical plot
    plt.plot(x,y,'ro') #plotting simulation curve
    plt.plot(x,y_val,'bo') #plotting theoretical curve

#shade the interior of the triangle
triangle = patches.Polygon(triangle_vertices, closed=True, color='green', alpha=0.5, label='Triangle Area')
plt.gca().add_patch(triangle)

#setting up axes and grid for the plot
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)

#adding a legend
plt.legend()

#saving the generated plot
plt.savefig('../figs/triangle.pdf')

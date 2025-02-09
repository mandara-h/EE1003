import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the shared library
lu_solver = ctypes.CDLL("./lu_solver.so")

# Define argument and return types
lu_solver.solve_lu.argtypes = [ctypes.POINTER(ctypes.c_double)]
lu_solver.solve_lu.restype = None

# Create an array to store results
solution = (ctypes.c_double * 2)()

# Call the C function
lu_solver.solve_lu(solution)

# Extract solution values
p, q = solution[0], solution[1]

# Plot the equations
x = np.linspace(-10, 10, 400)
y1 = (5 + 2*x) / 7  # Rearranged -2p + 7q = 5
y2 = (15 - 7*x) / 8  # Rearranged 7p + 8q = 15

plt.figure(figsize=(8, 6))
plt.plot(x, y1, label='-2p + 7q = 5', color='blue')
plt.plot(x, y2, label='7p + 8q = 15', color='red')
plt.scatter(p, q, label='Point Of Intersection', color='yellow', marker='o', s=100, zorder=3)
plt.text(p + 0.3, q, f'({p:.2f}, {q:.2f})', fontsize=12, verticalalignment='bottom')

plt.xlabel('p')
plt.ylabel('q')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True, linestyle='--', linewidth=0.5)
plt.legend()
plt.savefig('../figs/fig.pdf')


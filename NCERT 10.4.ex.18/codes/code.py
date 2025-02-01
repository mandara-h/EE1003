import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the shared library
math_lib = ctypes.CDLL("./math_functions.so")  # Use "math_functions.dll" on Windows

# Define function prototypes
math_lib.f.argtypes = [ctypes.c_double]
math_lib.f.restype = ctypes.c_double

math_lib.newton_raphson.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_int]
math_lib.newton_raphson.restype = ctypes.c_double

math_lib.companion_matrix_root.argtypes = []
math_lib.companion_matrix_root.restype = ctypes.c_double

math_lib.fixed_point_iteration.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_int]
math_lib.fixed_point_iteration.restype = ctypes.c_double

# Compute values
x_min = 1/3  # Minimum of the function
x_nr = math_lib.newton_raphson(0, 1e-6, 100)  # Newton-Raphson root
x_cm = math_lib.companion_matrix_root()  # Companion matrix root
x_fp = math_lib.fixed_point_iteration(0, 1e-6, 100)  # Fixed-point iteration root

# Function to evaluate f(x)
def f_python(x):
    return math_lib.f(x)

# Plot the function
x_vals = np.linspace(-1, 1, 400)
y_vals = np.vectorize(f_python)(x_vals)

plt.figure(figsize=(8, 6))
plt.plot(x_vals, y_vals, label="f(x) = 3x² - 2x + 1/3", color='blue')
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')

# Mark the computed roots with different sizes
plt.scatter(x_min, f_python(x_min), color='green', label='Theoretical Root', s=250, zorder=3)
plt.scatter(x_nr, f_python(x_nr), color='red', label='Newton-Raphson Root', s=200, zorder=3)
plt.scatter(x_cm, f_python(x_cm), color='purple', label='Companion Matrix Root', s=150, zorder=3)
plt.scatter(x_fp, f_python(x_fp), color='orange', label='Fixed-Point Root', s=100, zorder=3)

# Labels and legend
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.savefig('../figs/fig.pdf')


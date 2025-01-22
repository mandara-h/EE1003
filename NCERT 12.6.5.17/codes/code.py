import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the shared object file
gradient_ascent = ctypes.CDLL('./gradient_ascent.so')

# Define argument and return types for the C functions
gradient_ascent.volume.restype = ctypes.c_double
gradient_ascent.volume.argtypes = [ctypes.c_double]

gradient_ascent.volume_derivative.restype = ctypes.c_double
gradient_ascent.volume_derivative.argtypes = [ctypes.c_double]

gradient_ascent.gradient_ascent.restype = ctypes.c_double
gradient_ascent.gradient_ascent.argtypes = [
    ctypes.c_double,  # x0
    ctypes.c_double,  # alpha
    ctypes.c_double,  # epsilon
    ctypes.c_int      # max_iter
]

# Parameters for gradient ascent
x0 = 1.0       # Initial guess
alpha = 0.01   # Step size
epsilon = 1e-6 # Convergence tolerance
max_iter = 1000

# Call the gradient ascent function
x_opt = gradient_ascent.gradient_ascent(
    ctypes.c_double(x0),
    ctypes.c_double(alpha),
    ctypes.c_double(epsilon),
    ctypes.c_int(max_iter)
)

# Compute the maximum volume
max_volume = gradient_ascent.volume(x_opt)

# Plotting the volume function V(x)
x_values = np.linspace(0.1, 8.9, 100)  # x range for plotting
v_values = [gradient_ascent.volume(ctypes.c_double(x)) for x in x_values]

plt.figure(figsize=(8, 6))
plt.plot(x_values, v_values, label=r"$V(x)$", color='blue')
plt.scatter([x_opt], [max_volume], color='green', label=f"Max at x = {x_opt:.2f}, V = {max_volume:.2f}")
plt.xlabel("x (side length cut off in cm)")
plt.ylabel("Volume $V(x)$ (cubic cm)")
plt.legend()
plt.grid()
plt.savefig('../figs/fig.pdf')

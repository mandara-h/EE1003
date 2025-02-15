import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the shared object file
lib = ctypes.CDLL('./dice_simulation.so')

# Set the return types and argument types for the C functions
lib.seed_random.restype = None
lib.roll_die.restype = ctypes.c_int
lib.simulate_AB.restype = ctypes.c_int
lib.simulate_AB.argtypes = [ctypes.c_int]
lib.simulate_die_rolls.restype = None
lib.simulate_die_rolls.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int)]

# Seed the random number generator
lib.seed_random()

# Simulate Pr(AB)
num_simulations = 1000
rolls_per_simulation = 10000
results_AB = []
for _ in range(num_simulations):
    count_AB = lib.simulate_AB(rolls_per_simulation)
    probability_AB = count_AB / rolls_per_simulation
    results_AB.append(probability_AB)

# Create Pr(AB) stem plot
plt.figure(figsize=(10, 6))
plt.stem(range(num_simulations), results_AB, linefmt='C0-', markerfmt='C0o')
plt.xlabel('Simulation Number')
plt.ylabel('Pr(AB)')
plt.ylim(0, max(results_AB) * 1.1 + 1e-10)
plt.grid(True, alpha=0.3)
plt.savefig('../figs/Pr_AB_simulation_results.pdf')
plt.close()

# Simulate die rolls
num_rolls = 1000000
results = (ctypes.c_int * 10)()
lib.simulate_die_rolls(num_rolls, results)

# Calculate probabilities
probabilities = [count / num_rolls for count in results]

# Create PMF stem plot for die rolls
plt.figure(figsize=(10, 6))
plt.stem(range(1, 11), probabilities, linefmt='C0-', markerfmt='C0o')
plt.xlabel('Outcome')
plt.ylabel('Probability')
plt.xticks(range(1, 11))
plt.ylim(0, max(probabilities) * 1.1 + 1e-10)
plt.grid(True, alpha=0.3)
plt.savefig('../figs/die_roll_pmf.pdf')
plt.close() 

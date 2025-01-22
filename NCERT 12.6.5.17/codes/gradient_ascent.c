#include <math.h>

// Function to compute the volume V(x)
double volume(double x) {
    return ((324 * x) - (72 * x * x) + (4 * x * x * x));
}

// Function to compute the derivative dV/dx
double volume_derivative(double x) {
    return (324 - (144 * x) + (12 * x * x));
}

// Gradient ascent algorithm
double gradient_ascent(double x0, double alpha, double epsilon, int max_iter) {
    double x = x0; // Initial guess
    int iter = 0;

    while (iter < max_iter) {
        double grad = volume_derivative(x);

        // Update x
        double new_x = x + alpha * grad;

        // Ensure x remains within bounds 0 < x < 9
        if (new_x <= 0) {
            new_x = 0.0001;
        } else if (new_x >= 9) {
            new_x = 8.9999;
        }

        // Check for convergence
        if (fabs(new_x - x) < epsilon) {
            break;
        }

        x = new_x;
        iter++;
    }

    return x; // Return the x value that maximizes the volume
}


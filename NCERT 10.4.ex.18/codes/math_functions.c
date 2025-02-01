#include <stdio.h>
#include <math.h>

// Function f(x) = 3x^2 - 2x + 1/3
double f(double x) {
    return 3*x*x - 2*x + 1.0/3.0;
}

// Derivative f'(x) = 6x - 2
double df(double x) {
    return 6*x - 2;
}

// Newton-Raphson method
double newton_raphson(double x0, double tol, int max_iter) {
    double x_n = x0;
    for (int i = 0; i < max_iter; i++) {
        double f_val = f(x_n);
        double df_val = df(x_n);
        if (df_val == 0) return x_n; // Avoid division by zero
        double x_next = x_n - f_val / df_val;
        if (fabs(x_next - x_n) < tol) return x_next;
        x_n = x_next;
    }
    return x_n;
}

// Companion Matrix Root Calculation
double companion_matrix_root() {
    double a = -2.0/3.0;
    double b = 1.0/9.0;
    double discriminant = sqrt(a*a - 4*b);
    return (-a + discriminant) / 2.0; // One root of the quadratic equation
}

// Fixed-Point Iteration g(x) = (3x^2 + 1/3) / 2
double g(double x) {
    return (3*x*x + 1.0/3.0) / 2;
}

// Fixed-Point Iteration Method
double fixed_point_iteration(double x0, double tol, int max_iter) {
    double x_n = x0;
    for (int i = 0; i < max_iter; i++) {
        double x_next = g(x_n);
        if (fabs(x_next - x_n) < tol) return x_next;
        x_n = x_next;
    }
    return x_n;
}


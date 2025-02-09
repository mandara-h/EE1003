#include <stdio.h>
#include <stdlib.h>

// LU Decomposition function
void lu_decomposition(double A[2][2], double L[2][2], double U[2][2]) {
    // Initialize L as identity matrix
    L[0][0] = 1; L[0][1] = 0;
    L[1][0] = A[1][0] / A[0][0]; L[1][1] = 1;

    // Compute U
    U[0][0] = A[0][0]; U[0][1] = A[0][1];
    U[1][0] = 0; U[1][1] = A[1][1] - L[1][0] * A[0][1];
}

// Forward substitution
void forward_substitution(double L[2][2], double b[2], double y[2]) {
    y[0] = b[0];
    y[1] = b[1] - L[1][0] * y[0];
}

// Backward substitution
void backward_substitution(double U[2][2], double y[2], double x[2]) {
    x[1] = y[1] / U[1][1];
    x[0] = (y[0] - U[0][1] * x[1]) / U[0][0];
}

// Function exposed to Python
void solve_lu(double result[2]) {
    double A[2][2] = {{-2, 7}, {7, 8}};
    double b[2] = {5, 15};
    double L[2][2], U[2][2], y[2], x[2];

    lu_decomposition(A, L, U);
    forward_substitution(L, b, y);
    backward_substitution(U, y, x);

    // Store result in output array
    result[0] = x[0];
    result[1] = x[1];
}


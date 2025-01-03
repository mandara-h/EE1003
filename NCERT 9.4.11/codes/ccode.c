#include <stdio.h>
#include <math.h>

float y_val(float x_n, float y_n, float h){
	return (y_n + (h * (2*pow(x_n,2) + x_n) / (pow(x_n,3) + pow(x_n,2) + x_n + 1)));
}

float x_val(float x_n, float h){
	return (x_n + h);
}

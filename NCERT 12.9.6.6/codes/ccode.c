#include <stdio.h>
#include <math.h>

float y(float x_n, float y_n, float h){
	return (y_n + (h * (x_n*log(x_n) - 2*(y_n/x_n))));
}

float x(float x_n, float h){
	return (x_n + h);
}

float y_val(float x){
	return ((0.25 * pow(x,2) * log(x)) - (0.0625 * (pow(x,2) - (1/pow(x,2)))));
}

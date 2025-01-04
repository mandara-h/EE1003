#include <stdio.h>
#include <math.h>

float y(float x_n, float y_n, float h){
	return (y_n + (h * (2*pow(x_n,2) + x_n) / (pow(x_n,3) + pow(x_n,2) + x_n + 1)));
}

float x(float x_n, float h){
	return (x_n + h);
}

float y_val(float x){
	return ((0.25 * log(pow(x+1,2)*pow(pow(x,2)+1,3))) - (0.5 * atan(x)) + 1);
}

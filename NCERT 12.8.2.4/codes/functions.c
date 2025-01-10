#include <stdio.h>

float yAB(float y_n, float h){
	return (y_n + h*(1.5));
}

float yBC(float y_n, float h){
	return (y_n - h*(0.5));
}

float yCA(float y_n, float h){
	return (y_n + h*(0.5));
}

float x(float x_n, float h){
	return (x_n + h);
}

float y_valAB(float x){
	return (1.5*(x + 1));
}

float y_valBC(float x){
	return ((-0.5)*(x-7));
}

float y_valCA(float x){
	return (0.5*(x+1));
}

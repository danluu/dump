#include <stdio.h>
#include <stdlib.h>
#include <math.h>

double wat(double x) {
  asm volatile("" :: "m" (x));
  double res = sin(x);
  asm volatile("" :: "m" (res));  
  return res;
}

int main() {
  double bogus = 0.0;
  asm volatile("" :: "m" (bogus));  
  double res = wat(bogus);
  asm volatile("" :: "m" (res));  
  return 0;
}

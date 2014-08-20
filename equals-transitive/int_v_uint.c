#include <stdio.h>

int main() {
  unsigned long a = 0xffffffffffffffff;
  long b = -1;
  printf("%i", b > a);
  printf("%i", a > b);
  printf("%i", a == b);
}



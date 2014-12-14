#define __STDC_FORMAT_MACROS

#include <stdio.h>

int single_add(int a, int b) {
  return a + b;
}

int main(int argc, char** argv) {
  printf("%i", single_add((int)argv[1],(int)argv[2]));
  return 0;
}

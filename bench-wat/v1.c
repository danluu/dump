#include <stdlib.h>
#include <stdio.h>


void repeat(char* array, int NUMBER) {
  int i;
  int j = 1;
  for (i = 0; i < NUMBER; ++i) {
    j = j * 7;
    if (j > NUMBER) {
      j = j - NUMBER;
    }
    array[j] = 5;
  }
}

// Number to guess: How big of an array (in bytes)
// can we allocate and fill with 5s in a second?
// The catch: We do it out of order instead of in order.
int main(int argc, char **argv) {
  int NUMBER, i;
  NUMBER = atoi(argv[1]);

  char* array = malloc(NUMBER);
  repeat(array, NUMBER);

  return 0;
}

#include <stdlib.h>
#include <stdio.h>

// #include "iacaMarks.h"

int nearest_power_of_two(int v) {
  v--;
  v |= v >> 1;
  v |= v >> 2;
  v |= v >> 4;
  v |= v >> 8;
  v |= v >> 16;
  v++;
  return v;
}

// Number to guess: How big of an array (in bytes)
// can we allocate and fill with 5s in a second?
// The catch: We do it out of order instead of in order.

void repeat(char* array, int NUMBER, int ORIGINAL_NUMBER) {
  int i;
  int j = 1;
  for (i = 0; i < ORIGINAL_NUMBER; ++i) {
    // IACA_START
    j = (j * 7) & NUMBER;
    array[j] = 5;
  }
  // IACA_END
}

int main(int argc, char **argv) {
  int NUMBER, ORIGINAL_NUMBER;
  // we do this so that we can round by taking a bit mask
  // thanks dan luu :)

  ORIGINAL_NUMBER = atoi(argv[1]);
  NUMBER = nearest_power_of_two(ORIGINAL_NUMBER) - 1;

  char* array = malloc(NUMBER);
  repeat(array, NUMBER, ORIGINAL_NUMBER);
  
  return 0;
}

#include <stdlib.h>
#include <stdio.h>

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

void repeat(volatile char* array, int NUMBER, int ORIGINAL_NUMBER) {
  int i;
  int j = 1;
  for (i = 0; i < ORIGINAL_NUMBER; ++i) {
    j = (j * 7) & NUMBER;
    array[j] = 5;
  }
}

int main(int argc, char **argv) {
  int NUMBER, ORIGINAL_NUMBER;
  // we do this so that we can round by taking a bit mask
  // thanks dan luu :)

  ORIGINAL_NUMBER = atoi(argv[1]);
  NUMBER = nearest_power_of_two(ORIGINAL_NUMBER) - 1;
  printf("%d\n", NUMBER);

  volatile char* array = malloc(NUMBER);
  repeat(array, NUMBER, ORIGINAL_NUMBER);
  // Prevent things from being optimized out.
  int i;
  for (i = 0; i < NUMBER; i++) {
    asm volatile("" :: "m" (array[i]));
  }
  
  return 0;
}

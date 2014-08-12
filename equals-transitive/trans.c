#include <stdio.h>
int main(void) {
  long   x = 9007199254740992;    // 2^53
  double y = 9007199254740992.0;  // 2.0^53
  long   z = 9007199254740993;    // 2^53+1
  printf("x == y: %d\n", x == y);
  printf("y == z: %d\n", y == z);
  printf("x == z: %d\n", x == z);
  return 0;
}


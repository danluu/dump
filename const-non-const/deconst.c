#include <stdio.h>

void wat(int* mutable) {
  *mutable += 1;
}

void wat2(int* mutable) {
  *mutable = 100;
}

int main() {
  const int immutable = 10;
  printf("%i\n", immutable);
  wat((int*) &immutable);
  printf("%i\n", immutable);
  wat2((int*) &immutable);
  printf("%i\n", immutable);

  return 0;
}

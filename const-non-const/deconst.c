#include <stdio.h>
#include <stdlib.h>
#include "wat3.h"

void wat(int* mutable) {
  *mutable += 1;
}

void watb(const int* mutable) {
  *(int*) mutable += 1;
}


void wat2(int* mutable) {
  *mutable = 100;
}

void wat2b(const int* mutable) {
  *(int*) mutable = 101;
}

const int * make_immutable() {
  int* p = malloc(sizeof(int));
  *p = 20;
  return (const int*) p;
}

int main() {
  const int immutable = 10;
  printf("%i\n", immutable);
  wat((int*) &immutable);
  printf("%i\n", immutable);
  wat2((int*) &immutable);
  printf("%i\n", immutable);
  wat3((int*) &immutable);
  printf("%i\n", immutable);

  const int* immutable2 = (const int*) make_immutable();
  printf("%i\n", *immutable2);
  wat((int*) immutable2);
  printf("%i\n", *immutable2);
  watb(immutable2);
  printf("%i\n", *immutable2);
  wat2((int*) immutable2);
  printf("%i\n", *immutable2);
  wat2b(immutable2);
  printf("%i\n", *immutable2);
  wat3((int*) immutable2);
  printf("%i\n", *immutable2);

  return 0;
}

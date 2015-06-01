#include <stdio.h>

int main() {
  int areas[] = {10, 12, 13, 14, 20};
  char name[] = "Zed";
  char more_name[] = {'Z','e','d',' ','S','\0'};


  printf("%ld %ld\n", sizeof(int), sizeof(areas));
  printf("%ld %ld\n", sizeof(char), sizeof(name));
  printf("%ld %ld\n", sizeof(char), sizeof(more_name));
  return 0;
}

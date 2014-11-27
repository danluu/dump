#include <stdio.h>
#include <stdlib.h>

int main() {
  int *ptr = malloc(sizeof(int));
  if (ptr == NULL) { 
    printf("Failed to malloc a single int\n");
    return 1;
  }

  *ptr = 1;
  *ptr = 100;

  free(ptr);

  printf("malloc'd an int, assigned to it, and free'd it\n");
  return 0;
}

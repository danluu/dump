#include <stdio.h>

int main(int argc, char *argv[]) {
  for (int i = 1; i < argc; i++) {
    printf("arg %d: %s\n", i, argv[i]);
  }

  char *print_me[] = {"Foo", "Bar"};
  int num_prints = 2;

  for (int i = 0; i < num_prints; i++) {
    printf("%d: %s\n", i, print_me[i]);
  }
}

#include <stdio.h>

int main() {
  int ages[] = {5,6,7,8,9};
  char *names[] = {"Zero", "One", "Two","Three","Four"};

  int count = sizeof(ages) / sizeof(int);
  for (int i = 0; i < count; i++) {
    printf("%s %d\n", names[i], ages[i]);
  }

  printf("-----------\n");

  int *cur_age = ages;
  char **cur_name = names;

  for (int i = 0; i < count; i++) {
    printf("%p %p\n", cur_name, cur_age);
    printf("%s %d\n", *(cur_name++), *(cur_age++));
  }
}

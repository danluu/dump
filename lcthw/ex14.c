#include <stdio.h>
#include <ctype.h>

int is_printable(char ch);
void print_letters(char arg[]);

void print_args(int argc, char *argv[]) {
  for (int i = 1; i < argc; i++) {
    print_letters(argv[i]);
  }
}

void print_letters(char arg[]) {
  for (int i = 0; arg[i] != '\0'; i++) {
    char ch = arg[i];
    if (is_printable(ch)) {
      printf("'%c' == %d ", ch, ch);
    }
  }

  printf("\n");
}

int is_printable(char ch) {
  return isalpha(ch) || isblank(ch) || isdigit(ch);
}

int main(int argc, char *argv[]) {
  print_args(argc, argv);
  return 0;
}

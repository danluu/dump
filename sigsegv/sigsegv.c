#include <stdio.h>

int main() {
  getchar();
  asm volatile( "jmp 0x61616161");
  return 0;
}

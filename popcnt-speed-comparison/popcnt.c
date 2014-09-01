#include <stdio.h>
#include <string.h>
#include <x86intrin.h>

#define LEN 4096
#define LINE_SIZE 128
#define ITERATIONS 1000000

unsigned long long buffer[LEN] __attribute__((aligned(LINE_SIZE)));

// Hardware-accelerated population count (using POPCNT instruction)
int builtin_popcnt(const unsigned long long* buf, int len) {
  int cnt = 0;
  for (int i = 0; i < len; ++i) {
    cnt += __builtin_popcountll(buf[i]);
  }
  return cnt;
}

int run_builtin_popcnt(const unsigned long long* buf, int len, int iterations) {
  int total = 0;

  asm volatile("" :: "m" (buffer));

  for (int i = 0; i < 1000; ++i) {
    total += builtin_popcnt(buffer, LEN);
  }

  asm volatile("" :: "m" (total));
  return total;
}

int main() {
  printf("%i", run_builtin_popcnt(buffer, LEN, ITERATIONS));
}


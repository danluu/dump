#include <stdio.h>
#include <string.h>
#include <x86intrin.h>
#include "../rdtsc.h"

#define LEN 4096
#define LINE_SIZE 128
#define ITERATIONS 1000000


// Hardware-accelerated population count (using POPCNT instruction)
int builtin_popcnt(const unsigned long long* buf, int len) {
  int cnt = 0;
  for (int i = 0; i < len; ++i) {
    cnt += __builtin_popcountll(buf[i]);
  }
  return cnt;
}

int run_builtin_popcnt(int len, int iterations) {
  unsigned long long buffer[LEN] __attribute__((aligned(LINE_SIZE)));


  int total = 0;
  uint64_t tsc_before, tsc_after, tsc, min_tsc;
  min_tsc = 0;
  min_tsc--;

  asm volatile("" :: "m" (buffer[0]));

  for (int i = 0; i < 1000; ++i) {
    RDTSC_START(tsc_before);
    total += builtin_popcnt(buffer, LEN);
    RDTSC_STOP(tsc_after);
    tsc = tsc_after - tsc_before;
    min_tsc = min_tsc < tsc ? min_tsc : tsc;
  }

  asm volatile("" :: "m" (total));
  return min_tsc;
}

int main() {
  printf("%i\n", run_builtin_popcnt(LEN, ITERATIONS));
}


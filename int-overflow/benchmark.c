#define __STDC_FORMAT_MACROS

#include <stdio.h>
#include <inttypes.h>
#include <stdint.h>
#include <sys/mman.h>
#include "../rdtsc.h"

#define MAX_SIZE 10000

// Do 'n' accesses with a relative offset of 'align'
// pointer_chase == 0: do reads and use the read in a running computation
// pointer_chase == 1: do read and use read to find next address
uint64_t add_numbers(int n, int runs) {
  int a[MAX_SIZE];
  int sum = 0; // Prevent code from being optimized away
  uint64_t tsc_before, tsc_after, tsc, min_tsc;

  min_tsc = UINT64_MAX;

  int i, j;
  for (j = 0; j < n; j++) {
    a[j] = 0;
  }


  for (i = 0; i < runs; i++) {
    // Prevent things from being optimized out.
    for (j = 0; j < n; j++) {
      asm volatile("" :: "m" (a[j]));
    }
    RDTSC_START(tsc_before);
    for (j = 0; j < n; j++) {
      sum += a[j];
    }
    RDTSC_STOP(tsc_after);
    tsc = tsc_after - tsc_before;
    min_tsc = min_tsc < tsc ? min_tsc : tsc;
  }
  
  asm volatile("" :: "m" (sum));

  return min_tsc;
}

void test_and_print(int n) {
  double diff;
  int runs = 100000;

  uint64_t auto_time = add_numbers(n, runs);
  // diff = (double)aligned_time / (double)unaligned_time;

  printf("----------%i accesses--------\n", n);
  printf("Page-aligned time:         %" PRIu64 "\n", auto_time);
  // printf("Page-unaligned (+64) time: %" PRIu64 "\n", unaligned_time);
  // printf("Difference: %f\n", diff);
}

int main() {
  test_and_print(10000);
  test_and_print(1000);
  return 0;
}

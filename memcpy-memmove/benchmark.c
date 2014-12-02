// Measure the cost of associativity misses

#define __STDC_FORMAT_MACROS // For PRIu64, etc.

#include <inttypes.h>
#include <stdio.h>
#include <string.h>
#include "../rdtsc.h"

// #define GRAPH // This is the dumbest thing ever. TODO: take an argument

#define SCRATCH_SIZE 134217728 // 1 GB of uint64
#define PAGE_SIZE 4096

// memcpy or memmove
uint64_t access_mem(size_t length, int runs, int memcpy) {
  //  static uint64_t a[2 * MAX_NUM_LINES * PG_SIZE];
 #ifdef HUGEPAGE
  uint64_t *a = mmap(NULL, ALLOC_SIZE, PROT_READ | PROT_WRITE,
		     MAP_PRIVATE| MAP_ANONYMOUS, -1, 0);
  madvise(a, ALLOC_SIZE, MADV_HUGEPAGE);
#else
  static uint64_t a[SCRATCH_SIZE];
  static uint64_t b[SCRATCH_SIZE];
#endif // HUGEPAGE

  uint64_t tsc_before, tsc_after, tsc, min_tsc;

  uint64_t *src = a;
  uint64_t *dst = b;

  min_tsc = UINT64_MAX;

  asm volatile("" :: "m" (a[0]));
  asm volatile("" :: "m" (b[0]));

  // TODOs:
  // Move regions around so we're not running out of cache for small sizes?
  for (int i = 0; i < runs; i++) {
    RDTSC_START(tsc_before);
    if (memcpy) {
      memcpy(src, dst, length);
    } else {
      memmove(src, dst, length);
    }
    RDTSC_STOP(tsc_after);
    tsc = tsc_after - tsc_before;
    min_tsc = min_tsc < tsc ? min_tsc : tsc;
  }

  asm volatile("" :: "m" (a[0]));
  asm volatile("" :: "m" (b[0]));

  return min_tsc;
}

void test_and_print(int length) {
  double diff;
  uint64_t memcpy_time, memmove_time;
  int runs = 10000;

  memcpy_time = access_mem(length, runs, 1);
  memmove_time = access_mem(length, runs, 0);
  diff = (double)memcpy_time / (double)memmove_time;

  printf("----------%i--------\n", length);
  printf("memcpy  time:         %" PRIu64 "\n", memcpy_time);
  printf("memmove time:         %" PRIu64 "\n", memmove_time);
  printf("Difference: %f\n", diff);
}

int main() {
  for (int i = 1; i < 134217728; i *=2) {
    test_and_print(i);
  }
  return 0;
}

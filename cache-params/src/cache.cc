#include <iostream>
#include <vector>

#include "rdtsc.h"

#define BUFFER_SIZE 1024 * 1024 * 128
#define LINE_SIZE 128

uint64_t run_and_time_fn(std::vector<uint8_t>& buf, size_t len, int iterations, uint64_t(*fn)(const std::vector<uint8_t>&, size_t)) {

  uint64_t total = 0;
  uint64_t tsc_before, tsc_after, tsc, min_tsc;
  min_tsc = 0;
  min_tsc--;

  for (int i = 0; i < iterations; ++i) {
    for (size_t j = 0; j < len; ++j) {
      asm volatile("" :: "m" (buf[j]));
    }
    RDTSC_START(tsc_before);
    total += fn(buf, len);
    RDTSC_STOP(tsc_after);
    tsc = tsc_after - tsc_before;
    min_tsc = min_tsc < tsc ? min_tsc : tsc;
  }

  //  assert(total == iterations * 3); // Check that we don't have an off by one error.

  asm volatile("" :: "m" (total));
  return min_tsc;
}

uint64_t naive_loop(const std::vector<uint8_t>& buf, size_t size) {
  uint64_t cnt = 0;
  // Note: unrolling this loop manually does not increase performance
  // when compiling with -O2.
  for (size_t i = 0; i < size; i += LINE_SIZE) {
    cnt += buf[i];
  }
  return cnt;
}

int main() {
  std::vector<uint8_t> buf(BUFFER_SIZE);

  const int iters = 32;
  const size_t len = 16 * 1024;
  uint64_t cycles = run_and_time_fn(buf, len, iters, naive_loop);

  double num_loads = len / LINE_SIZE;
  double cycles_per_load = cycles / num_loads;

  std::cout << cycles_per_load << std::endl;

  return 0;
}

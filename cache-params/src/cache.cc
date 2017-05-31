#include <iostream>
#include <string>
#include <sstream>
#include <vector>

#include "rdtsc.h"

#define BUFFER_SIZE 1024 * 1024 * 128
#define LINE_SIZE 128
#define MAX_CACHE_SIZE 16 * 1024 * 1024

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

template <typename T>
std::string join(std::vector<T> const &v) {
  std::stringstream ss;

  for (size_t i = 0; i < v.size(); ++i) {
    if (i != 0) {
      ss << ",";
    }
    ss << v[i];
  }

  return ss.str();
}

int main() {
  std::vector<uint8_t> buf(BUFFER_SIZE);

  std::vector<size_t> sizes;
  for (size_t s = LINE_SIZE; s <= MAX_CACHE_SIZE; s <<= 1) {
    std::cout << s << std::endl;
    sizes.push_back(s);
  }

  const int iters = 4;
  std::vector<double> cycles_per_load;

  for (const size_t len : sizes) {
    uint64_t cycles = run_and_time_fn(buf, len, iters, naive_loop);

    double num_loads = len / LINE_SIZE;
    double cpl = cycles / num_loads;
    cycles_per_load.push_back(cpl);
  }

  std::cout << join(sizes) << std::endl;
  std::cout << join(cycles_per_load) << std::endl;

  return 0;
}

#include <iostream>
#include <string>
#include <sstream>
#include <vector>

#include "rdtsc.h"

constexpr size_t BUFFER_SIZE = 1024 * 1024 * 128;
constexpr size_t LINE_SIZE = 128 / 8; // Number of uint64_t per cache line.
constexpr size_t MAX_CACHE_SIZE = 16 * 1024 * 1024 / 8; // In units of uint64_t

uint64_t run_and_time_fn(std::vector<uint64_t>& buf,
                         size_t len,
                         int iterations,
                         uint64_t(*fn)(const std::vector<uint64_t>&, size_t)) {

  uint64_t total = 0;
  uint64_t tsc_before, tsc_after, tsc, min_tsc;
  min_tsc = 0;
  min_tsc--;

  for (size_t j = 0; j < len; ++j) {
    asm volatile("" :: "m" (buf[j]));
  }

  for (int i = 0; i < iterations; ++i) {
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

std::vector<double> sweep_timing(std::vector<uint64_t>& buf,
                                 std::vector<size_t> const & sizes,
                                 int iterations,
                                 uint64_t(*fn)(const std::vector<uint64_t>&, size_t)) {
  std::vector<double> cycles_per_load;

  for (const size_t len : sizes) {
    uint64_t cycles = run_and_time_fn(buf, len, iterations, fn);

    double num_loads = len / LINE_SIZE;
    std::cout << num_loads << std::endl;
    double cpl = cycles / num_loads;
    cycles_per_load.push_back(cpl);
  }

  return cycles_per_load;
}

uint64_t noop(const std::vector<uint64_t>& buf, size_t size) {
  uint64_t cnt = 0;

  return cnt;
}

uint64_t naive_loop(const std::vector<uint64_t>& buf, size_t size) {
  uint64_t cnt = 0;
  // Note: unrolling this loop manually does not increase performance
  // when compiling with -O2.
  for (size_t i = 0; i < size; i += LINE_SIZE) {
    cnt += buf[i];
  }
  return cnt;
}

uint64_t naive_list(const std::vector<uint64_t>& buf, size_t size) {
  uint64_t cnt = 0;
  size_t i = 0;
  while (size -= LINE_SIZE > 0) {
    i = buf[i];
    cnt += i;
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
  std::vector<uint64_t> buf(BUFFER_SIZE);

  std::vector<size_t> sizes;
  for (size_t s = LINE_SIZE; s <= MAX_CACHE_SIZE; s <<= 1) {
    sizes.push_back(s);
  }

  const int iters = 4;

  // Set up buf for naive_list.
  for (int i = 0; i < buf.size(); ++i) {
    if (i >= buf.size() - LINE_SIZE) {
      buf[i] = 0;
    } else {
      buf[i] = i + LINE_SIZE;
    }
  }
  buf[buf.size() - 1] = 0;

  auto cycles_per_load_noop = sweep_timing(buf, sizes, iters, noop);
  auto cycles_per_load_naive_loop = sweep_timing(buf, sizes, iters, naive_loop);
  auto cycles_per_load_naive_list = sweep_timing(buf, sizes, iters, naive_list);

  std::cout << join(sizes) << std::endl;
  std::cout << join(cycles_per_load_noop) << std::endl;
  std::cout << join(cycles_per_load_naive_loop) << std::endl;
  std::cout << join(cycles_per_load_naive_list) << std::endl;

  return 0;
}

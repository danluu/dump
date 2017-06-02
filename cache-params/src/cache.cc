#include <assert.h>

#include <algorithm>
#include <iostream>
#include <random>
#include <sstream>
#include <vector>

#include "rdtsc.h"

// TODO: warm up cache before timing starts. This could be done by doing one iteration before timing begins.

constexpr size_t WORD_SIZE = 8;
constexpr size_t BUFFER_SIZE = 1024 * 1024 * 128 / WORD_SIZE;
constexpr size_t LINE_SIZE = 128 / WORD_SIZE;
constexpr size_t LINE_SIZE_BITS = 7 - 3;
constexpr size_t MAX_CACHE_SIZE = 8 * 1024 * 1024 / WORD_SIZE;
constexpr size_t INTERNAL_ITERS = 32;
constexpr size_t ITERS = 4;

// Backing buffer must be twice the size of measured cache size because of our naive scheme to send list accesses
// to a distance location by flipping the high bit, which gives us half utilization of the buffer.
static_assert(MAX_CACHE_SIZE * 2 < BUFFER_SIZE, "Buffer size not large enough for high-bit flip scheme.");
// In fact, we should assert something larger to make sure that when we clear the cache, we clear everything with
// high probaiblity regardless of the replacement scheme.

uint64_t run_and_time_fn(std::vector<uint64_t>& buf,
                         size_t len,
                         int iterations,
                         std::pair<uint64_t, uint64_t>(*fn)(const std::vector<uint64_t>&, size_t)) {

  uint64_t total = 0;
  uint64_t tsc_before, tsc_after, tsc, min_tsc;
  min_tsc = 0;
  min_tsc--;

  for (size_t j = 0; j < len; ++j) {
    asm volatile("" :: "m" (buf[j]));
  }

  for (int i = 0; i < iterations; ++i) {
    auto result = fn(buf, len);
    total += result.second;
    tsc = result.first;
    min_tsc = min_tsc < tsc ? min_tsc : tsc;
  }

  asm volatile("" :: "m" (total));
  return min_tsc;
}

std::vector<double> sweep_timing(std::vector<uint64_t>& buf,
                                 std::vector<size_t> const & sizes,
                                 int iterations,
                                 std::pair<uint64_t, uint64_t>(*fn)(const std::vector<uint64_t>&, size_t)) {
  std::vector<double> cycles_per_load;

  for (const size_t len : sizes) {
    uint64_t cycles = run_and_time_fn(buf, len, iterations, fn);

    double num_loads = (len / LINE_SIZE) * INTERNAL_ITERS;
    double cpl = cycles / num_loads;
    cycles_per_load.push_back(cpl);
  }

  return cycles_per_load;
}

std::pair<uint64_t, uint64_t> noop(const std::vector<uint64_t>& buf, size_t size) {
  uint64_t cnt = 0;
  uint64_t tsc_before, tsc_after;
  RDTSC_START(tsc_before);
  for (size_t ii = 0; ii < INTERNAL_ITERS; ++ii) {

  }
  RDTSC_STOP(tsc_after);
  return std::make_pair(tsc_after - tsc_before, cnt);
}

std::pair<uint64_t, uint64_t> naive_loop(const std::vector<uint64_t>& buf, size_t size) {
  uint64_t cnt = 0;
  uint64_t tsc_before, tsc_after;

  // Warmup.
  for (size_t i = 0; i < size; i += LINE_SIZE) {
    cnt += buf[i];
  }

  // Timed execution.
  RDTSC_START(tsc_before);
  for (size_t ii = 0; ii < INTERNAL_ITERS; ++ii) {
    // Note: unrolling this loop manually does not increase performance
    // when compiling with -O2.
    for (size_t i = 0; i < size; i += LINE_SIZE) {
      cnt += buf[i];
    }
  }
  RDTSC_STOP(tsc_after);
  return std::make_pair(tsc_after - tsc_before, cnt);
}

void make_naive_list(std::vector<uint64_t>& buf, size_t size) {
  for (int i = 0; i < buf.size(); ++i) {
    if (i >= buf.size() - LINE_SIZE) {
      buf[i] = 0;
    } else {
      buf[i] = i + LINE_SIZE;
    }
  }
  buf[buf.size() - 1] = 0;
}

std::pair<uint64_t, uint64_t> naive_list(const std::vector<uint64_t>& buf, size_t size) {
  uint64_t cnt = 0;
  uint64_t tsc_before, tsc_after;

  // Warmup.
  size_t idx = 0;
  for (size_t i = 0; i < size; i += LINE_SIZE) {
    idx = buf[idx];
    cnt += idx;
  }

  // Timed execution.
  RDTSC_START(tsc_before);
  for (size_t ii = 0; ii < INTERNAL_ITERS; ++ii) {
    idx = 0;
    for (size_t i = 0; i < size; i += LINE_SIZE) {
      idx = buf[idx];
      cnt += idx;
    }
  }
  RDTSC_STOP(tsc_after);
  return std::make_pair(tsc_after - tsc_before, cnt);
}

// Note that this scheme effectively flips the high bit of every other access. This increases the probability
// of associativity misses.
void make_list(std::vector<uint64_t>& buf, size_t size) {
  assert(size % 2 == 0);

  std::vector<uint64_t> perm(size / LINE_SIZE);
  for (int i = 0; i < perm.size(); ++i) {
    perm[i] = i;
  }

  auto rengine = std::default_random_engine{};
  std::shuffle(std::begin(perm), std::end(perm), rengine);

  // Naive way to get number of bits in size.
  int num_bits = 0;
  size_t size_mut = size;
  while (size_mut != 0) {
    ++num_bits;
    size_mut >>= 1;
  }

  assert(num_bits != 0);
  uint64_t mask = 1 << num_bits;

  // At this point, perm should be a random permutation of {0, 1, ..., size-1}
  // We now use this to generate a list, but we flip the high bit of the address each time to make sure
  // we don't hit an open DRAM row when going to the next access, if we get a cache miss.
  size_t idx = 0;
  for (int i = 0; i < perm.size(); ++i) {
    size_t new_idx = perm[i] << LINE_SIZE_BITS;
    buf[idx] = new_idx;
    idx = new_idx;
  }
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
  std::vector<size_t> sizes_in_bytes;
  for (size_t s = LINE_SIZE * 8; s <= MAX_CACHE_SIZE; s <<= 1) {
    sizes.push_back(s);
    sizes_in_bytes.push_back(s*WORD_SIZE);
  }

  const int iters = ITERS;

  make_naive_list(buf, MAX_CACHE_SIZE);

  auto cycles_per_load_noop = sweep_timing(buf, sizes, iters, noop);
  auto cycles_per_load_naive_loop = sweep_timing(buf, sizes, iters, naive_loop);
  auto cycles_per_load_naive_list = sweep_timing(buf, sizes, iters, naive_list);

  make_list(buf, MAX_CACHE_SIZE);
  auto cycles_per_load_list = sweep_timing(buf, sizes, iters, naive_list);

  std::cout << join(sizes_in_bytes) << std::endl;
  std::cout << join(cycles_per_load_noop) << std::endl;
  std::cout << join(cycles_per_load_naive_loop) << std::endl;
  std::cout << join(cycles_per_load_naive_list) << std::endl;
  std::cout << join(cycles_per_load_list) << std::endl;

  return 0;
}

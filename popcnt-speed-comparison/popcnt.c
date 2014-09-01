#include <stdio.h>
#include <string.h>
#include <x86intrin.h>
#include <assert.h>
#include "../rdtsc.h"

#define LEN 32
#define LINE_SIZE 128
#define ITERATIONS 1000

uint64_t buffer[LEN] __attribute__((aligned(LINE_SIZE)));

void setup_buffer() {
  buffer[0] = 1;
  buffer[LEN-1] = 3;
}

// Hardware-accelerated population count (using POPCNT instruction)
uint32_t builtin_popcnt(const uint64_t* buf, int len) {
  int cnt = 0;
  for (int i = 0; i < len; ++i) {
    cnt += __builtin_popcountll(buf[i]);
  }
  return cnt;
}

uint32_t builtin_popcnt_unrolled(const uint64_t* buf, int len) {
  assert(len % 4 == 0);
  int cnt = 0;
  for (int i = 0; i < len; i+=4) {
    cnt += __builtin_popcountll(buf[i]);
    cnt += __builtin_popcountll(buf[i+1]);
    cnt += __builtin_popcountll(buf[i+2]);
    cnt += __builtin_popcountll(buf[i+3]);
  }
  return cnt;
}

// Attempt to work out false depdency errata.
uint32_t builtin_popcnt_unrolled_errata(const uint64_t* buf, int len) {
  assert(len % 4 == 0);
  int cnt[4];
  for (int i = 0; i < 4; ++i) {
    cnt[i] = 0;
  }

  for (int i = 0; i < len; i+=4) {
    cnt[0] += __builtin_popcountll(buf[i]);
    cnt[1] += __builtin_popcountll(buf[i+1]);
    cnt[2] += __builtin_popcountll(buf[i+2]);
    cnt[3] += __builtin_popcountll(buf[i+3]);
  }
  return cnt[0] + cnt[1] + cnt[2] + cnt[3];
}


int run_builtin_popcnt(int len, int iterations) {

  uint32_t total = 0;
  uint64_t tsc_before, tsc_after, tsc, min_tsc;
  min_tsc = 0;
  min_tsc--;

  asm volatile("" :: "m" (buffer[0]));

  for (int i = 0; i < iterations; ++i) {
    RDTSC_START(tsc_before);
    total += builtin_popcnt(buffer, LEN);
    RDTSC_STOP(tsc_after);
    tsc = tsc_after - tsc_before;
    min_tsc = min_tsc < tsc ? min_tsc : tsc;
  }

  assert(total == iterations * 3); // Check that we don't have an off by one error.

  asm volatile("" :: "m" (total));
  return min_tsc;
}

int run_builtin_popcnt_unrolled(int len, int iterations) {

  uint32_t total = 0;
  uint64_t tsc_before, tsc_after, tsc, min_tsc;
  min_tsc = 0;
  min_tsc--;

  asm volatile("" :: "m" (buffer[0]));

  for (int i = 0; i < iterations; ++i) {
    RDTSC_START(tsc_before);
    total += builtin_popcnt_unrolled(buffer, LEN);
    RDTSC_STOP(tsc_after);
    tsc = tsc_after - tsc_before;
    min_tsc = min_tsc < tsc ? min_tsc : tsc;
  }

  assert(total == iterations * 3); // Check that we don't have an off by one error.

  asm volatile("" :: "m" (total));
  return min_tsc;
}

int run_builtin_popcnt_unrolled_errata(int len, int iterations) {

  uint32_t total = 0;
  uint64_t tsc_before, tsc_after, tsc, min_tsc;
  min_tsc = 0;
  min_tsc--;

  asm volatile("" :: "m" (buffer[0]));

  for (int i = 0; i < iterations; ++i) {
    RDTSC_START(tsc_before);
    total += builtin_popcnt_unrolled_errata(buffer, LEN);
    RDTSC_STOP(tsc_after);
    tsc = tsc_after - tsc_before;
    min_tsc = min_tsc < tsc ? min_tsc : tsc;
  }

  assert(total == iterations * 3); // Check that we don't have an off by one error.

  asm volatile("" :: "m" (total));
  return min_tsc;
}


// Code from Wojciech Mula.

// lookup for SSE
uint8_t POPCOUNT_4bit[16] __attribute__((aligned(16))) = {
  /* 0 */ 0,
  /* 1 */ 1,
  /* 2 */ 1,
  /* 3 */ 2,
  /* 4 */ 1,
  /* 5 */ 2,
  /* 6 */ 2,
  /* 7 */ 3,
  /* 8 */ 1,
  /* 9 */ 2,
  /* a */ 2,
  /* b */ 3,
  /* c */ 2,
  /* d */ 3,
  /* e */ 3,
  /* f */ 4
};

// ---- SSSE3 - better alorithm, inner loop unrolled ----------------------
uint32_t ssse3_popcount3(uint8_t* buffer, int chunks16) {
static char MASK_4bit[16] = {0xf, 0xf, 0xf, 0xf, 0xf, 0xf, 0xf, 0xf, 0xf, 0xf, 0xf, 0xf, 0xf, 0xf, 0xf, 0xf};

uint32_t result;

#ifdef DEBUG
assert(chunks16 % 4 == 0);
#endif

__asm__ volatile ("movdqu (%%eax), %%xmm7" : : "a" (POPCOUNT_4bit));
__asm__ volatile ("movdqu (%%eax), %%xmm6" : : "a" (MASK_4bit));
__asm__ volatile ("pxor    %%xmm5, %%xmm5" : : ); // xmm5 -- global accumulator

result = 0;

int k, n, i;

i = 0;
while (chunks16 > 0) {
// max(POPCOUNT_8bit) = 8, thus byte-wise addition could be done
// for floor(255/8) = 31 iterations
#define MAX (7*4)
if (chunks16 > MAX) {
k = MAX;
chunks16 -= MAX;
}
else {
k = chunks16;
chunks16 = 0;
}
#undef MAX
__asm__ volatile ("pxor %xmm4, %xmm4"); // xmm4 -- local accumulator
for (n=0; n < k; n+=4) {
#define body(index) \
__asm__ volatile( \
"movdqa  (%%eax), %%xmm0\n" \
"movdqa    %%xmm0, %%xmm1\n" \
"psrlw         $4, %%xmm1\n" \
"pand      %%xmm6, %%xmm0\n" \
"pand      %%xmm6, %%xmm1\n" \
"movdqa    %%xmm7, %%xmm2\n" \
"movdqa    %%xmm7, %%xmm3\n" \
"pshufb    %%xmm0, %%xmm2\n" \
"pshufb    %%xmm1, %%xmm3\n" \
"paddb     %%xmm2, %%xmm4\n" \
"paddb     %%xmm3, %%xmm4\n" \
: : "a" (&buffer[index]));

body(i);
body(i + 1*16);
body(i + 2*16);
body(i + 3*16);
#undef body
i += 4*16;
}

// update global accumulator (two 32-bits counters)
__asm__ volatile (
"pxor   %xmm0, %xmm0\n"
"psadbw %xmm0, %xmm4\n"
"paddd  %xmm4, %xmm5\n"
);
}

// finally add together 32-bits counters stored in global accumulator
__asm__ volatile (
"movhlps   %%xmm5, %%xmm0\n"
"paddd     %%xmm5, %%xmm0\n"
"movd      %%xmm0, %%eax\n"
: "=a" (result)
);

return result;
}

// End imported code.
int run_mula_popcnt(int len, int iterations) {
  //  uint8_t buffer[LEN*8] __attribute__((aligned(LINE_SIZE))); 

  uint32_t total = 0;
  uint64_t tsc_before, tsc_after, tsc, min_tsc;
  min_tsc = 0;
  min_tsc--;

  asm volatile("" :: "m" (buffer[0]));

  for (int i = 0; i < 1000; ++i) {
    RDTSC_START(tsc_before);
    total += ssse3_popcount3((uint8_t*)buffer, LEN/2);
    RDTSC_STOP(tsc_after);
    tsc = tsc_after - tsc_before;
    min_tsc = min_tsc < tsc ? min_tsc : tsc;
  }

  assert(total == iterations * 3); // Check that we don't have an off by 1 error.

  asm volatile("" :: "m" (total));
  return min_tsc;
}

int main() {
  setup_buffer();
  printf("builtin: %i\n", run_builtin_popcnt(LEN, ITERATIONS));
  printf("builtin unrolled: %i\n", run_builtin_popcnt_unrolled(LEN, ITERATIONS));
  printf("builtin errata: %i\n", run_builtin_popcnt_unrolled_errata(LEN, ITERATIONS));
  printf("SSSE3: %i\n", run_mula_popcnt(LEN, ITERATIONS));
  printf("%i\n", run_builtin_popcnt(LEN, ITERATIONS));
  printf("%i\n", run_builtin_popcnt_unrolled(LEN, ITERATIONS));
  printf("%i\n", run_builtin_popcnt_unrolled_errata(LEN, ITERATIONS));
  printf("%i\n", run_mula_popcnt(LEN, ITERATIONS));
}


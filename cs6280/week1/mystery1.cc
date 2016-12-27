// Sample mystery program to measure how long an add takes. Flawed.
// dick sites 2016.06.25

#include <stdint.h>
#include <stdio.h>
#include <time.h>
#include <x86intrin.h>

static const int kIterations = 1000 * 1000000;

int main (int argc, const char** argv) {
    uint64_t startcy, stopcy;

    uint64_t sum = 0;

    time_t t = time(NULL);// A number that the compiler does not know
    int incr = t & 255;// Unknown increment 0..255

    startcy = __rdtsc();
    for (int i = 0; i < kIterations; ++i) {
        sum += incr;
    }
    stopcy = __rdtsc();

    int64_t elapsed = stopcy - startcy;// Signed to avoid compiled code for negative unsigned
    double felapsed = elapsed;

    fprintf(stdout, "%d iterations, %lld cycles, %4.2f cycles/iteration\n",
            kIterations, elapsed, felapsed / kIterations);

    // fprintf(stdout, "%lu %lu\n", t, sum);// Make sum live

    return 0;
}

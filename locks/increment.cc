#include <stdlib.h>
#include <thread>

#define NUM_REPEAT 10000
#define NUM_ITERS 10000
#define NUM_THREADS 2

int counter = 0;

void dummy_fn() {
  for (int i = 0; i < NUM_ITERS; ++i) {
    counter++;
  }
}

void asm_inc() {
  int *p_counter = &counter;
  for (int i = 0; i < NUM_ITERS; ++i) {
    __asm__("incl (%0) \n\t" : : "r" (p_counter));
  }
}

void increment_lots() {
  counter = 0;
  std::thread t[NUM_THREADS];
  for (int i = 0; i < NUM_THREADS; ++i) {
    t[i] = std::thread(asm_inc);
  }
  for (int i = 0; i < NUM_THREADS; ++i) {
    t[i].join();
  }
  printf("%i,haswell\n", counter);
}

int main () {
  for (int i = 0; i < NUM_REPEAT; ++i) {
    increment_lots();
  }
  return 0;
}

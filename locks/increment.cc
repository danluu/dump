#include <stdlib.h>
#include <thread>

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
    __asm__(
	    "incl (%0) \n\t"
	    : "+r" (p_counter)
	    );
  }
}

int main () {
  std::thread t[NUM_THREADS];
  for (int i = 0; i < NUM_THREADS; ++i) {
    t[i] = std::thread(asm_inc);
  }
  for (int i = 0; i < NUM_THREADS; ++i) {
    t[i].join();
  }
  printf("Counter value: %i\n", counter);
  return 0;
}

#include <assert.h>
#include <stdlib.h>

#include <thread>

#define NUM_ITERS 100
#define NUM_THREADS 1024

void dummy_fn(int tid) {
  const int block_length = 1000;
  int *wat = static_cast<int*>(malloc(sizeof(int) * block_length));
  for (int i = 0; i < block_length; ++i) {
    wat[i] = i;
  }
  for (int i = 0; i < block_length; ++i) {
    if(wat[i] != i) {
      printf("tid %i: Expected %X found %X\n", tid, i, wat[i]);
    }
  }
  free(wat);
  return;
}

int main () {
  std::thread t[NUM_THREADS];

  for (int i = 0; i < NUM_THREADS; ++i) {
    t[i] = std::thread(dummy_fn, i);
  }

  for (int i = 0; i < NUM_THREADS; ++i) {
    t[i].join();
  }
  return 0;
}

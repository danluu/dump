// Check different between addresses in stack and 
// `ulimit -s`
// Build with `g++ -std=c++11 -pthread wat.cc`

#include <cstdio>
#include <thread>

static const int num_threads = 10;
 
void call_from_thread(int tid) {
  int a;
  // Using printf instead of cout because cout isn't
  // threadsafe.
  printf("%d:%p\n", tid, &a);
}
 

int main() {
  std::thread t[num_threads];
 
  for (int i = 0; i < num_threads; ++i) {
    t[i] = std::thread(call_from_thread, i);
  }
  for (int i = 0; i < num_threads; ++i) {
    t[i].join();
  }
 
  return 0;
}

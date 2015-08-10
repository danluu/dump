#include <assert.h>

#include <iostream>
#include <random>
#include <vector>

int get_max_bucket(std::default_random_engine &generator, std::uniform_int_distribution<int>& distribution,
		   int num_days, int num_people) {
  std::vector<int> buckets(num_days, 0);
  
  for (int i = 0; i < num_people; ++i) {
    int bucket_in = distribution(generator);
    ++buckets[bucket_in];
  }

  int max = -1;
  for (int i = 0; i < buckets.size(); ++i) {
    if (buckets[i] > max) {
      max = buckets[i];
    }
  }
  assert(max != -1);
  return max;
}

int main() {
  const int num_days = 1000000000;
  const int num_people = 1000000000;
  const int max_people = 8;
  const int num_runs = 1;

  std::default_random_engine generator(0);
  std::uniform_int_distribution<int> distribution(0,num_days-1);

  for (int i = 0; i < num_runs; ++i) {
    /*
    if (get_max_bucket(generator, distribution, num_days, num_people) > max_people) {
      std::cout << 1 << std::endl;
    } else {
      std::cout << 2 << std::endl;
    }
    */
    std::cout << get_max_bucket(generator, distribution, num_days, num_people) << std::endl;
  }
}

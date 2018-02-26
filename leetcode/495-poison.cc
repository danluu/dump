#include <cassert>
#include <vector>

class Solution {
public:
  int findPoisonedDuration(std::vector<int> const & timeSeries, int const duration) {
    if (timeSeries.size() == 0) {
      return 0;
    }

    int count = 0;
    int prev = timeSeries[0] - duration;
    for (int const x : timeSeries) {
      int const delta = x - prev;
      if (delta >= duration) {
	count += duration;
      } else {
	count += delta;
      }
      prev = x;
    }
    return count;
  }
};

int main() {
  Solution s;

  {
    std::vector<int> in = {1,4};
    assert(s.findPoisonedDuration(in, 2) == 4);
  }

  {
    std::vector<int> in = {1,2};
    assert(s.findPoisonedDuration(in, 2) == 3);
  }

  {
    std::vector<int> in = {};
    assert(s.findPoisonedDuration(in, 2) == 0);
  }
}

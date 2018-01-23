#include <algorithm>
#include <cassert>
#include <vector>

class Solution {
public:
  int maxSubArray(std::vector<int>& nums) {
    int cur = 0;
    int best = std::numeric_limits<int>::min();

    for (int x : nums) {
      cur = std::max(0, cur);
      cur += x;
      best = std::max(best, cur);
    }

    return best;
  }
};


int main() {
  Solution *s = new Solution();

  std::vector<int> in0 = {4, -1, 2, 1};
  assert(s->maxSubArray(in0) == 6);

  std::vector<int> in0b = {-2,1,-3,4,-1,2,1,-5,4};
  assert(s->maxSubArray(in0b) == 6);

  std::vector<int> in1 = {-2, -1, -3, -4};
  assert(s->maxSubArray(in1) == -1);

  std::vector<int> in2 = {100, -102, 1, 50};
  assert(s->maxSubArray(in2) == 100);

  delete s;
  return 0;
}

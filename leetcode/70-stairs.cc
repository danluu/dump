#include <cassert>
#include <iostream>

class Solution {
public:
  int climbStairs(int n) {
    if (n <= 1) {
      return 1;
    }

    int cur = 1;
    int prev = 1;
    for (int i = 2; i <= n; ++i) {
      int tmp = cur;
      cur = cur + prev;
      prev = tmp;
    }

    return cur;
  }
};

int main () {
  Solution s = Solution();
  assert(s.climbStairs(1) == 1);
  assert(s.climbStairs(2) == 2);
  assert(s.climbStairs(3) == 3);
  assert(s.climbStairs(4) == 5);
  assert(s.climbStairs(5) == 8);

  return 0;
}

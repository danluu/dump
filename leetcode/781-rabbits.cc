#include <cassert>
#include <memory>
#include <unordered_map>
#include <vector>

class Solution {
public:
  int numRabbits(std::vector<int> const & answers) {
    std::unordered_map<int, int> count;
    for (int x : answers) {
      ++count[x];
    }

    int res = 0;
    for (auto const & kv : count) {
      int num_per_group = kv.first + 1;
      int num_groups = (kv.second + num_per_group - 1) / num_per_group;
      res += num_groups * num_per_group;
    }

    return res;
  }
};

int main() {
  std::unique_ptr<Solution> s(new Solution);

  {  
    std::vector<int> in = {1, 1, 2};
    assert(s->numRabbits(in) == 5);
  }

  {  
    std::vector<int> in = {10, 10, 10};
    assert(s->numRabbits(in) == 11);
  }

  {  
    std::vector<int> in;
    assert(s->numRabbits(in) == 0);
  }

  {  
    std::vector<int> in = {1, 0, 1, 0, 0};
    assert(s->numRabbits(in) == 5);
  }

  {  
    std::vector<int> in = {1, 1, 1, 0, 0};
    assert(s->numRabbits(in) == 6);
  }
}

#include <cassert>
#include <memory>
#include <string>
#include <unordered_set>

class Solution {
public:
  int numJewelsInStones(std::string const &J, std::string const &S) {
    std::unordered_set<char> jewels;
    for (auto const &c : J) {
      jewels.insert(c);
    }

    int res = 0;
    for (auto const &c : S) {
      if (jewels.find(c) != jewels.end()) {
	++res;
      }
    }

    return res;
  }
};

int main () {
  std::unique_ptr<Solution> s(new Solution);

  assert(s->numJewelsInStones("aA", "aAAbbbb") == 3);
  assert(s->numJewelsInStones("z", "ZZ") == 0);
  assert(s->numJewelsInStones("", "ZZ") == 0);
  assert(s->numJewelsInStones("aA", "") == 0);
  assert(s->numJewelsInStones("", "") == 0);
}

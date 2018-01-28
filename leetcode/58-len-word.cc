#include <cassert>
#include <memory>
#include <sstream>
#include <string>

class Solution {
public:
  int lengthOfLastWord(std::string s) {
    if (s.size() == 0) {
      return 0;
    }
    
    std::istringstream iss(s);
    size_t res = 0;
    while (iss) {
      std::string x;
      iss >> x;
      if (x.size() > 0) {
	res = x.size();
      }
    }

    return res;
  }
};

int main() {
  std::unique_ptr<Solution> s(new Solution);
  assert(s->lengthOfLastWord("Hello World") == 5);
  assert(s->lengthOfLastWord("") == 0);
  assert(s->lengthOfLastWord(" ") == 0);
  assert(s->lengthOfLastWord(" ") == 0);
  assert(s->lengthOfLastWord("xx ") == 2);
  assert(s->lengthOfLastWord("x   xx ") == 2);
  
  return 0;
}

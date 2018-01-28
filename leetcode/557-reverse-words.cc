#include <cassert>
#include <iostream>
#include <sstream>
#include <string>

class Solution {
public:
  std::string reverseWords(std::string s) {
    if (s.size() == 0) {
      return "";
    }

    std::istringstream iss(s);
    std::string res;
    while (iss) {
      std::string word;
      iss >> word;

      std::string reversed(word.rbegin(), word.rend());
      res += reversed + ' ';
    }
    res.resize(res.size() - 2);
    return res;
  }
};

int main () {
  Solution s;
  assert(s.reverseWords("") == "");
  assert(s.reverseWords("foo") == "oof");
  assert(s.reverseWords("foo bar") == "oof rab");
  

  return 0;
}

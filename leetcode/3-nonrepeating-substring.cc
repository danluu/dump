#include <algorithm>
#include <cassert>
#include <iostream>
#include <memory>
#include <string>
#include <sys/types.h>
#include <unordered_map>

bool no_repeats(std::unordered_map<char,int>& count) {
  for (auto& kv : count) {
    if (kv.second > 1) {
      return false;
    }
  }
  return true;
}

class Solution {
public:
  int lengthOfLongestSubstring(std::string s) {
    std::unordered_map<char,int> count;
    ssize_t back = -1;
    ssize_t front = -1;
    int max_size = 0;
    while (back + 1 < s.size()) {
      if (front + 1 < s.size() && no_repeats(count)) {
	front += 1;
	count[s[front]] += 1;
      } else {
	back += 1;
	count[s[back]] -= 1;
      }

      if (no_repeats(count)) {
	max_size = std::max(max_size, static_cast<int>(front - back));
      }
    }

    return max_size;
  }
};

int main() {
  std::unique_ptr<Solution> s(new Solution);
  assert(s->lengthOfLongestSubstring("abcabcbb") == 3);
  assert(s->lengthOfLongestSubstring("bbbbbbbbbbbbbb") == 1);
  assert(s->lengthOfLongestSubstring("pwwkew") == 3);
  assert(s->lengthOfLongestSubstring("pwxwkewx") == 4);
  assert(s->lengthOfLongestSubstring("pwxwxkxexw") == 3);

  return 0;
}

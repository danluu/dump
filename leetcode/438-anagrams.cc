#include <cassert>
#include <iostream>
#include <iterator>
#include <memory>
#include <unordered_map>
#include <string>
#include <vector>

template<typename T>
std::ostream & operator<<(std::ostream & os, std::vector<T> vec)
{
    os<<"{ ";
    std::copy(vec.begin(), vec.end(), std::ostream_iterator<T>(os, " "));
    os<<"}";
    return os;
}

class Solution {
public:
  bool isMatch(std::unordered_map<char, int>& target, std::unordered_map<char, int>& candiddate) {
    for (auto& kv : target) {
      if (candiddate[kv.first] != kv.second) {
	return false;
      }
    }
    return true;
  }

  std::vector<int> findAnagrams(std::string s, std::string p) {
    size_t n = p.size();
    std::unordered_map<char, int> target;

    for (char &c : p) {
      ++target[c];
    }


    std::vector<int> res;

    size_t cur_size = 0;
    std::unordered_map<char, int> cur_window;
    for (size_t i = 0; i < s.size(); ++i) {
      ++cur_window[s[i]];
      ++cur_size;
      if (cur_size > n) {
	--cur_size;
	--cur_window[s[i-cur_size]];
      }
      if (cur_size == n) {
	if (isMatch(target, cur_window)) {
	  res.push_back(i - (cur_size - 1));
	}
      }
    }
    return res;
  }
};

int main() {
  std::unique_ptr<Solution> s(new Solution());

  std::vector<int> res0 = s->findAnagrams("cbaebabacd", "abc");
  assert(res0[0] == 0);
  assert(res0[1] == 6);
  assert(res0.size() == 2);

  std::vector<int> res1 = s->findAnagrams("abab", "ab");
  assert(res1[0] == 0);
  assert(res1[1] == 1);
  assert(res1[2] == 2);
  assert(res1.size() == 3);

  std::vector<int> res2 = s->findAnagrams("aaaa", "a");
  assert(res2[0] == 0);
  assert(res2[1] == 1);
  assert(res2[2] == 2);
  assert(res2[3] == 3);
  assert(res2.size() == 4);

  std::vector<int> res3 = s->findAnagrams("aaaa", "aaa");
  assert(res3[0] == 0);
  assert(res3[1] == 1);
  assert(res3.size() == 2);

  std::vector<int> res4 = s->findAnagrams("aabaa", "aaa");
  assert(res4.size() == 0);

  return 0;
}

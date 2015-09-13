/*
ID: danluu1
PROG: msquare
LANG: C++11
*/

#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <algorithm> 
#include <bitset>
#include <cassert>
#include <cmath>
#include <iostream>
#include <fstream>
#include <functional>
#include <limits>
#include <map>
#include <numeric>
#include <queue> 
#include <set>
#include <sstream>
#include <string>
#include <tuple>
#include <unordered_map>
#include <unordered_set>
#include <vector>

using namespace std;

uint32_t rev4(uint32_t old) {  
  return ((0xF & old) << 12) |
    ((0xF0 & old) << 4) |
    ((0xF00 & old) >> 4) |
    ((0xF000 & old) >> 12);
}

uint32_t trans(uint32_t old, int i) {
  uint32_t top_row =     0xFFFF & old;
  uint32_t bot_row = 0xFFFF0000 & old;
  uint32_t rev_top = rev4(top_row);
  uint32_t rev_bot = rev4(bot_row >> 16) << 16;  
  
  uint32_t last_bot = 0xF0000 & old;
  uint32_t last_top = 0xF000 & old;
  uint32_t new_top = ((top_row <<  4) & 0xFFFF) | (last_top >> 12);
  uint32_t new_bot = ((bot_row >> 4) & 0xFFFF0000)  | (last_bot << 12);
  
  uint32_t unchanged = old & 0xF00FF00F;
  uint32_t ul = 0xF0 & old;
  uint32_t ur = 0xF00 & old;
  uint32_t bl = 0x0F000000 & old;
  uint32_t br = 0x00F00000 & old;
  uint32_t changed = (ul << 4) | (br << 4) | (ur << (3 * 4)) | (bl >> (5 * 4));
  switch (i) {
  case 0:
    return (rev_top << 16) | (rev_bot  >> 16);
    break;
  case 1:
    return new_top | new_bot;
    break;
  case 2:
    return changed | unchanged;
    break;
  default:
    assert(false);
    break;
  }
  return -1;
}

// Using bounded dfs to avoid having to carry a history for bfs. But bfs might be better?
// In this case we just keep it in our stack.
bool dfs(uint32_t state, uint32_t target, unordered_map<uint32_t, int> &seen, int bound, int depth, vector<int> &res, int pop) {
  // cout << "dfs depth/bound " << depth << "/" << bound << " seen.size " << seen.size() << endl;
  if (state == target) {
    return true;
  }
  if (bound == depth) {
    return false;
  }

  if (seen.count(state) != 0) {
    assert(seen.count(state) == 1);
    if (seen[state] <= depth) {
      return false;
    }
  }
  seen[state] = depth;

  for (int i = 0; i < 3; ++i) {
    uint32_t new_state = trans(state, i);
    // cout << i << " old " << state << endl;
    // cout << "after " << new_state << endl;
    // assert(__pop_count(new_state) == pop);
    auto found = dfs(new_state, target, seen, bound, depth+1, res, pop);
    if (found) {
      res.push_back(i);
      return true;
    }
  }

  return false;
}

int main() {
  ofstream fout ("msquare.out");
  ifstream fin ("msquare.in");

  uint32_t target = 0;
  uint32_t state = 0;
  for (int i = 1; i <= 8; ++i) {
    int val;
    fin >> val;
    target |= val << (4 * (i-1));
    state |= i << (4 * (i-1));
  }
  cout << std::hex << target << endl;
  cout << state << endl;  
  int pop = 0;
  // int pop = __pop_count(state);
  // assert(__pop_count(target) == pop);

  int i = 0;
  while (i < 10000) {
    unordered_map<uint32_t, int> seen;
    vector<int> res;
    if (dfs(state, target, seen, i, 0, res, pop)) {
      fout << i << endl;
      for (int j = res.size()-1; j >= 0; --j) {
	switch (res[j]) {
	case 0:
	  fout << "A"; break;
	case 1:
	  fout << "B"; break;
	case 2:
	  fout << "C"; break;
	}
      }
      fout << endl;
      return 0;
    }
    ++i;
  }

  fout << "FAIL\n";
  
  return 0;  
}

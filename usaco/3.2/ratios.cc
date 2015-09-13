/*
ID: danluu1
PROG: ratios
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

bool is_divisible(const vector<int> &res, const vector<int> &goal){
  for (int i = 0; i < 3; ++i) {
    if (goal[i] != 0 && (res[i] % goal[i] != 0)) {
      return false;
    }
  }
  return true;
}

pair<bool, int> equal_multiple(const vector<int> &res, const vector<int> &goal) {
  for (int i = 0; i < 3; ++i) {
    if ((goal[i] == 0 && res[i] != 0) || (res[i] == 0 && goal[i] != 0)) {
      return pair<bool, int>(false, -1);
    }
  }
  
  int maybe_multiple = 0;
  for (int i = 0; i < 3; ++i) {
    if (goal[i] != 0) {
      if (maybe_multiple == 0) {
	maybe_multiple = res[i] / goal[i];
      } else {
	if (res[i] / goal[i] != maybe_multiple) {
	  return pair<bool, int>(false, -1);
	}
      }
    }
  }
  return pair<bool, int>(true, maybe_multiple);
}

// bounded dfs
tuple<bool, vector<int>, int> dfs(vector<int> amts, const vector<vector<int>> &bases, const vector<int> &goal, int bound,
				  unordered_set<uint64_t> &seen) {
  // each of the 3 elements gets 21 bits, which is enough for 2M.
  unsigned long long ull_amt = amts[0] | (static_cast<uint64_t>(amts[1]) << 21) | (static_cast<uint64_t>(amts[2]) << 42);
  if (seen.find(ull_amt) != seen.end()) {
    return tuple<bool, vector<int>, int>(false, amts, -1);
  }
  seen.insert(ull_amt);

  vector<int> res(3, 0);
  for (int i = 0; i < 3; ++i) {
    for (int j = 0; j < 3; ++j) {
      res[j] += amts[i] * bases[i][j];
    }
  }

  auto divisible = is_divisible(res, goal);
  if (divisible) {
    auto temp = equal_multiple(res, goal);
    if (temp.first) {
      return tuple<bool, vector<int>, int>(true, amts, temp.second);
    }
  }

  int sum = accumulate(amts.begin(), amts.end(), 0);
  if (sum >= bound) {
    assert(sum == bound);
    return tuple<bool, vector<int>, int>(false, amts, -1);
  }

  for (int i = 0; i < 3; ++i) {
    ++amts[i];
    auto temp = dfs(amts, bases, goal, bound, seen);
    if (get<0>(temp)) {
      return temp;
    }
    --amts[i];
  }

  return tuple<bool, vector<int>, int>(false, amts, -1);
}

// Pure brute force solution.
pair <vector<int>, int> brutal(const vector<vector<int>> &bases, const vector<int> &goal) {
  vector<int> amts(3);
  int record = 10000;
  vector<int> best;
  for (amts[0] = 0; amts[0] <= 100; ++amts[0]) {
    for (amts[1] = 0; amts[1] <= 100; ++amts[1]) {
      for (amts[2] = 0; amts[2] <= 100; ++amts[2]) {
	
	vector<int> res(3, 0);
	for (int i = 0; i < 3; ++i) {
	  for (int j = 0; j < 3; ++j) {
	    res[j] += amts[i] * bases[i][j];
	  }
	}

	auto divisible = is_divisible(res, goal);
	if (divisible) {
	  auto temp = equal_multiple(res, goal);
	  if (temp.first) {
	    if (temp.second < record) {
	      record = temp.second;
	      best = amts;
	    }
	  }
	}	
      }
    }
  }
  
  return pair<vector<int>, int>(best, record);
}

int main() {
  ofstream fout ("ratios.out");
  ifstream fin ("ratios.in");

  vector<int> goal(3);
  vector<vector<int>> bases(3, vector<int>(3));

  for (int i = 0; i < 3; ++i) {
    fin >> goal[i];
  }

  for (int i = 0; i < 3; ++i) {
    for (int j = 0; j < 3; ++j) {
      fin >> bases[i][j];
    }
  }

  /*
  for (int i = 0; i < 100; ++i) {
    vector<int> amts(3, 0);
    unordered_set<unsigned long long> seen;
    auto res = dfs(amts, bases, goal, i, seen);
    if (get<0>(res)) {
      for (const auto &x : get<1>(res)) {
	fout << x << " ";
      }
      fout << get<2>(res) << endl;
      return 0;
    }
  }
  */
  auto res = brutal(bases, goal);
  if (res.second <= 200) {
    for (const auto &x : res.first) {
      fout << x << " ";
    }
    fout << res.second << endl;    
  } else {
    fout << "NONE" << endl;
  }
  return 0;  
}

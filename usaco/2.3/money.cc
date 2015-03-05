/*
ID: danluu1
PROG: money
LANG: C++11
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <algorithm> 
#include <cassert>
#include <cmath>
#include <iostream>
#include <fstream>
#include <limits>
#include <map>
#include <queue> 
#include <set>
#include <sstream>
#include <string>
#include <tuple>
#include <unordered_map>
#include <unordered_set>
#include <vector>

using namespace std;

// Too slow! Memoizing this actually makes it slower, too.
long long solve(vector<int> &cache, int target, int idx, const vector<int> &coins) {
  auto cache_val = cache[(idx << 16) + target];
  if (cache_val != -1) {
    return cache_val;
  }
  if (target == 0) {
    return 1;
  }
  if (idx >= coins.size()) {
    return 0;
  }
  long long ans = 0;
  do {
    ans += solve(cache, target, idx+1, coins);
    target -= coins[idx];
  } while (target >= 0);
  cache[(idx << 16) + target] = ans;
  return ans;
}

int main() {
  ofstream fout ("money.out");
  ifstream fin ("money.in");

  int num_coins;
  fin >> num_coins;
  
  int target;
  fin >> target;

  vector<int> coins;
  for (int i = 0; i < num_coins; ++i) {
    int value;
    fin >> value;
    coins.push_back(value);
  }
  // sort(coins.begin(), coins.end(), greater<int>());

  // vector<int> cache((coins.size() << 16) + 1, -1);
  // fout << solve(cache, target, 0, coins) << endl;

  // Note: this could be reduced to a 1-d array since we never look back more than 1.
  vector<vector<long long>> table(coins.size(), vector<long long>(target+1, 0));
  for (int i = 0; i < coins.size(); ++i) {
    for (int j = 1; j <= target; ++j) {
      // cout << i << " " << j << " " << coins[i] << endl;
      long long ways = 0;
      if (j % coins[i] == 0) {
	// cout << "mod\n";
	ways += 1;
      }
      if (i-1 >= 0) {
	ways += table[i-1][j];
	int last = j - coins[i];
	while (last > 0) {
	  ways += table[i-1][last];
	  last -= coins[i];
	}
      }
      table[i][j] = ways;
    }
  }


  /*
  for (int i = 0; i < coins.size(); ++i) {
    for (int j = 1; j <= target; ++j) {
      cout << table[i][j] << " ";
    }
    cout << endl;
  }
  */
  fout << table[coins.size()-1][target] << endl;
  
  return 0;
}

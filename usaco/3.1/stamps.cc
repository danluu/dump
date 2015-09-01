/*
ID: danluu1
PROG: stamps
LANG: C++11
*/

#include <math.h>
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

/*
// Brute force method in comments.
void solve_helper(const vector<int> &svals, unordered_set<int> &valid, int n_left, int pos, int cur) {  
  // cout << "DEBUG solve_helper n_left " << n_left << " pos " << pos << " cur " << cur << endl;
  valid.insert(cur);
  if (n_left <= 0) {
    return;
  }
  
  for (int i = pos; i < svals.size(); ++i) {
    solve_helper(svals, valid, n_left - 1, i, cur + svals[i]);
  }
}

int solve(const vector<int> &svals, int n) {
  unordered_set<int> valid;
  solve_helper(svals, valid, n, 0, 0);

  vector<int> valid_sort(valid.begin(), valid.end());
  sort(valid_sort.begin(), valid_sort.end());
  int streak = 0;
  int last = 0;
  // Skip first entry, which will be 0.
  for (int i = 1; i < valid_sort.size(); ++i) {
    int x = valid_sort[i];
    // cout << x << " " << streak << endl;
    if (x == last + 1) {
      ++streak;
    } else {
      return streak;
    }
    last = x;
  }
  return streak;
}
*/

int main() {
  ofstream fout ("stamps.out");
  ifstream fin ("stamps.in");

  int k, n;
  fin >> k >> n;

  vector<int> svals(n);
  int x;
  for (int i = 0; i < n; ++i) {
    fin >> x;
    svals[i] = x;
  }

  sort(svals.begin(), svals.end(), greater<int>());


  // DP. Table is coins used vs value, entry is number of coins remaining.
  int max_val = min(svals[0] * k, 2000000);
  int min_val = svals[svals.size()-1];
  // cout << "max " << max_val << " min " << min_val << endl;

  if (min_val != 1) {
    fout << 0 << endl;
    return 0;
  }

  // rem actually holds number of coins used. Bad name!
  int sentinel = numeric_limits<int>::max()/2;
  cerr << "alloc rem\n";
  vector<int> rem(max_val+1, sentinel);
  // vector<vector<int>> rem(2, vector<int>(max_val+1, sentinel));
  // vector<vector<int>> rem(2, vector<int>(2000000, sentinel));
  cerr << "alloc rem success\n";
  for (int i = 1; i <= k; ++i) {
    rem[i*svals[0]] = i;
  }

  for (int i = 1; i < n; ++i) {
    int cur = svals[i];
    for (int j = 1; j <= max_val; ++j) {
      int unused = rem[j];
      if (cur == j) {
	rem[j] = 1;
      } else if (j - cur >= 1) {
	rem[j] = min(unused, rem[j-cur] + 1);
      } else {
	// rem[j] = rem[j]
      }
    }
  }

  /*
  for (int i = 0; i < n; ++i) {
    for (int j = 1; j <= max_val; ++j) {
      if (rem[i][j] > k) {
	cout << "-" << " ";
      } else {
	cout << rem[i][j] << " ";
      }
    }
    cout << endl;
  }
*/

  int streak = 0;
  for (int j = 1; j <= max_val; ++j) {
    if (rem[j] <= k) {
      ++streak;
    } else {
      // cout << "last val " << rem[n-1][j] << endl;
      break;
    }
  }

  fout << streak << endl;

  return 0;  
}

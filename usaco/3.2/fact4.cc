/*
ID: danluu1
PROG: fact4
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
  ofstream fout ("fact4.out");
  ifstream fin ("fact4.in");

  long long n;
  fin >> n;

  long long total = 1;
  for (long long i = 1; i <= n; ++i) {
    total *= i;
    while (total % 10 == 0) {
      // cout << "/10 reduction from " << total << endl;
      total = total / 10;
    }
    if (total > 1000000) {
      // cout << "%100 reduction from " << total << endl;
      total = total % 100;
    }
    // cout << "total " << total << endl;
  }

  fout << total % 10 << endl;

  return 0;  
}

/*
ID: danluu1
PROG: subset
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

long long table(const vector<vector<long long>>& a, int i, int j) {
  long long ways_without = a[i-1][j];
  // cout << i << ":" << j << endl;
  long long ways_with = 0;
  if (i == j) {
    ways_with += 1;
  }
  if (j - i >= 0) {
    assert(a[i-1][j-i] >= 0);
    ways_with += a[i-1][j-i];
  }
  // assert(ways_with + ways_without >= 0);
  return ways_with + ways_without;
}

int main() {
  ofstream fout ("subset.out");
  ifstream fin ("subset.in");

  int n;
  fin >> n;

  int sum = n * (n+1) / 2;
  if (sum % 2 != 0) {
    fout << 0 << endl;
    return 0;
  }
  int target = sum / 2;

  vector<vector<long long>> a(n+1, vector<long long>(target+1,-1));
  
  for (int i = 0; i <= n; ++i) {
    a[i][0] = 0;
  }

  for (int j = 0; j <= target; ++j) {
    a[0][j] = 0;
  }
  
  // i = use all numbers <= i.
  // j = number of ways to form sum of j.
  for (int i = 1; i <= n; ++i) {
    for (int j = 1; j <= target; ++j) {
      a[i][j] = table(a, i, j);
    }
  }

  long long ways = a[n][target];
  assert(ways % 2 == 0);
  fout << ways/2 << endl;
  
  return 0;

}

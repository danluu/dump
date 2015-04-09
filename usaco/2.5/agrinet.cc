/*
ID: danluu1
PROG: agrinet
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

int find_min(const vector<int>& dist, const vector<bool>& seen) {
  int min = numeric_limits<int>::max();
  int min_idx = -1;
  for (int i = 0; i < dist.size(); ++i) {
    if (dist[i] < min && !seen[i]) {
      min = dist[i];
      min_idx = i;
    }
  }
  assert(min_idx >= 0);
  return min_idx;
}

int solve(const vector<vector<int>>& a) {
  assert(a.size() > 0);

  vector<int> dist(a.size(), numeric_limits<int>::max());
  vector<bool> seen(a.size(), false);
  seen[0] = true;
  int found = 1;
  int cost = 0;
  
  for (int i = 0; i < a.size(); ++i) {
    dist[i] = a[0][i];
  }

  while (found < a.size()) {
    int next = find_min(dist, seen);
    cost += dist[next];
    cout << "found " << next << ":" << dist[next] << "--" << cost << endl;
    seen[next] = true;
    for (int i = 0; i < a.size(); ++i) {
      if (dist[i] > a[next][i]) {
	dist[i] = a[next][i];
      }
    }
    ++found;    
  }
  return cost;
}

int main() {
  ofstream fout ("agrinet.out");
  ifstream fin ("agrinet.in");

  int n;
  fin >> n;

  vector<vector<int>> a(n, vector<int>(n, -1024));
  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < n; ++j) {
      int x;
      fin >> x;
      a[i][j] = x;
      if (i == j) {
	assert(x == 0);
      }
    }
  }

  fout << solve(a) << endl;

  return 0;
}

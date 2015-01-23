/*
ID: danluu1
PROG: ariprog
LANG: C++11
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <algorithm> 
#include <cassert>
#include <iostream>
#include <fstream>
#include <limits>
#include <map>
#include <queue> 
#include <set>
#include <sstream>
#include <string>
#include <tuple>
#include <unordered_set>
#include <vector>

using namespace std;

#define HUGE_NUM 250*250*2+1

int is_bisquare[HUGE_NUM];

void set_bisquares(int m) {
  memset(is_bisquare, 0, HUGE_NUM * sizeof(int));
  for (int i = 0; i <= m; ++i) {
    for (int j = i; j <= m; ++j) {
      is_bisquare[i*i + j*j] = 1;
    }
  }
  cout << "finished set\n";
}

int cmp_pairs(const pair<int,int>& left, const pair<int,int>& right) {
  if (left.second < right.second) {
    return 1;
  } else if (left.second == right.second) {
    return left.first < right.first;
  } else {
    return 0;
  }
  assert(0);
}
  
vector<int> create_bisquares(int m) {
  vector<int> bisquares;
  for (int i = 0; i < HUGE_NUM; ++i) {
    if (is_bisquare[i]) {
      bisquares.push_back(i);
    }
  }
  return bisquares;
}

int seq_starts_at(int diff, int n, int start) {
  int i = 0;
  int current = start;
  while (i < n) {
    if (current >= HUGE_NUM || !is_bisquare[current]) {
      return 0;
    }
    current += diff;
    ++i;
  }
  return 1;
}

vector<int> possible_diffs(const vector<int>& bisquares, int start) {
  vector<int> diffs(bisquares.size() - start + 1);
  for (int i = start+1; i < bisquares.size(); ++i) {
    diffs[i-start+1] = bisquares[i] - bisquares[start];
  }
  return diffs;
}

// Prune solution by only starting at real bisquare values and avoiding impossible diffs.
void solve_reverse(int n, int m, ofstream& fout) {
  int found_one = 0;
  set_bisquares(m);
  vector<pair<int,int>> ans;
  ans.reserve(10000);
  auto bisquares = create_bisquares(m);
  for (int start = 0; start < bisquares.size(); ++start) {
    auto diffs = possible_diffs(bisquares, start);
    for (auto& diff : diffs) {
      if (diff > 0 && seq_starts_at(diff, n, bisquares[start])) {
	ans.push_back(make_pair(bisquares[start],diff));
      }
    }
  }

  sort(ans.begin(), ans.end(), cmp_pairs);
  
  for (auto &a : ans) {
    fout << a.first << " " << a.second << endl;
  }
  if (ans.size() == 0) {
    fout << "NONE\n";
  }
  return;
}

int main() {
  ofstream fout ("ariprog.out");
  ifstream fin ("ariprog.in");

  int n, m;
  fin >> n >> m;

  // cout << n << " " << m << endl;
  solve_reverse(n, m, fout);

  return 0;
}

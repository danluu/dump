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
  set<int> unique_bisquares;
  for (int i = 0; i <= m; ++i) {
    for (int j = i; j <= m; ++j) {
      unique_bisquares.insert(i*i + j*j);
    }
  }
  vector<int> bisquares(unique_bisquares.begin(), unique_bisquares.end());
  return bisquares;
}

int seq_starts_at(const vector<int>& bisquares, int diff, int n, int start) {
  int i = start;
  int target = bisquares[start];
  int seq_len = 0;
  int bsize = bisquares.size();
  while (seq_len < n) {
    if (bisquares[i] == target) {
      target += diff;
      ++seq_len;
    } else if (bisquares[i] > target || i >= bsize) {
      return 0;
    }
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

void solve_reverse(int n, int m, ofstream& fout) {
  int found_one = 0;
  vector<pair<int,int>> ans;
  ans.reserve(10000);
  auto bisquares = create_bisquares(m);
  for (int start = 0; start < bisquares.size(); ++start) {
    auto diffs = possible_diffs(bisquares, start);
    for (auto& diff : diffs) {
      if (seq_starts_at(bisquares, diff, n, start)) {
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

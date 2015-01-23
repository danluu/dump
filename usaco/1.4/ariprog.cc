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
#include <unordered_set>
#include <vector>

using namespace std;

#define HUGE_NUM 250*250*2

//int bisquares[HUGE_NUM];

unordered_set<int> find_bisquares(int m) {
  unordered_set<int> bisquares;
  for (int i = 0; i <= m; ++i) {
    for (int j = i; j <= m; ++j) {
      // cout << "bs:" << i*i + j*j << endl;
      bisquares.insert(i*i + j*j);
    }
  }
  return bisquares;
}

/*
void set_bisquares(int m) {
  memset(bisquares, 0, HUGE_NUM * sizeof(int));
  for (int i = 0; i <= m; ++i) {
    for (int j = i; j <= m; ++j) {
      bisquares[i*i + j*j] = 1;
    }
  }
}
*/

vector<int> create_bisquares(int m) {
  vector<int> bisquares;
  for (int i = 0; i <= m; ++i) {
    for (int j = i; j <= m; ++j) {
      bisquares.push_back(i*i + j*j);
    }
  }
  sort(bisquares.begin(), bisquares.end());
  return bisquares;
}


int check_diff_len_start(const unordered_set<int>& bisquares, int diff, int n, int start) {
  int current = start;
  for (int i = 0; i < n; ++i) {
    if (bisquares.find(current) == bisquares.end()) {
      // cout << "diff n start " << diff << " " << n << " " << start << endl;
      // cout << "failed at " << i << endl;
      return 0;
    }
    current += diff;
  }
  return 1;
}

// Need to change lengths first, starting value second.
void solve(int n, int m, ofstream& fout) {
  auto bisqures = find_bisquares(m);
  cout << "#bisquares " << bisqures.size() << endl;
  int found_one = 0;
  
  // i = delta, j = starting val
  for (int i = 1; i <= 2*m*m; ++i) {
    for (int j = 0; j <= 2*m*m; ++j) {
      if (check_diff_len_start(bisqures, i, n, j)) {
	found_one = 1;
	fout << j << " " << i << endl;
      }
    }
  }

  if (!found_one) {
    fout << "NONE\n";
  }
}

/*
void solve_faster(int n, int m, ofstream& fout) {
  set_bisquares(m);
  int found_one = 0;
  
  // i = delta, j = starting val
  for (int i = 1; i <= 2*m*m; ++i) {
    vector<int> ans;
    for (int offset = 0; offset < i; ++offset) {
      int run_length = 0;
      for (int j = offset; j <= 2*m*m; j+=i) {
	if (bisquares[j]) {
	  ++run_length;
	  //	  cout << "delta " << i << "j " << j << " " << run_length << endl;
	  if (run_length >= n) {
	    found_one = 1;
	    // fout << j - (n-1)*i << " " << i << endl;	  
	    ans.push_back(j - (n-1)*i);
	  }
	} else {
	  run_length = 0;
	}
      }
    }
    sort(ans.begin(), ans.end());
    for (auto& start : ans) {
      fout << start << " " << i << endl;
    }
  }

  if (!found_one) {
    fout << "NONE\n";
  }
}
*/

int seq_starts_at(vector<int>& bisquares, int diff, int n, int start) {
  int i = start;
  int target = bisquares[start];
  int seq_len = 0;
  while (seq_len < n) {
    if (bisquares[i] == target) {
      target += diff;
      ++seq_len;
    } else if (bisquares[i] > target || i >= bisquares.size()) {
      return 0;
    }
    ++i;
  }
  return 1;
}

void solve_reverse(int n, int m, ofstream& fout) {
  int found_one = 0;
  auto bisquares = create_bisquares(m);
  for (int diff = 1; diff < 2*m*m; ++diff) {
    for (int start = 0; start < bisquares.size(); ++start) {
      if (seq_starts_at(bisquares, diff, n, start)) {
	found_one = 1;
	fout << bisquares[start] << " " << diff << endl;
      }
    }
  }

  if (!found_one) {
    fout << "NONE\n";
  }
  return;
}

int main() {
  ofstream fout ("ariprog.out");
  ifstream fin ("ariprog.in");

  int n, m;
  fin >> n >> m;

  cout << n << " " << m << endl;
  solve_reverse(n, m, fout);

  return 0;
}

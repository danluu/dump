/*
ID: danluu1
PROG: holstein
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

bool feed_matches(const vector<int>& rda, const vector<vector<int>>& feeds, int set) {
  vector<int> obtained(rda.size(),0);
  for (int i = 0; i < feeds.size(); ++i) {
    if (set & (1 << i)) {
      for (int j = 0; j < feeds[i].size(); ++j) {
	// cout << i << ":" << j << endl;
	obtained[j] += feeds[i][j];
      }
    }
  }

  for (int i = 0; i < rda.size(); ++i) {
    if (rda[i] > obtained[i]) {
      return false;
    }
  }
  return true;
}

int try_k_feeds(const vector<int>& rda, const vector<vector<int>>& feeds, int k) {
  cout << "try_k_feeds " << k << endl;
  int set = (1 << k) - 1;
  int limit = 1 << feeds.size();
  while (set < limit) {
    // cout << "trying " << set << endl;
    if (feed_matches(rda, feeds, set)) {
      return set;
    }
    
    // Gosper's hack: generate next iteration.
    int c = set & -set;
    int r = set + c;
    set = (((r^set) >> 2) / c) | r;
  }
  return 0;
}

int main() {
  ofstream fout ("holstein.out");
  ifstream fin ("holstein.in");

  int num_vitamins, num_feeds;
  fin >> num_vitamins;

  cout << "reading vitamins\n";
  vector<int> rda(num_vitamins);
  for (int i = 0; i < num_vitamins; ++i) {
    int x;
    fin >> x;
    rda[i] = x;
  }

  fin >> num_feeds;
  cout << "reading feeds\n";
  vector<vector<int>> feeds(num_feeds, vector<int>(num_vitamins));
  for (int i = 0; i < num_feeds; ++i) {
    for (int j = 0; j < num_vitamins; ++j) {
      int x;
      fin >> x;
      feeds[i][j] = x;
    }
  }

  // i = number of feeds to try.
  for (int i = 1; i <= num_feeds; ++i) {
    int ans = try_k_feeds(rda, feeds, i);
    if (ans) {
      ostringstream result;
      result << i << " ";
      for (int j = 0; j < feeds.size(); ++j) {
	if (ans & (1<<j)) {
	  result << j+1 << " ";
	}
      }
      string res_str = result.str();
      res_str.pop_back();
      fout << res_str << endl;
      return 0;
    }

  }
  
  assert(0);
  return 0;
}

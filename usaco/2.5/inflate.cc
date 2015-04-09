/*
ID: danluu1
PROG: inflate
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

int solve(const vector<pair<int,int>>& items, int bound) {
  vector<int> best(bound+1);
  best[0] = 0;
  for (int i = 1; i < best.size(); ++i) {
    int best_i = 0;
    for (const auto& p : items) {
      if (i >= p.second) {
	int cur = p.first + best[i-p.second];
	if (cur > best_i) {
	  best_i = cur;
	}	  
      }
    }
    best[i] = best_i;
  }
  return best[bound];
}

int main() {
  ofstream fout ("inflate.out");
  ifstream fin ("inflate.in");


  int bound, num;
  fin >> bound >> num;

  vector<pair<int,int>> items;
  for (int i = 0; i < num; ++i) {
    int score, cost;
    fin >> score >> cost;
    // cout << "item " << score << " " << cost << endl;
    items.push_back(make_pair(score, cost));
  }

  fout << solve(items, bound) << endl;
  return 0;
}

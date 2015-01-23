/*
ID: danluu1
PROG: milk3
LANG: C++11
*/

#include <stdio.h>
#include <stdlib.h>
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
#include <vector>

using namespace std;


void solve_helper(vector<pair<int,int>> buckets, set<vector<pair<int,int>>>& seen, set<int>& ans){
  // pour from i to j
  for (int i = 0; i < buckets.size(); ++i) {
    for (int j = 0; j < buckets.size(); ++j) {
      if (i != j) {
	int target_space = buckets[j].second - buckets[j].first;
	auto newb = buckets;
	if (newb[i].first > target_space) {
	  newb[i].first -= target_space;
	  newb[j].first += target_space;
	  assert(newb[j].first == newb[j].second);
	} else {
	  newb[j].first += newb[i].first;
	  newb[i].first = 0;
	}
	if (seen.find(newb) == seen.end()) {
	  seen.insert(newb);
	  if (newb[0].first == 0) {
	    ans.insert(newb[2].first);
	  }
	  solve_helper(newb, seen, ans);
	} else {
	  // State already reached. Ignore.
	}
      }
    }
  }
}

set<int> solve(vector<pair<int,int>> buckets){
  cout << "solve\n";
  set<vector<pair<int,int>>> seen;
  set<int> ans;
  ans.insert(buckets[2].first);
  solve_helper(buckets, seen, ans);
  return ans;
}

int main() {
  ofstream fout ("milk3.out");
  ifstream fin ("milk3.in");

  int a, b, c;
  fin >> a >> b >> c;

  vector<pair<int,int>> buckets = {make_pair(0,a), make_pair(0,b), make_pair(c,c)};

  set<int> ans = solve(buckets);
  // sort(ans.begin(), ans.end());

  int i = 0;
  for (auto it = ans.begin(); it != ans.end(); ++it) {
    fout << *it;
    if (i != ans.size()-1) {
      fout << " ";
    }
    ++i;
  }
  fout << endl;

  return 0;
}

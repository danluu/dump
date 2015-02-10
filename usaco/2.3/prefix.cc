/*
ID: danluu1
PROG: prefix
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

// Segfaults due to stack depth. See version below for explicit stack.
int longest_helper(const vector<string>& possible, const string& all, int pos) {
  cout << "pos: " << pos << " size: " << all.size() << endl;
  int best = pos;
  for (auto& x : possible) {
    if (all.substr(pos, x.size()) == x) {
      cout << "trying " << x << endl;
      int attempt = longest_helper(possible, all, pos + x.size());
      best = max(attempt, best);
    }
  }
  return best;
}

int longest(const vector<string>& possible, const string& all) {
  // return longest_helper(possible, all, 0);
  vector<int> pos;
  unordered_set<int> seen; // memoize, sort of. Result already stored, so just need to check that that haven't seen it.
  pos.push_back(0);
  int best = 0;
  while (pos.size() > 0) {
    int current = pos.back();
    pos.pop_back();
    // cout << "current: " << current << " size: " << all.size() << endl;
    for (auto& x : possible) {
      if (all.substr(current, x.size()) == x) {
	// cout << "trying " << x << endl;
	int next = current + x.size();
	best = max(next, best);
	if (seen.find(next) == seen.end()) {
	  seen.insert(next);
	  pos.push_back(next);
	}
      }
    }
  }
  return best;
}

int main() {
  ofstream fout ("prefix.out");
  ifstream fin ("prefix.in");

  vector<string> possible;
  string x;
  // cout << "on\n";
  while (true) {
    fin >> x;
    if (x == ".") {
      break;
    }
    // cout << x << endl;
    possible.push_back(x);
  }

  ostringstream all;
  while (fin >> x) {
    all << x; // Note: this is slow. Use a buffer if too slow.
  }
  // cout << "all: " << all << endl;

  string temp = all.str();
  int ans = longest(possible, temp);
  fout << ans << endl;
  
  return 0;

}

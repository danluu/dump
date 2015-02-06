/*
ID: danluu1
PROG: lamps
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

string vbool(vector<bool> lamps) {
  // reverse(lamps.begin(), lamps.end());
  ostringstream os;
  for (auto bit : lamps) {
    if (bit) {
      os << "1";
    } else {
      os << "0";
    }
  }
  return os.str();
}

// Note: these check functions should only be called with the correct parity.

// This solution is overly complicated because I thought there were N possible buttons, but there are only 4.
void check_helper(unordered_set<vector<bool>>& valid, const vector<int>& on, const vector<int>& off, int presses, int num_lamps, vector<bool> lamps, int current_bit) {
  if (presses == 0 || current_bit > 4) {
    for (auto& x : on) {
      if (!lamps[x-1]) {
	// cout << "Failing on cond " << x << ":" << vbool(lamps) << endl;
	return;
      }
    }
    for (auto& x : off) {
      if (lamps[x-1]) {
	// cout << "Failing off cond " << x << ":" << vbool(lamps) << endl;
	return;
      }
    }
    valid.insert(lamps);
    return;
  }

  check_helper(valid, on, off, presses, num_lamps, lamps, current_bit+1);
  // cout << "Setting current_bit " << current_bit << endl;
  if (current_bit <= 1) {
    for (int i = 0; i < num_lamps; i += current_bit+1) {
      lamps[i] = !lamps[i];
    }
  } else if (current_bit == 2) {
    for (int i = 1; i < num_lamps; i += 2) {
      lamps[i] = !lamps[i];
    }
  } else {
    for (int i = 0; i < num_lamps; i += 3) {
      lamps[i] = !lamps[i];
    }
  }
  // cout << vbool(lamps) << endl;
  check_helper(valid, on, off, presses-1, num_lamps, lamps, current_bit+1);
}

void check_lamps(unordered_set<vector<bool>>& valid, const vector<int>& on, const vector<int>& off, int presses, int num_lamps) {
  vector<bool> lamps(num_lamps,true);
  check_helper(valid, on, off, presses, num_lamps, lamps, 0);
}

int main() {
  ofstream fout ("lamps.out");
  ifstream fin ("lamps.in");

  int num_lamps;
  fin >> num_lamps;

  int presses;
  fin >> presses;

  vector<int> on;
  
  int x;
  // cout << "on\n";
  while (true) {
    fin >> x;
    if (x == -1) {
      break;
    }
    // cout << x << endl;
    on.push_back(x);
  }

  vector<int> off;
  while (true) {
    fin >> x;
    if (x == -1) {
      break;
    }
    off.push_back(x);
  }

  unordered_set<vector<bool>> valid_lamps;
  for (int i = 0; i <= presses; ++i) {
    if (i % 2 == presses % 2) {
      check_lamps(valid_lamps, on, off, i, num_lamps);
    }
  }

  vector<vector<bool>> sort_lamps(valid_lamps.size());
  copy(valid_lamps.begin(), valid_lamps.end(), sort_lamps.begin());
  sort(sort_lamps.begin(), sort_lamps.end());

  if (sort_lamps.size() == 0) {
    fout << "IMPOSSIBLE\n";
  } else {
    for (auto single : sort_lamps) {
      fout << vbool(single) << endl;
    }
  }
  return 0;

}

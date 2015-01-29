/*
ID: danluu1
PROG: sort3
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

int main() {
  ofstream fout ("sort3.out");
  ifstream fin ("sort3.in");

  int n;
  fin >> n;

  vector<int> all(n);
  vector<int> count(4,0);
  for (int i = 0; i < n; ++i) {
    int x;
    fin >> x;
    ++count[x];
    all[i] = x;
  }


  cout << "counts\n";
  for (auto& x : count) {
    cout << x << endl;
  }
  
  // First dim is region. Second is count of value in that region.
  int extra[4][4];
  for (int i = 0; i < 4; ++i) {
    for (int j = 0; j < 4; ++ j) {
      extra[i][j] = 0;
    }
  }
  for (int i = 0; i < count[1]; ++i) {
    //cout << all[i] << " in 1\n";
    ++extra[1][all[i]];
  }
  for (int i = count[1]; i < count[1] + count[2]; ++i) {
    //cout << all[i] << " in 2\n";
    ++extra[2][all[i]];
  }
  for (int i = count[1] + count[2]; i < count[1] + count[2] + count[3]; ++i) {
    //cout << all[i] << " in 3\n";
    ++extra[3][all[i]];
  }

  // Do all swaps that swap a pair into the correct location.
  int swaps = 0;
  for (int i = 1; i < 4; ++i) {
    for (int j = i; j < 4; ++j) {
      if (i != j) {
	while (extra[i][i] < count[i] && extra[j][i] > 0 && extra[i][j] > 0) {
	  cout << "swap " << i << ":" << j << endl;
	  cout << "to " << extra[i][i] << " switching " << extra[i][j] << ":" << extra[j][i] << endl;
	  ++swaps;
	  ++extra[i][i];
	  ++extra[j][j];
	  --extra[i][j];
	  --extra[j][i];
	}
      }
    }
  }

  // Now we've swapped all pairs into the correct locations and we only cycles like
  // 2 3 1
  // remaining.
  // For each of these we need 2 swaps.

  cout << count[1] << ":" << extra[1][1] << endl;
  assert(count[1] >= extra[1][1]);
  swaps += 2*(count[1] - extra[1][1]);
  
  fout << swaps << endl;
  
  return 0;
}

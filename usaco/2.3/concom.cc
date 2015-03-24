/*
ID: danluu1
PROG: concom
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

#define MAXCOM 100
#define MAXP MAXCOM+1

int main() {
  ofstream fout ("concom.out");
  ifstream fin ("concom.in");

  int num_in;
  fin >> num_in;
  vector<vector<int>> ctl(MAXP, vector<int>(MAXP,0));
  vector<vector<bool>> seen(MAXP, vector<bool>(MAXP,0));  
  for (int i = 0; i < num_in; ++i) {
    int a, b, percent;
    fin >> a >> b >> percent;
    ctl[a][b] = percent;
  }

  for (int i = 1; i < MAXP; ++i) {
    for (int j = 1; j < MAXP; ++j) {
      if (i != j && !seen[i][j] && ctl[i][j] > 50) {
	seen[i][j] = true;
	// Now ctl i->j.
	// Indirectly ctl i->j->k.
	for (int k = 1; k < MAXP; ++k) {
	  ctl[i][k] += ctl[j][k];
	  if (seen[j][k]) {
	    seen[i][k] = true;
	  }
	}
	j = 0;
      }
    }
  }

  for (int i = 1; i < MAXP; ++i) {
    for (int j = 1; j < MAXP; ++j) {
      if (i != j && ctl[i][j] > 50) {
	fout << i << " " << j << endl;
      }
    }
  }

  return 0;
}

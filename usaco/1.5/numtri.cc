/*
ID: danluu1
PROG: numtri
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

int solve(vector<vector<int>>& a, int n) {
  for (int i = n-2; i >=0; --i) {
    for (int j = 0; j <= i; ++j) {
      a[i][j] += max(a[i+1][j],a[i+1][j+1]);
    }
  }
  return a[0][0];
}

int main() {
  ofstream fout ("numtri.out");
  ifstream fin ("numtri.in");

  int n;
  fin >> n;

  vector<vector<int>> a;
  
  for (int i = 0; i < n; ++i) {
    vector<int> row;
    for (int j = 0; j <= i; ++j) {
      int x;
      fin >> x;
      row.push_back(x);
    }
    a.push_back(row);
  }

  fout << solve(a,n) << endl;

  return 0;
}

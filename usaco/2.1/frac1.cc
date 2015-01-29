/*
ID: danluu1
PROG: frac1
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

double eps = double(1) / double(1000000000);

bool close(double lhs, double rhs) {
  return (fabs(lhs - rhs) < eps);
}

bool cmp_frac(const pair<int,int>& lhs, const pair<int,int>& rhs) {
  double left = double(lhs.first) / double(lhs.second);
  double right = double(rhs.first) / double(rhs.second);
  if (close(left, right)) {
    return lhs.second < rhs.second;
  } else {
    return left < right;
  }
}

int main() {
  ofstream fout ("frac1.out");
  ifstream fin ("frac1.in");

  int n;
  fin >> n;

  vector<pair<int,int>> order;
  for (int i = 1; i <= n; ++i) {
    for (int j = 0; j <= i; ++j) {
      order.push_back({j,i});
    }
  }

  sort(order.begin(), order.end(), cmp_frac);

  double previous = -1.0;
  for (auto& x : order) {
    double frac = double(x.first)/double(x.second);
    if (!close(frac, previous)) {
      fout << x.first << "/" << x.second << endl;
    }
    previous = frac;
  }
  
  return 0;
}

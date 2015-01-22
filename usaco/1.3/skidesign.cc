/*
ID: danluu1
PROG: skidesign
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

// takes a list of elevations and lower bound of range
// upper bound is lower + 17.
int cost_for_range(vector<int>& elevations, int lower) {
  int upper = lower + 17;
  assert(lower >= 0);
  assert(upper <= 100);
  
  int total_cost = 0;
  for (auto& y: elevations) {
    int diff = 0;
    if (y < lower) {
      diff = lower - y;
    }
    if (y > upper) {
      diff = y - upper;
    }
    total_cost += (diff * diff);
  }
  return total_cost;
}

int main() {
  ofstream fout ("skidesign.out");
  ifstream fin ("skidesign.in");

  int num_hills;
  fin >> num_hills;

  vector<int> elevations;
  for (int i = 0; i < num_hills; ++i) {
    int y;
    fin >> y;
    elevations.push_back(y);
  }

  int best_cost = numeric_limits<int>::max();
  for (int i = 0; i < 100-17; ++i) {
    int cost = cost_for_range(elevations, i);
    if (cost < best_cost) {
      best_cost = cost;
    }
  }

  fout << best_cost << endl;

  return 0;
}

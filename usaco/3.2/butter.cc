/*
ID: danluu1
PROG: butter
LANG: C++11
*/

#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <algorithm> 
#include <bitset>
#include <cassert>
#include <cmath>
#include <iostream>
#include <fstream>
#include <functional>
#include <limits>
#include <map>
#include <numeric>
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
  ofstream fout ("butter.out");
  ifstream fin ("butter.in");


  int num_cows, num_nodes, num_paths;
  fin >> num_cows >> num_nodes >> num_paths;

  vector<int> hascow(num_nodes, 0);
  vector<vector<int>> g(num_nodes, vector<int>(num_nodes+1, numeric_limits<int>::max() / 2));

  for (int i = 0; i < num_cows; ++i) {
    int p;
    fin >> p;
    ++hascow[p-1];
  }

  for (int i = 0; i < num_paths; ++i) {
    int left, right, dist;
    fin >> left >> right >> dist;
    g[left-1][right-1] = dist;
    g[right-1][left-1] = dist;
  }

  for (int k = 0; k < num_nodes; ++k) {
    for (int i = 0; i < num_nodes; ++i) {
      for (int j = 0; j < num_nodes; ++j) {
	g[i][j] = min(g[i][j], g[i][k] + g[k][j]);
      }
    }
  }

  int best_node = -1;
  int best_dist = numeric_limits<int>::max();
  for (int i = 0; i < num_nodes; ++i) {
    int sum_dists = 0;
    for (int j = 0; j < num_nodes; ++j) {
      if (i != j) {
	sum_dists += hascow[j] * g[i][j];
      }
    }
    if (sum_dists < best_dist) {
      best_node = i;
      best_dist = sum_dists;
    }
  }

  fout << best_dist << endl;
  
  return 0;  
}

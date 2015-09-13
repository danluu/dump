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

class Order {
  bool Operator()(pair<int, int> &a, pair<int, int> &b) {
    return a.second < a.first;
  }
};

void dijk(vector<vector<int>> &g, const vector<int> &hascow, const int start, const int num_nodes) {
  vector<int> d(num_nodes, numeric_limits<int>::max() / 2);

  d[start] = 0;
  // Note: this queue has no decrease key op, so we just toss everything in
  // and check on withdrawl.
  priority_queue<pair<int, int>, vector<pair<int, int>>, Order> qu;
  for (const auto &p : g[start]) {
    qu.insert(p);
  }

  for (const auto & p : qu) {
    cout << p.first << ":" << p.second << endl;
  }
}


int main() {
  ofstream fout ("butter.out");
  ifstream fin ("butter.in");


  int num_cows, num_nodes, num_paths;
  fin >> num_cows >> num_nodes >> num_paths;

  vector<int> hascow(num_nodes, 0);
  vector<vector<int>> g(num_nodes, vector<pair<int, int>>);

  for (int i = 0; i < num_cows; ++i) {
    int p;
    fin >> p;
    ++hascow[p-1];
  }

  for (int i = 0; i < num_paths; ++i) {
    int left, right, dist;
    fin >> left >> right >> dist;
    g[left].push_back(pair<int, int>(right, dist));
    g[right].push_back(pair<int, int>(left, dist));
  }

  for (int i = 0; i < num_paths; ++i) {
    if (hascow[i]) {
      dijk(g, hascow, i, num_nodes);
      return 0;
    }
  }

  int best_dist = numeric_limits<int>::max() / 2;


  fout << best_dist << endl;
  
  return 0;  
}

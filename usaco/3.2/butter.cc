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

struct Order {
  bool operator()(pair<int, int> &a, pair<int, int> &b) {
    return (a.second > b.second);
  }
};

void dijk(const vector<vector<pair<int,int>>> &g, vector<vector<int>> &res, const vector<int> &hascow, const int start, const int num_nodes) {
  // cout << "dijk " << start << endl;
  vector<int> d(num_nodes, numeric_limits<int>::max() / 2);

  d[start] = 0;
  // Note: this queue has no decrease key op, so we just toss everything in
  // and check on withdrawl.
  priority_queue<pair<int, int>, vector<pair<int, int>>, Order> qu;
  for (auto p : g[start]) {
    qu.push(p);
  }

  while (qu.size() > 0) {
    auto p = qu.top();
    qu.pop();
    int node = p.first;
    int dist = p.second;
    if (d[node] == numeric_limits<int>::max() / 2) {
      d[node] = dist;
      for (auto p : g[node]) {
	qu.push(pair<int, int>(p.first, p.second + d[node]));
      }
    }
  }

  // cout << "djik assign final\n";
  for (int i = 0; i < num_nodes; ++i) {
    // cout << "start:i " << start << ":" << i << " -- " << d[i] << endl;
    res[start][i] = d[i];
  }
}


int main() {
  ofstream fout ("butter.out");
  ifstream fin ("butter.in");


  int num_cows, num_nodes, num_paths;
  fin >> num_cows >> num_nodes >> num_paths;

  vector<int> hascow(num_nodes, 0);
  vector<vector<pair<int, int>>> g(num_nodes);
  vector<vector<int>> res(num_nodes, vector<int>(num_nodes));

  for (int i = 0; i < num_cows; ++i) {
    int p;
    fin >> p;
    ++hascow[p-1];
  }

  for (int i = 0; i < num_paths; ++i) {
    int left, right, dist;
    fin >> left >> right >> dist;
    g[left-1].push_back(pair<int, int>(right-1, dist));
    g[right-1].push_back(pair<int, int>(left-1, dist));
  }

  for (int i = 0; i < num_nodes; ++i) {
    dijk(g, res, hascow, i, num_nodes);
  }

  int best_dist = numeric_limits<int>::max() / 2;
  for (int i = 0; i < num_nodes; ++i) {
    int cur_dist = 0;
    // cout << "start " << i << endl;
    for (int j = 0; j < num_nodes; ++j) {
      cur_dist += hascow[j] * res[i][j];
      // cout << cur_dist << " " << hascow[j] << " : " << res[i][j] << endl;
    }
    if (cur_dist < best_dist) {
      best_dist = cur_dist;
    }
  }

  fout << best_dist << endl;
  
  return 0;  
}

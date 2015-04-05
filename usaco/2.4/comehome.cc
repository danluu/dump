/*
ID: danluu1
PROG: comehome
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

int c2i(char c) {
  int idx;
  if (c <= 'Z') {
    idx = c - 'A';
  } else {
    idx = c - 'a' + 26;
  }
  return idx;
}

bool char_has_cow(char c) {
  if (c <= 'Z') {
    assert(c >= 'A');
    int idx = c - 'A';
    if (c != 'Z') {
      // cout << "Found cow in " << c << endl;
      return true;
    }
  } else {
    assert(c >= 'a');
    assert(c <= 'z');
  }
  return false;
}

int find_min(const vector<int>& dist, const unordered_set<int> seen) {
  int res = numeric_limits<int>::max();
  int idx = -1;
  for (int i = 0; i < dist.size(); ++i) {
    if (dist[i] > 0 && dist[i] < res && seen.find(i) == seen.end()) {
      res = dist[i];
      idx = i;
    }     
  }
  return idx;
}

// Note: this could be sped up by using a heap.
pair<int,int> solve(const vector<vector<int>>& graph, const vector<bool>& has_cow, int num_nodes) {
  vector<int> dist(52, -512);
  unordered_set<int> seen;

  dist[25] = 0;
  seen.insert(25);
  for (int i = 0; i < 52; ++i) {
    if (graph[25][i] > -1) {
      dist[i] = graph[25][i];
    }
  }
  while (seen.size() < num_nodes) {
    int closest = find_min(dist, seen);
    assert(closest >= 0);
    seen.insert(closest);
    if (has_cow[closest]) {
      /*
      for (int i = 0; i < dist.size(); ++i) {
	cout << i << ":" << dist[i] << endl;
      }      
      */
      return make_pair(closest, dist[closest]);
    }
    for (int i = 0; i < 52; ++i) {
      if (graph[closest][i] >= 0 && (dist[i] > dist[closest] + graph[closest][i] || dist[i] < 0))  {
	dist[i] = dist[closest] + graph[closest][i];
      }
    }
  }
  
  assert(0);
  return make_pair(-1, -1);
}

// This has a lot of redundant stuff because it assumed that any pasture index could have a cow or not.
int main() {
  ofstream fout ("comehome.out");
  ifstream fin ("comehome.in");

  int nump;
  fin >> nump;

  // Graph is reverse so we can start from 'Z'.
  vector<vector<int>> graph(52, vector<int>(52, -512));
  vector<bool> has_cow(52, false);
  unordered_set<int> exists;
  
  for (int i = 0; i < nump; ++i) {
    char from, to;
    int dist;
    fin >> from >> to >> dist;
    // cout << "Read " << from << ":" << to << " -- " << dist << endl;
    int idx_f = c2i(from);
    int idx_t = c2i(to);
    exists.insert(idx_f);
    exists.insert(idx_t);
    if (char_has_cow(from)) {
	has_cow[idx_f] = true;
    }
    if (char_has_cow(to)) {
      has_cow[idx_t] = true;
    }
    if (graph[idx_f][idx_t] < 0 || dist < graph[idx_f][idx_t]) {
      graph[idx_f][idx_t] = dist;
      graph[idx_t][idx_f] = dist;
    }
  }

  pair<int,int> ans = solve(graph, has_cow, exists.size());
  int idx = ans.first;
  int dist = ans.second;
  fout << static_cast<char>(idx + 'A') << " " << dist << endl;

  return 0;
}

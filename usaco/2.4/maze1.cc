/*
ID: danluu1
PROG: maze1
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

void dfs(const vector<vector<int>> &graph, vector<int>& distance, int c_node, int c_dist) {
  distance[c_node] = c_dist;
  for (auto &next : graph[c_node]) {
    if (distance[next] > distance[c_node] + 1) {
      dfs(graph, distance, next, c_dist+1);
    }
  }
}

int main() {
  ofstream fout ("maze1.out");
  ifstream fin ("maze1.in");

  int input_w, input_h;
  fin >> input_w >> input_h;
  int w_limit = 2*input_w;
  int h_limit = 2*input_h;

  // vector<pair<int,int>> hole;
  // unordered_map<pair<int,int>,vector<pair<int,int>>> graph;

  vector<int> hole;
  vector<vector<int>> graph(input_w * input_h, vector<int>(0));
  vector<int> distance0(input_w * input_h, numeric_limits<int>::max());
  vector<int> distance1(input_w * input_h, numeric_limits<int>::max());  
  
  // 0,0 @ top left.
  for (int i = 0; i <= h_limit; ++i) {
    char junk_endl;
    fin.get(junk_endl);    
    for (int j = 0; j <= w_limit; ++j) {
      char c;
      fin.get(c);
      cout << c;
      bool hwall = i % 2 == 0;
      bool vwall = j % 2 == 0;
      int x = (j-1)/2;
      int y = (i-1)/2;
      int idx = y * input_w + x;
      
      if (hwall && vwall) {
	assert(c == '+');
      }
      // Horizontal wall row.
      if (hwall && !vwall) {
	// Found '-' or ' '
	if (c == '-') {
	} else if (c == ' ') {
	  if (i == 0 || i == h_limit) {
	    hole.push_back(idx);
	  } else {
	    // Normal hole.
	    // y is always associated with the lower 'y' value.
	    int edge_idx = idx + input_w;
	    graph[idx].push_back(edge_idx);
	    graph[edge_idx].push_back(idx);
	  }
	} else {
	  assert(0);
	}
      }
      // Vertical wall col.
      if (vwall & !hwall) {
	if (c == '|') {	  
	} else if (c == ' ') {
	  if (j == 0 || j == w_limit) {
	    hole.push_back(idx);
	  } else {
	    // Normal hole.
	    int edge_idx = idx + 1;
	    // cout << "Edge from " << idx << ":" << edge_idx << endl;
	    graph[idx].push_back(edge_idx);
	    graph[edge_idx].push_back(idx);	    
	  }
	} else {
	  assert(0);
	}
      }
    }
    cout << endl;
  }
  
  assert(hole.size() == 2);
  cout << "holes " << hole[0] << " " << hole[1] << endl;
  dfs(graph, distance0, hole[0], 1);
  cout << "Call again\n";
  dfs(graph, distance1, hole[1], 1);

  // Special case graph that immediately returns from dfs.
  if (distance1.size() == 1) {
    fout << 1 << endl;
    return 0;
  }

  int largest_min = 0;
  for (int i = 0; i < distance0.size(); ++i) {
    int node_min = min(distance0[i], distance1[i]);
    // cout << node_min << " " << distance0[i] << " " << distance1[i] << endl;
    if (i % input_w == 0) {
      cout << endl;
    }
    cout << "\t" << distance1[i];
    if (node_min > largest_min) {
      largest_min = node_min;
    }
  }
  cout << endl;

  fout << largest_min << endl;
  return 0;
}

/*
ID: danluu1
PROG: cowtour
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

double dist(pair<double, double> a, pair<double, double> b) {
  double mag = (a.first - b.first) * (a.first-b.first) +
    (a.second - b.second) * (a.second - b.second);
  return sqrt(mag);
}

// Floyd-Warshall.
void fw(vector<vector<double>> &cdist, int nump) {
  for (int k = 0; k < nump; ++k) {
    for (int i = 0; i < nump; ++i) {
      for (int j = 0; j < nump; ++j) {
	double with_k = cdist[i][k] + cdist[k][j];
	if (with_k < cdist[i][j]) {
	  cdist[i][j] = with_k;
	}
      }
    }
  }
}

double connect(const vector<vector<double>>& cdist, const vector<pair<double, double>> &locs, int nump, int ii, int jj) {
  double bridge = dist(locs[ii], locs[jj]);  
  
  double ii_max = 0;
  double jj_max = 0;
  for (int i = 0; i < nump; ++i) {
    if (i != ii && cdist[i][ii] != numeric_limits<double>::infinity() && cdist[i][ii] > ii_max) {
      ii_max = cdist[i][ii];
    }
    if (i != jj && cdist[i][jj] != numeric_limits<double>::infinity() && cdist[i][jj] > jj_max) {
      jj_max = cdist[i][jj];
    }    
  }

  return bridge + ii_max  + jj_max;
}

int main() {
  ofstream fout ("cowtour.out");
  ifstream fin ("cowtour.in");

  int nump;
  fin >> nump;

  vector<pair<double,double>> locs(nump);
  vector<vector<bool>> graph(nump, vector<bool>(nump));
  
  for (int i = 0; i < nump; ++i) {
    double x;
    double y;
    fin >> x >> y;
    locs[i] = make_pair(x, y);
  }

  for (int i = 0; i < nump; ++i) {
    for (int j = 0; j < nump; ++j) {
      char c;
      fin >> c;
      if (c == '1') {
	graph[i][j] = true;
      } else {
	graph[i][j] = false;
      }
    }
  }

  vector<vector<double>> orig_dist(nump,
				   vector<double>(nump, numeric_limits<double>::infinity()));

  for (int i = 0; i < nump; ++i) {
    for (int j = 0; j < nump; ++j) {
      if (graph[i][j]) {
	orig_dist[i][j] = dist(locs[i], locs[j]);	
      }
      // cout << "\t" << orig_dist[i][j];	      
    }
    // cout << endl;
  }
  fw(orig_dist, nump);

  // Maximum that doesn't use new path.
  double old_max = 0;  
  for (int i = 0; i < nump; ++i) {
    for (int j = 0; j < i; j++) {
      if (orig_dist[i][j] != numeric_limits<double>::infinity() && orig_dist[i][j] > old_max) {
	old_max = orig_dist[i][j];
      }	
    }
  }

  double min_max = numeric_limits<double>::infinity();
  for (int i = 0; i < nump; ++i) {
    for (int j = 0; j < i; ++j) {
      if (orig_dist[i][j] == numeric_limits<double>::infinity()) {
	double cur = connect(orig_dist, locs, nump, i, j);
	if (cur < min_max) {
	  min_max = cur;
	}
      }
    }
  }

  fout.precision(6);
  if (old_max > min_max) {
    fout << std::fixed << old_max << endl;
  } else {
    fout << std::fixed << min_max << endl;
  }

  return 0;
}

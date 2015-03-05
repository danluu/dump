/*
ID: danluu1
PROG: nocows
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

int main() {
  ofstream fout ("nocows.out");
  ifstream fin ("nocows.in");

  long num, height;
  fin >> num >> height;

  vector<vector<long>> ways(num+1, vector<long>(height+1, 0));

  if (num <= 3 || height <= 2) {
    if ((num == 1 && height == 1) ||
	(num == 3 && height == 2)) {
      fout << 1 << endl;
    } else {
      fout << 0 << endl;
    }
    return 0;
  }
  
  ways[1][1] = 1;
  ways[3][2] = 1;

  // ways[num_nodes][height].
  for (long i = 4; i <= num; ++i) {
    for (long j = 3; j <= height; ++j) {
      long sum = 0; // Number of ways to make a tree of height < j
      // k is number of nodes in left sub-tree.
      for (long k = 1; k < i-1; ++k) {
	// cout << i << " " << j << " " << k << endl;
	// l is height of smaller subtree. Could be left or right.
	// We handle both cases here. Taller subtree must be height
	// j - 1.
	long left_tall = ways[k][j-1];
	long right_tall = ways[i-1-k][j-1];		  
	for (long l = 1; l < j-1; ++l) {
	  long right_short = ways[i-1-k][l];
	  sum += left_tall * right_short % 9901;
	  long left_short = ways[k][l];
	  sum += left_short * right_tall % 9901;
	}
	// Don't double count tall/tall case.
	sum += left_tall * right_tall % 9901;
      }
      ways[i][j] = sum % 9901;
    }
  }

  fout << ways[num][height] << endl;
  
  return 0;

}

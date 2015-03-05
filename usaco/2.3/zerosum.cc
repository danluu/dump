/*
ID: danluu1
PROG: zerosum
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

/*
 Brute force method. Each int represents exactly one possibility
 ' ', '+', '-'. maps to 0, 1, 2
 The first digit is special cased since it shouldn't have an operator
*/


int main() {
  ofstream fout ("zerosum.out");
  ifstream fin ("zerosum.in");

  int digits;
  fin >> digits;

  int max = 1;
  for (int i = 0; i < digits; ++i) {
    max *= 3;
  }
  
  // cout << max << endl;
  vector<char> op2str = {' ', '+', '-'};
  vector<string> all_results;
  for (int i = 0; i < max; ++i) {
    int iter = i;
    int sum = 0;
    int temp = 0;
    int last_op = 1;
    ostringstream result;

    for (int j = 1; j <= digits; ++j) {
      int op = iter % 3;
      // only + for first digit.
      if (j == 1 && op != 1) {
	goto end;
      }
      if (j != 1) {
	result << op2str[op];
      }
      result << j;
      iter /= 3;
      // cout << "op: " << op << " last_op: " << last_op << " temp: " << temp << endl;
      if (op == 0) {
	temp *= 10;
	temp += j;
      } else if (op == 1 || op == 2) {
	if (last_op == 1) {
	  sum += temp;
	} else if (last_op == 2) {
	  sum -= temp;
	}
	last_op = op;
	temp = j;
      } else {
	assert(0);
      }
    }
    // Handle last digit(s).
    if (last_op == 1) {
      sum += temp;
    } else if (last_op == 2) {
      sum -= temp;
    }

    if (sum == 0) {
      all_results.push_back(result.str());
    } else {
      // cout << sum << endl;
    }
  end:
    int ignore = 0;
  }

  sort(all_results.begin(),all_results.end());
  for (auto &s : all_results) {
    fout << s << endl;
  }
  return 0;
}

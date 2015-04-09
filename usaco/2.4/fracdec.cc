/*
ID: danluu1
PROG: fracdec
LANG: C++11
*/

#include <math.h>
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

long unique(long x, long y) {
  return x + (y << 32);
}

// There is a bug here that will cause an extra \n to come out if we have a multiple of 76 in length.
int wrap(int len, stringstream& ss) {
  if ((len + 1) >= 76) {
    ss << "\n";
    return 0;
  }
  return len + 1;
}

string solve(long num, long den) {
  long orig_num = num;
  vector<long> cur;
  unordered_map<long, long> seen;
  int idx = 0;

  while (1) {
    // cout << "solve " << num << " " << den << endl;
    auto iter = seen.find(unique(num, den));
    bool repeat = iter != seen.end();
    if (num == 0 || repeat) {
      stringstream ss;
      int line_len = 0;
      for (int i = 0; i < cur.size(); i++) {
	// cout << "output loop " << i << ":" << line_len << endl;
	if (repeat && (*iter).second == i) {
	  ss << "(";
	  line_len = wrap(line_len, ss);
	}
	ss << cur[i];
	line_len = wrap(line_len, ss);      

	if (i == 0) {
	  ss << ".";
	  line_len = wrap(line_len, ss);
	  if (orig_num > den) {
	    int num_digits = static_cast<int>(log10(cur[i]));
	    line_len += num_digits; // We've already added one, but we don't add one for the ".".
	  }
	}
      }
      if (repeat) {
	ss << ")";
	line_len = wrap(line_len, ss);      
      }
      if (orig_num % den == 0) {
	ss << "0";
	line_len = wrap(line_len, ss);      
      }
      return ss.str();
    }
  
    seen[unique(num, den)] = idx;
    cur.push_back(num/den);
    ++idx;
    num = 10 * (num % den);  
  }
}

int main() {
  ofstream fout ("fracdec.out");
  ifstream fin ("fracdec.in");

  long num, den;
  fin >> num >> den;

  fout << solve(num, den) << endl;
  return 0;
}

/*
ID: danluu1
PROG: runround
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

bool runround(unsigned long x) {
  vector<int> digits;
  vector<int> seen(10,0);
  if (x == 0) {
    return false;
  }
  while (x > 0) {
    int d = x % 10;
    if (d == 0 || seen[d] > 0) {
      return false;
    }
    ++seen[d];
    digits.push_back(d);
    x /= 10;
  }

  fill(seen.begin(), seen.end(), 0);
  reverse(digits.begin(), digits.end());
  int index = 0;
  int length = digits.size();
  for (int i = 0; i < length; ++i) {    
    int steps = digits[index];
    if (seen[steps] > 0) {
      return false;
    }
    ++seen[steps];
    index = (index + steps) % length;
  }  
  return index == 0;  
}

int main() {
  ofstream fout ("runround.out");
  ifstream fin ("runround.in");

  unsigned long n;
  fin >> n;

  unsigned long current = n+1;
  while (!runround(current)) {
    ++current;
  }
  fout << current << endl;
  return 0;

}

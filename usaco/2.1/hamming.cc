/*
ID: danluu1
PROG: hamming
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

// 
int popcount(int x) {
  assert(x < (1 << 8));
  int original = x;
  int count = 0;
  for (int i = 0; i < 8; ++i) {
    count += (x&1);
    x >>= 1;
  }
  // cout << "popcount(" << original << "):" << count << endl;
  return count;
}

int is_distance_d(const vector<int>& words, int x, int d) {
  for (auto& y : words) {
    // cout << x << ":" << y << endl;
    int diff = x ^ y;
    if (popcount(diff) < d) {
      return false;
    }
  }
  return true;
}

int main() {
  ofstream fout ("hamming.out");
  ifstream fin ("hamming.in");

  int n, b, d;
  fin >> n >> b >> d;

  int cur = 0;
  vector<int> words;

  // Brute force at most 256 possibilities.
  while (words.size() < n && cur < (1 << b)) {
    if (is_distance_d(words, cur, d)) {
      words.push_back(cur);
    }
    ++cur;
  }

  int num = 0;
  for (auto& x : words) {
    if (!(num%10 == 0)) {
      fout << " ";
    }
    fout << x;
    if (num%10 == 9) {
      fout << endl;
    }
    ++num;
  }
  if (num%10 != 0) {
    fout << endl;
  }
  return 0;
}

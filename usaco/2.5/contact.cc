/*
ID: danluu1
PROG: contact
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

void count(const string &all_bits, unordered_map<string, int> &freqs, int len) {
  for (int i = 0; i <= static_cast<int>(all_bits.length()) - len; ++i) {
    string sequence = all_bits.substr(i, len);
    freqs[sequence]++;
  }
}

unordered_map<string, int> freqs;

bool sortfn(string left, string right) {
  if (freqs[left] == freqs[right] && left.length() == right.length()) {
    return left < right;
  } else if (freqs[left] == freqs[right]) {
    return left.length() < right.length();
  } else {
    return freqs[left] > freqs[right];
  }
}

int main() {
  ofstream fout ("contact.out");
  ifstream fin ("contact.in");

  int a, b, n;
  fin >> a >> b >> n;
  string s;

  stringstream bits;
  while (fin >> s) {
    bits << s;
  }

  string all_bits =  bits.str();
  for (int i = a; i <= b; ++i) {
    count(all_bits, freqs, i);
  }

  vector<string> order(freqs.size());

  int i = 0;
  for (auto const &ps : freqs) {
    // cout << ps.first << " " << ps.second << endl;
    order[i++] = ps.first;
  }

  sort(order.begin(), order.end(), sortfn);
  i = 0;
  int last_freq = -1;
  int num_same = 0;
  for (auto const &key : order) {
    int val = freqs[key];
    if (last_freq != val) {
      if (last_freq != -1) {
	fout << endl;
      }
      if (i++ >= n) {
	return 0;
      }
      fout << val << endl;
      last_freq = val;
      num_same = 0;
    } else {
      num_same++;
      if (num_same < 6) {
	fout << " ";
      } else {
	fout << endl;
	num_same = 0;
      }
    }
    fout << key;
  }
  fout << endl;
  return 0;  
}

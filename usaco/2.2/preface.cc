/*
ID: danluu1
PROG: preface
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

vector<pair<int,string>> numeral = {{1000,"M"},{900,"CM"},{500,"D"},{400,"CD"},
			   {100,"C"},{90,"XC"},{50,"L"},{40,"XL"},
			   {10,"X"},{9,"IX"},{5,"V"},{4,"IV"},
			   {1,"I"}};

string int2roman(int x) {
  string roman = "";
  for (auto& kv : numeral) {
    while (x >= kv.first) {
      roman += kv.second;
      x -= kv.first;
    }
  }
  return roman;
}

int main() {
  ofstream fout ("preface.out");
  ifstream fin ("preface.in");

  int n;
  fin >> n;

  vector<int> counts(7,0);
  for (int i = 1; i <= n; ++i) {
    string numeral = int2roman(i);
    for (auto& c : numeral) {
      switch(c) {
      case 'I': ++counts[0]; break;
      case 'V': ++counts[1]; break;
      case 'X': ++counts[2]; break;
      case 'L': ++counts[3]; break;
      case 'C': ++counts[4]; break;
      case 'D': ++counts[5]; break;
      case 'M': ++counts[6]; break;
      }
    }
  }

  vector<char> outputs = {'I','V','X','L','C','D','M'};
  for (int i = 0; i < counts.size(); ++i) {
    if (counts[i] > 0) {
      fout << outputs[i] << " " << counts[i] << endl;
    }
  }
  return 0;
}

/*
ID: danluu1
PROG: palsquare
LANG: C++11
*/

#include <stdio.h>
#include <stdlib.h>
#include <cassert>
#include <iostream>
#include <fstream>
#include <queue> 
#include <set>
#include <string>
#include <vector>

#define MAX_NUM 300

using namespace std;

vector<char> int2char= {'0','1','2','3','4','5','6','7','8','9',
			'A','B','C','D','E','F','G','H','I','J','K'};

string my_itoa(int x, int b, int debug) {
  vector<char> stack;
  int rest = x;

  while (rest > 0) {
    if (debug) {
      cout << "rest " << rest << endl;
    }
    char value = int2char[rest % b];
    rest = rest / b;
    stack.push_back(value);
  }
  string res(stack.rbegin(),stack.rend());
  return res;
}

int main() {
  ofstream fout ("palsquare.out");
  ifstream fin ("palsquare.in");
  int base;

  fin >> base;

  for (int i = 1; i <= MAX_NUM; ++i) {
    int square = i * i;
    string buffer = my_itoa(square, base, 0);
    size_t len = buffer.size();
    int palindrome = 1;
    // cout << "Checking " << buffer << endl;
    for (int j = 0; j < len/2; ++j) {
      if (buffer[j] != buffer[len-j-1]) {
	// cout << buffer[j] << " "<< buffer[len-j-1] << endl;
	palindrome = 0;
      }
    }
    if (palindrome) {
      fout << my_itoa(i,base,0) << " " << buffer << endl;
      cout << i << " " << my_itoa(i,base,0) << " " << buffer << endl;
    }
  }
  return 0;
}

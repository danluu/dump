/*
ID: danluu1
PROG: dualpal
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

int is_palindrome(int x, int base){
  string buffer = my_itoa(x, base, 0);
  size_t len = buffer.size();
  // cout << "Checking " << buffer << endl;
  for (int j = 0; j < len/2; ++j) {
    if (buffer[j] != buffer[len-j-1]) {
      // cout << buffer[j] << " "<< buffer[len-j-1] << endl;
      return 0;
    }
  }
  return 1;
}

int is_dual_palindrome(int x) {
  int num_palindromes = 0;
  for (int b = 2; b <= 10; ++b) {
    num_palindromes += is_palindrome(x, b);
  }
  // cout << x << " " << num_palindromes << endl;
  return (num_palindromes >= 2);
}

int main() {
  ofstream fout ("dualpal.out");
  ifstream fin ("dualpal.in");
  int n, start;

  int num_palindromes = 0;
  fin >> n >> start;

  int current = start+1;

  while (num_palindromes < n) {
    int is_dual = is_dual_palindrome(current);
    if (is_dual) {
      ++num_palindromes;
      fout << current << endl;
    }
    ++current;
  }
  return 0;
}

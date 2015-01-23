/*
ID: danluu1
PROG: pprime
LANG: C++11
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <algorithm> 
#include <cassert>
#include <iostream>
#include <fstream>
#include <limits>
#include <map>
#include <queue> 
#include <set>
#include <sstream>
#include <string>
#include <tuple>
#include <unordered_set>
#include <vector>

using namespace std;

bool is_prime(int x) {
  if (x % 2 == 0 || x < 1) {
    return false;
  }
  for (int i = 3; i < 2*sqrt(x); i+= 2) {
    if (x % i == 0) return false;
  }
  return true;
}

// Need to run twice, once for odd and once for even.
void generate_pp(vector<int>& pp, vector<int> temps, int digits, int len, int bound) {
  cout << "generate_pp\n";
  assert(digits % 2 == 0);
  if (digits == 0) {
    return;
  }
  vector<int> possible = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
  vector<int> new_temps;
  for (const auto& x : temps) {
    for (const auto& y : possible) {
      int temp = y * 1 + x * 10 + y * pow10(len + 1);
      new_temps.push_back(temp);
      if (y != 0 && temp <= bound && is_prime(temp)) {
	// cout << "x " << x << " y " << y << " temp " << temp << endl;
	pp.push_back(temp);
      }
    }
  }
  generate_pp(pp, new_temps, digits-2, len+2, bound);
}

int digits_needed(int x) {
  int digits = 0;
  int temp = x;
  while (temp > 0) {
    temp /= 10;
    ++digits;
  }
  return digits;
}

int main() {
  ofstream fout ("pprime.out");
  ifstream fin ("pprime.in");

  int a,b;
  fin >> a >> b;

  int max_digits = digits_needed(b);
  int odd_extra_digits = (max_digits-1) - ((max_digits+1)%2);
  int even_extra_digits = (max_digits-2) - ((max_digits)%2);
  cout << "digits " << max_digits << " odd " << odd_extra_digits << " even " << even_extra_digits << endl;
  
  // auto sieve = make_primes_sieve(b);
  cout << "sieve done\n";
  vector<int> starter_odd = {0,1,2,3,4,5,6,7,8,9};
  vector<int> pp_odd = {2,3,5,7};
  generate_pp(pp_odd, starter_odd, odd_extra_digits, 1, b);
  vector<int> pp_even = {11};
  vector<int> starter_even = {0,11,22,33,44,55,66,77,88,99};
  generate_pp(pp_even, starter_even, even_extra_digits, 2, b);

  pp_odd.insert(pp_odd.end(),pp_even.begin(), pp_even.end());
  sort(pp_odd.begin(), pp_odd.end());
  for (auto& x : pp_odd) {
    if (x >= a) {
      fout << x << endl;
    }
  }
  return 0;
}

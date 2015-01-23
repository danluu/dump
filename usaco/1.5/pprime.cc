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

vector<char> int2char= {'0','1','2','3','4','5','6','7','8','9',
			'A','B','C','D','E','F','G','H','I','J','K'};

bool is_prime(const vector<int>& primes, int x) {
  for (int i = 0; i < primes.size(); ++i) {
    if (x % primes[i] == 0) {
      return false;
    }
  }
  return true;
}

// If too slow, try sieve.
vector<int> make_primes(int b) {
  std::vector<int> primes;
  primes.push_back(2);
  for(int i = 3; i <= b; ++i) {
    if (is_prime(primes, i)) {
      primes.push_back(i);
    }
  }
  return primes;
}

vector<bool> make_primes_sieve(int b) {
  vector<bool> sieve(b+1);
  int ssize = sieve.size();
  for (int i = 0; i < ssize; ++i) {
    sieve[i] = true;
  }
  sieve[0] = false;
  sieve[1] = false;

  for (int i = 0; i < ssize; ++i) {
    if (sieve[i]) {
      for (int j = i+i; j < ssize; j+=i) {
	sieve[j] = false;
      }
    }
  }
  return sieve;
}

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

int is_palindrome_fast(int x) {
  int reverse = 0;
  int temp = x;
  while (temp > 0) {
    int digit = temp % 10;
    reverse = reverse * 10 + digit;
    temp = temp / 10;
  }
  return x == reverse;
}

int pow10(int exp) {
  int ans = 10;
  while (exp > 1) {
    ans *= 10;
    --exp;
  }
  return ans;
}

// Need to run twice, once for odd and once for even.
void generate_pp(const vector<bool>& sieve, vector<int>& pp, vector<int> temps, int digits, int len, int bound) {
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
      if (y != 0 && temp <= bound && sieve[temp]) {
	// cout << "x " << x << " y " << y << " temp " << temp << endl;
	pp.push_back(temp);
      }
    }
  }
  generate_pp(sieve, pp, new_temps, digits-2, len+2, bound);
}

int digits_needed(int x) {
  int digits = 0;
  int temp = x;
  while (temp > 0) {
    //    cout << "temp " << temp << " digits " << digits << endl;
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

  /*
  vector<int> primes = make_primes(b);
  cout << "primes done\n";
  for (const auto& x : primes) {
    if (is_palindrome(x, 10) && x >= a) {
      fout << x << endl;
    }
  }
  */

  /*
  auto sieve = make_primes_sieve(b);
  for (int x = a; x <= b; ++x) {
    if (sieve[x] && is_palindrome_fast(x)) {
      fout << x << endl;
    }
  }
  */


  int max_digits = digits_needed(b);
  int odd_extra_digits = (max_digits-1) - ((max_digits+1)%2);
  int even_extra_digits = (max_digits-2) - ((max_digits)%2);
  cout << "digits " << max_digits << " odd " << odd_extra_digits << " even " << even_extra_digits << endl;
  
  auto sieve = make_primes_sieve(b);
  vector<int> starter_odd = {0,1,2,3,4,5,6,7,8,9};
  vector<int> pp_odd = {2,3,5,7};
  generate_pp(sieve, pp_odd, starter_odd, odd_extra_digits, 1, b);
  vector<int> pp_even = {11};
  vector<int> starter_even = {0,11,22,33,44,55,66,77,88,99};
  generate_pp(sieve, pp_even, starter_even, even_extra_digits, 2, b);

  pp_odd.insert(pp_odd.end(),pp_even.begin(), pp_even.end());
  sort(pp_odd.begin(), pp_odd.end());
  for (auto& x : pp_odd) {
    if (x >= a) {
      fout << x << endl;
    }
  }
  return 0;
}

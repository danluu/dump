/*
ID: danluu1
PROG: sprime
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

void make_primes_sieve(vector<bool>& sieve) {
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
}

int lbound(int n) {
  if (n == 1) {
    return 0;
  }
  int bound = 10;
  n-=2;
  while (n > 0) {
    --n;
    bound *= 10;
  }
  return bound;
}

bool is_sprime(int x, vector<bool>& sieve) {
  while (x > 0) {
    if (!sieve[x]) {
      return 0;
    }
    x /= 10;
  }
  return 1;
}


bool is_prime(int x) {
  if (x % 2 == 0 || x < 1) {
    return false;
  }
  for (int i = 3; i < 2*sqrt(x); i+= 2) {
    if (x % i == 0) return false;
  }
  return true;
}

vector<int> generate_sprimes(vector<int> temps, int digits) {
  if (digits == 0) {
    return temps;
  }
  vector<int> possible = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
  vector<int> new_temps;
  for (const auto& left : temps) {
    for (const auto& right : possible) {
      int candidate = left * 10 + right;
      if (is_prime(candidate)) {
	new_temps.push_back(candidate);
      }
    }
  }
  return generate_sprimes(new_temps, digits-1);
}

int main() {
  ofstream fout ("sprime.out");
  ifstream fin ("sprime.in");

  int n;
  fin >> n;

  vector<int> temps = {2,3,5,7};
  auto sprimes = generate_sprimes(temps,n-1);
  sort(sprimes.begin(), sprimes.end());
  for (auto& x : sprimes) {
    fout << x << endl;
  }
  return 0;
}

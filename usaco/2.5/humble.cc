/*
ID: danluu1
PROG: humble
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

/*
vector<bool> sieve(long x) {
  long lmax = sqrt(x);
  ++lmax;

  vector<bool> s(lmax);
  for (long i = 0; i < s.size(); ++i) {
    s[i] = true;
  }

  for (long i = 2; i < s.size(); ++i) {
    if (s[i] == true) {
      for (long j = 2; j < s.size(); j += i) {
	s[j] = false;
      }
    }
  }
  return s;
}
*/

long long solve(const vector<long long>& primes, int n) {
  priority_queue<long long, vector<long long>, greater<long long>> q;
  unordered_set<long long> seen;

  for (const auto& p : primes) {
    seen.insert(p);
    q.push(p);
  }

  int i = 0;
  while (i < n-1) {
    assert(q.size() > 0);
    long long cur = q.top();
    q.pop();
    seen.erase(cur);
    // cout << i << " " << cur << endl;
    for (const auto& x : primes) {
      long long next = x * cur;
      // cout << "check " << next << endl;      
      if (seen.find(next) == seen.end()) {
	// cout << "push " << next << endl;
	seen.insert(next);
	q.push(next);
      }
    }
    ++i;
  }

  return q.top();
}

long long solve2(const vector<long long>& primes, int n) {
  set<long long> q;

  for (const auto& p : primes) {
    q.insert(p);
  }

  int i = 0;
  while (i < n-1) {
    assert(q.size() > 0);
    long long cur = *q.begin();
    q.erase(q.begin());
    // cout << i << " " << cur << endl;
    for (const auto& x : primes) {
      long long next = x * cur;
      // cout << "check " << next << endl;      
      q.insert(next);
    }
    ++i;
  }

  return *q.begin();  
}

long long solve3(const vector<long long>& primes, int n) {
  vector<long long> h(n + 1);
  vector<int> prime_idx(primes.size(), 0);
  int i = 0;
  h[0] = 1;
  while (i < n) {
    long long min_i = numeric_limits<long long>::max();
    int min_idx = -1;
    for (int j = 0; j < primes.size(); ++j) {
      long long cur = primes[j] * h[prime_idx[j]];
      // cout << "trying " << cur << endl;      
      if (cur < min_i && cur > h[i]) {
	min_i = cur;
      }
    }
    // cout << "H " << min_i << " " << i << endl;
    h[++i] = min_i;
    
    // Need to increment all beacuse we can tie.
    for (int j = 0; j < primes.size(); ++j) {
      long long cur = primes[j] * h[prime_idx[j]];
      if (cur == min_i) {
	++prime_idx[j];
      }
    }
  }
  
  return h[n];  
}

int main() {
  ofstream fout ("humble.out");
  ifstream fin ("humble.in");

  int k, n;
  fin >> k >> n;

  vector<long long> primes;
  
  for (int i = 0; i < k; ++i) {
    long long p;
    fin >> p;
    primes.push_back(p);
  }


  fout << solve3(primes, n) << endl;
  
  return 0;
}

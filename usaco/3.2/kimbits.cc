/*
ID: danluu1
PROG: kimbits
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

int main() {
  ofstream fout ("kimbits.out");
  ifstream fin ("kimbits.in");

  long long N, L, I;
  fin >> N >> L >> I;

  // TODO: fix this to not overflow for "large" problems.
  cout << "make fact\n";
  vector<long long> fact(N+1);
  fact[0] = 1;
  for (long long i = 1; i <= N; ++i) {
    fact[i] = i * fact[i-1];
  }
  for (const auto& x : fact) {
    cout << x << " ";
  }
  cout << endl;

  // TODO: use recurrence to calculate (n choose k).
  // This shouldn't overflow.
  cout << "make choose\n";
  vector<vector<long long>> choose(N+1, vector<long long>(N+1));
  for (long long i = 0; i <= N; ++i) {
    for (long long j = 0; j <= N; ++j) {
      if (j > i) {
	choose[i][j] = 0;
      } else {
	assert(i-j >= 0);
	choose[i][j] = fact[i] / (fact[i-j] * fact[j]);
      }
      cout << choose[i][j] << " " ;
    }
    cout << endl;
  }

  cout << "make ways\n";
  vector<vector<long long>> ways(N+1, vector<long long>(N+1));
  for (long long i = 0; i <= N; ++i) {
    for (long long j = 0; j <= N; ++j) {
      long long sum = 0;
      for (long long k = 0; k <= j; ++k) {
	sum += choose[i][k];
      }
      ways[i][j] = sum;
      cout << ways[i][j] << " ";
    }
    cout << endl;
  }

  // cout << "final loop\n";
  long long n = N;
  long long l = L;
  long long i = I;
  while (n > 0) {
    cout << "start n " << n << " l " << l << " i " << i << " cmp " << ways[n-1][l] << endl;
    if (i > ways[n-1][l]) {
      fout << "1";
      i -= ways[n-1][l];
      --l;
    } else {
      fout << "0";
    }
      --n;
      assert(l >= 0);
      //    cout << "end   n " << n << " l " << l << " i " << i << endl;
  }
  fout << endl;

  return 0;  
}

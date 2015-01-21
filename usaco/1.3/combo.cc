/*
ID: danluu1
PROG: combo
LANG: C++11
*/

#include <stdio.h>
#include <stdlib.h>
#include <algorithm> 
#include <cassert>
#include <iostream>
#include <fstream>
#include <queue> 
#include <set>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

// Consider corner case of max_n == 1.
// x could be 3 or -1.
int possible_to_combo(int x, int max_n) {
  int wat = x;
  while (wat > max_n) {
    wat -= max_n;
  }

  while (wat < 1) {
    wat += max_n;
  }
  return wat;
}

vector<int> possible(int x, int max_n) {
  vector<int> range;
  for (int i = (x-2); i <= (x+2); ++i) {
    int x = possible_to_combo(i, max_n);
    range.push_back(x);
  }
  return range;
}


void solve_helper(set<string>& solutions, vector<int> partial_sol, vector<int> partial_comb, int max) {
  if (partial_sol.size() >= 3) {
    assert(partial_sol.size() == 3);
    ostringstream result;
    result << partial_sol[2] << "," << partial_sol[1] << "," << partial_sol[0];
    solutions.insert(result.str());
    return;
  }

  for (auto &x : partial_comb) {
    int digit = partial_comb.back();
    vector<int> possible_digits = possible(digit, max);
    partial_comb.pop_back();
    for (auto &y : possible_digits) {
      partial_sol.push_back(y);
      solve_helper(solutions, partial_sol, partial_comb, max);
      partial_sol.pop_back();
    }
    partial_comb.push_back(digit);
  }
}

void solve(set<string>& solutions, vector<int> combo, int max) {
  vector<int> partial_sol;
  solve_helper(solutions, partial_sol, combo, max);
}

int main() {
  ofstream fout ("combo.out");
  ifstream fin ("combo.in");

  int max_n;
  fin >> max_n;

  int a, b, c;
  vector<int> fj_comb;
  fin >> a >> b >> c;
  fj_comb.push_back(a);
  fj_comb.push_back(b);
  fj_comb.push_back(c);

  vector<int> m_comb;
  fin >> a >> b >> c;
  m_comb.push_back(a);
  m_comb.push_back(b);
  m_comb.push_back(c);

  set<string> solutions;
  solve(solutions, fj_comb, max_n);
  solve(solutions, m_comb, max_n);

  /*
  for (const auto& elem: solutions) {
    cout << elem << endl;
  }
  */

  fout << solutions.size() << endl;
  return 0;
}

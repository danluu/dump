/*
ID: danluu1
PROG: barn1
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
#include <string>
#include <vector>

using namespace std;

struct farmer {
  int cost;
  int units;
};

// smallest first.
bool cmp_cost(const farmer& a, const farmer& b) {
  return a.cost < b.cost;
}

int main() {
  ofstream fout ("barn1.out");
  ifstream fin ("barn1.in");

  int boards, stalls, cows;
  fin >> boards >> stalls >> cows;

  vector<int> gaps;
  vector<int> stall_list;
  for (int i = 0; i < cows; ++i) {
    int current_stall;    
    fin >> current_stall;
    stall_list.push_back(current_stall);
  }
  
  sort(stall_list.begin(), stall_list.end());

  int last_stall = -1;
  for (int i = 0; i < cows; ++i) {
    int current_stall = stall_list[i];
    // cout << current_stall << " " << current_stall - last_stall -1 << endl;
    // No point in covering before first cow.
    if (i != 0) {
      assert(last_stall != -1);
      gaps.push_back(current_stall - last_stall - 1);
    }

    last_stall = current_stall;
  }

  // No point in covering after last cow.
  // gaps.push_back(stalls - last_stall - 1);

  /*
  for (auto x : gaps) {
    cout << x << endl;
  }
  */

  while (fin >> boards) {
    assert(0);
  }

  cout << "Sorting\n";
  sort(gaps.begin(), gaps.end(), greater<int>());

  int not_covered = 0;
  for (int i = 0; i < boards; ++i) {
    not_covered += gaps[i];
    // cout << gaps[i] << endl;
  }

  cout << "covered\n";
  int total_gaps = 0;
  for (int i = boards - 1; i < gaps.size(); ++i) {
    // cout << gaps[i] << endl;
    total_gaps += gaps[i];
  }

  cout << total_gaps << " " << cows << endl;
  fout << total_gaps + cows << endl;

  return 0;
}

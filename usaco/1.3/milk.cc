/*
ID: danluu1
PROG: milk
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
  ofstream fout ("milk.out");
  ifstream fin ("milk.in");

  int demand, num_farmers;
  fin >> demand >> num_farmers;

  vector<farmer> all;
  
  cout << "Reading input data\n";
  for (int i = 0; i < num_farmers; ++i) {
    int cost, units;
    fin >> cost >> units;
    farmer f;
    f.cost = cost;
    f.units = units;
    all.push_back(f);
  }

  while (fin >> demand) {
    assert(0);
  }

  cout << "Sorting\n";
  sort(all.begin(), all.end(), cmp_cost);


  cout << "Producing output\n";
  int supplied = 0;
  int total_cost = 0;
  int i = 0;
  while (supplied < demand) {
    int delta = 0;
    if (all[i].units + supplied >= demand) {
      delta = demand - supplied;
    } else {
      delta = all[i].units;
    }
    total_cost += delta * all[i].cost;
    supplied += delta;
    ++i;
    assert(i <= all.size());
  }

  fout << total_cost << endl;

  return 0;
}

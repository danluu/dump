/*
ID: danluu1
PROG: wormhole
LANG: C++11
*/

#include <stdio.h>
#include <stdlib.h>
#include <algorithm> 
#include <cassert>
#include <iostream>
#include <fstream>
#include <map>
#include <queue> 
#include <set>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

int cmp_pairs(const pair<int,int>& left, const pair<int,int>& right) {
  if (left.second < right.second) {
    return 1;
  } else if (left.second == right.second) {
    return left.first < right.first;
  } else {
    return 0;
  }
  assert(0);
}

// next wormhole from here (without teleports).
// -1 means we fall off the map.
map<int,int> make_exit_next(const vector<pair<int,int>>& holes) {
  map<int,int> exit_next;
  for (int i = 0; i < holes.size()-1; ++i) {
    if (holes[i].second == holes[i+1].second) {
      exit_next[i] = i+1;
    } else {
      exit_next[i] = -1;
    }
  }
  exit_next[holes.size()-1] = -1;
  return exit_next;
}

void print_pairing(const map<int,int>& exit_next, const map<int,int>& worm_next) {
  cout << "exits\n";
  for (int i = 0; i < exit_next.size(); ++i) {
    cout << i << "," << exit_next.at(i) << endl;
  }

  cout << "pairs\n";
  for (int i = 0; i < worm_next.size(); ++i) {
    cout << i << "," << worm_next.at(i) << endl;
  }
}

// Check for a cycle starting at some particular point.
// The 2* is because running into a node while exiting is not the same as running into it while
// entering.
int cycle_starting_at(const map<int,int>& exit_next, const map<int,int>& worm_next, int start) {
  int loc = start;
  int exit = 1;
  for (int i = 0; i <= 2*exit_next.size(); ++i) {
    if (exit) {
      loc = exit_next.at(loc);
    } else {
      loc = worm_next.at(loc);
    }
    exit = !exit;
    if (loc == -1) {
      if (i > exit_next.size()) {
	cout << i << " iters " << start << " start\n";
	print_pairing(exit_next, worm_next);
      }
      return 0;
    }
  }
  return 1;
}

// Check for a cycle in the "current" graph.
int test_cycle(const map<int,int>& exit_next, map<int,int> worm_next) {
  for (int i = 0; i < exit_next.size(); ++i) {
    if (cycle_starting_at(exit_next, worm_next, i)) {
      return 1;
    }
  }
  return 0;
}

// Note: max size of remaining is 12.
int try_helper(const map<int,int>& exit_next, map<int,int> worm_next, vector<int> remaining) {
  int num_cycles = 0;
  if (remaining.size() == 0) {
    return test_cycle(exit_next, worm_next);
  }
  int pair_first = remaining.back();
  remaining.pop_back();
  assert(remaining.size() != 0);
  for (int i = 0; i < remaining.size(); ++i) {
    int pair_second = remaining[i];
    vector<int> new_remaining = remaining;
    new_remaining.erase(new_remaining.begin()+i);
    map<int,int> new_worm_next = worm_next;
    new_worm_next[pair_first] = pair_second;
    new_worm_next[pair_second] = pair_first;
    num_cycles += try_helper(exit_next, new_worm_next, new_remaining);
  }
  return num_cycles;
}

int try_all_pairs(const vector<pair<int,int>>& holes) {
  auto exit_next = make_exit_next(holes);

  vector<int> remaining;
  for (int i = 0; i < exit_next.size(); ++i) {
    remaining.push_back(i);
  }

  map<int,int> worm_next;
  return try_helper(exit_next, worm_next, remaining);
}

int main() {
  ofstream fout ("wormhole.out");
  ifstream fin ("wormhole.in");

  int num_holes;
  fin >> num_holes;

  vector<pair<int,int>> holes;
  for (int i = 0; i < num_holes; ++i) {
    int x, y;
    fin >> x >> y;
    holes.push_back(make_pair(x, y));
  }

  sort(holes.begin(), holes.end(), cmp_pairs);

  for (int i = 0; i < holes.size(); ++i) {
    cout << holes[i].first << " " << holes[i].second << endl;
  }

  fout << try_all_pairs(holes) << endl;

  return 0;
}

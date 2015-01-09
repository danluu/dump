/*
ID: danluu1
PROG: beads
LANG: C++11
*/

#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int break_run(char a, char b) {
  return ((a == 'r' && b == 'b') ||
	  (a == 'b' && b == 'r'));
}

int main() {
  ofstream fout ("beads.out");
  ifstream fin ("beads.in");
  int bead_len;
  string beads;

  // Lay out beads end to end, twice. Walk through string.
  // b/r switch ends a run. Want longest two runs in a row.
  // If that's longer than len, then we wrapped around and the
  // answer is len.
  fin >> bead_len >> beads;

  string doubled = beads + beads;
  int max_run_len = 0;
  for (std::string::iterator it = doubled.begin(); it != doubled.end(); ++it) {
    std::string::iterator sub_it = it;
    char past = 'w';
    char current = *sub_it;
    int run_len = 0;
    while (sub_it != doubled.end() && !break_run(past, current)) {
      ++run_len;
      ++sub_it;
      if (past == 'w') {
	past = current;
      }
      current = *sub_it;
    }
    past = *sub_it;
    // Now we have one run. Do a second one.
    while (sub_it != doubled.end() && !break_run(past, current)) {
      ++run_len;
      ++sub_it;
      current = *sub_it;
    }

    if (run_len > max_run_len) {
      max_run_len = run_len;
    }
  }

  /* Doesn't work because runs that start with a w get started too late
  char last = 'w';
  int w_run = 0;
  int runs[2] = {0, 0}; // Last two runs. runs[0] is current.
  int max_pair_runs = 0;
  for (int i = 0; i < 2; ++i) {
    for (char &c : beads) {
      if (break_run(c, last)) {
	int pair_runs = runs[0] + runs[1];
	if (pair_runs > max_pair_runs) {
	  max_pair_runs = pair_runs;
	}
	runs[1] = runs[0];
	runs[0] = 0;
      } else {
	runs[0]++;
      }
      if (c == 'r' || c == 'b') {
	last = c;
	w_run = 0;
      }
    }
  }
  if (max_pair_runs > len) {
    max_pair_runs = len;
  }
  */
  // cout << len << endl << beads;
  if (max_run_len > bead_len) {
    max_run_len = bead_len;
  }
  fout << max_run_len << endl;
}

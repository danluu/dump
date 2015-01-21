/*
ID: danluu1
PROG: crypt1
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

/*
Position in slot

          0 1 2     <-- number 'abc'
        x   3 4     <-- number 'de'; the 'x' means 'multiply'
     -----------
p1      * * * *     <-- product of e * abc; first star might be 0 (absent)
p2    * * * *       <-- product of d * abc; first star might be 0 (absent)
     -----------
     * * * * *     <-- sum of p1 and p2 (e*abc + 10*d*abc) == de*abc
*/

// true if every digit in candidate is in digits.
int check_int(const set<int>& digits, int candidate) {
  ostringstream os;
  os << candidate;
  string candidate_str = os.str();
  for (auto &c : candidate_str) {
    int ic = c - '0';
    if (digits.find(ic) == digits.end()) {
      return 0;
    }
  }
  return 1;
}

int check(const set<int>& digits, const vector<int>& slots) {
  int top = 100 * slots[0] + 10 * slots[1] + 1 * slots[2];
  int bottom =               10 * slots[3] + 1 * slots[4];

  int p1 = top * slots[4];
  int p2 = top * slots[3];

  int both = top * bottom;
  bool valid_result = check_int(digits, p1) && check_int(digits, p2) && check_int(digits, both);
  bool result_fits = p1 < 1000 && p2 < 1000 && both < 10000;
  return valid_result && result_fits;
						      /*
  if (valid_result && result_fits) {
    cout << top << " " << bottom << " " << p1 << " " << p2 << " " << both << endl;
    return 1;
  } else {
    return 0;
  }
						      */
}

int solve(const set<int>& digits, vector<int> slots) {
  if (slots.size() >= 5) {
    assert(slots.size() == 5);
    return check(digits, slots);
  }
  int ans = 0;
  for (auto &x : digits) {
    slots.push_back(x);
    ans += solve(digits, slots);
    slots.pop_back();
  }
  return ans;
}

int main() {
  ofstream fout ("crypt1.out");
  ifstream fin ("crypt1.in");

  int num_digits;
  fin >> num_digits;

  set<int> digits;
  for (int i = 0; i < num_digits; ++i) {
    int some_digit;    
    fin >> some_digit;
    digits.insert(some_digit);
  }

  vector<int> slots;
  int ans = solve(digits, slots);

  fout << ans << endl;
  return 0;
}

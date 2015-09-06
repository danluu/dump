/*
ID: danluu1
PROG: spin
LANG: C++11
*/

#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <algorithm> 
#include <bitset>
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

struct whl {
  int speed;
  int pos;
  bitset<360> mask;
};

bitset<360> rotset(bitset<360> bs, int x) {
  bitset<360> rot = (bs << x) | (bs >> (360 -x));
  return rot;
}

bitset<360> revrot(bitset<360> bs, int x) {
  bitset<360> rot = (bs >> x) | (bs << (360 -x));
  return rot;
}

bool solved(const vector<struct whl> &whls) {
  bitset<360> all;
  all.set();
  
  for (const auto &w : whls) {
    bitset<360> rot = rotset(w.mask, w.pos);
    bitset<360> rotcheck = rotset(rot, 360-w.pos);
    bitset<360> rotcheck2 = revrot(rot, w.pos);
    assert(w.mask == rotcheck);
    assert(w.mask == rotcheck2);
    assert(w.mask.count() == rot.count());
    // cout << w.pos << endl;
    // cout << w.mask << endl;
    // cout << rot << endl;
    all &= rot;
  }
  
  if (all.any()) {
    return true;
  } else {
    return false;
  }
}

void advance(vector<struct whl> &w) {
  for (auto &x : w) {
    x.pos = (x.pos + x.speed) % 360;
  }
}

void print_whl(const struct whl &w) {
  cout << w.pos << ":" << w.speed << endl;
  cout << w.mask << endl;
}

void print_all(const vector<struct whl> &whls) {
  for (const auto &w : whls) {
    print_whl(w);
  }
}

int main() {
  ofstream fout ("spin.out");
  ifstream fin ("spin.in");

  vector<struct whl> whls;

  int speed;
  int num_notches;
  while (fin >> speed) {
    struct whl temp;
    temp.speed = speed;
    temp.pos = 0;
    temp.mask.reset();
    fin >> num_notches;
    // cout << "num: " << num_notches << endl;
    for (int i = 0; i < num_notches; ++i) {
      int start, len;
      fin >> start >> len;
      // cout << "start:len " << start << ":" << len << endl;      
      for (int j = 0; j <= len; ++j) {
	temp.mask[(start+j)%360] = 1;
      }
      // cout << temp.mask << endl;
    }
    whls.push_back(temp);
  }

  // print_all(whls);

  #define MAXT 360
  int t = 0;
  while (t < MAXT && !solved(whls)) {
    advance(whls);
    ++t;
    // cout << "ATTEMPT " << t << endl;
    // print_all(whls);
  }

  if (t < MAXT) {
    fout << t << endl;
  } else {
    fout << "none\n";
  }
  return 0;  
}

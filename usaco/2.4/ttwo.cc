/*
ID: danluu1
PROG: ttwo
LANG: C++11
*/

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

#define TIMEOUT 160000

enum Dir { N, S, E, W };

struct blob {
  int x;
  int y;
  Dir dir;
};

void step(blob &obj, const vector<vector<bool>>& grid) {
  assert(obj.y >= 0);
  assert(obj.y <= 9);
  assert(obj.x >= 0);
  assert(obj.x <= 9);
    
  switch (obj.dir) {
  case N:
    if (obj.y == 9 || grid[obj.x][obj.y+1]) {
      obj.dir = E;
    } else {
      ++obj.y;
    }
    break;
  case E:
    if (obj.x == 9 || grid[obj.x+1][obj.y]) {
      obj.dir = S;
    } else {
      ++obj.x;
    }
    break;
  case S:
    if (obj.y == 0 || grid[obj.x][obj.y-1]) {
      obj.dir = W;
    } else {
      --obj.y;
    }
    break;
  case W:
    if (obj.x == 0 || grid[obj.x-1][obj.y]) {
      obj.dir = N;
    } else {
      --obj.x;
    }
    break;
  default:
    cout << obj.dir << endl;
    assert(0);
  }
}

int main() {
  ofstream fout ("ttwo.out");
  ifstream fin ("ttwo.in");

  vector<vector<bool>> grid(10, vector<bool>(10, false));

  blob farmer;
  blob cow;
  farmer.dir = N;
  cow.dir = N;

  // 0,0 @ bottom left.
  for (int i = 9; i >= 0; --i) {
    string row;
    fin >> row;
    for (int j = 0; j < 10; ++j) {
      if (row[j] == '*') {
	grid[j][i] = true;
      }

      if (row[j] == 'F') {
	farmer.y = i;
	farmer.x = j;
      }

      if (row[j] == 'C') {
	cow.y = i;
	cow.x = j;
      }      
    }
    // cout << row << endl;
  }

  //cout << farmer.x << " " << farmer.y << endl;
  //cout << cow.x << " " << cow.y << endl;

  int time = 0;
  while (++time < TIMEOUT) {
    step(cow, grid);
    step(farmer, grid);
    //cout << "time:   " << time << endl;
    //cout << "cow:    " << cow.x << "," << cow.y << endl;
    //cout << "farmer: " << farmer.x << "," << farmer.y << endl;    
    if (cow.x == farmer.x && cow.y == farmer.y) {
      break;
    }
  }

  if (time >= TIMEOUT) {
    fout << 0 << endl;
  } else {
    fout << time << endl;
  }
  return 0;
}

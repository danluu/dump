/*
ID: danluu1
PROG: castle
LANG: C++11
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <algorithm> 
#include <cassert>
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
Approach:

Make a graph of the rooms.
Find an arbitrary parent of each node.
Try all legal node mergers and use parent vector to count room size; take max
*/

int find_rooms(const vector<vector<int>>& edges, vector<int>& parent, int current) {
  // cout << "find_rooms " << current << endl;
  int num_rooms = 0;
  if (current == -1) {
    for (int i = 0; i < edges.size(); ++i) {
      // Could resume from last point instead of restarting.
      if (parent[i] == -1) {
	parent[i] = i;
	find_rooms(edges, parent, i);
	++num_rooms;
      }
    }
  } else {
    for (auto& next : edges[current]) {
      if (next >= 0 && parent[next] == -1) {
	parent[next] = parent[current];      
	find_rooms(edges, parent, next);
      }
    }
  }
  return num_rooms;
}

int merge_room_size(const vector<int>& parent, int current, int next) {
  int room_size = 0;
  for (auto& x : parent) {
    if (x == current || x == next) {
      ++room_size;
    }
  }
  return room_size;
}

int biggest_room(const vector<int>& parent) {
  vector<int> room_size(parent.size(),0);
  for (auto& x : parent) {
    ++room_size[x];
  }

  int biggest = 0;
  for (auto& x : room_size) {
    if (x > biggest) {
      biggest = x;
    }
  }
  return biggest;
}

bool is_top(int x, int max_x, int max_y) {
  return x < max_x;
}

bool is_bottom(int x, int max_x, int max_y) {
  return x > (((max_y-1) * max_x) -1);
}

bool is_left(int x, int max_x, int max_y) {
  return x % max_x == 0;
}

bool is_right(int x, int max_x, int max_y) {
  return x % max_x == (max_x - 1);
}

bool east_neighbor(int i, int new_id, int max_x, int max_y) {
  return !is_right(i, max_x, max_y) && new_id - 1 == i;
}

int x_val(int i, int max_x) {
  return i % max_x;
}

int y_val(int i, int max_x) {
  return i / max_x;
}

int main() {
  ofstream fout ("castle.out");
  ifstream fin ("castle.in");

  int max_x, max_y;
  fin >> max_x >> max_y;

  // Node id number is x + max_x * y
  cout << "Making edges\n";
  vector<vector<int>> edges(max_y*max_x);
  // We don't need to push edge in both directions since we'll hit the other direction
  // through normal traversal.
  // We push a "negative" edge so that we know which mergers to try. This is basically legacy code
  // and this could be solved more simply without adding negative edges.
  for (int i = 0; i < max_x * max_y; ++i) {
    int walls;
    fin >> walls;
    // cout << "processing " << i << ":" << walls << endl;
    if (!(walls & 1)) {
      // West/left wall.
      assert(i-1>=0);
      assert(!is_left(i, max_x, max_y));
      edges[i].push_back(i-1);
    } else {
      // Push back possible wall if not on edge.
      if (!is_left(i, max_x, max_y)) {
	edges[i].push_back(-(i-1));
      }
    }
    if (!(walls & 2)) {
      // North/top wall.
      assert(i-max_x >= 0);
      assert(!is_top(i, max_x, max_y));
      edges[i].push_back(i-max_x);
    } else {
      if (!is_top(i, max_x, max_y)) {
	edges[i].push_back(-(i-max_x));
      }
    }
    if (!(walls & 4)) {
      // East/right wall.
      assert(i+1 < max_x * max_y);
      assert(!is_right(i, max_x, max_y));
      edges[i].push_back(i+1);
    } else {
      if (!is_right(i, max_x, max_y)) {
	edges[i].push_back(-(i+1));
      }
    }
    if (!(walls & 8)) {
      // South/bottom wall.      
      assert(i+max_x < max_x * max_y);
      assert(!is_bottom(i, max_x, max_y));
      edges[i].push_back(i+max_x);
    } else {
      if (!is_bottom(i, max_x, max_y)) {
	edges[i].push_back(-(i+max_x));
      }
    }
  }

  cout << "First find_rooms\n";
  vector<int> parent(max_x * max_y, -1);
  int num_rooms = find_rooms(edges, parent, -1);
  fout << num_rooms << endl;
  int room_size = biggest_room(parent);
  fout << room_size << endl;

  int x_loc = -1;
  int y_loc = -1;
  int is_east = 0;

  // iterate through all walls and try with each removed.
  int mod_max = 0;
  for (int i = 0; i < edges.size(); ++i) {
    for (int j = 0; j < edges[i].size(); ++j) {
      // cout << i << ":" << j << " " << edges[i][j] << endl;
      if (edges[i][j] < 0) {
	int new_id = -edges[i][j];
	if (
	    east_neighbor(i, new_id, max_x, max_y) ||
	    (new_id + max_x == i) // North neighbor.
	    ) {
	  int current_size = merge_room_size(parent, parent[i], parent[new_id]);
	  if (
	      (current_size > mod_max) ||
	      (current_size == mod_max && x_val(i, max_x) < x_loc) ||
	      (current_size == mod_max && x_val(i, max_x) == x_loc && y_val(i, max_x) > y_loc) ||
	    (current_size == mod_max && x_val(i, max_x) == x_loc && y_val(i, max_x) == y_loc && !east_neighbor(i, new_id, max_x, max_y))
	    ) {
	  // cout << "Removing " << i << " " << y_val(i, max_x)+1 << ":" << x_val(i, max_x)+1 << endl;
	  // cout << "size: " << current_size << endl;
	  mod_max = current_size;
	  x_loc = x_val(i, max_x);
	  y_loc = y_val(i, max_x);
	  is_east = east_neighbor(i, new_id, max_x, max_y);
	}
	}
      }
    }
  }
  fout << mod_max << endl;
  fout << y_loc + 1 << " " << x_loc + 1 << " ";
  if (is_east) {
    fout << "E\n";
  } else {
    fout << "N\n";
  }
  return 0;
}

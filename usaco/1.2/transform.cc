/*
ID: danluu1
PROG: transform
LANG: C++11
*/

#include <cassert>
#include <iostream>
#include <fstream>
#include <queue> 
#include <string>
#include <vector>

using namespace std;

#define MAX_SIZE 10

void copy_mat(int src[MAX_SIZE][MAX_SIZE], int dst[MAX_SIZE][MAX_SIZE], int mat_size) {
  for (int i = 0; i < mat_size; ++i) {
    for (int j = 0; j < mat_size; ++j) {
      dst[i][j] = src[i][j];
    }
  }
}

int equals_mat(int src[MAX_SIZE][MAX_SIZE], int dst[MAX_SIZE][MAX_SIZE], int mat_size) {
  for (int i = 0; i < mat_size; ++i) {
    for (int j = 0; j < mat_size; ++j) {
      if (dst[i][j] != src[i][j]) {
	return 0;
      }
    }
  }
  return 1;
}

void read_mat(int dst[MAX_SIZE][MAX_SIZE], ifstream &fin, int mat_size) {
  char x;
  for (int i = 0; i < mat_size; ++i) {
    for (int j = 0; j < mat_size; ++j) {
      fin >> x;
      if (x == '@') {
	dst[i][j] = 1;
      } else {
	dst[i][j] = 0;
      }
    }
  }
}

void transpose_mat(int a[MAX_SIZE][MAX_SIZE], int mat_size) {
  for (int i = 0; i < mat_size; ++i) {
    for (int j = i; j < mat_size; ++j) {
      int tmp = a[i][j];
      a[i][j] = a[j][i];
      a[j][i] = tmp;
    }
  }
}

// Horizontal reflection
void reflect_mat(int a[MAX_SIZE][MAX_SIZE], int mat_size) {
  for (int i = 0; i < mat_size; ++i) {
    for (int j = 0; j < mat_size/2; ++j) {
      int tmp = a[i][j];
      a[i][j] = a[i][mat_size-j-1];
      a[i][mat_size-j-1] = tmp;
    }
  }
}

void rotate_90_mat(int a[MAX_SIZE][MAX_SIZE], int mat_size) {
  transpose_mat(a, mat_size);
  reflect_mat(a, mat_size);
}

int solve(ifstream &fin) {
  int mat_size;

  int original[MAX_SIZE][MAX_SIZE];
  int a[MAX_SIZE][MAX_SIZE];
  int target[MAX_SIZE][MAX_SIZE];

   fin >> mat_size;
  read_mat(original, fin, mat_size);
  read_mat(target, fin, mat_size);

  assert(equals_mat(original, original, mat_size));
  copy_mat(original, a, mat_size);
  assert(equals_mat(original, a, mat_size));
  assert(equals_mat(a, original, mat_size));

  // 90
  rotate_90_mat(a, mat_size);
  if (equals_mat(a, target, mat_size)) {
    return 1;
  }

  // 180
  rotate_90_mat(a, mat_size);
  if (equals_mat(a, target, mat_size)) {
    return 2;
  }

  // 270
  rotate_90_mat(a, mat_size);
  if (equals_mat(a, target, mat_size)) {
    return 3;
  }

  // Back to original
  rotate_90_mat(a, mat_size);
  assert(equals_mat(original, a, mat_size));

  // Reflect.
  reflect_mat(a, mat_size);
  if (equals_mat(a, target, mat_size)) {
    return 4;
  }
  
  // 90
  rotate_90_mat(a, mat_size);
  if (equals_mat(a, target, mat_size)) {
    return 5;
  }

  // 180
  rotate_90_mat(a, mat_size);
  if (equals_mat(a, target, mat_size)) {
    return 5;
  }

  // 270
  rotate_90_mat(a, mat_size);
  if (equals_mat(a, target, mat_size)) {
    return 5;
  }

  // Back to original
  rotate_90_mat(a, mat_size);
  reflect_mat(a, mat_size);
  assert(equals_mat(original, a, mat_size));

  if (equals_mat(target, original, mat_size)) {
    return 6;
  }

  return 7;
}

int main() {
  ofstream fout ("transform.out");
  ifstream fin ("transform.in");

  int ans = solve(fin);
  fout << ans << endl;
  
  return 0;
}

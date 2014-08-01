#include <stdio.h>

#define SIZE 1000

long a[SIZE][SIZE][SIZE];

int main() {
  // Initialize
  for (int k = 0; k < SIZE; ++k) {
    for (int j = 0; j < SIZE; ++j) {
      for (int i = 0; i < SIZE; ++i) {
	a[k][j][i] = 11*i*j*k + 2*i + 7*j;
      }
    }
  }

  for (int k = 1; k < SIZE; ++k) {
    for (int j = 0; j < SIZE; ++j) {
      for (int i = 0; i < SIZE; ++i) {
	int without_k = a[k-1][j][i];
	int with_k = a[k-1][k][i] + a[k-1][j][k];
	a[k][j][i] = without_k < with_k ? without_k : with_k;
      }
    }
  }  
}

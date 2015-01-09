/*
ID: danluu1
PROG: ride
LANG: C++11
*/

#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int product_val(string s) {
  int prod_val = 1;
  for (char &c : s) {
    int val = c - 'A' + 1;
    prod_val *= val;
  }
  return prod_val;
}

int main() {
  ofstream fout ("ride.out");
  ifstream fin ("ride.in");
  string a, b;
  fin >> a >> b;
  // cout << a << endl << b << endl;
  // cout << product_val(a) << endl << product_val(b) << endl;

  if (product_val(a) % 47 == product_val(b) % 47) {
    // cout << "GO\n";
    fout << "GO\n";
  } else {
    // cout << "STAY\n";
    fout << "STAY\n";
  }

  return 0;
}

/* N = 1
   
 */

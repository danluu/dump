/*
ID: danluu1
PROG: friday
LANG: C++11
*/

#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int days_per_month[12] = 
  {31, 28, 31, 
   30, 31, 30, 
   31, 31, 30, 
   31, 30, 31};

int fridays[7] = {0, 0, 0, 0, 0, 0, 0};

// Jan is month 0, so April is month 3.
int leap_day(int month) {
  int year = month/12 + 1900;
  if (year % 100 == 0) {
    if (month % 12 == 1 && year % 400 == 0) {
      return 1;
    } else {
      return 0;
    }
  } else if (year % 4 == 0 && month % 12 == 1) {
    return 1;
  } else {
    return 0;
  }
}

int main() {
  ofstream fout ("friday.out");
  ifstream fin ("friday.in");
  int a;
  fin >> a;

  int num_months = a * 12;
  int d = 0; // Absolute day number from Jan 1 1900

  // Sunday is day 0. Monday is 1. Add 13 to get offset from Sunday.
  d += 13;
  int num_iters = 0;
  
  for (int m = 0; m < num_months; ++m) {
    int weekday = d % 7;
    fridays[weekday]++;
    num_iters++;
    // cout << weekday << endl;
    d += days_per_month[m % 12];
    d += leap_day(m);
  }

  // Our days are relative to Sunday. The output should be relative to Saturday.
  for (int i = 6; i < 7; ++i) {
    fout << fridays[i] << " ";
  }
  for (int i = 0; i < 5; ++i) {
    fout << fridays[i] << " ";
  }
  fout << fridays[5] << endl; // Quick hack to avoid printing a trailing space.
  return 0;
}

/* First year
Sa 0
Tu 3
Tu 3
Fr 6
Su 1
We 4
Fr 6
Mo 2
Th 5
Sa 0
Tu 3
Th 5
2 1 1 3 1 2 2
*/

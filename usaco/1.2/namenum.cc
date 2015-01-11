/*
ID: danluu1
PROG: namenum
LANG: C++11
*/

#include <cassert>
#include <iostream>
#include <fstream>
#include <queue> 
#include <set>
#include <string>
#include <vector>

using namespace std;

vector<vector<char>> num2char = {
  {}, // 0
  {}, // 1
  {'A','B','C'}, // 2
  {'D','E','F'}, // 3
  {'G','H','I'}, // 4
  {'J','K','L'}, // 5
  {'M','N','O'}, // 6
  {'P','R','S'}, // 7
  {'T','U','V'}, // 8
  {'W','X','Y'}  // 9
};

set<string> read_dict(int postfix) {
  ifstream fin ("dict.txt");
  string word;
  set<string> dict;
  while (fin >> word) {
    if (postfix) {
      for (int i = 1; i <= word.size(); ++i) {
	string postfix = word.substr(word.size() - i, i);
	dict.insert(postfix);
      }
    } else {
      dict.insert(word);
    }
  }
  return dict;
}

vector<string> possible_words(string digits, set<string> postfix_dict) {
  if (digits.size() == 0) {
    cout << "Returning empty string\n";
    vector<string> empty = vector<string>{""};
    return empty;
  }

  cout << "possible_words recursive path\n";
  char c = *digits.begin();
  // Note that using digits.at(0) or converting to a .c_str() and pulling the first char seems to
  // cause odd non-deterministic behavior on the USACO grading machine.
  cout << c << endl;
  int first = atoi(&c);
  cout << first << endl;
  vector<char> letters = num2char[first];
  string rest = digits.substr(1, digits.size()-1);
  
  vector<string> rest_results = possible_words(rest, postfix_dict);
  for (auto s : rest_results) {
    // cout << s << endl;
  }
  vector<string> results;
  for (char x : letters) {
    for (string s : rest_results) {
      string wat = s;
      wat.insert(0,1,x);
      if (postfix_dict.find(wat) != postfix_dict.end()) {
	results.push_back(wat);
      }
    }
  }
  return results;
}

int main() {
  ofstream fout ("namenum.out");
  ifstream fin ("namenum.in");

  set<string> dict = read_dict(0);
  set<string> postfix_dict = read_dict(1);
  cout << dict.size() << endl;
  
  string digits;
  fin >> digits;

  vector<string> all_possible = possible_words(digits, postfix_dict);
  vector<string> in_dict;
  for (auto s : all_possible) {
    if (dict.find(s) != dict.end()) {
      in_dict.push_back(s);
    }
  }

  cout << all_possible.size() << endl;
  cout << in_dict.size() << endl;
  if (in_dict.size() == 0) {
    fout << "NONE" << endl;
  } else {
    for (auto s : in_dict) {
      fout << s << endl;
    }
  }

  return 0;
}

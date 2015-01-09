/*
ID: danluu1
PROG: milk2
LANG: C++11
*/

#include <cassert>
#include <iostream>
#include <fstream>
#include <queue> 
#include <string>
#include <vector>

using namespace std;

/*
  Create priority queue of start and stop times.
  Pull out smallest time and do appropriate bookkeeping
*/

int main() {
  ofstream fout ("milk2.out");
  ifstream fin ("milk2.in");
  int num_cows;
  int a, b;
  std::priority_queue<int, std::vector<int>, std::greater<int>> start, stop;
  fin >> num_cows;
  for (int i = 0; i < num_cows; ++i) {
    fin >> a >> b;
    start.push(a);
    stop.push(b);
  }
  
  int num_milking = 0;
  int last_time = 0;
  int max_milking = 0;
  int max_free = 0;
  int current_milking = 0;
  int current_free = 0;
  int milking_started = 0;
  while (start.size() > 0 || stop.size() > 0) {
    if (start.size() == 0 ||
	(stop.top() && (stop.top() < start.top()))
	) {
      cout << "stop\n";
      // Pick "stop milking" event off queue.
      int current_time = stop.top(); stop.pop();
      --num_milking;
      assert(max_milking >= 0);
      current_milking += (current_time - last_time);
      if (num_milking >= 1) {
	// 
      } else {
	if (current_milking > max_milking) {
	  max_milking = current_milking;
	}
	current_milking = 0;
      }
      last_time = current_time;
    } else if (stop.size() == 0 ||
	       start.top() < stop.top()
	       ) {
      // Pick "start milking" event off queue.
      cout << "start\n";
      int current_time = start.top(); start.pop();
      ++num_milking;
      if (num_milking == 1) {
	if (milking_started) {
	  current_free = (current_time - last_time);
	  if (current_free > max_free) {
	    max_free = current_free;
	  }
	} else {
	  milking_started = 1;
	}
	current_free = 0;
      } else {
	current_milking += (current_time - last_time);
      }
      last_time = current_time;
    } else if (start.top() == stop.top()) {
      cout << "tie\n";
      // Should only happen when at least 1 milking is occuring, so no net change in state.
      int current_time = start.top(); start.pop();
      stop.pop();
      current_milking += (current_time - last_time);
      last_time = current_time;
    } else {
      cout << "Bad fallthrough of giant if/else\n";
    }
    if (current_milking > max_milking) {
      max_milking = current_milking;
    }
    if (current_free > max_free) {
      cout << "Impossible setting of max free\n";
      max_free = current_free;
    }
  }

  fout << max_milking << " " << max_free << endl;
  return 0;
}

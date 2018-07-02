#include <algorithm>
#include <cassert>
#include <vector>

#include <iostream> // TODO: remove.

struct Interval {
  int start;
  int end;
  Interval() : start(0), end(0) {}
  Interval(int s, int e) : start(s), end(e) {}
};

// Shouldn't use initializer list because Interval has an explicit constructor
// and is therefore not an aggregate type.
Interval make_interval(int s, int e) {
  return Interval(s, e);
}

bool compareIntervalEnds(Interval const & a, Interval const & b) {
  if (a.end == b.end) {
    return a.start > b.start;
  } else {
    return a.end < b.end;
  }
}

class Solution {
public:
  int eraseOverlapIntervals(std::vector<Interval>& intervals) {
    for (auto const & x : intervals) {
      std::cout << x.start << ":" << x.end << std::endl;
    }
    
    std::sort(intervals.begin(), intervals.end(), compareIntervalEnds);
    
    std::cout << std::endl;
    std::cout << std::endl;

    for (auto const & x : intervals) {
      std::cout << x.start << ":" << x.end << std::endl;
    }

    return 0; // TODO: remove.
  }
};


int main() {
  Solution s;

  {
    std::vector<Interval> in = {make_interval(1,2),
				make_interval(2,3),
				make_interval(3,4),
				make_interval(1,3)
    };

    assert(s.eraseOverlapIntervals(in) == 1);
  }
  
}

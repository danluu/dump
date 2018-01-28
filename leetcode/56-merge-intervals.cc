#include <algorithm>
#include <cassert>
#include <memory>
#include <vector>

struct Interval {
  int start;
  int end;
  Interval() : start(0), end(0) {}
  Interval(int s, int e) : start(s), end(e) {}

  // bool operator > (const Interval& other) const {
  //   if (start == other.start) {
  //     return start.end < other.end
  //   } else {
  //     return start > other.start;
  //   }
  //   assert(false);
  // }
};

// Sort b larger end interval in case of tie.
struct interval_lt {
  inline bool operator() (const Interval& left, const Interval& right) {
    if (left.start == right.start) {
      return right.end > left.end;
    } else {
      return left.start < right.start;
    }
    assert(false);
  }
};

// Have a make_* fn because Interval isn't POD.
Interval make_interval(int start, int end) {
  Interval x = {start, end};
  return x;
}

class Solution {
public:
  std::vector<Interval> merge(std::vector<Interval>& intervals) {
    std::vector<Interval> res;

    std::sort(intervals.begin(), intervals.end(), interval_lt());
    
    int cur_start = 0;
    int cur_end = -1;
    for (Interval& i : intervals) {
      if (cur_start > cur_end) {
	cur_start = i.start;
	cur_end = i.end;
      } else if (i.start <= cur_end) {
	cur_end = std::max(cur_end, i.end);
      } else {
	assert(i.start > cur_end);
	res.push_back(make_interval(cur_start, cur_end));
	cur_start = i.start;
	cur_end = i.end;
      }
    }
    if (cur_end >= cur_start) {
      res.push_back(make_interval(cur_start, cur_end));
    }
    
    return res;
  }
};

int main() {
  std::unique_ptr<Solution> s(new Solution);
  
  std::vector<Interval> in0 = {make_interval(1,3), make_interval(2,6), make_interval(8,10), make_interval(15,18)};
  std::vector<Interval> res0 = s->merge(in0);
  assert(res0.size() == 3);
  assert(res0[0].start == 1);
  assert(res0[0].end == 6);
  assert(res0[1].start == 8);
  assert(res0[1].end == 10);
  assert(res0[2].start == 15);
  assert(res0[2].end == 18);

  std::vector<Interval> in1 = {make_interval(1,2), make_interval(8,10), make_interval(15,18), make_interval(2,6)};
  std::vector<Interval> res1 = s->merge(in1);
  assert(res1.size() == 3);
  assert(res1[0].start == 1);
  assert(res1[0].end == 6);
  assert(res1[1].start == 8);
  assert(res1[1].end == 10);
  assert(res1[2].start == 15);
  assert(res1[2].end == 18);

  std::vector<Interval> in2 = {make_interval(1,2), make_interval(8,10), make_interval(15,18), make_interval(2,8)};
  std::vector<Interval> res2 = s->merge(in2);
  assert(res2.size() == 2);
  assert(res2[0].start == 1);
  assert(res2[0].end == 10);
  assert(res2[1].start == 15);
  assert(res2[1].end == 18);

  std::vector<Interval> in3 = {make_interval(1,2), make_interval(8,11), make_interval(15,18), make_interval(9,15)};
  std::vector<Interval> res3 = s->merge(in3);
  assert(res3.size() == 2);
  assert(res3[0].start == 1);
  assert(res3[0].end == 2);
  assert(res3[1].start == 8);
  assert(res3[1].end == 18);
}

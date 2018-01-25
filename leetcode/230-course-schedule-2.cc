#include <algorithm>
#include <cassert>
#include <iostream>
#include <iterator>
#include <memory>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>

template<typename T>
std::ostream & operator<<(std::ostream & os, std::vector<T> vec)
{
    os<<"{ ";
    std::copy(vec.begin(), vec.end(), std::ostream_iterator<T>(os, " "));
    os<<"}";
    return os;
}

class Solution {
public:
  bool traverse(int node, std::unordered_map<int,std::vector<int>>& g, std::unordered_set<int>& courses, std::vector<int>& order, std::unordered_set<int>& stack) {
    stack.insert(node);
    courses.erase(node);
    for (int next : g[node]) {
      if (stack.find(next) != stack.end()) {
	return false;
      }

      if (courses.find(next) != courses.end()) {
	bool schedulable = traverse(next, g, courses, order, stack);
	if (!schedulable) {
	  return false;
	}
      }
    }
    stack.erase(node);
    order.push_back(node);
    return true;
  }

  bool postOrder(std::unordered_map<int,std::vector<int>>& g, std::unordered_set<int>& courses, std::vector<int>& order) {
    std::unordered_set<int> stack;
    while (courses.size() != 0) {
      auto node_it = courses.begin();
      int node = *node_it;
      bool scheduable = traverse(node, g, courses, order, stack);
      if (!scheduable) {
	return false;
      }
    }
    return true;
  }

  std::vector<int> findOrder(int numCourses, std::vector<std::pair<int, int>>& prerequisites) {
    std::unordered_map<int,std::vector<int>> g; // graph.
    std::unordered_set<int> courses;
    std::vector<int> order;

    for (int i = 0; i < numCourses; ++i) {
      courses.insert(i);
    }

    // Construct dependency graph.
    for (auto& p : prerequisites) {
      g[p.second]; // Create vector with default constructor if it doesn't exist.
      g[p.second].push_back(p.first);
    }

    bool schedulable = postOrder(g, courses, order);
    if (!schedulable) {
      std::vector<int> nil;

      return nil;
    } else {
      assert(order.size() == numCourses);

      std::reverse(order.begin(), order.end());

      return order;
    }
    assert(false);
  }
};

int main() {
  std::unique_ptr<Solution> s(new Solution());

  std::vector<std::pair<int,int>> pre0 = {{1,0}};
  std::vector<int> res0 = s->findOrder(2, pre0);
  assert(res0[0] == 0);
  assert(res0[1] == 1);

  std::vector<std::pair<int,int>> pre1 = {{1,0},{2,0},{3,1},{3,2}};
  std::vector<int> res1 = s->findOrder(4, pre1);
  assert(res1[0] == 0);
  assert((res1[1] == 1 && res1[2] == 2) ||
	 (res1[1] == 2 && res1[2] == 1));
  assert(res1[3] == 3);

  std::vector<std::pair<int,int>> pre2 = {{1,0}, {0,1}};
  std::vector<int> res2 = s->findOrder(2, pre2);
  assert(res2.size() == 0);

  return 0;
}

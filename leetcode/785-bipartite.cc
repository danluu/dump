#include <cassert>
#include <unordered_map>
#include <unordered_set>
#include <vector>

class Solution {
public:
  bool explore(int node, std::unordered_map<int, std::unordered_set<int>> & g, std::unordered_map<int, bool> color) {
    if (g.find(node) == g.end()) {
      return true;
    }

    assert(color.find(node) == color.end());
    
    color[node] = true;
    
    std::vector<int> stack;
    for (auto const & dst : g[node]) {
      stack.push_back(dst);
      assert(color.find(dst) == color.end());
      color[dst] = false;
    }

    while (stack.size() != 0) {
      int cur = stack.back();
      stack.pop_back();
      int color_cur = color[cur];
      for (auto const & dst : g[cur]) {
	auto got = color.find(dst);
	if (got != color.end()) {
	  if (color_cur == got->second) {
	    return false;
	  }
	} else {
	  stack.push_back(dst);
	  color[dst] = !color_cur;
	}
      }
    }

    return true;
  }
  
  bool isBipartite(std::vector<std::vector<int>> const & graph) {
    std::unordered_map<int, std::unordered_set<int>> g;
    for (int i = 0; i < graph.size(); ++i) {
      for (int j = 0; j < graph[i].size(); ++j) {
	int to = graph[i][j];
	g[i].insert(to);
	g[to].insert(i);
      }
    }
    
    std::unordered_map<int, bool> color;
    for (int i = 0; i < graph.size(); ++i) {
      if (color.find(i) == color.end()) {
	if (!explore(i, g, color)) {
	  return false;
	}
      }
    }
    return true;
  }
};

int main() {
  Solution s;

  {
    std::vector<std::vector<int>> in = {{1,3}, {0,2}, {1,3}, {0,2}};
    assert(s.isBipartite(in) == true);
  }

  {
    std::vector<std::vector<int>> in = {{1,2,3}, {0,2}, {0,1,3}, {0,2}};
    assert(s.isBipartite(in) == false);
  }

}

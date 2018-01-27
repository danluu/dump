#include <cassert>
#include <memory>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>

class Node {
public:
  // TODO: make node data private.
  std::unordered_map<char, std::vector<Node*>> edges;
  bool is_end; // TODO: don't make this public, add constructor.
private:
};


class Regex {
public:
  Regex(std::string pattern) {
    nodes.push_back(std::make_unique<Node>()); // node 0.

    for (char& c : pattern) {
      nodes.push_back(std::make_unique<Node>());
      size_t cur = nodes.size() - 1;
      size_t prev = cur -1;

      nodes[prev]->edges[c].push_back(nodes[cur].get());
    }

    nodes[nodes.size() - 1]->is_end = true;
  }

  bool match(std::string candidate) {
    states.clear();
    states.insert(nodes[0].get());

    for (char& c : candidate) {
      std::unordered_set<Node*> next_states;
      for (Node* node : states) {
	if (node->edges.find(c) != node->edges.end()) {
	  for (Node* next_node : node->edges[c]) {
	    next_states.insert(next_node);
	  }
	}
      }
      states = next_states;
    }

    for (Node* node : states) {
      if (node->is_end) {
	return true;
      }
    }
    return false;
  }
   

private:
  std::vector<std::unique_ptr<Node>> nodes;
  std::unordered_set<Node*> states;

};

int main() {
  // {
  //   Regex r0("a*b*");
  //   assert(r0.match(""));
  //   assert(r0.match("a"));
  //   assert(r0.match("aa"));
  //   assert(r0.match("b"));
  //   assert(r0.match("bb"));
  //   assert(r0.match("abb"));
  //   assert(r0.match("aabb"));

  //   assert(!r0.match("aba"));
  //   assert(!r0.match("aabba"));
  //   assert(!r0.match("ba"));
  //   assert(!r0.match("xy"));
  // }
  
  {
    Regex r0("ab");
    assert(r0.match("ab"));
    assert(!r0.match(""));
    assert(!r0.match("aba"));
    assert(!r0.match("ba"));
    assert(!r0.match("aa"));
  }


  {
    Regex r0("");
    assert(r0.match(""));
    assert(!r0.match("a"));
    assert(!r0.match("aba"));
    assert(!r0.match("ba"));
    assert(!r0.match("aa"));
  }

  {
    Regex r1("aa");
    assert(!r1.match(""));
    assert(!r1.match("a"));
    assert(!r1.match("aaa"));
    assert(r1.match("aa"));
  }

  return 0;
}

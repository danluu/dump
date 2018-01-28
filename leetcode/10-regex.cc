#include <cassert>
#include <iostream>
#include <memory>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>

class Node {
public:
  Node(int id) :
    m_id(id),
    m_is_end(false)
  {}

  // Node(int id, bool is_end) :
  //   m_id(id),
  //   m_is_end(is_end)
  // {}

  int id() const { return m_id; }
  bool is_end() const { return m_is_end; }
  void set_end() { m_is_end = true; }


  // TODO: make node data private.
  std::unordered_map<char, std::vector<Node*>> edges;
private:
  int m_id;
  bool m_is_end; // TODO: don't make this public, add constructor.
};


class Regex {
public:
  void print_nodes() {
    std::cout << "print_nodes" << std::endl;
    for (const auto& src : m_nodes) {
      std::cout << "src " << src->id() << ":" << src->is_end() << std::endl;
      for (const auto& kv: src->edges) {
	std::cout << kv.first << " ";
	for (const Node* const dest : kv.second) {
	  std::cout << dest->id() << " ";
	}
	std::cout << std::endl;
      }
    }
  }

  Regex(std::string pattern) {
    // TODO: instead of special casing the epsilon self loop, it can be
    // handled as part of the reachable_set connections.
    // std::cout << "compiling " << pattern << std::endl;

    std::unordered_set<Node*> reachable_set;

    m_nodes.push_back(std::make_unique<Node>(0));
    reachable_set.insert(m_nodes[0].get());
    m_nodes[0]->edges['\0'].push_back(m_nodes[0].get()); // epsilon self loop.

    for (int i = 0; i < pattern.size(); ++i) {
      char c = pattern[i];
      size_t cur = m_nodes.size();
      size_t prev = cur -1;
      m_nodes.push_back(std::make_unique<Node>(cur));

      if (i + 1 < pattern.size() && pattern[i+1] == '*') {
	m_nodes[prev]->edges[c].push_back(m_nodes[prev].get()); // self loop.
	++i;
      } else {
	reachable_set.clear();
	m_nodes[prev]->edges[c].push_back(m_nodes[cur].get());
      }

      reachable_set.insert(m_nodes[cur].get());
      for (Node* prev_node : reachable_set) {
	prev_node->edges['\0'].push_back(m_nodes[cur].get());
      }
    }
    m_nodes[m_nodes.size() -1]->set_end();
    // print_nodes();
  }

  // TODO: make this private.
  void step(char c) {
    // print_states();
    std::unordered_set<Node*> next_states;
    for (Node* const node : m_states) {
      if (node->edges.find(c) != node->edges.end()) {
	for (Node* const next_node : node->edges[c]) {
	  next_states.insert(next_node);
	}
      }
      if (c != '\0') {
	if (node->edges.find('.') != node->edges.end()) {
	  for (Node* const next_node : node->edges['.']) {
	    next_states.insert(next_node);
	  }
	}
      }
    }
    m_states = next_states;
  }

  bool match(std::string candidate) {
    m_states.clear();
    m_states.insert(m_nodes[0].get());

    // TODO: have to special case empty string (go along all epsilon edges).
    for (char& c : candidate) {
      // std::cout << "processing " << c << std::endl;
      step('\0');
      step(c);
    }
    // std::cout << "extra processing at end" << std::endl;
    step('\0');
    // print_states();

    for (Node* node : m_states) {
      if (node->is_end()) {
	return true;
      }
    }
    return false;
  }


private:
  void print_states() {
    std::cout << "states ";
    for (Node* state : m_states) {
      std::cout << state->id() << " ";
    }
    std::cout << std::endl;
  }

  std::vector<std::unique_ptr<Node>> m_nodes;
  std::unordered_set<Node*> m_states;
};

int main() {
  {
    Regex r0("a*b*");
    assert(r0.match("ab"));
    assert(r0.match("a"));

    assert(r0.match("aa"));
    assert(r0.match("b"));
    assert(r0.match("bb"));
    assert(r0.match("abb"));
    assert(r0.match("aabb"));

    assert(!r0.match("aba"));
    assert(!r0.match("aabba"));
    assert(!r0.match("ba"));
    assert(!r0.match("xy"));

    assert(!r0.match("bab"));
    assert(!r0.match("ba"));

    assert(!r0.match("baa"));
    assert(!r0.match("xb"));
    assert(!r0.match("xbbb"));
    assert(!r0.match("babb"));
    assert(!r0.match("baabb"));

    assert(!r0.match("aba"));
    assert(!r0.match("ax"));

    assert(!r0.match("aaax"));
    assert(!r0.match("ba"));
    assert(!r0.match("bba"));
    assert(!r0.match("abba"));
    assert(!r0.match("aabba"));


    assert(r0.match(""));
  }

  {
    Regex r0("za*b*");

    assert(r0.match("zab"));
    assert(r0.match("za"));

    assert(r0.match("zaa"));
    assert(r0.match("zb"));
    assert(r0.match("zbb"));
    assert(r0.match("zabb"));
    assert(r0.match("zaabb"));

    assert(!r0.match("ab"));
    assert(!r0.match("a"));

    assert(!r0.match("aa"));
    assert(!r0.match("b"));
    assert(!r0.match("bb"));
    assert(!r0.match("abb"));
    assert(!r0.match("aabb"));
  }

  {
    Regex r0("a*b*c");
    assert(!r0.match("ab"));
    assert(!r0.match("a"));

    assert(!r0.match("aa"));
    assert(!r0.match("b"));
    assert(!r0.match("bb"));
    assert(!r0.match("abb"));
    assert(!r0.match("aabb"));

    assert(r0.match("abc"));
    assert(r0.match("ac"));

    assert(r0.match("aac"));
    assert(r0.match("bc"));
    assert(r0.match("bbc"));
    assert(r0.match("abbc"));
    assert(r0.match("aabbc"));

    assert(!r0.match("abcc"));
    assert(!r0.match("acc"));

    assert(!r0.match("aacc"));
    assert(!r0.match("bcc"));
    assert(!r0.match("bbcc"));
    assert(!r0.match("abbcc"));
    assert(!r0.match("aabbcc"));
  }


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
    Regex r0(".*");
    assert(r0.match(""));
    assert(r0.match("a"));
    assert(r0.match("aa"));
    assert(r0.match("aaa"));
    assert(r0.match("xxxaaabbb"));
  }

  {
    Regex r0("c.*d");
    assert(r0.match("cd"));
    assert(r0.match("cad"));
    assert(r0.match("caad"));
    assert(r0.match("caaad"));
    assert(r0.match("cxxxaaabbbd"));

    assert(!r0.match("c"));
    assert(!r0.match("ca"));
    assert(!r0.match("caa"));
    assert(!r0.match("caaa"));
    assert(!r0.match("cxxxaaabbb"));

    assert(!r0.match("cdc"));
    assert(!r0.match("cda"));
    assert(!r0.match("cada"));
    assert(!r0.match("caada"));
    assert(!r0.match("cxxxaaabbdb"));
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

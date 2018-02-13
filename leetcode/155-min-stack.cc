#include <limits>
#include <vector>

// ["MinStack","push","push","push","getMin","pop","top","getMin"]
// [[],[-2],[0],[-3],[],[],[],[]]

// TODO: what is spec when pop or getMin are called on an empty stack?
class MinStack {
public:
  MinStack() {}

  int top() const {
    return m_stack[m_stack.size() -1];    
  }
  
  int getMin() const {
    return m_min[m_min.size() -1];
  }
  
  void push(int x) {
    int old_min = std::numeric_limits<int>::max();
    if (m_min.size() > 0) {
      old_min = getMin();
    }

    m_stack.push_back(x);
    m_min.push_back(std::min(x, old_min));
  }
  
  void pop() {
    m_stack.pop_back();
    m_min.pop_back();
  }  
private:
  std::vector<int> m_stack;
  std::vector<int> m_min;
};

int main () {}

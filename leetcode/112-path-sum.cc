#include <cassert>
#include <memory>

struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class Solution {
public:
  bool hasPathSumHelper(TreeNode* node, int sum) {
    int remainder = sum - node->val;
    if (node->left == nullptr && node->right == nullptr) {
      return sum == node->val;
    } else if (node->left == nullptr) {
      return hasPathSumHelper(node->right, remainder);
    } else if (node->right == nullptr) {
      return hasPathSumHelper(node->left, remainder);
    } else {
      return hasPathSumHelper(node->left, remainder) || hasPathSumHelper(node->right, remainder);
    }
  }

  bool hasPathSum(TreeNode* root, int sum) {
    if (root == nullptr) {
      return false;
    }

    return hasPathSumHelper(root, sum);
  }
};

int main() {
  std::unique_ptr<Solution> s(new Solution());

  std::unique_ptr<TreeNode> l0(new TreeNode(5));

  assert(s->hasPathSum(l0.get(), 5));
  assert(! s->hasPathSum(l0.get(), 4));
  assert(! s->hasPathSum(l0.get(), 6));
  assert(! s->hasPathSum(l0.get(), 0));

  std::unique_ptr<TreeNode> l1_0(new TreeNode(4));
  std::unique_ptr<TreeNode> l1_1(new TreeNode(8));
  
  l0->left=l1_0.get();
  assert(!s->hasPathSum(l0.get(), 5));
  assert(s->hasPathSum(l0.get(), 9));
  assert(! s->hasPathSum(l0.get(), 10));
  assert(! s->hasPathSum(l0.get(), 13));
  l0->right=l1_1.get();
  assert(! s->hasPathSum(l0.get(), 5));
  assert(s->hasPathSum(l0.get(), 9));
  assert(s->hasPathSum(l0.get(), 13));

  return 0;
}


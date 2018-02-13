struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class Solution {
public:
  // WARNING: this assumes that both p and q are in the tree.
  TreeNode* lowestCommonAncestor(TreeNode* node, TreeNode* p, TreeNode* q) {
    if (node == nullptr || node == p || node == q) {
      return node;
    }

    TreeNode *left = lowestCommonAncestor(node->left, p, q);
    TreeNode *right = lowestCommonAncestor(node->right, p, q);

    if (left && right) {
      return node;
    } else if (left) {
      return left;
    } else if (right) {
      return right;
    } else {
      return nullptr;
    }
  }
};

int main () {}

#include <iostream>

struct ListNode {
  int val;
  ListNode *next;
  ListNode(int x) : val(x), next(nullptr) {}
};

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
      // std::cout << "merge " << l1 << ":" << l2 << std::endl;
      if (l1 == nullptr && l2 == nullptr) {
	return nullptr;
      }
      if (l1 == nullptr) {
	return l2;
      }
      if (l2 == nullptr) {
	return l1;
      }
      

      ListNode* head = nullptr;
      if (l1->val < l2->val) {
	head = l1;
	l1 = l1->next;
      } else {
	head = l2;
	l2 = l2->next;
      }

      ListNode* cur = head;

      while (l1 != nullptr || l2 != nullptr) {
	// std::cout << l1 << ":" << l2 << "  " << cur << std::endl;
	if (l1 == nullptr) {
	  // std::cout << "l1 empty" << std::endl;
	  cur->next = l2;
	  cur = cur->next;
	  l2 = l2->next;
	} else if (l2 == nullptr) {
	  // std::cout << "l2 empty" << std::endl;
	  cur->next = l1;
	  cur = cur->next;
	  l1 = l1->next;
	} else if (l1->val < l2->val) {
	  // std::cout << "l1 < l2" << std::endl;
	  cur->next = l1;
	  cur = cur->next;
	  l1 = l1->next;
	} else {
	  // std::cout << "else" << std::endl;
	  cur->next = l2;
	  cur = cur->next;
	  l2 = l2->next;
	}
      }

      return head;
    }
};

int main() {
  ListNode *a0 = new ListNode(1);
  ListNode *a1 = new ListNode(2);
  ListNode *a2 = new ListNode(3);
  a0->next = a1;
  a1->next = a2;

  ListNode *b0 = new ListNode(1);
  ListNode *b1 = new ListNode(3);
  ListNode *b2 = new ListNode(4);
  b0->next = b1;
  b1->next = b2;

  Solution s = Solution();
  s.mergeTwoLists(a0, b0);

  delete a0; delete a1; delete a2;
  delete b0; delete b1; delete b2;

  return 0;
}

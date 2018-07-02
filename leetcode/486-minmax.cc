#include <algorithm>
#include <cassert>
#include <memory>
#include <vector>

#include <iostream> // TODO: remove.

class Solution {
public:
  bool PredictTheWinner(std::vector<int> const & nums) {
    if (nums.size() % 2 == 0) {
      return true;
    }

    std::vector<std::vector<long>> a(nums.size(), std::vector<long>(nums.size(), 0));

    long total = 0;
    for (auto const & x : nums) {
      total += x;
    }

    for (size_t i = 0; i < nums.size(); ++i) {
      // std::cout << i << ":" << i << std::endl;
      a[i][i] = nums[i];
    }

    {
      ssize_t span = 1;
      for (ssize_t i = 0; i + span < nums.size(); ++i) {
	int j = i + span;
	a[i][j] = std::max(nums[i], nums[j]);
	// std::cout << i << ":" << j << "\t" << a[i][j] << std::endl;	
      }
    }
    
    for (ssize_t span = 2; span < nums.size(); ++span) {
      for (ssize_t i = 0; i + span < nums.size(); ++i) {
	ssize_t j = i + span;
	//a[i][j] = std::max(nums[i] + ???(a[i+1][j]),
	//		   nums[j] + ???(a[i][j-1]))

	long top = a[i+2][j];
	if (j - 1 >= 0) {
	  top = std::min(top, a[i+1][j-1]);
	}

	// std::cout << "top " << top << std::endl;

	long bottom = 0;
	if (j - 1 >= 0) {
	  bottom = a[i+1][j-1];
	}
	if (j - 2 >= 0) {
	  bottom = std::min(bottom, a[i][j-2]);
	}

	// std::cout << "bottom " << bottom << std::endl;

	a[i][j] = std::max(nums[i] + top,
			   nums[j] + bottom);
	// std::cout << i << ":" << j << "\t" << a[i][j] << std::endl;

      }
    }

    long our_score = a[0][nums.size()-1];
    long their_score = total - our_score;
    // std::cout << "scores " << our_score << ":" << their_score << std::endl;
    return our_score >= their_score;
  }
};

int main() {
  std::unique_ptr<Solution> s(new Solution);

  // Tie is defined as win.
  {
    std::vector<int> in = {0};
    asserts(h->PredictTheWinner(in));
  }


  {
    std::vector<int> in = {1, 5, 2};
    assert(!s->PredictTheWinner(in));
  }

  {
    std::vector<int> in = {1, 5, 233, 7};
    assert(s->PredictTheWinner(in));
  }
}

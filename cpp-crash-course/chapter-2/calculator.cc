#include <iostream>

enum class Operation {
    kAdd,
    kSubtract,
    kMultiply,
    kDivide,
};

struct Calculator {
    Operation op_;

    Calculator(Operation op) : op_(op) {}
    
    int calculate(int xx, int yy) {
        if (op_ == Operation::kAdd) {
            return xx + yy;
        } else if (op_ == Operation::kSubtract) {
            return xx - yy;
        } else if (op_ == Operation::kMultiply) {
            return xx * yy;
        } else if (op_ == Operation::kDivide) {
            return xx / yy;
        } else {
            return -1;
        }
    }
};

int main () {
    Calculator adder(Operation::kAdd);
    std::cout << "4 + 5: " << adder.calculate(4,5) << std::endl;

    Calculator divider(Operation::kDivide);
    std::cout << "21 + 6: " << divider.calculate(21,6) << std::endl;

    return 0;
}
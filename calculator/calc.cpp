#include <iostream>
#include <sstream>
#include <string>
#include <vector>

int64_t calc() {
    // std::istringstream istream(input);
    std::string tok;
    std::vector<int64_t> stack;
    while (std::cin >> tok) {
        int64_t digits;
        if (std::istringstream(tok) >> digits) {
            stack.push_back(digits);
        } else {
            if (stack.size() < 2) {
                // No error to avoid failing fuzzer.
                std::cout << "Ran out of operands\n";
                return 0;
            }
            int64_t op2 = stack.back(); stack.pop_back();
            int64_t op1 = stack.back(); stack.pop_back();
            if (tok == "+") {
                stack.push_back(op1 + op2);
            } else {
                // No error to avoid failing fuzzer.
                std::cout << "Invalid input: " << tok << " with operands: "
                          << op1 << ":" << op2 << std::endl;
                return 0;
            }
                
        }
    }
    return stack.back();
}

int main() {
    std::cout << calc() << std::endl;
}

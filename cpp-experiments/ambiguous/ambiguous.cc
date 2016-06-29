#include <iostream>

void wat(int foo) {
    std::cout << "int" << std::endl;
}

void wat(unsigned foo) {
    std::cout << foo << std::endl;
}

void wat(unsigned long foo) {
    std::cout << "long" << std::endl;
}

int main() {
    unsigned long foo = 1;
    wat(foo);
}

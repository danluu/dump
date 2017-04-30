#include <iostream>

int main() {
    int x = 1;

    // x.~int();
    // error: expected a class name after '~' to name a destructor

    using int_too = int;
    int_too y = 2;
    y.~int_too();

    std::cout << x << " " << y << " " << std::endl;
    // prints "1 2"
}

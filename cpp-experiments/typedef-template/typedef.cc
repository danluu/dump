#include <iostream>

typedef int TypeA;
typedef int TypeB;

template <typename Foo>
void dut(Foo x, Foo y) {
    std::cout << x << ":" << y << std::endl;
}

int main() {
    int one = 1;
    TypeA a = 2;
    TypeB b = 3;
    dut(one, one);
    dut(one, a);
    dut(a, b);
    dut(b, b);
}

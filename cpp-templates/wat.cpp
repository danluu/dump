#include <iostream>
#include <type_traits>

using namespace std;

void foo() {
    cout << "foo\n";
}

template <bool ISTRUE>
void fooBoolConstant() {
    cout << "fooBoolConstant\n";
}

template <bool ISTRUE, typename enable_if<ISTRUE>::type* = nullptr>
void fooBoolTemplate() {
    cout << "fooBoolTrue\n";
}

template <bool ISTRUE, typename enable_if<!ISTRUE>::type* = nullptr>
void fooBoolTemplate() {
    cout << "fooBoolFalse\n";
}

/*
template <bool ISTRUE, typename enable_if_t<ISTRUE>>
void fooBoolTemplate2() {
    cout << "fooBoolTrue\n";
}

template <bool ISTRUE, typename enable_if_t<!ISTRUE>>
void fooBoolTemplate2() {
    cout << "fooBoolFalse\n";
}
*/

int main() {
    foo();
    fooBoolConstant<true>();

    fooBoolTemplate<true>();
    fooBoolTemplate<true>();
    fooBoolTemplate<false>();
    return 0;
}

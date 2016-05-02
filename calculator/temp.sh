clang++ -g -DNATIVEJIT_PLATFORM_POSIX -msse4.2 -std=c++14 -Wall -Wextra -Werror -c calc.cpp -o calc.cpp.o -I ../../NativeJIT/inc

clang++ -g -DNATIVEJIT_PLATFORM_POSIX -msse4.2 -std=c++14 -Wall -Wextra -Werror calc.cpp.o -o calc -rdynamic -L../../NativeJIT/build-linux-clang/src/CodeGen/ -lCodeGen -L../../NativeJIT/build-linux-clang/src/NativeJIT/ -lNativeJIT

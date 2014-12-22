CC = clang
CPPC = clang++
FLAGS = -O3 -W -Wall -Wextra -g

all: increment

increment: increment.cc
	$(CPPC) $^ $(FLAGS) -std=c++11 -pthread -o $@

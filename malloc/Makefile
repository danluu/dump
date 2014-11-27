CC = clang
FLAGS = -Os -W -Wall -Wextra

all: malloc.so test-0 test-1

malloc.so: malloc.c
	$(CC) $^ $(FLAGS) -o $@ -shared -fPIC

test-0: test/test-0.c
	$(CC) $^ $(FLAGS) -o $@

test-1: test/test-1.c
	$(CC) $^ $(FLAGS) -o $@

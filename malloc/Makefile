CC = clang
FLAGS = -Os -W -Wall -Wextra

all: malloc.so test-0

malloc.so: malloc.c
	$(CC) $^ $(FLAGS) -o $@ -shared -fPIC

test-0: test/test-0.c
	$(CC) $^ $(FLAGS) -o $@

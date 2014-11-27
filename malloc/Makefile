CC = clang
FLAGS = -Os -W -Wall -Wextra

all: malloc.so

malloc.so: malloc.c
	$(CC) $^ $(FLAGS) -o $@ -shared -fPIC

Debugging log:

Ok. It compiles. Yay!

But ls and basically any other command segfault :-(.

But test-0 (malloc a couple of ints) works!

And then test-1 fails...

And we can't run test-1 under gdb because gdb segfaults if we LD_PRELOAD malloc.so

Hmm. Maybe use a tiny program that execs something with our malloc.so so that gdb can use normal malloc. Is using two mallocs going to be screwy?

But gdb doesn't crash under the wrapper? Is the wrapper not using our funny malloc? But it definitely uses our funny malloc outside of gdb.

Wait a sec. If we print something from our malloc, it doesn't get printed with test-0. So test-0 doesn't call our malloc? test-1 does and I guess printf mallocs something because printing from there blows up the entire world?

But running after doing another make causes test-1 to segfault from inside the wrapper in gdb? How did tha that happen? 

Ah-ha! Assert that block_ptr->free == 0 and that magic is correct fails.

The problem is that sizeof(struct block_meta) is 32, but...

p/x *(struct block_meta*)(ptr-24)
$20 = {size = 0x4, next = 0x0, free = 0x0, magic = 0x1234, data = {0x1}}

It seems like the tutorial I was following was wrong? This was so suspicious that I even left a comment as I was copying it down.
struct block_meta {
  size_t size;
  struct block_meta *next;
  int free;
  int magic;    // For debugging only. TODO: remove this in non-debug mode.
  char data[1]; // Used to get pointer to data. Is this safe?
};

Removing the data member and just returning a pointer to the correct offset, instead of a pointer to the data member seems to work.

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

Ah-ha! Assert that block_ptr->free == 0 fails.

Whoops. 
struct block_meta *get_block_ptr(void *ptr) {
  return (struct block_meta*)ptr - META_SIZE;
}

Needed to be:
char *get_block_ptr(void *ptr) {
  return (char*)ptr - META_SIZE;
}

or

struct block_meta *get_block_ptr(void *ptr) {
  return (struct block_meta*)ptr - 1;
}


We can see this in gdb:
(gdb) x block_ptr
0x7ffff7dea560 <_dl_fini>:      0xe5894855

(gdb) x ptr -4
0x603f74:       0x00001234


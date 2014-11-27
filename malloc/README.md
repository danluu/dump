Debugging log:

Ok. It compiles. Yay!

But ls and basically any other command segfault :-(.

But test-0 (malloc a couple of ints) works!

And then test-1 fails...

And we can't run test-1 under gdb because gdb segfaults if we LD_PRELOAD malloc.so

Hmm. Maybe use a tiny program that execs something with our malloc.so so that gdb can use normal malloc. Is using two mallocs going to be screwy?

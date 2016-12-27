### Assignment 1a.
~~~
$ clang -O0 mystery1.cc -o mystery1
$ ./mystery1
~~~
Then compile optimized and run via
~~~
$ clang -O2 mystery1.cc -o mystery1_opt
$ ./mystery1_opt
~~~
Explain what happened here. You may find it useful to look at the generated code:
~~~
$ clang -O0 -S mystery1.cc -o mystery1.s
$ clang -O2 -S mystery1.cc -o mystery1_opt.s
~~~

mystery1.s:

Compare to 1000000000, jge jumps out of loop if >=.
~~~
LBB0_1:                                 ## =>This Inner Loop Header: Depth=1
	cmp	dword ptr [rbp - 56], 1000000000
	jge	LBB0_4
## BB#2:                                ##   in Loop: Header=BB0_1 Depth=1
	movsxd	rax, dword ptr [rbp - 52]
	add	rax, qword ptr [rbp - 40]
	mov	qword ptr [rbp - 40], rax
## BB#3:                                ##   in Loop: Header=BB0_1 Depth=1
	mov	eax, dword ptr [rbp - 56]
	add	eax, 1
	mov	dword ptr [rbp - 56], eax
	jmp	LBB0_1
LBB0_4:
~~~

mystery1_opt.s:

Loop elided because the program has no side effects that depend on the loop.

### Assignment 1b.

Comment out second-to-last line and see what happens.

mystery1b:
1000000000 iterations, 5157851576 cycles, 5.16 cycles/iteration

mystery1b_opt:
1000000000 iterations, 31 cycles, 0.00 cycles/iteration

mystery1b_opt.s:

~~~
	imul	r14, rax, 1000000000
~~~

Because the same value is getting added in every iteration, the compiler can just multiply by the number of iterations in the loop instead of adding the same number each time.

### Assignment 1c.

Declare the variable incr “volatile” and rerun -O0 and -O2.

mystery1c:
1000000000 iterations, 4540416448 cycles, 4.54 cycles/iteration
1472083365 165000000000

mystery1c_opt:
1000000000 iterations, 677928934 cycles, 0.68 cycles/iteration
1472083379 179000000000

Two things are happening here: mystery1c is faster than mystery1b (this is true across multiple runs), and mystery1c_opt doesn't run in constant time, unlike mystery1c.

mystery1c_opt:

~~~
	mov	eax, 1000000000
	.align	4, 0x90
LBB0_1:                                 ## =>This Inner Loop Header: Depth=1
	movsxd	rcx, dword ptr [rbp - 28]
	add	rcx, rbx
	movsxd	rdx, dword ptr [rbp - 28]
	add	rdx, rcx
	movsxd	rcx, dword ptr [rbp - 28]
	add	rcx, rdx
	movsxd	rdx, dword ptr [rbp - 28]
	add	rdx, rcx
	movsxd	rbx, dword ptr [rbp - 28]
	add	rbx, rdx
	add	eax, -5
	jne	LBB0_1
~~~

`volatile` forces an actual load to the location to occur. The memory hasn't been marked `UC`, so each of the memory accesses should be a cache hit. Also, the loop is unrolled 5 times.


mystery1b:

~~~
LBB0_1:                                 ## =>This Inner Loop Header: Depth=1
	cmp	dword ptr [rbp - 56], 1000000000
	jge	LBB0_4
## BB#2:                                ##   in Loop: Header=BB0_1 Depth=1
	movsxd	rax, dword ptr [rbp - 52]
	add	rax, qword ptr [rbp - 40]
	mov	qword ptr [rbp - 40], rax
## BB#3:                                ##   in Loop: Header=BB0_1 Depth=1
	mov	eax, dword ptr [rbp - 56]
	add	eax, 1
	mov	dword ptr [rbp - 56], eax
	jmp	LBB0_1
LBB0_4:
~~~

mystery1c:

~~~
LBB0_1:                                 ## =>This Inner Loop Header: Depth=1
	cmp	dword ptr [rbp - 56], 1000000000
	jge	LBB0_4
## BB#2:                                ##   in Loop: Header=BB0_1 Depth=1
	mov	eax, dword ptr [rbp - 52]
	movsxd	rcx, eax
	add	rcx, qword ptr [rbp - 40]
	mov	qword ptr [rbp - 40], rcx
## BB#3:                                ##   in Loop: Header=BB0_1 Depth=1
	mov	eax, dword ptr [rbp - 56]
	add	eax, 1
	mov	dword ptr [rbp - 56], eax
	jmp	LBB0_1
LBB0_4:
~~~

Both inner loops are doing basically the same work. The one difference is that, in `mystery1c`, the `movsxd` is a `reg, reg` operation instead of a `reg, memory` operation. That seems likely to be a side effect of a compiler implementation detail.

### Assignment 1d.

The above exploration gives cycles per iteration but there are more instructions than just the desired “sum += incr;” per loop. How would you measure just the adds, or measure several things that let you then closely approximate just the add time?

We could try wrapping just the add in `rdtsc`, but there's enough slop with `rdtsc` that we shouldn't expect to be able to get a good measurement with that. If we use the appropriate serializing instructions, we can reduce the slop, but those heavily perturb the measurement, and if we're just measuring a couple of instructions the execution environment will be very unnatural since we'll have waited for everything to drain out.

Alternately, we could measure an emtpy loop and subtract out the time it takes for an empty loop to run.

### Assignment 1e.

measure how long each of these take:

* 64-bit integer add (almost completely done above)
* 64-bit integer multiply
* 64-bit integer divide
* Double-precision floating-point add, multiply, and divide

Some notes on the bug so far, before I take a break fror a while

The following code will segfault
~~~
a = rand(100,100)
times(a,a)
dlopen_e("wat")
blas_set_num_threads(32)
println("about to segfault!")
times(a,a)
~~~

`times` is a fn which does less work than `*`, which is the key part of `peakflops` that caused the failure. If `peakflops` is used, `blas_set_num_threads(1)` is sufficient to cause a segfault. The more stuff is removed from `peakflops`, the higher the number necessary to cause a segfault. 

`times` calls `A_mul_B!(similar(B,T,(size(A,1),size(B,2))),A,B)`. A_mul_B! is a function call that should get inlined, but swapping that in makes the segfault go away. Tracing that through, it looks like we eventually call BLAS.gemm! (probably with dgemm?) before we finally segfault.

Deleting any line of the existing code causes the segfault to disappear. Deleing `sys.so` (necessary to run valgrind) also causes the segfault to disappear.

Waiting too long before calling the last `times` also causes the segfault to disappear. The longer the wait, the higher the argument to `blas_set_num_threads` necessary to cause a segfault.

The backtrace is
~~~
134     ../nptl/sysdeps/unix/sysv/linux/x86_64/pthread_cond_wait.S: No such file or directory.
(gdb) bt
#0  pthread_cond_wait@@GLIBC_2.3.2 () at ../nptl/sysdeps/unix/sysv/linux/x86_64/pthread_cond_wait.S:134#1  0x00007ffff1cb7c23 in blas_thread_server () from /home/dluu/dev/julia/usr/bin/../lib/libopenblas.so
#2  0x00007ffff6ade182 in start_thread (arg=0x7fffebcc6700) at pthread_create.c:312
#3  0x00007ffff680afbd in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:111
~~~

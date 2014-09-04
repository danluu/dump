# The following code segfaults.
code_native(match,(Regex,String))

# It seems like we segfault on any code that's stubbed out to some external thing.
# getting code_native for a matrix multiply also segfaults.
# code_type is fine, but code_native and code_llvm blow up.

# GDB backtrace
# Program received signal SIGSEGV, Segmentation fault.
# 0x00007ffff6d9f424 in emit_function (lam=0x1c7fcf0, cstyle=true) at codegen.cpp:3445
# 3445            for(size_t i=0; i < jl_tuple_len(lam->specTypes); i++) {
# (gdb) bt
# #0  0x00007ffff6d9f424 in emit_function (lam=0x1c7fcf0, cstyle=true) at codegen.cpp:3445
# #1  0x00007ffff6d7cd2f in to_function (li=0x1c7fcf0, cstyle=true) at codegen.cpp:570
# #2  0x00007ffff6d7d253 in jl_cstyle_compile (f=0x1c6e780) at codegen.cpp:698
# #3  0x00007ffff6d803c7 in jl_get_llvmf (f=0x1c6e6a0, types=0x2b4b300, getwrapper=false)
#     at codegen.cpp:870
# #4  0x00007ffff6d80492 in jl_dump_function (f=0x1c6e6a0, types=0x2b4b300, dumpasm=true, 
#     dumpwrapper=false) at codegen.cpp:888
# #5  0x00007ffff4aa8f77 in ?? ()
# #6  0x0000000000000006 in ?? ()
# #7  0x00007fffffffcd40 in ?? ()
# #8  0x0000000000000000 in ?? ()

# Seems to be dying on this line?
#         for(size_t i=0; i < jl_tuple_len(lam->specTypes); i++) {
# What's lam-specTypes? What's lam?
# we have jl_lambda_info_t *lam

# lam is li from
# static Function *to_function(jl_lambda_info_t *li, bool cstyle)
# cstyle is true

# lam is from li is from
# void jl_cstyle_compile(jl_function_t *f)

# that comes from jl_get_llvmf, 
#        sf = jl_method_lookup_by_type(jl_gf_mtable(f), types, 0, 0);

# note that we called this with getwrapper = false because jl_dump_function was called with dumpwrapper = false
# which seems to (?) come directly from the code_native and code_llvm calls

# Turning


# code_llvm  (f::Callable, types::(Type...)) = print(_dump_function(f, types, false, false))
# code_native(f::Callable, types::(Type...)) = print(_dump_function(f, types, true, false))

# into 

# code_llvm  (f::Callable, types::(Type...)) = print(_dump_function(f, types, false, true))
# code_native(f::Callable, types::(Type...)) = print(_dump_function(f, types, true, true))

# fixes the segfault, but gives us a bunch of wrapper stuff. What's going on there?

# Well, it calls jl_compile instead of jl_cstyle_compile, that calls to_function with cstyle=false instead of cstyle=true
# Weirdly, it calls it on the same argument, this sf thing.
# Hoe does this work? If We're getting a pointer to a julia function, how could we compile it as a c function?

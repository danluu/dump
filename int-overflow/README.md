time dev/bz2-src/bzip2-1.0.6-normal/bzip2 all_dev.tar

real    1m27.252s
user    1m25.832s
sys     0m0.512s

$ time dev/bz2-src/bzip2-1.0.6-normal-O3/bzip2 all_dev.tar

real    1m26.723s
user    1m25.961s
sys     0m0.648s

$ time dev/bz2-src/bzip2-1.0.6-ftrapv/bzip2 all_dev.tar

real    2m6.883s
user    2m6.273s
sys     0m0.544s

$ time dev/bz2-src/bzip2-1.0.6-ftrapv-O3/bzip2 all_dev.tar

real    2m3.928s
user    2m3.239s
sys     0m0.620s

$ time dev/bz2-src/bzip2-1.0.6-clang/bzip2 all_dev.tar                                                                                   

real    1m31.786s
user    1m30.312s
sys     0m0.600s

$ time dev/bz2-src/bzip2-1.0.6-clang-ftrapv/bzip2 all_dev.tar                                                                            
blocksort.c:930:23: runtime error: unsigned integer overflow: 0 - 1 cannot be represented in type 'unsigned int'
compress.c:166:17: runtime error: unsigned integer overflow: 0 - 1 cannot be represented in type 'unsigned int'
blocksort.c:924:23: runtime error: unsigned integer overflow: 0 - 1 cannot be represented in type 'unsigned int'
blocksort.c:921:66: runtime error: unsigned integer overflow: 0 - 1 cannot be represented in type 'unsigned int'
blocksort.c:891:52: runtime error: unsigned integer overflow: 0 - 1 cannot be represented in type 'unsigned int'
blocksort.c:269:22: runtime error: unsigned integer overflow: 0 - 1 cannot be represented in type 'unsigned int'

real    1m58.227s
user    1m55.564s
sys     0m0.604s

-O1
----------10000 accesses--------
Page-aligned time:         12329
----------1000 accesses--------
Page-aligned time:         1272

-O1 -fsanitize=signed-integer-overflow
----------10000 accesses--------
Page-aligned time:         62773
----------1000 accesses--------
Page-aligned time:         6307

-O2 
0000000000400530 <single_add>:
  400530:       01 f7                   add    %esi,%edi
  400532:       89 f8                   mov    %edi,%eax
  400534:       c3                      retq   
  400535:       66 66 2e 0f 1f 84 00    data32 nopw %cs:0x0(%rax,%rax,1)
  40053c:       00 00 00 00 

000000000041df90 <single_add>:
  41df90:       53                      push   %rbx
  41df91:       89 fb                   mov    %edi,%ebx
  41df93:       01 f3                   add    %esi,%ebx
  41df95:       70 04                   jo     41df9b <single_add+0xb>
  41df97:       89 d8                   mov    %ebx,%eax
  41df99:       5b                      pop    %rbx
  41df9a:       c3                      retq   
  41df9b:       89 f8                   mov    %edi,%eax
  41df9d:       89 f1                   mov    %esi,%ecx
  41df9f:       bf a0 89 62 00          mov    $0x6289a0,%edi
  41dfa4:       48 89 c6                mov    %rax,%rsi
  41dfa7:       48 89 ca                mov    %rcx,%rdx
  41dfaa:       e8 91 13 00 00          callq  41f340 <__ubsan_handle_add_overflow>
  41dfaf:       eb e6                   jmp    41df97 <single_add+0x7>

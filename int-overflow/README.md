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

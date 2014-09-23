Bytes / cycle. SSSE 3 is an implementation that's allegedly faster than using the hardware popcnt instruction. Other lines are various ways of gcc/clang to emit popcnt.

This graph is from `clang -O3 -mpopcnt`

| Algorithm | 1k | 4k | 16k | 65k | 256k | 1M | 4M | 16M |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Intrinsic | 6.9 | 7.3 | 7.4 | 7.5 | 7.5 | 7.5 | 7.5 | 7.5 |
| PSHUFB | 11.5 | 13.0 | 13.3 | 13.4 | 13.1 | 13.4 | 13.0 | 12.6 |
| Unrolled Intrinsic | 12.5 | 14.4 | 15.0 | 15.1 | 15.2 | 15.2 | 15.2 | 15.2 |
| Unrolled Intrinsic 2 | 14.3 | 16.3 | 17.0 | 17.2 | 17.2 | 17.0 | 16.8 | 16.7 |
| Assembly | 17.5 | 23.7 | 25.3 | 25.3 | 26.3 | 26.3 | 25.3 | 24.3 |

Note to self: try running n copies of this at once to see if varying n changes the relative speed of the movdqa versions.

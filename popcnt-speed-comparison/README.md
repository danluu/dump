Bytes / cycle. SSSE 3 is an implementation that's allegedly faster than using the hardware popcnt instruction. Other lines are various ways of gcc/clang to emit popcnt.

This graph is from `clang -O3 -mpopcnt`

![Bytes per cycle](bytes_per_cycle.png)
![Bytes per cycle](bytes_per_cycle-1.png)

Note to self: try running n copies of this at once to see if varying n changes the relative speed of the movdqa versions.

Just messing around with software fuzzing for Julia. Not much here, since I don't know how software fuzzers should work and don't know Julia. Despite that, this has found the following bugs:


[8286: exponent of large number causes crash \(SIGABRT\)(https://github.com/JuliaLang/julia/issues/8286)

[8277: code near exception incorrectly optimized out](https://github.com/JuliaLang/julia/issues/8277)

[8266: hang/bad result on ndigits](https://github.com/JuliaLang/julia/pull/8266)

[8241: hang/segfault on long symbol](https://github.com/JuliaLang/julia/pull/8241)

[8239: segfault on code_native/code_llvm](https://github.com/JuliaLang/julia/pull/8239)

And then there are surprising things that aren't bugs:

[Inconsistent handling of some operators](https://groups.google.com/forum/#!topic/julia-users/ljQ-nHpXitU)

Address space randomiziation causes some methods to be randomized across invocations of julia.

And there are things I haven't gotten around to debugging/patching yet:

`searchindex` returns an unclear error message: 
~~~
julia> searchindex("q8NWiRVEW3NRTGXW6At7qN5aU2dhJ0ZGHSMfcH50k1Xsn1HIiPNRO0NXVhafnLkEd55","wKPx3QydhlLKz3fZQK3fCVhl6ZwMoFDq18ti1Ozcswi\
Av0Yq4k9utZgoN4KhdvIJiUjQcTIFZyD1cNmdsf1PcmmXMeh10N1",-234321342423423234534534543)
ERROR: error compiling searchindex: error compiling _searchindex: cannot convert type to a julia type
 in searchindex at string.jl:307
~~~

`sprandn` with bad args can take an arbitrary long time before erroring out.

`displayable` psuedo-randomly hangs.

`peakflops` segfaults



Just messing around with software fuzzing for Julia. Not much here, since I don't know how software fuzzers should work and don't know Julia. Despite that, this has found the following bugs:

[8266: hang/bad result on ndigits](https://github.com/JuliaLang/julia/pull/8266)

[8241: hang/segfault on long symbol](https://github.com/JuliaLang/julia/pull/8241)

[8239: segfault on code_native/code_llvm](https://github.com/JuliaLang/julia/pull/8239)

And then there are surprising things that aren't bugs:

[Inconsistent handling of some operators](https://groups.google.com/forum/#!topic/julia-users/ljQ-nHpXitU)




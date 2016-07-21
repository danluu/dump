### ʕ╯•ᴥ•ʔ╯︵‾‾: move function arguments into the function name

e.g., instead of `foo(a,b)`, we have `foo_a_b`.

#### Usage

~~~julia
$> julia
               _
   _       _ _(_)_     |  A fresh approach to technical computing
  (_)     | (_) (_)    |  Documentation: http://docs.julialang.org
   _ _   _| |_  __ _   |  Type "help()" to list help topics
  | | | | | | |/ _` |  |
  | | |_| | | | (_| |  |  Version 0.2.0-rc2+92
 _/ |\__'_|_|_|\__'_|  |  Commit multiple_def/3130435* 2013-10-30 13:17:37 UTC
|__/                   |  x86_64-apple-darwin12.5.0

julia> include("ʕ╯•ᴥ•ʔ╯︵‾‾.jl")

julia> function mul(x, y)
         x * y
       end
foo (generic function with 1 method)

julia> a = 10
10

julia> @ʕ╯•ᴥ•ʔ╯︵‾‾ mul_a_a
100

julia> @ʕ╯•ᴥ•ʔ╯︵‾‾ mul_a_15
150
~~~

#### FAQs

##### Why?
Why not? This was a quick post-dinner pair programming project one lazy night, with [Leah Hanson](https://github.com/astrieanna/).

#### TODOs
Support named arguments.

~~Make a macro that lets you declare variables and functions with arbitrary names, such as `(`, and ` `, allowing names like `(۶ૈ ᵒ̌ Дᵒ̌)۶ૈ=͟͟͞͞ ⌨`. I don't know that this is possible without using quoted strings or modifying the parser, and it seems unlikely that [Julia](https://github.com/JuliaLang/julia/) will accept a pull request that puts `ʕ╯•ᴥ•ʔ╯︵‾‾` into the parser as a token that special cases the rest of the line up to some special delimeter. Oh well. Strings it is.~~ This basically works, but these things need better testing and names.


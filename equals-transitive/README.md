~~~
$ ghci
Prelude> -- 2^53 == 2.0^53
Prelude>  9007199254740992 == 9007199254740992.0 
True
Prelude> -- 2.0^53 == 2^53 + 1
Prelude>  9007199254740992.0 == 9007199254740993
True
Prelude> -- 2^53 == 2^53 + 1
Prelude>  9007199254740992 == 9007199254740993
False
~~~
| Language | Transitive | Unique ints | Allowed |
| --- | --- | --- | --- |
| C gcc 4.6.4 | No | Yes | Yes |
| Clojure 1.4 | No | Yes | Yes |
| C# Mono 2.10.8.1 | No | Yes | Yes |
| Haskell 7.4.1 | No | Yes | Yes |
| Java 1.7 | No | Yes | Yes |
| perl 5.14.2 | No | Yes | Yes |
| Ruby 1.8.7 | No | Yes | Yes |
| Scala 2.9.2 | No | Yes | Yes |
| Scheme (racket) | No | Yes | Yes |
| Go 1.3 | Yes | Yes | Yes |
| Julia 0.3 rc1 | Yes | Yes | Yes |
| Lisp SBCL 1.0.55 | Yes | Yes | Yes |
| Python 2.7.3 | Yes | Yes | Yes |
| Ruby 2.0 | Yes | Yes | Yes |
| javascript[^J] | Yes | No | Yes |
| Lua | Yes | No | Yes |
| Octave 3.6.2 | Yes | No | Yes |
| Ocaml 3.12.1 | - | - | No |
~~~
int main() {
  unsigned long a = 0xffffffffffffffff;
  long b = -1;
  printf("%i", b > a);
  printf("%i", a > b);
  printf("%i", a == b);
}
~~~
| Language | Correct | Incorrect | Error | No ULong |
| --- | --- | --- | --- | --- |
| C gcc 4.6.4 |  | X | |
| Clojure 1.1 | | | | X |
| C# Mono 2.10.8.1 |  | | X | |
| Haskell 7.4.1 | | | | X |
| Java 1.7 | | | | X |
| perl 5.14.2 | | | | X |
| Ruby 1.8.7 | | | | X |
| Scala 2.9.2 | | | | X |
| Go 1.3 | | | X | |
| Julia 0.3 rc1 | X | | | |
| Python 2.7.3 | | | | X |
| Ruby 2.0 | | | | X |
| javascript | | | | X |
| Lua | | | | X |
| Octave 3.6.2 | | | | X |
| Ocaml 3.12.1 | | | | X |
~~~
Prelude> min nan 1
1.0
Prelude> min 1 nan
NaN
~~~

| Language | 1st | 2nd | NaN | non-NaN | Exception |
| --- | --- | --- | --- | --- | --- |
| Scheme (racket) | | | X | | |
| Clojure 1.4 | | | X | | |
| C# Mono 2.10.8.1 | | | X | | |
| Java 1.7 | | | X | | |
| Scala 2.9.2 | | | X | | |
| Go 1.3 | | | X | | |
| javascript | | | X | | |
| Octave 3.6.2 | | | X | | |
| Haskell 7.4.1 | | X | | | |
| Ocaml 3.12.1 | | X | | | |
| Lua | X | | | | |
| perl 5.14.2 | X | | | | |
| Python 2.7.3 | X | | | | |
| C gcc 4.6.4 | | | | X | |
| Julia 0.3 rc1[^S] | | | | X | |
| Lisp SBCL 1.0.55 | | | | | X |
| Ruby 1.8.7 | | | | | X |
| Ruby 2.0 | | | | | X |


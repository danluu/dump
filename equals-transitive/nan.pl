#!/usr/bin/perl

use List::Util qw( min max );

$nan = -sin(9**9**9);
$x = 1.0;
$a = min($nan, $x);
$b = min($x, $nan);
print("min(nan,x) $a\n");
print("min(x,nan) $b\n");

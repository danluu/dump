#!/usr/bin/perl

$x = 9007199254740992;    
$y = 9007199254740992.0;  
$z = 9007199254740993;    
$a = $x == $y;
$b = $y == $z;
$c = $x == $z;
print("x == y $a\n");
print("y == z $b\n");
print("x == z $c\n");

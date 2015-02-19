--Memory unit for CS552 Spring 1998
--Final project
--by Phil Atkinson

--CHANGE THE LINES MARKED BELOW TO POINT TO YOUR INPUT AND OUTPUT FILES

library ieee;
use ieee.std_logic_1164.all;
use ieee.math_real.all;
use std.textio.all;


--Define the interface
entity memory_unit5 is port (
   clk, AS, RD, WR, LD, DUMP_SIG:   in std_logic;
   addr:               in std_logic_vector(15 downto 0);
   Data_in:           in std_logic_vector(15 downto 0);   
   Data_out:           out std_logic_vector(15 downto 0);   
   READY:             out std_logic
);
end memory_unit5;
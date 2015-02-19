--Cache unit for CS552 Spring 1998
--Final project
--by Phil Atkinson
--Modified on 4/23/97 - Took out do_nothing statment if a write-hit occurs
--			Old code set hit to 0 if a write hit occured.


--CHANGE THE LINE MARKER BELOW TO YOUR OUTPUT FILE

library ieee;
use ieee.std_logic_1164.all;
use std.textio.all;

entity cache_unit is port (
   clk, RW, CA, DUMP_SIG, ENABLE:   in std_logic;
   word:		    in std_logic;
   index:                   in std_logic_vector(7 downto 0);
   tag_in:                  in std_logic_vector(6 downto 0);   
   tag_out:                 out std_logic_vector(6 downto 0);   
   data_in:		    in std_logic_vector(15 downto 0);
   data_out:		    out std_logic_vector(15 downto 0);
   valid, dirty:  	    out std_logic;
   HIT:                     out std_logic
);
end cache_unit;
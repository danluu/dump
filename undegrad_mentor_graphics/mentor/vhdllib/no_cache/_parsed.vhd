-----------------------------------------------------
-- highly unoptimized. Could save one cycle on back to back ops
-- change for pipelined version - unless it doesn't matter for CPI
-- which it might not..

-- need to retest now that it has no clock dependance

library ieee ;
use ieee.std_logic_1164.all;
use ieee.math_real.all;
use std.textio.all;


-----------------------------------------------------

entity no_cache is port(	
	clk, ready_in, go, read, write:		in std_logic;
	addr_out:               out std_logic_vector(15 downto 0);
	addr_in:                in std_logic_vector(15 downto 0);
	debug: out std_logic_vector(15 downto 0);
	reset:		in std_logic;
	AS, RD, WR, LD, ready_out:		out std_logic -- LD is unused
);
end no_cache;
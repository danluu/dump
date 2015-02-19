-----------------------------------------------------
-- need to set ready_out, TAG?
-- need to fully reset?
--need to set INDEX? or assume it's hardwired?
--writeback to memory wont work. what is CPU_DATA supposed to control? cache or mem input?

--to use: toggle go signal for one cycle only

--clean miss on read is working correctly

library ieee ;
use ieee.std_logic_1164.all;
use ieee.math_real.all;
use std.textio.all;


-----------------------------------------------------

entity direct is port(	
	clk, ready_in, go, read_i, write_i:		in std_logic;
	addr_out:               out std_logic_vector(15 downto 0);
	addr_in:                in std_logic_vector(15 downto 0);
	debug: out std_logic_vector(15 downto 0);
	reset:		in std_logic;
	AS, RD, WR, LD, ready_out:		out std_logic;
----------------------------------------------------
	HIT, VALID, DIRTY, word_in: in std_logic;
	RW, CA, ENABLE, WORD: out std_logic;
	TAG: out std_logic_vector(6 downto 0); -- tag going out to mem/cache
	tag_back: in std_logic_vector(6 downto 0); -- "TAG_OUT" from cache
	tag_addr: in std_logic_vector(6 downto 0); -- tag bits coming in from CPU
	CPU_DATA: out std_logic -- control which data goes into cache
);
end direct;
--ALU Noop passes through B, not A
--Enable MemoryOut register w/ MemRead signal
--ThreeOps and ALUSrcC are the same?

-----------------------------------------------------

library ieee ;
use ieee.std_logic_1164.all;

-----------------------------------------------------

entity control is port(	
	clk, reset, data_ready:	in std_logic;
	opcode:		in std_logic_vector(4 downto 0);
	function_code:	in std_logic_vector(1 downto 0);
MemAccess:	out std_logic;	
Halt, ThreeOps, MemRead, MemWrite, IRWrite, PCWrite, RegWrite, RegAddrSrc, Beqz, Bltz, ALUSrcC, ArithmOp:	out std_logic;
	ShiftType, ALUSrcA, MemDataSrc, RegDataSrc:	out std_logic_vector(1 downto 0);
	ALUOp, ALUSrcB, MemAddrSrc, ImmKind, PCDataSrc:	out std_logic_vector(2 downto 0)
	
);
end control;
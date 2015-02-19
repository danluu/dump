Library ieee;
Library vhdl552;
Library std;

Use ieee.std_logic_1164.all;
Use std.textio.all;
Use ieee.math_real.all;

Entity \EI$48\ is
		port(
			DUMP_SIG : in std_logic;
			MemAccess : in std_logic;
			MemRead : in std_logic;
			MemWrite : in std_logic;
			LD : inout std_logic
		) ; 
end \EI$48\;

Architecture qspro_shadow of \EI$48\ is

--  COMPONENT DECLARATIONS

	component \/u/d/l/dluu/mentor/vhdlsym/cache_unit63\
		port(
			index : in std_logic_vector(7 downto 0) ;
			tag_in : in std_logic_vector(6 downto 0) ;
			tag_out : out std_logic_vector(6 downto 0) ;
			data_in : in std_logic_vector(15 downto 0) ;
			data_out : out std_logic_vector(15 downto 0) ;
			clk : in std_logic;
			RW : in std_logic;
			CA : in std_logic;
			DUMP_SIG : in std_logic;
			ENABLE : in std_logic;
			word : in std_logic;
			valid : out std_logic;
			dirty : out std_logic;
			HIT : out std_logic
		) ; 
	end component;

	component \/u/j/e/jeshua/mentor/dluu/vhdlsym/direct89\
		port(
			addr_out : out std_logic_vector(15 downto 0) ;
			addr_in : in std_logic_vector(15 downto 0) ;
			debug : out std_logic_vector(15 downto 0) ;
			TAG : out std_logic_vector(6 downto 0) ;
			tag_back : in std_logic_vector(6 downto 0) ;
			tag_addr : in std_logic_vector(6 downto 0) ;
			clk : in std_logic;
			ready_in : in std_logic;
			go : in std_logic;
			read_i : in std_logic;
			write_i : in std_logic;
			reset : in std_logic;
			AS : out std_logic;
			RD : out std_logic;
			WR : out std_logic;
			LD : out std_logic;
			ready_out : out std_logic;
			HIT : in std_logic;
			VALID : in std_logic;
			DIRTY : in std_logic;
			word_in : in std_logic;
			RW : out std_logic;
			CA : out std_logic;
			ENABLE : out std_logic;
			WORD : out std_logic;
			CPU_DATA : out std_logic
		) ; 
	end component;

	component \/u/j/e/jeshua/mentor/dluu/vhdlsym/memory_unit455\
		port(
			addr : in std_logic_vector(15 downto 0) ;
			Data_in : in std_logic_vector(15 downto 0) ;
			Data_out : out std_logic_vector(15 downto 0) ;
			clk : in std_logic;
			AS : in std_logic;
			RD : in std_logic;
			WR : in std_logic;
			LD : in std_logic;
			DUMP_SIG : in std_logic;
			READY : out std_logic
		) ; 
	end component;

-- INLINE CONFIGURATIONS

	for \I$14\ : \/u/d/l/dluu/mentor/vhdlsym/cache_unit63\ use entity vhdl552.cache_unit(complete_cache);
	for \I$11\ : \/u/j/e/jeshua/mentor/dluu/vhdlsym/direct89\ use entity vhdl552.direct(version1);
	for \I$10\ : \/u/j/e/jeshua/mentor/dluu/vhdlsym/memory_unit455\ use entity vhdl552.memory_unit4(mem1);

-- SIGNAL DECLARATIONS

	signal \N$39\ : std_logic;
	signal DIRTY : std_logic;
	signal ready_in : std_logic;
	signal \N$31\ : std_logic;
	signal \N$35\ : std_logic;
	signal HIT : std_logic;
	signal \N$27\ : std_logic;
	signal \N$38\ : std_logic;
	signal \N$28\ : std_logic;
	signal \N$34\ : std_logic;
	signal VALID : std_logic;
	signal \N$42\ : std_logic_vector(15 downto 0) ;
	signal addr : std_logic_vector(15 downto 0) ;
	signal \N$294\ : std_logic_vector(6 downto 0) ;

begin

	\I$14\ : \/u/d/l/dluu/mentor/vhdlsym/cache_unit63\
		port map(
			clk => open,
			RW => \N$35\,
			CA => \N$28\,
			DUMP_SIG => DUMP_SIG,
			ENABLE => \N$31\,
			word => \N$38\,
			valid => VALID,
			dirty => DIRTY,
			HIT => HIT,
			data_out => open,
			data_in => open,
			tag_out => open,
			tag_in(6) => \N$294\(6),
			tag_in(5) => \N$294\(5),
			tag_in(4) => \N$294\(4),
			tag_in(3) => \N$294\(3),
			tag_in(2) => \N$294\(2),
			tag_in(1) => \N$294\(1),
			tag_in(0) => \N$294\(0),
			index => open
		);
	\I$11\ : \/u/j/e/jeshua/mentor/dluu/vhdlsym/direct89\
		port map(
			clk => open,
			ready_in => ready_in,
			go => MemAccess,
			read_i => MemRead,
			write_i => MemWrite,
			reset => open,
			AS => \N$27\,
			RD => \N$34\,
			WR => \N$39\,
			LD => LD,
			ready_out => open,
			HIT => HIT,
			VALID => VALID,
			DIRTY => DIRTY,
			word_in => open,
			RW => \N$35\,
			CA => \N$28\,
			ENABLE => \N$31\,
			WORD => \N$38\,
			CPU_DATA => open,
			tag_addr => open,
			tag_back => open,
			TAG(6) => \N$294\(6),
			TAG(5) => \N$294\(5),
			TAG(4) => \N$294\(4),
			TAG(3) => \N$294\(3),
			TAG(2) => \N$294\(2),
			TAG(1) => \N$294\(1),
			TAG(0) => \N$294\(0),
			debug(15) => \N$42\(15),
			debug(14) => \N$42\(14),
			debug(13) => \N$42\(13),
			debug(12) => \N$42\(12),
			debug(11) => \N$42\(11),
			debug(10) => \N$42\(10),
			debug(9) => \N$42\(9),
			debug(8) => \N$42\(8),
			debug(7) => \N$42\(7),
			debug(6) => \N$42\(6),
			debug(5) => \N$42\(5),
			debug(4) => \N$42\(4),
			debug(3) => \N$42\(3),
			debug(2) => \N$42\(2),
			debug(1) => \N$42\(1),
			debug(0) => \N$42\(0),
			addr_in => open,
			addr_out(15) => addr(15),
			addr_out(14) => addr(14),
			addr_out(13) => addr(13),
			addr_out(12) => addr(12),
			addr_out(11) => addr(11),
			addr_out(10) => addr(10),
			addr_out(9) => addr(9),
			addr_out(8) => addr(8),
			addr_out(7) => addr(7),
			addr_out(6) => addr(6),
			addr_out(5) => addr(5),
			addr_out(4) => addr(4),
			addr_out(3) => addr(3),
			addr_out(2) => addr(2),
			addr_out(1) => addr(1),
			addr_out(0) => addr(0)
		);
	\I$10\ : \/u/j/e/jeshua/mentor/dluu/vhdlsym/memory_unit455\
		port map(
			clk => open,
			AS => \N$27\,
			RD => \N$34\,
			WR => \N$39\,
			LD => LD,
			DUMP_SIG => DUMP_SIG,
			READY => ready_in,
			Data_out => open,
			Data_in => open,
			addr(15) => addr(15),
			addr(14) => addr(14),
			addr(13) => addr(13),
			addr(12) => addr(12),
			addr(11) => addr(11),
			addr(10) => addr(10),
			addr(9) => addr(9),
			addr(8) => addr(8),
			addr(7) => addr(7),
			addr(6) => addr(6),
			addr(5) => addr(5),
			addr(4) => addr(4),
			addr(3) => addr(3),
			addr(2) => addr(2),
			addr(1) => addr(1),
			addr(0) => addr(0)
		);

end qspro_shadow;

Library ieee;
Library vhdl552;
Library std;

Use ieee.std_logic_1164.all;
Use std.textio.all;
Use ieee.math_real.all;

Entity top_cache_qsim is
end top_cache_qsim;

Architecture qspro_shadow of top_cache_qsim is

--  COMPONENT DECLARATIONS

	component \/u/j/e/jeshua/mentor/dluu/vhdlsym/control46\
		port(
			opcode : in std_logic_vector(4 downto 0) ;
			function_code : in std_logic_vector(1 downto 0) ;
			ShiftType : out std_logic_vector(1 downto 0) ;
			ALUSrcA : out std_logic_vector(1 downto 0) ;
			MemDataSrc : out std_logic_vector(1 downto 0) ;
			RegDataSrc : out std_logic_vector(1 downto 0) ;
			ALUOp : out std_logic_vector(2 downto 0) ;
			ALUSrcB : out std_logic_vector(2 downto 0) ;
			MemAddrSrc : out std_logic_vector(2 downto 0) ;
			ImmKind : out std_logic_vector(2 downto 0) ;
			PCDataSrc : out std_logic_vector(2 downto 0) ;
			clk : in std_logic;
			reset : in std_logic;
			data_ready : in std_logic;
			MemAccess : out std_logic;
			Halt : out std_logic;
			ThreeOps : out std_logic;
			MemRead : out std_logic;
			MemWrite : out std_logic;
			IRWrite : out std_logic;
			PCWrite : out std_logic;
			RegWrite : out std_logic;
			RegAddrSrc : out std_logic;
			Beqz : out std_logic;
			Bltz : out std_logic;
			ALUSrcC : out std_logic;
			ArithmOp : out std_logic
		) ; 
	end component;

	component \EI$48\
		port(
			DUMP_SIG : in std_logic;
			MemAccess : in std_logic;
			MemRead : in std_logic;
			MemWrite : in std_logic;
			LD : inout std_logic
		) ; 
	end component;

-- INLINE CONFIGURATIONS

	for \I$63\ : \/u/j/e/jeshua/mentor/dluu/vhdlsym/control46\ use entity vhdl552.control(version1);
	for \I$48\ : \EI$48\ use entity vhdl552.\EI$48\(qspro_shadow);

-- SIGNAL DECLARATIONS

	signal MemAccess : std_logic;
	signal LD : std_logic;
	signal MemRead : std_logic;
	signal DUMP_SIG : std_logic;
	signal MemWrite : std_logic;

begin

	\I$63\ : \/u/j/e/jeshua/mentor/dluu/vhdlsym/control46\
		port map(
			clk => open,
			reset => open,
			data_ready => open,
			MemAccess => MemAccess,
			Halt => open,
			ThreeOps => open,
			MemRead => MemRead,
			MemWrite => MemWrite,
			IRWrite => open,
			PCWrite => open,
			RegWrite => open,
			RegAddrSrc => open,
			Beqz => open,
			Bltz => open,
			ALUSrcC => open,
			ArithmOp => open,
			PCDataSrc => open,
			ImmKind => open,
			MemAddrSrc => open,
			ALUSrcB => open,
			ALUOp => open,
			RegDataSrc => open,
			MemDataSrc => open,
			ALUSrcA => open,
			ShiftType => open,
			function_code => open,
			opcode => open
		);
	\I$48\ : \EI$48\
		port map(
			DUMP_SIG => DUMP_SIG,
			MemAccess => MemAccess,
			MemRead => MemRead,
			MemWrite => MemWrite,
			LD => LD
		);

end qspro_shadow;


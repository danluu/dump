Library ieee;
Library vhdl552;
Library std;

Use ieee.std_logic_1164.all;
Use ieee.math_real.all;
Use std.textio.all;

Entity \EI$1041\ is
		port(
			LD : in std_logic;
			DUMP_SIG : in std_logic;
			MemAccess : in std_logic;
			MemRead : in std_logic;
			MemWrite : in std_logic;
			\data_ready_0_\ : out std_logic
		) ; 
end \EI$1041\;

Architecture qspro_shadow of \EI$1041\ is

--  COMPONENT DECLARATIONS

	component \/u/d/l/dluu/mentor/vhdlsym/memory_unit55\
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

	component \/u/j/e/jeshua/mentor/dluu/vhdlsym/no_cache59\
		port(
			addr_out : out std_logic_vector(15 downto 0) ;
			addr_in : in std_logic_vector(15 downto 0) ;
			debug : out std_logic_vector(15 downto 0) ;
			clk : in std_logic;
			ready_in : in std_logic;
			go : in std_logic;
			read : in std_logic;
			write : in std_logic;
			reset : in std_logic;
			AS : out std_logic;
			RD : out std_logic;
			WR : out std_logic;
			LD : out std_logic;
			ready_out : out std_logic
		) ; 
	end component;

-- INLINE CONFIGURATIONS

	for \I$23\ : \/u/d/l/dluu/mentor/vhdlsym/memory_unit55\ use entity vhdl552.memory_unit;
	for \I$24\ : \/u/j/e/jeshua/mentor/dluu/vhdlsym/no_cache59\ use entity vhdl552.no_cache(version1);

-- SIGNAL DECLARATIONS

	signal \N$294\ : std_logic;
	signal \N$81\ : std_logic;
	signal \N$78\ : std_logic;
	signal \N$80\ : std_logic;
	signal \N$85\ : std_logic_vector(15 downto 0) ;
	signal \N$83\ : std_logic_vector(15 downto 0) ;

begin

	\I$23\ : \/u/d/l/dluu/mentor/vhdlsym/memory_unit55\
		port map(
			clk => open,
			AS => \N$78\,
			RD => \N$80\,
			WR => \N$81\,
			LD => LD,
			DUMP_SIG => DUMP_SIG,
			READY => open,
			Data_out => open,
			Data_in => open,
			addr => open
		);
	\I$24\ : \/u/j/e/jeshua/mentor/dluu/vhdlsym/no_cache59\
		port map(
			clk => open,
			ready_in => open,
			go => MemAccess,
			read => MemRead,
			write => MemWrite,
			reset => open,
			AS => \N$78\,
			RD => \N$80\,
			WR => \N$81\,
			LD => \N$294\,
			ready_out => \data_ready_0_\,
			debug(15) => \N$85\(15),
			debug(14) => \N$85\(14),
			debug(13) => \N$85\(13),
			debug(12) => \N$85\(12),
			debug(11) => \N$85\(11),
			debug(10) => \N$85\(10),
			debug(9) => \N$85\(9),
			debug(8) => \N$85\(8),
			debug(7) => \N$85\(7),
			debug(6) => \N$85\(6),
			debug(5) => \N$85\(5),
			debug(4) => \N$85\(4),
			debug(3) => \N$85\(3),
			debug(2) => \N$85\(2),
			debug(1) => \N$85\(1),
			debug(0) => \N$85\(0),
			addr_in => open,
			addr_out(15) => \N$83\(15),
			addr_out(14) => \N$83\(14),
			addr_out(13) => \N$83\(13),
			addr_out(12) => \N$83\(12),
			addr_out(11) => \N$83\(11),
			addr_out(10) => \N$83\(10),
			addr_out(9) => \N$83\(9),
			addr_out(8) => \N$83\(8),
			addr_out(7) => \N$83\(7),
			addr_out(6) => \N$83\(6),
			addr_out(5) => \N$83\(5),
			addr_out(4) => \N$83\(4),
			addr_out(3) => \N$83\(3),
			addr_out(2) => \N$83\(2),
			addr_out(1) => \N$83\(1),
			addr_out(0) => \N$83\(0)
		);

end qspro_shadow;

Library ieee;
Library vhdl552;
Library std;

Use ieee.std_logic_1164.all;
Use ieee.math_real.all;
Use std.textio.all;

Entity toplevel_qsim is
end toplevel_qsim;

Architecture qspro_shadow of toplevel_qsim is

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

	component \EI$1041\
		port(
			LD : in std_logic;
			DUMP_SIG : in std_logic;
			MemAccess : in std_logic;
			MemRead : in std_logic;
			MemWrite : in std_logic;
			\data_ready_0_\ : out std_logic
		) ; 
	end component;

-- INLINE CONFIGURATIONS

	for \I$1040\ : \/u/j/e/jeshua/mentor/dluu/vhdlsym/control46\ use entity vhdl552.control(version1);
	for \I$1041\ : \EI$1041\ use entity vhdl552.\EI$1041\(qspro_shadow);

-- SIGNAL DECLARATIONS

	signal MemWrite : std_logic;
	signal data_ready : std_logic;
	signal LD : std_logic;
	signal MemAccess : std_logic;
	signal DUMP_SIG : std_logic;
	signal MemRead : std_logic;

begin

	\I$1040\ : \/u/j/e/jeshua/mentor/dluu/vhdlsym/control46\
		port map(
			clk => open,
			reset => open,
			data_ready => data_ready,
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
	\I$1041\ : \EI$1041\
		port map(
			LD => LD,
			DUMP_SIG => DUMP_SIG,
			MemAccess => MemAccess,
			MemRead => MemRead,
			MemWrite => MemWrite,
			\data_ready_0_\ => data_ready
		);

end qspro_shadow;


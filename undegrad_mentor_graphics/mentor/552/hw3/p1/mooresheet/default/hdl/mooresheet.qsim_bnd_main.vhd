Library ieee;
Library vhdl552;

Use ieee.std_logic_1164.all;

Entity mooresheet_qsim is
end mooresheet_qsim;

Architecture qspro_shadow of mooresheet_qsim is

--  COMPONENT DECLARATIONS

	component \/u/d/l/dluu/mentor/vhdlsym/det_101014\
		port(
			clk : in std_logic;
			inp : in std_logic;
			reset : in std_logic;
			outp : out std_logic
		) ; 
	end component;

-- INLINE CONFIGURATIONS

	for \I$1\ : \/u/d/l/dluu/mentor/vhdlsym/det_101014\ use entity vhdl552.det_10101(cs552);

-- SIGNAL DECLARATIONS

	signal \in\ : std_logic;
	signal reset : std_logic;
	signal \OUT\ : std_logic;
	signal clk : std_logic;

begin

	\I$1\ : \/u/d/l/dluu/mentor/vhdlsym/det_101014\
		port map(
			clk => clk,
			inp => \in\,
			reset => reset,
			outp => \OUT\
		);

end qspro_shadow;


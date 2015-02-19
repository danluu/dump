Library ieee;
Library vhdl552;

Use ieee.std_logic_1164.all;

Entity mealysheet_qsim is
end mealysheet_qsim;

Architecture qspro_shadow of mealysheet_qsim is

--  COMPONENT DECLARATIONS

	component \/u/d/l/dluu/mentor/vhdlsym/det_10101_mealy4\
		port(
			clk : in std_logic;
			inp : in std_logic;
			reset : in std_logic;
			outp : out std_logic
		) ; 
	end component;

-- INLINE CONFIGURATIONS

	for \I$415\ : \/u/d/l/dluu/mentor/vhdlsym/det_10101_mealy4\ use entity vhdl552.det_10101_mealy(mealy);

-- SIGNAL DECLARATIONS

	signal \in\ : std_logic;
	signal reset : std_logic;
	signal \OUT\ : std_logic;
	signal clk : std_logic;

begin

	\I$415\ : \/u/d/l/dluu/mentor/vhdlsym/det_10101_mealy4\
		port map(
			clk => clk,
			inp => \in\,
			reset => reset,
			outp => \OUT\
		);

end qspro_shadow;


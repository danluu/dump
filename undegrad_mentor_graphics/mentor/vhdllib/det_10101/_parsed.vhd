library ieee;
use ieee.std_logic_1164.all;

entity det_10101 is port (
  signal clk, inp, reset : in std_logic;
  signal outp : out std_logic);
end det_10101;
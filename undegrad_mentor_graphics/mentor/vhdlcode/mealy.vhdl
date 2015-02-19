library ieee;
use ieee.std_logic_1164.all;

entity det_10101_mealy is port (
  signal clk, inp, reset : in std_logic;
  signal outp : out std_logic);
end det_10101_mealy;

architecture mealy of det_10101_mealy is

type state_type is (s0, s1, s2, s3, s4, s5);
signal state, next_state : state_type;
begin  -- cs552

  state_logic:process(state,inp)
  begin
    case state  is
      when s0  =>
      if inp = '1' then
              outp <= '0';
        next_state <= s1;
      else
        outp <= '0';
        next_state <= s0;
      end if;
      when s1  =>
        
      if inp = '1' then
        outp <= '0';
        next_state <= s1;
      else
        outp <= '0';
        next_state <= s2;
      end if;
      when s2  =>
 
      if inp = '1' then
        outp <= '0';
        next_state <= s3;
      else
        outp <= '0';
        next_state <= s0;
      end if;
      when s3  =>

      if inp = '1' then
        outp <= '0';
        next_state <= s1;
      else
        outp <= '0';
        next_state <= s4;
      end if;
      when s4  =>

      if inp = '1' then
        outp <= '0';
        next_state <= s5;
      else
        outp <= '0';
        next_state <= s0;
      end if;
      when s5  =>
      if inp = '1' then
        next_state <= s1;
        outp <= '1';
      else
        outp <= '0';
        next_state <= s4;
      end if;
    end case;
  end process state_logic;

  state_register: process (clk, reset)
  begin  -- process
    if reset = '1' then                 -- asynchronous reset (active high)
      state <= s0;
    elsif clk'event and clk = '1' then  -- rising clock edge
      state <= next_state;

    end if;
  end process state_register;
      
end mealy;

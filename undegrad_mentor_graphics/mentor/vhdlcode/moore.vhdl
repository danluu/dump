library ieee;
use ieee.std_logic_1164.all;

entity det_10101 is port (
  signal clk, inp, reset : in std_logic;
  signal outp : out std_logic);
end det_10101;

architecture cs552 of det_10101 is

type state_type is (s0, s1, s2, s3, s4, s5);
signal state, next_state : state_type;
begin  -- cs552

  state_logic:process(state,inp)
  begin
    case state  is
      when s0  =>
      outp <= '0';
      if inp = '1' then
        next_state <= s1;
      else
        next_state <= s0;
      end if;
      when s1  =>
      outp <= '0';
      if inp = '1' then
        next_state <= s1;
      else
        next_state <= s2;
      end if;
      when s2  =>
      outp <= '0';
      if inp = '1' then
        next_state <= s3;
      else
        next_state <= s0;
      end if;
      when s3  =>
      outp <= '0';
      if inp = '1' then
        next_state <= s1;
      else
        next_state <= s4;
      end if;
      when s4  =>
      outp <= '0';
      if inp = '1' then
        next_state <= s5;
      else
        next_state <= s0;
      end if;
      when s5  =>
      outp <= '1';
      if inp = '1' then
        next_state <= s1;
      else
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
      
end cs552;

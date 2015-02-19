--Memory unit for CS552 Spring 1998
--Final project
--by Phil Atkinson

--CHANGE THE LINES MARKED BELOW TO POINT TO YOUR INPUT AND OUTPUT FILES

library ieee;
use ieee.std_logic_1164.all;
use ieee.math_real.all;
use std.textio.all;


--Define the interface
entity memory_unit4 is port (
   clk, AS, RD, WR, LD, DUMP_SIG:   in std_logic;
   addr:               in std_logic_vector(15 downto 0);
   Data_in:           in std_logic_vector(15 downto 0);   
   Data_out:           out std_logic_vector(15 downto 0);   
   READY:             out std_logic
);
end memory_unit4;

architecture mem1 of memory_unit4 is

begin

   mem_behavior:process(LD, clk, DUMP_SIG, addr, AS, RD, WR)

     subtype memword is bit_vector(15 downto 0);
     type memory_array is array(natural range 0 to ((2**16)-1)) of memword;
     variable store: memory_array;
     variable wait_val: integer;
     variable request: integer := 0;
     variable result: integer := 0;
     variable seed1: integer := 1;
     variable seed2: integer := 10;
     variable clock_time: time;



--Random number for memory delay
     procedure RANDOM(variable s1, s2: inout integer; 
                   variable num: out integer) is
       variable r: real;
       variable n: integer;

     begin
       UNIFORM(s1, s2, r);
       r := r * 10.0;
       r := ROUND(r);
       num := INTEGER(r) rem 4;
     end RANDOM;


     function vec_to_nat(vec: in bit_vector) return natural is
        variable result: natural := 0;

     begin
        for index in vec'range loop
           result := result*2 + bit'pos(vec(index));
        end loop;
        return result;
      end vec_to_nat;

     function natural_to_bv(nat: in natural; length: in natural) return bit_vector is
       variable temp: natural := nat;
       variable result: bit_vector(length-1 downto 0) := (others => '0');
     begin
       for index in result'reverse_range loop
         result(index) := bit'val(temp rem 2);
         temp := temp /2;
         exit when temp = 0;
       end loop;
       return result;
     end natural_to_bv;

     procedure load is
--################Change the path to your file!!!!!!!####################
	file binary_file : text is "/u/d/l/dluu/mentor/vhdlcode/t4.mem";
        variable L: line;
      	variable ch: character;
	variable line_number: natural := 0;
	variable addr: natural;
	variable word: memword;

    	procedure read_hex_natural (L: inout line; n: out natural) is
	  variable result: natural := 0;
	begin
	  for i in 1 to 4 loop
	    read(L, ch);
	    if '0' <= ch and ch <= '9' then
	      result := result*16 + character'pos(ch) - character'pos('0');
	    elsif 'A' <= ch and ch <= 'F' then
	      result := result*16 + character'pos(ch) - character'pos('A') + 10;
	    elsif 'a' <= ch and ch <= 'f' then
	      result := result*16 + character'pos(ch) - character'pos('a') + 10;
	    end if;
	  end loop;
	  n := result;
	end read_hex_natural;

	procedure read_hex_word (L: inout line; word: out memword) is
	  variable digit: natural;
	  variable r: natural := 15;
	begin
   	  for i in 1 to 4 loop
	    read(L, ch);
	    
	    if '0' <= ch and ch <= '9' then
	      digit := character'pos(ch) - character'pos('0');
	    elsif 'A' <= ch and ch <= 'F' then 
 	      digit := character'pos(ch) - character'pos('A') + 10;
	    elsif 'a' <= ch and ch <= 'f' then
	      digit := character'pos(ch) - character'pos('a') + 10;
	    end if;
	   
	    word(r downto r-3) := natural_to_bv(digit, 4);
	    if (r /= 3) then
 		r := r - 4;
	    end if;
	  end loop;
	end read_hex_word;

      begin
        while not endfile(binary_file) loop
	  readline(binary_file, L);
	  line_number := line_number + 1;
	  read_hex_natural(L, addr);
	  read(L, ch);
	  read_hex_word(L, word);
	  store(addr) := word;
        end loop;
      end load;

      procedure do_write is
      begin
        store(vec_to_nat(To_bitvector(addr))) := To_bitvector(Data_in);
        READY <= '1';
      end do_write;

      procedure do_read is
      begin
	 Data_out <= To_X01(store(vec_to_nat(To_bitvector(addr))));
         READY <= '1';
      end do_read;

      procedure do_nothing is
      begin
         READY <= '0';
         Data_out <= "WWWWWWWWWWWWWWWW";
      end do_nothing;


      procedure write_mem is
--########Change the path to your output file too!!!!!      
      file dump: text is out "/u/d/l/dluu/mentor/vhdlcode/outfile4.txt";
      variable outline: line;

      begin

        for i in 0 to 65535 loop 
          if (store(i) /= "0000000000000000") then
	    write (outline, i);
            write (outline, string'(" "));
	    write (outline, store(i));
            writeline (dump, outline);
          end if;
        end loop;
      end write_mem;

  begin	
    
    if rising_edge(LD) then
      load;
    end if;

    if rising_edge(DUMP_SIG) then
      write_mem;
    end if;

--Reset mem when these events occur
    if falling_edge(AS) or falling_edge(RD) or falling_edge(WR) then
      request := 0;
      do_nothing;
    end if;

    if falling_edge(clk) then
      if AS = '1' then

--Check if the address lines changed in the last clock cycle
--if so, then reset the memory to accept another request
	if (addr'last_event <= (now - clock_time)) then
	  request := 0;
	  do_nothing;
        end if;
	
	clock_time := now;

--Check if a new request is there
        if (request = 0 and (RD = '1' or WR = '1')) then
	  request := 1;
	  RANDOM(seed1, seed2, wait_val);
          wait_val := wait_val + 4;
        end if;


--Delay memory from 4-8 cycles
        if wait_val = 0 then
          if RD = '1' then
            do_read;
          elsif WR = '1' then
            do_write;
          end if;
	else
	  wait_val := wait_val - 1;
	end if;
 
      else 
        do_nothing;
      end if;
    end if;
  end process mem_behavior;

end mem1;










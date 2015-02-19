--Cache unit for CS552 Spring 1998
--Final project
--by Phil Atkinson
--Modified on 4/23/97 - Took out do_nothing statment if a write-hit occurs
--			Old code set hit to 0 if a write hit occured.


--CHANGE THE LINE MARKER BELOW TO YOUR OUTPUT FILE

library ieee;
use ieee.std_logic_1164.all;
use std.textio.all;

entity cache_unit is port (
   clk, RW, CA, DUMP_SIG, ENABLE:   in std_logic;
   word:		    in std_logic;
   index:                   in std_logic_vector(7 downto 0);
   tag_in:                  in std_logic_vector(6 downto 0);   
   tag_out:                 out std_logic_vector(6 downto 0);   
   data_in:		    in std_logic_vector(15 downto 0);
   data_out:		    out std_logic_vector(15 downto 0);
   valid, dirty:  	    out std_logic;
   HIT:                     out std_logic
);
end cache_unit;



architecture complete_cache of cache_unit is

  constant NUM_OF_WORDS : natural := 256;

begin

   cache_behavior:process(clk, DUMP_SIG, RW, CA, word)

     subtype memword is bit_vector(15 downto 0);
     type block_array is array(natural range 0 to 1) of memword;


--Define a cacheline as a record
     type cacheline is record
       tag: bit_vector(6 downto 0);
       data: block_array;
       valid: std_logic;
       dirty: std_logic;
     end record;

--A cache is an array of cachelines
     type cache_array is array(natural range 0 to ((2**8) - 1)) of cacheline;

     variable cache_mem: cache_array;
     variable start: natural := 0;

     function vec_to_nat(vec: in bit_vector) return natural is
        variable result: natural := 0;

     begin
        for index in vec'range loop
           result := result*2 + bit'pos(vec(index));
        end loop;
        return result;
      end vec_to_nat;

     function bit_to_nat(b: in std_logic) return natural is
     
     begin
	if b = '0' then
          return 0;
        elsif b = '1' then
          return 1;
        end if;
     end bit_to_nat;

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


   procedure do_nothing is
      begin
         HIT <= '0';
         data_out <= (others => 'W');
         tag_out <= (others => 'W');
	 dirty <= 'W';
      end do_nothing;


--Compare write
      procedure do_write is
	variable index_num: natural := vec_to_nat(To_bitvector(index));
      begin
        cache_mem(index_num).data(bit_to_nat(word)) := To_bitvector(data_in);
        cache_mem(index_num).tag := To_bitvector(tag_in);
	cache_mem(index_num).dirty := '1';
      end do_write;

--Compare read
      procedure do_read is
	variable index_num: natural := vec_to_nat(To_bitvector(index));
      begin
	 data_out <= To_X01(cache_mem(index_num).data(bit_to_nat(word)));
	 dirty <= (cache_mem(index_num).dirty);
	 valid <= (cache_mem(index_num).valid);
      end do_read;

--Access read
      procedure read_mem is
        variable index_num: natural := vec_to_nat(To_bitvector(index));
      begin
        data_out <= To_X01(cache_mem(index_num).data(bit_to_nat(word)));
        tag_out <= To_X01(cache_mem(index_num).tag);
      end read_mem;

--Access write
      procedure write_mem is
        variable index_num: natural := vec_to_nat(To_bitvector(index));
      begin
        cache_mem(index_num).data(bit_to_nat(word)) := To_bitvector(data_in);
        cache_mem(index_num).tag := To_bitvector(tag_in);
	cache_mem(index_num).dirty := '0';
	cache_mem(index_num).valid := '1';
      end write_mem;          

--Check if there's a hit
    procedure compare is
       variable index_num: natural := vec_to_nat(To_bitvector(index));
     begin
     if ((To_X01(cache_mem(index_num).tag) = tag_in) and 
         (cache_mem(index_num).valid = '1')) then
	   hit <= '1';
           if RW = '0' then
             do_read;
           elsif RW = '1' then
             do_write;
           end if;
     else
       do_nothing;
       valid <= cache_mem(index_num).valid;
       dirty <= cache_mem(index_num).dirty;
       hit <= '0';
       end if;
     end compare;

      procedure dump_mem is
--########Change the path to your output file too!!!!!      
      file dump: text is out "/u/d/l/dluu/mentor/vhdlcode/cacheout.txt";
      variable outline: line;

      begin
	write (outline, string'("  Tag      Data"));
        writeline(dump, outline);
	for i in 0 to (NUM_OF_WORDS-1) loop 
          if (cache_mem(i).data(0) /= "0000000000000000") or 
	     (cache_mem(i).data(1) /= "0000000000000000")then
	    write (outline, i);
            write (outline, string'(" "));
            write (outline, cache_mem(i).tag);
            write (outline, string'(" "));
	    write (outline, cache_mem(i).data(0));
            write (outline, string'(" "));
	    write (outline, cache_mem(i).data(1));
            writeline (dump, outline);
          end if;
        end loop;
      end dump_mem;

     procedure clear_cache is

     begin
       for i in 0 to (NUM_OF_WORDS-1) loop
	 cache_mem(i).data(0) := (others => '0');
	 cache_mem(i).data(1) := (others => '0');
	 cache_mem(i).tag  := (others => '0');
	 cache_mem(i).dirty := '0';
	 cache_mem(i).valid := '0';
       end loop;
    end clear_cache;

  begin	

    if start = 0 then
	do_nothing;
	start := 1;
	clear_cache;
    end if;
    
    if rising_edge(DUMP_SIG) then
      dump_mem;
    end if;

    if rising_edge(RW) then
      do_nothing;
    end if;
  
--May need to switch to falling edge to fix timing issues
    if falling_edge(clk) then
      if ENABLE = '1' and CA = '0' then 
          compare;
      elsif ENABLE = '1' and CA = '1' and RW = '0' then
          read_mem;
      elsif ENABLE = '1' and CA = '1' and RW = '1' then
	  do_nothing;
          write_mem;
      else 
        do_nothing;
      end if;
    end if;

  end process cache_behavior;

end complete_cache;

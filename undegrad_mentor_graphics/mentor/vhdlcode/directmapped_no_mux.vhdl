-----------------------------------------------------
-- need to set ready_out, TAG?
-- need to fully reset?
--need to set INDEX? or assume it's hardwired?
--writeback to memory wont work. what is CPU_DATA supposed to control? cache or mem input?

--to use: toggle go signal for one cycle only

--clean miss on read is working correctly

library ieee ;
use ieee.std_logic_1164.all;
use ieee.math_real.all;
use std.textio.all;


-----------------------------------------------------

entity direct is port(	
	clk, ready_in, go, read_i, write_i:		in std_logic;
	addr_out:               out std_logic_vector(15 downto 0);
	addr_in:                in std_logic_vector(15 downto 0);
	debug: out std_logic_vector(15 downto 0);
	reset:		in std_logic;
	AS, RD, WR, LD, ready_out:		out std_logic;
----------------------------------------------------
	HIT, VALID, DIRTY, word_in: in std_logic;
	RW, CA, ENABLE, WORD: out std_logic;
	TAG: out std_logic_vector(6 downto 0); -- tag going out to mem/cache
	tag_back: in std_logic_vector(6 downto 0); -- "TAG_OUT" from cache
	tag_addr: in std_logic_vector(6 downto 0); -- tag bits coming in from CPU
	CPU_DATA: out std_logic -- control which data goes into cache
);
end direct;

-----------------------------------------------------

architecture version1 of direct is

		-- note: many of these states are never used
    type state_type is (IDLE, WAITING, HOLDING, HOLD1, hold_debug, COMPARE, RCM_WRITE0, RCM_WRITE1, RDM_WRITE0, RDM_WRITE1, RCM_WRITEP1, RCM_WRITEP2, RCM_WRITEP3 ,RDM_WRITEP0, RDM_WRITEP1, RCM_READ, WM_WRITE);
    signal next_state, current_state: state_type;
	signal read, write: std_logic;

begin
    
    -- cocurrent process#1: state registers
    state_reg: process(clk, reset, addr_in)
    begin

	if (reset='1') then
            current_state <= IDLE; 
					ENABLE <= '1'; -- always enabled for direct mapped
	else --if (clk'event and clk='1') then
--	    current_state <= next_state;
--	end if; --moved to end to make everything posedge

--    end process;						  

    -- cocurrent process#2: combinational logic
--	comb_logic: process(current_state, go, ready_in)
--	begin

--	if current_state or go then
	case current_state is

		when IDLE =>	 -- debug <= '0';
		if (clk'event and clk='1') then
			ready_out <= '0';
		end if;
		if ((clk'event and clk='1') or (addr_in'event)) then
				addr_out(0) <= '0';
				addr_out(8 downto 1) <= addr_in(8 downto 1);
				addr_out(15 downto 9) <= tag_back;
				TAG <= tag_addr; 
				WORD <= word_in;
		end if;
			if go = '0' then
--				ENABLE <= '0';
			if (clk'event and clk='1') then
				current_state <= IDLE; --next_state <= IDLE;
			end if;
			elsif go ='1' then
			if (clk'event and clk='1') then
				ENABLE <= '1';
				current_state <= COMPARE; --next_state <= COMPARE;
				CA <= '0';
			end if;
				if read_i = '1' then
				if ((clk'event and clk='1') or (addr_in'event)) then
					WORD <= word_in;
					TAG <= tag_addr;
				end if;
				if (clk'event and clk='1') then
					read <= read_i;
					write <= write_i;
					RW <= '0';
				end if;
				end if;
				if write_i = '1' then
				if ((clk'event and clk='1') or (addr_in'event)) then

					WORD <= word_in;
					TAG <= tag_addr;
				end if;
				if (clk'event and clk='1') then
					read <= read_i;
					write <= write_i;
					RW <= '1';
					CPU_DATA <= '1';
				end if;
				end if;
			end if;

	    when COMPARE =>	 -- debug <= '1';
			if read ='1' then 
				if (hit = '1' and valid = '1') then
				if (clk'event and clk='1') then	
					ready_out <= '1';
					current_state <= IDLE; -- next_state <= IDLE;	
				end if; 
				elsif (dirty = '1' and valid = '1') then -- dirty miss 
				if (clk'event and clk='1') then	
					AS <= '1';
					RD <= '0';
					WR <= '1';

					CA <= '1';
					RW <= '0';

					current_state <= RDM_WRITE0; -- next_state <= RDM_WRITE0;
				end if;
				if ((clk'event and clk='1') or (addr_in'event)) then

					
					addr_out(0) <= '0';
					addr_out(8 downto 1) <= addr_in(8 downto 1);
					addr_out(15 downto 9) <= tag_back; 
					TAG <= tag_back;
					CPU_DATA <= '0' ; --might not work
					WORD <= '0';					-- [][][]

				end if;
				elsif dirty = '0' then -- clean miss - need to add TAG <= stuff lines
				if (clk'event and clk='1') then
					AS <= '1';
					RD <= '1';
					WR <= '0'; --1?

					CA <= '1';
					RW <= '0'; --is RW posedge? testing..


					current_state <= RCM_WRITE0; -- next_state <= RCM_WRITE0;
				end if;
				if ((clk'event and clk='1') or (addr_in'event)) then
					addr_out(0) <= '0';
					addr_out(8 downto 1) <= addr_in(8 downto 1);
					addr_out(15 downto 9) <= tag_addr; 
					TAG <= tag_addr;
					WORD <= '0';
					CPU_DATA <= '0';
				end if;
				end if;
			elsif write ='1' then 
				if (hit ='1' and valid = '1') then
				if (clk'event and clk='1') then	
					ready_out <= '1';
					current_state <= IDLE; -- next_state <= IDLE;
				end if;
				elsif (dirty = '1' and valid = '1') then -- dirty miss write
				if (clk'event and clk='1') then	
					AS <= '1';
					RD <= '0';
					WR <= '1';

					current_state <= RDM_WRITE0; -- next_state <= RDM_WRITE0;
				end if;
				if ((clk'event and clk='1') or (addr_in'event)) then

					addr_out(0) <= '0';
					addr_out(8 downto 1) <= addr_in(8 downto 1);
					addr_out(15 downto 9) <= tag_back; 
					CA <= '1';
					RW <= '0';
					TAG <= tag_back;
					WORD <= '0';	
					CPU_DATA <= '0';				

				end if;
				elsif dirty = '0' then -- clean miss write
				if (clk'event and clk='1') then
					AS <= '1';
					RD <= '1';
					WR <= '0';

					CA <= '1';
					RW <= '0';
					current_state <= RCM_WRITE0; -- next_state <= RCM_WRITE0;
				end if;
				if ((clk'event and clk='1') or (addr_in'event)) then
					addr_out(0) <= '0';
					addr_out(8 downto 1) <= addr_in(8 downto 1);
					addr_out(15 downto 9) <= tag_addr; 

					TAG <= tag_addr;
					WORD <= '0';
					CPU_DATA <= '0';
				end if;
				end if;
			end if;
			when RDM_WRITE0 =>	 -- debug <= '1';
			if (clk'event and clk='1') then	
			if ready_in ='0' then 
				current_state <= RDM_WRITE0; -- next_state <= RDM_WRITE0;
			end if;
			elsif ready_in ='1' then
			if (clk'event and clk='1') then	
				current_state <= RDM_WRITE1;
			end if;
			if ((clk'event and clk='1') or (addr_in'event)) then
			   -- next_state <= RDM_WRITE1;
				WORD <= '1';	-- does this cause a write? changing WORD changes ADDR?
				addr_out(0) <= '0';
				addr_out(8 downto 1) <= addr_in(8 downto 1);
				addr_out(15 downto 9) <= tag_back; 
			end if;
			end if;

--			when RDM_WRITEP1 =>
--				RW = '0';
--				next_state <= RDM_WRITE1;

			when RDM_WRITE1 =>	 -- debug <= '1';
			
				if ready_in ='0' then 
				if (clk'event and clk='1') then	
					current_state <= RDM_WRITE1; -- next_state <= RDM_WRITE1;
				end if;
				elsif ready_in ='1' then
				if (clk'event and clk='1') then	
--				if read = '1'; 
--					AS <= '1';
--					RD <= '1';
--					WR <= '1';

--					CA <= '1';
--					RW <= '1'; -- don't need?
--					WORD <= '0';
--					TAG <= tag_addr;
--					current_state <= RCM_WRITE0; -- next_state <= RCM_WRITE0;
--					end if;
--					if write = '1';
--						next_state <= WCM--[][][];
--					end if;

					AS <= '1';
					RD <= '1';
					WR <= '0'; --1?

					CA <= '1';
					RW <= '0'; --is RW posedge? testing..
					current_state <= RCM_WRITE0; -- next_state <= RCM_WRITE0;
					end if;
				if ((clk'event and clk='1') or (addr_in'event)) then
					addr_out(0) <= '0';
					addr_out(8 downto 1) <= addr_in(8 downto 1);
					addr_out(15 downto 9) <= tag_addr; 
					TAG <= tag_addr;
					WORD <= '0';
					CPU_DATA <= '0';
				
					
				end if;
			end if;

--			when RDM_WRITEP2 =>
--				RW = '1';
--				next_state <= RDM_READ;

			when RCM_WRITE0 =>	 -- debug <= '1';
			if (clk'event and clk='1') then	
			if ready_in ='0' then 
				current_state <= RCM_WRITE0; -- next_state <= RCM_WRITE0;
			elsif ready_in ='1' then
--				WORD <= '1';
				RW <= '1';
				current_state <= RCM_WRITEP1; -- next_state <= RCM_WRITE1;

			end if;
			end if;

			when RCM_WRITEP1 =>
			if (clk'event and clk='1') then	
				RW <= '0';
				CPU_DATA <= '0';
				WORD <= '1';
				addr_out(0) <= '1';
				addr_out(8 downto 1) <= addr_in(8 downto 1);
				addr_out(15 downto 9) <= tag_addr; 
				current_state <= RCM_WRITEP2;
			end if;

			when RCM_WRITEP2 =>	 -- debug <= '1';
			if (clk'event and clk='1') then	
			if ready_in ='0' then 
				current_state <= RCM_WRITEP2; -- next_state <= RCM_WRITE0;
			elsif ready_in ='1' then
--				WORD <= '1';
				RW <= '1';
				current_state <= RCM_WRITEP3; -- next_state <= RCM_WRITE1;
			end if;
			end if;

			when RCM_WRITEP3 =>
			if (clk'event and clk='1') then	
				RW <= '0';
				CPU_DATA <= '0';
				WORD <= '1';
				current_state <= RCM_WRITE1;
			end if;


			when RCM_WRITE1 =>	 -- debug <= '1';
			if (clk'event and clk='1') then	
--				RW <= '0';
--				WORD <= '1';
				if ready_in ='0' then 
					current_state <= RCM_WRITE1; -- next_state <= RCM_WRITE1;
				elsif ready_in ='1' then
					if read = '1' then
						RW <= '0';
						CA <= '0';
						WORD <= word_in;
						--CPU_DATA doesn't matter
						TAG <= tag_addr;	
					elsif write = '1' then
						CA <= '0';
						RW <= '1';
						CPU_DATA <= '1';
						WORD <= word_in;
						TAG <= tag_addr;
					end if;
					current_state <= HOLD1; -- next_state <= IDLE;
					--ready_out <= '1'; --too early
					
				end if;
				end if;
			when HOLD1 => -- added hold_debug.. 
			if (clk'event and clk='1') then	
				RW <= '0';
				ready_out <= '1';
				current_state <= IDLE;
			end if;

--			when hold_debug =>
--				ready_out <='1';


--			when RCM_WRITEP2 =>
--				RW <= '1';
--				CPU_DATA <= '0';
--				if read = '1' then 
--					next_state <= RCM_READ;
--				end if;
--				if write ='1' then 
--					next_state <= WM_WRITE;
--				end if;

			when RCM_READ =>
				RW <= '0';
				WORD <= word_in; 
				CA <= '0';
--				RW <= '0'; 				
				current_state <= IDLE; -- next_state <= IDLE;
				ready_out <= '1';

			when WM_WRITE =>
				-- need to write in CPU DATA, not mem data
				-- add signal CPU_DATA that controls a MUX which selects
				-- between the CPU data and MEM data for DATA_IN
				RW <= '1';
				CPU_DATA <= '1';
				WORD <= word_in;
				TAG <= tag_addr;
				CA <= '0';
--				RW <= '1';
				current_state <= IDLE; -- next_state <= IDLE;
				ready_out <= '1';


	    when others =>
--			debug <= '3';
			next_state <= IDLE;
	end case;
--	end if;
	end if;

    end process;

end version1;

-----------------------------------------------------





























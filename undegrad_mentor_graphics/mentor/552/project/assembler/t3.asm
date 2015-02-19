// Program to test the cache for CS 552-2, Spring 2002 .
//
// Test the cache memory system.  This could have two resulting memory
// outputs--one for each type of cache.


// Get the address of MEM.

        andi    r1 0		//r1 = 0
        ori     r1 MEM		//r1 = MEM =30
        addi    r2 r1 0 	//r2 = MEM =30

// Write to MEM+0, MEM+1, MEM+3, MEM+4

        sti     r1 r1 0 	//Mem[MEM]: Mem[30] = 30
        addi    r1 r1 1 	//r1 = Mem+1 = 31
        sti     r1 r1 0		//Mem[MEM+1]: Mem[31] = 31
        addi    r1 r1 2 	//r1 = MEM+3 = 33
        sti	r1 r1 0		//Mem[MEM+3]: Mem[33] = 33
        addi    r1 r1 1 	//r1 = Mem+4 = 34
        sti     r1 r1 0		//Mem[MEM+4]: Mem[34] = 34

// Flush back MEM+0 through MEM+4  (first time)
	
        lui     r7 0x02   	//r7 = 0x0200
			      	// shift to cause a conflict

        add     r1 r2 r7	//r1 = MEM + 0x0200

        sti     r1 r1 0					
        addi    r1 r1 1
        sti     r1 r1 0
        addi    r1 r1 2
        sti     r1 r1 0
        addi    r1 r1 1
        sti     r1 r1 0

// Flush back MEM+0 through MEM+4  (second time--for 2-way cache)

        add     r1 r2 r7	//r1 = MEM + 0x0200
        add     r1 r1 r7	//r1 = MEM + 0x0400

        sti     r1 r1 0
        addi    r1 r1 1
        sti     r1 r1 0
        addi    r1 r1 2
        sti     r1 r1 0
        addi    r1 r1 1
        sti     r1 r1 0

        halt

// MEM must be on a double-word boundary (an even address).

        data    0xffff
MEM:
        data    0x8888         
        data    0x8888         
        data    0x8888         
        data    0x8888         
        data    0x8888         
        data    0x8888         

        data    0xffff


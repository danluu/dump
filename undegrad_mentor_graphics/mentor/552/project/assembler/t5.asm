// Test program 5 for CS 552-2, Spring 2002.
//
// More tests of shift and ALU instructions.
// And test for beqz


// Set up the address and test number for saving after a fail.

        lui     r6 0         // r6 = 0
        ori     r6 RESULT
        lui     r7 0         // r7 = 0
	beqz	r0 START
	halt

// Test a few ALU instructions.
START:
        addi    r7 r7 1         // test 0 + 1 = 1

	lui	r2 0
        xori    r2 0xFF      	// r2 = -1
        subi    r3 r0 1         // r3 = -1
    	sub     r4 r2 r3        // compare r2 and r3
        beqz    r4 OK1
	beqz	r0 FAIL

OK1:
        addi    r7 r7 1         // test 1 + 1 = 2

        addi    r3 r3 1         // r3 = 0
        sub     r4 r0 r3        // compare r0 and r3
	beqz	r4 OK2
        beqz    r0 FAIL


// Test some shift instructions.
OK2:
        addi    r7 r7 1         // test 2 + 1 = 3

        and    	r2 r0 r0       	// r2 = 0
        ori     r2 0x0c         // r2 = 12
        addi    r3 r0 0         // r3 = 0
        ori     r3 0xc0         // r3 = r2 >>(rot.) 12
        rori    r4 r2 0x0c      // r4 = r2 >>(rot.) 12
        sub     r5 r3 r4        // compare r3 and r4
        beqz	r5 OK3
        beqz    r0 FAIL

OK3:
        addi    r7 r7 1         // test 3 + 1 = 4

        addi    r2 r0 1         // r2 = 1
        ror     r2 r2 r2        // r2 = 0x8000
        addi    r1 r2 0         // save 0x8000 for later
        srli    r3 r2 15        // r3 = r2 >> 15 = 1
        subi    r4 r3 1         // compare r3 and 1
        beqz	r4 OK4		
        beqz    r0 FAIL

OK4:
        addi    r7 r7 1         // test 4 + 1 = 5

        or      r2 r1 r0         // r2 = 0x8000
        srai    r2 r2 15        // r2 = -1
        addi    r3 r2 1         // the result should be zero
        beqz	r3 OK5			
        beqz    r0 FAIL

OK5:
        addi    r7 r7 1         // test 5 + 1 = 6

        addi    r4 r1 0         // r4 = 0x8000
        srli    r4 r4 0x0c      // r4 = 0x0008
        subi    r5 r4 0x08      // compare r4 and 0x08
        beqz	r5 OK			
        beqz    r0 FAIL

OK:     addi    r7 r7 1         // test = 7 ==> OK

FAIL:
        sti      r7 r6 0
        sti      r0 r6 1
        sti      r1 r6 2
        sti      r2 r6 3
        sti      r3 r6 4
        sti      r4 r6 5
        sti      r5 r6 6
        sti      r6 r6 7
        sti      r7 r6 8
        halt

        data    0xffff
RESULT:
NUM:    data    0x8888
R0:     data    0x8888
R1:     data    0x8888
R2:     data    0x8888
R3:     data    0x8888
R4:     data    0x8888
R5:     data    0x8888
R6:     data    0x8888
R7:     data    0x8888
        data    0xffff

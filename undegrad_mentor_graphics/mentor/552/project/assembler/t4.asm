// Test program 4 for CS 552-2, Spring 2002.
//
// Test for addt, subt, addm, subm, blez, xor


	addi 	r1 r0 4		//r1 = 4 - counter value
	ori	r2 DATA1	//r2 = DATA1
	ori 	r3 DATA2	//r3 = DATA2
	
LOOP:
	ld	r5 r2 r1	//r5 = Mem[DATA1+r1]
	ld	r6 r3 r1	//r6 = Mem[DATA2+r1]

	lui	r4 0		//r4 = 0
	ori	r4 RESULT1	//r4 = RESULT1
	ld 	r7 r4 r1	//r7 = Mem[RESULT1+r1]	
	addt	r7 r5 r6	//
	st 	r7 r4 r1

	xor	r4 r4 r4	//r4 = 0
	ori	r4 RESULT2	//r4 = RESULT2
	ld	r7 r4 r1	//r7 = Mem[RESULT2+r1]	
	subt	r7 r5 r6
	st	r7 r4 r1

	xor	r4 r4 r4	//r4 = 0
	ori	r4 RESULT3
	add	r4 r4 r1	//get to end of data
	addm	r7 r5 r4	//r7 = r5 + Mem[r4]
	st	r7 r4 r0

	lui	r4 0		//r4 = 0
	ori	r4 RESULT4
	add	r4 r4 r1	//get to end of data
	subm	r7 r5 r4	//r7 = r5 - Mem[r4]
	st	r7 r4 r0

	
	subi	r1 r1 1		//Decrement counter
	sub	r7 r0 r1
	blez	r7 LOOP		//Loop taken 5 times

	
	halt		

	data	0xFFFF

DATA1:	
	data	0x0011
	data 	0x0022
	data	0x0033
	data	0x0044
	data	0x0055
	
	data	0xFFFF

DATA2:	
	data	0x0066
	data 	0x0077
	data	0x0088
	data	0x0099
	data	0x00AA
	
	data	0xFFFF


RESULT1:

	data	0x1000
	data	0x1000
	data	0x1000
	data 	0x1000
	data	0x1000

	data	0xFFFF

RESULT2:

	data	0x2FFF
	data	0x2FFF
	data	0x2FFF
	data 	0x2FFF
	data	0x2FFF

	data	0xFFFF

RESULT3:

	data	0x3000
	data	0x3000
	data	0x3000
	data 	0x3000
	data	0x3000

	data	0xFFFF

RESULT4:

	data	0xC000
	data	0xC000
	data	0xC000
	data 	0xC000
	data	0xC000

	data	0xFFFF




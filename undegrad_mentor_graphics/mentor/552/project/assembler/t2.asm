// Test program 2 for CS 552-2, Spring 2002.
// 
//
// Test for LUI LD ST ADD SUB JALR JR RET HALT
//
// If your design is functioning correctly, it should follow
// the control path and stop at OK

		
			
	lui	r1 0X0F		//r1 = 0x0f00 = 3840	
	ori 	r2 TARGET1	//r2 = TARGET1	= 10
	ori 	r4 0xA		//r4 = 10
	ori 	r5 0x1		//r5 = 1
	add	r6 r4 r0 	//r6 = 10	
	jalr	r7 r2		//Jump to TARGET1
	add     r2 r0 r0	//r2 = 0
	ori     r2 TARGET2 	//r2 = TARGET2 = 24
	jr      r2		//Jump to TARGET2
	halt

			
TARGET1: add 	r6 r6 r4	//r6 = 20	
	 st 	r6 r1 r0	//Mem[0x0F00] = 20
	 sub    r1 r1 r5	//r1 = 0x0EFF
	 lui    r3 0XAB		//r3 = 0xAB00
	 st     r3 r1 r0	//Mem[0x0EFF] = 0xAB00
	 sub    r1 r1 r5	//r1 = 0x0EFE
	 add    r6 r3 r6	//r6 = 0XAB14
         st     r6 r1 r0	//Mem[0x0EFE] = 0xAB14
	 sub    r1 r1 r5	//r1 = 0x0EFD
	 lui    r6 0XBC		//r6 = 0xBC00
	 st     r6 r1 r0	//Mem[0x0EFD] = 0xBC00
         sub    r1 r1 r5	//r1 = 0x0EFC
	 ret			

// Bad Halting point
NOK: 	 halt

TARGET2: lui    r3 0X0F		//r3 = 0x0F00
	 sub    r3 r3 r5	//r3 = 0x0EFF
	 ld     r4 r3 r5	//r4 = Mem[0x0F00] = 20
	 ld     r6 r3 r0	//r6 = Mem[0x0EFF] = 0xAB00
	 st     r4 r1 r0	//Mem[0x0EFC] = 20
         sub    r1 r1 r5	//r1 = 0x0EFB
	 st     r6 r1 r0	//Mem[0x0EFB] = 0xAB00
	 sub    r1 r1 r5	//r1 = 0x0EFA
	 sub    r3 r3 r5	//r3 = 0x0EFE

	 mmove  r1 r3		//Mem[0xEFA] = Mem[0xEFE] = 0xAB14
         sub    r1 r1 r5	//r1 = 0x0EF9
         sub    r3 r3 r5	//r3 = 0x0EFD

	 mmove  r1 r3		//Mem[0x0EF9] = Mem[0x0EFD] = 0XBC00
         sub    r1 r1 r5	//r1 = 0x0EF8
         sub    r3 r3 r5	//r3 = 0x0EFD

	 st     r2 r1 r0	//Mem[0x0EF8] = TARGET2
	 sub    r1 r1 r5 	//r1 = 0x0EF7
	 
	 st     r1 r1 r0	//Mem[0x0EF7] = 0x0EF7
	 sub    r1 r1 r5	//r1 = 0x0Ef6

	 st     r3 r1 r0        //Mem[0x0EF6] = 0x0EFD

// Ok to halt here	
OK:	 halt








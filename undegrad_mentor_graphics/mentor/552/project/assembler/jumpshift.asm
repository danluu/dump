//This program test some of the jump and shift instructions
addi r1 r0 2	//r1 = 2
srl r1 r1 r1	//r1 = 0
ori r1 DATA	//r1 = DATA
xor r2 r2 r2	//r2 = 0

j 5		//Jump to j -4 instruction
halt
halt
jal 6		//r7 = return address, go to PART2
PART5: jal 15	//JAL to PART6
jalr r1 r2	//r1 = return address, go to END
j -4		//Jump to jal 6  instruction
halt
PART4: ret	//go to PART5
halt

PART2: ldi r3 r1 0	//r3 = 0xFEDC
addi r5 r0 15		//r5 = 15		
sra r4 r3 r5		//r4 = 0xFFFF
blez r4 1		//branch to PART3
halt

PART3: srl r3 r4 r5	//r3 = 0x0001
addt r6 r3 r4		//r6 = 0
blez r6 -10		//branch to PART4
halt
halt

PART6: xori r2 0x88	//r2 = 0xFF88
add r6 r1 r3		//r6 = DATA + 1
mmove r6 r1		//Mem[data + 1] = 0xFEDC
st r3 r1 r0		//Mem[DATA] = 0x0001
subt r2 r2 r2		//r2 = -r2
xor r2 r2 r2		//r2 = 0
ori r2 END		//r2 = END
ret			//Return to halt after PART5
j -1			//Loop infinately if program is bad

END: halt

DATA: data 0xFEDC

//this swaps two values using the xor.

lui r1 0
addi r1 r0 DATA	//Load the data location into r1
addi r2 r0 1	//Load offset of 1 into r2
ld r3 r1 r2	//Load data BF65 into r3
ldi r4 r1 0	//Load data 198C into r4
xor r3 r4 r3	//Swap r3 and r4
xor r4 r3 r4
xor r3 r4 r3
lui r5 0	//Load the address to jump to
ori r5 WRITE
jr r5		//jump to WRITE
halt

WRITE:
lui r7 0	//Load address 240
ori r7 240
st r3 r7 r0	//Store R3 in 240
sti r4 r7 1	//Store R4 in 241
halt		//Stop

DATA: data 0x198C
data 0xBF65

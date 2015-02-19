//this tests a number of R-type instructions

lui r1 0
addi r1 r0 DATA
addi r2 r0 1
ld r3 r1 r2
ldi r4 r1 0
add r3 r4 r0
srli  r4 r4 4
andi r4 0x0f
xori r4 0xFF
ror r4 r4 r4
ori r5 WRITE
jr r5
halt

WRITE:
lui r7 0
ori r7 240
st r3 r7 r0
sti r4 r7 1
halt

DATA: data 0x198C
data 0xBF65


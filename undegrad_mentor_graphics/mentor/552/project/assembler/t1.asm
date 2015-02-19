// Test program 1 for CS/ECE 552-2, Spring 2002
//
// This program computes the first N Fibonacci numbers.  The results
// should be stored in the memory, starting at the location pointed to
// by RESULT.
//
// The values stored should be:  0 1 1 2 3 5 8 13 ...
//
// They should start immediately after the value at FOLLOW, which will
// always be 8888.  That makes them easy to find.
//
// This program is not necessarily the best possible.  It does some
// stupid things to test more instruction functionality.  It also
// requires that the input number N be at least 2.
//
// Note:  Fib(10) = 55 base 10 = 37 base 16.
//
// Assembler note:  Because of the way that the assembler interprets the
// lui instruction, labels like "N" and "RESULT" must be in the first
// 256 words of memory in order for their addresses to be loadable.

                                // count up to R1
        andi    r7 0
        ori     r7 N
        ldi      r1 r7 0
                                // start with f0 = 0, f1 = 1
                                // R5 is the count
                                // R6 points at the result
                                // R2 hold the current number

        andi    r7 0	
        ori     r7 RESULT
        ldi	r6 r7 0

        andi    r2 0
        sti      r2 r6 0
        addi    r2 r2 1
        sti      r2 r6 1
        addi    r6 r6 2
        andi    r5 0
        ori     r5 1
LOOP:
                                // compute the next number
        ldi      r3 r6 -2
        add     r2 r2 r3
                                // save it
        sti      r2 r6 0
                                // increment pointer and count
        addi    r6 r6 1
        addi    r5 r5 1
                                // test for end of loop
        sub     r4 r5 r1
	bltz r4 LOOP
	
        halt                    // Done.

N:      data    10              // Find this Fibonacci number.
FOLLOW: data    0x8888
RESULT: data    0xabcd          // The result.

// End.

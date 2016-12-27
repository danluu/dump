	.section	__TEXT,__text,regular,pure_instructions
	.macosx_version_min 10, 11
	.intel_syntax noprefix
	.section	__TEXT,__literal8,8byte_literals
	.align	3
LCPI0_0:
	.quad	4741671816366391296     ## double 1.0E+9
	.section	__TEXT,__text,regular,pure_instructions
	.globl	_main
	.align	4, 0x90
_main:                                  ## @main
	.cfi_startproc
## BB#0:
	push	rbp
Ltmp0:
	.cfi_def_cfa_offset 16
Ltmp1:
	.cfi_offset rbp, -16
	mov	rbp, rsp
Ltmp2:
	.cfi_def_cfa_register rbp
	xor	edi, edi
	call	_time
	rdtsc
	mov	rsi, rdx
	shl	rsi, 32
	or	rsi, rax
	rdtsc
	mov	rcx, rdx
	shl	rcx, 32
	or	rcx, rax
	sub	rcx, rsi
	cvtsi2sd	xmm0, rcx
	mov	rax, qword ptr [rip + ___stdoutp@GOTPCREL]
	mov	rdi, qword ptr [rax]
	divsd	xmm0, qword ptr [rip + LCPI0_0]
	lea	rsi, [rip + L_.str]
	mov	edx, 1000000000
	mov	al, 1
	call	_fprintf
	xor	eax, eax
	pop	rbp
	ret
	.cfi_endproc

	.section	__TEXT,__cstring,cstring_literals
L_.str:                                 ## @.str
	.asciz	"%d iterations, %lld cycles, %4.2f cycles/iteration\n"


.subsections_via_symbols

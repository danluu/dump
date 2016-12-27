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
	push	r15
	push	r14
	push	r12
	push	rbx
Ltmp3:
	.cfi_offset rbx, -48
Ltmp4:
	.cfi_offset r12, -40
Ltmp5:
	.cfi_offset r14, -32
Ltmp6:
	.cfi_offset r15, -24
	xor	edi, edi
	call	_time
	mov	r15, rax
	rdtsc
	mov	rcx, rdx
	shl	rcx, 32
	or	rcx, rax
	movzx	eax, r15b
	imul	r14, rax, 1000000000
	rdtsc
	mov	rbx, rdx
	shl	rbx, 32
	or	rbx, rax
	sub	rbx, rcx
	cvtsi2sd	xmm0, rbx
	mov	r12, qword ptr [rip + ___stdoutp@GOTPCREL]
	mov	rdi, qword ptr [r12]
	divsd	xmm0, qword ptr [rip + LCPI0_0]
	lea	rsi, [rip + L_.str]
	mov	edx, 1000000000
	mov	al, 1
	mov	rcx, rbx
	call	_fprintf
	mov	rdi, qword ptr [r12]
	lea	rsi, [rip + L_.str.1]
	xor	eax, eax
	mov	rdx, r15
	mov	rcx, r14
	call	_fprintf
	xor	eax, eax
	pop	rbx
	pop	r12
	pop	r14
	pop	r15
	pop	rbp
	ret
	.cfi_endproc

	.section	__TEXT,__cstring,cstring_literals
L_.str:                                 ## @.str
	.asciz	"%d iterations, %lld cycles, %4.2f cycles/iteration\n"

L_.str.1:                               ## @.str.1
	.asciz	"%lu %llu\n"


.subsections_via_symbols

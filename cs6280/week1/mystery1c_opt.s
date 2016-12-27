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
	push	rbx
	push	rax
Ltmp3:
	.cfi_offset rbx, -40
Ltmp4:
	.cfi_offset r14, -32
Ltmp5:
	.cfi_offset r15, -24
	xor	ebx, ebx
	xor	edi, edi
	call	_time
	mov	r14, rax
	movzx	eax, r14b
	mov	dword ptr [rbp - 28], eax
	rdtsc
	mov	rsi, rdx
	shl	rsi, 32
	or	rsi, rax
	mov	eax, 1000000000
	.align	4, 0x90
LBB0_1:                                 ## =>This Inner Loop Header: Depth=1
	movsxd	rcx, dword ptr [rbp - 28]
	add	rcx, rbx
	movsxd	rdx, dword ptr [rbp - 28]
	add	rdx, rcx
	movsxd	rcx, dword ptr [rbp - 28]
	add	rcx, rdx
	movsxd	rdx, dword ptr [rbp - 28]
	add	rdx, rcx
	movsxd	rbx, dword ptr [rbp - 28]
	add	rbx, rdx
	add	eax, -5
	jne	LBB0_1
## BB#2:
	rdtsc
	mov	rcx, rdx
	shl	rcx, 32
	or	rcx, rax
	sub	rcx, rsi
	cvtsi2sd	xmm0, rcx
	mov	r15, qword ptr [rip + ___stdoutp@GOTPCREL]
	mov	rdi, qword ptr [r15]
	divsd	xmm0, qword ptr [rip + LCPI0_0]
	lea	rsi, [rip + L_.str]
	mov	edx, 1000000000
	mov	al, 1
	call	_fprintf
	mov	rdi, qword ptr [r15]
	lea	rsi, [rip + L_.str.1]
	xor	eax, eax
	mov	rdx, r14
	mov	rcx, rbx
	call	_fprintf
	xor	eax, eax
	add	rsp, 8
	pop	rbx
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

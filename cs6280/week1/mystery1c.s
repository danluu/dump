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
	sub	rsp, 96
	xor	eax, eax
	mov	ecx, eax
	mov	dword ptr [rbp - 4], 0
	mov	dword ptr [rbp - 8], edi
	mov	qword ptr [rbp - 16], rsi
	mov	qword ptr [rbp - 40], 0
	mov	rdi, rcx
	call	_time
	mov	qword ptr [rbp - 48], rax
	mov	rax, qword ptr [rbp - 48]
	and	rax, 255
	mov	edx, eax
	mov	dword ptr [rbp - 52], edx
	rdtsc
	shl	rdx, 32
	or	rax, rdx
	mov	qword ptr [rbp - 24], rax
	mov	dword ptr [rbp - 56], 0
LBB0_1:                                 ## =>This Inner Loop Header: Depth=1
	cmp	dword ptr [rbp - 56], 1000000000
	jge	LBB0_4
## BB#2:                                ##   in Loop: Header=BB0_1 Depth=1
	mov	eax, dword ptr [rbp - 52]
	movsxd	rcx, eax
	add	rcx, qword ptr [rbp - 40]
	mov	qword ptr [rbp - 40], rcx
## BB#3:                                ##   in Loop: Header=BB0_1 Depth=1
	mov	eax, dword ptr [rbp - 56]
	add	eax, 1
	mov	dword ptr [rbp - 56], eax
	jmp	LBB0_1
LBB0_4:
	lea	rsi, [rip + L_.str]
	mov	edx, 1000000000
	movsd	xmm0, qword ptr [rip + LCPI0_0] ## xmm0 = mem[0],zero
	mov	rax, qword ptr [rip + ___stdoutp@GOTPCREL]
	mov	qword ptr [rbp - 80], rax ## 8-byte Spill
	mov	dword ptr [rbp - 84], edx ## 4-byte Spill
	rdtsc
	shl	rdx, 32
	or	rax, rdx
	mov	qword ptr [rbp - 32], rax
	mov	rax, qword ptr [rbp - 32]
	sub	rax, qword ptr [rbp - 24]
	mov	qword ptr [rbp - 64], rax
	cvtsi2sd	xmm1, qword ptr [rbp - 64]
	movsd	qword ptr [rbp - 72], xmm1
	mov	rax, qword ptr [rbp - 80] ## 8-byte Reload
	mov	rdi, qword ptr [rax]
	mov	rcx, qword ptr [rbp - 64]
	movsd	xmm1, qword ptr [rbp - 72] ## xmm1 = mem[0],zero
	divsd	xmm1, xmm0
	mov	edx, dword ptr [rbp - 84] ## 4-byte Reload
	movaps	xmm0, xmm1
	mov	al, 1
	call	_fprintf
	lea	rsi, [rip + L_.str.1]
	mov	rcx, qword ptr [rip + ___stdoutp@GOTPCREL]
	mov	rdi, qword ptr [rcx]
	mov	rdx, qword ptr [rbp - 48]
	mov	rcx, qword ptr [rbp - 40]
	mov	dword ptr [rbp - 88], eax ## 4-byte Spill
	mov	al, 0
	call	_fprintf
	xor	r8d, r8d
	mov	dword ptr [rbp - 92], eax ## 4-byte Spill
	mov	eax, r8d
	add	rsp, 96
	pop	rbp
	ret
	.cfi_endproc

	.section	__TEXT,__cstring,cstring_literals
L_.str:                                 ## @.str
	.asciz	"%d iterations, %lld cycles, %4.2f cycles/iteration\n"

L_.str.1:                               ## @.str.1
	.asciz	"%lu %llu\n"


.subsections_via_symbols

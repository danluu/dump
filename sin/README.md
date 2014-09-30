~~~
0000000000403580 <__sin_sse2>:
  403580:	41 54                	push   %r12
  403582:	66 0f 28 d0          	movapd %xmm0,%xmm2
  403586:	55                   	push   %rbp
  403587:	53                   	push   %rbx
  403588:	48 83 ec 60          	sub    $0x60,%rsp
  40358c:	0f ae 5c 24 40       	stmxcsr 0x40(%rsp)
  403591:	8b 5c 24 40          	mov    0x40(%rsp),%ebx
  403595:	89 d8                	mov    %ebx,%eax
  403597:	80 e4 9f             	and    $0x9f,%ah
  40359a:	39 c3                	cmp    %eax,%ebx
  40359c:	89 44 24 50          	mov    %eax,0x50(%rsp)
  4035a0:	0f 85 5a 1c 00 00    	jne    405200 <__sin_sse2+0x1c80>
  4035a6:	31 ed                	xor    %ebp,%ebp
  4035a8:	f2 0f 11 14 24       	movsd  %xmm2,(%rsp)
  4035ad:	48 8b 14 24          	mov    (%rsp),%rdx
  4035b1:	48 89 d1             	mov    %rdx,%rcx
  4035b4:	48 c1 f9 20          	sar    $0x20,%rcx
  4035b8:	89 c8                	mov    %ecx,%eax
  4035ba:	25 ff ff ff 7f       	and    $0x7fffffff,%eax
  4035bf:	3d ff ff 4f 3e       	cmp    $0x3e4fffff,%eax
  4035c4:	0f 8e 96 00 00 00    	jle    403660 <__sin_sse2+0xe0>
  4035ca:	3d ff ff cf 3f       	cmp    $0x3fcfffff,%eax
  4035cf:	0f 8f ab 00 00 00    	jg     403680 <__sin_sse2+0x100>
  4035d5:	66 0f 28 e2          	movapd %xmm2,%xmm4
  4035d9:	f2 0f 10 05 77 58 0a 	movsd  0xa5877(%rip),%xmm0        # 4a8e58 <_IO_stdin_used+0x18>
  4035e0:	00 
  4035e1:	66 0f 28 ea          	movapd %xmm2,%xmm5
  4035e5:	f2 0f 59 e2          	mulsd  %xmm2,%xmm4
  4035e9:	f2 0f 59 c4          	mulsd  %xmm4,%xmm0
  4035ed:	66 0f 28 cc          	movapd %xmm4,%xmm1
  4035f1:	f2 0f 59 ca          	mulsd  %xmm2,%xmm1
  4035f5:	f2 0f 58 05 63 58 0a 	addsd  0xa5863(%rip),%xmm0        # 4a8e60 <_IO_stdin_used+0x20>
  4035fc:	00 
  4035fd:	f2 0f 59 c4          	mulsd  %xmm4,%xmm0
  403601:	f2 0f 5c 05 5f 58 0a 	subsd  0xa585f(%rip),%xmm0        # 4a8e68 <_IO_stdin_used+0x28>
  403608:	00 
  403609:	f2 0f 59 c4          	mulsd  %xmm4,%xmm0
  40360d:	f2 0f 58 05 5b 58 0a 	addsd  0xa585b(%rip),%xmm0        # 4a8e70 <_IO_stdin_used+0x30>
  403614:	00 
  403615:	f2 0f 59 c4          	mulsd  %xmm4,%xmm0
  403619:	66 0f 28 d8          	movapd %xmm0,%xmm3
  40361d:	f2 0f 5c 1d 33 59 0a 	subsd  0xa5933(%rip),%xmm3        # 4a8f58 <hp1+0x10>
  403624:	00 
  403625:	f2 0f 59 d9          	mulsd  %xmm1,%xmm3
  403629:	66 0f 28 ca          	movapd %xmm2,%xmm1
  40362d:	f2 0f 58 eb          	addsd  %xmm3,%xmm5
  403631:	f2 0f 5c cd          	subsd  %xmm5,%xmm1
  403635:	f2 0f 58 cb          	addsd  %xmm3,%xmm1
  403639:	f2 0f 59 0d 5f 59 0a 	mulsd  0xa595f(%rip),%xmm1        # 4a8fa0 <hp1+0x58>
  403640:	00 
  403641:	f2 0f 58 cd          	addsd  %xmm5,%xmm1
  403645:	66 0f 2e cd          	ucomisd %xmm5,%xmm1
  403649:	0f 8a f9 02 00 00    	jp     403948 <__sin_sse2+0x3c8>
  40364f:	0f 85 f3 02 00 00    	jne    403948 <__sin_sse2+0x3c8>
  403655:	66 0f 28 d5          	movapd %xmm5,%xmm2
  403659:	0f 1f 80 00 00 00 00 	nopl   0x0(%rax)
  403660:	40 84 ed             	test   %bpl,%bpl
  403663:	0f 85 a6 1b 00 00    	jne    40520f <__sin_sse2+0x1c8f>
  403669:	48 83 c4 60          	add    $0x60,%rsp
  40366d:	66 0f 28 c2          	movapd %xmm2,%xmm0
  403671:	5b                   	pop    %rbx
  403672:	5d                   	pop    %rbp
  403673:	41 5c                	pop    %r12
  403675:	c3                   	retq   
  403676:	66 2e 0f 1f 84 00 00 	nopw   %cs:0x0(%rax,%rax,1)
  40367d:	00 00 00 
  403680:	3d ff 5f eb 3f       	cmp    $0x3feb5fff,%eax
  403685:	0f 8f 3d 01 00 00    	jg     4037c8 <__sin_sse2+0x248>
  40368b:	85 c9                	test   %ecx,%ecx
  40368d:	f2 44 0f 10 0d 5a 58 	movsd  0xa585a(%rip),%xmm9        # 4a8ef0 <big>
  403694:	0a 00 
  403696:	0f 8e f4 08 00 00    	jle    403f90 <__sin_sse2+0xa10>
  40369c:	66 0f 28 ca          	movapd %xmm2,%xmm1
  4036a0:	66 0f 28 fa          	movapd %xmm2,%xmm7
  4036a4:	f2 41 0f 58 c9       	addsd  %xmm9,%xmm1
  4036a9:	66 0f 28 c1          	movapd %xmm1,%xmm0
  4036ad:	f2 41 0f 5c c1       	subsd  %xmm9,%xmm0
  4036b2:	f2 0f 5c f8          	subsd  %xmm0,%xmm7
  4036b6:	66 0f 28 c7          	movapd %xmm7,%xmm0
  4036ba:	f2 0f 11 0c 24       	movsd  %xmm1,(%rsp)
  4036bf:	66 0f 28 c8          	movapd %xmm0,%xmm1
  4036c3:	f2 0f 10 2d 2d 58 0a 	movsd  0xa582d(%rip),%xmm5        # 4a8ef8 <big+0x8>
  4036ca:	00 
  4036cb:	48 8b 14 24          	mov    (%rsp),%rdx
  4036cf:	f2 0f 59 c8          	mulsd  %xmm0,%xmm1
  4036d3:	66 0f 28 d8          	movapd %xmm0,%xmm3
  4036d7:	f2 0f 10 25 21 58 0a 	movsd  0xa5821(%rip),%xmm4        # 4a8f00 <big+0x10>
  4036de:	00 
  4036df:	f2 44 0f 10 05 28 58 	movsd  0xa5828(%rip),%xmm8        # 4a8f10 <big+0x20>
  4036e6:	0a 00 
  4036e8:	c1 e2 02             	shl    $0x2,%edx
  4036eb:	f2 0f 10 3d 25 58 0a 	movsd  0xa5825(%rip),%xmm7        # 4a8f18 <big+0x28>
  4036f2:	00 
  4036f3:	48 63 c2             	movslq %edx,%rax
  4036f6:	66 0f 28 f1          	movapd %xmm1,%xmm6
  4036fa:	f2 0f 59 d9          	mulsd  %xmm1,%xmm3
  4036fe:	f2 44 0f 10 14 c5 00 	movsd  0x4a9a00(,%rax,8),%xmm10
  403705:	9a 4a 00 
  403708:	8d 42 01             	lea    0x1(%rdx),%eax
  40370b:	f2 0f 59 f5          	mulsd  %xmm5,%xmm6
  40370f:	48 98                	cltq   
  403711:	f2 44 0f 10 1c c5 00 	movsd  0x4a9a00(,%rax,8),%xmm11
  403718:	9a 4a 00 
  40371b:	8d 42 02             	lea    0x2(%rdx),%eax
  40371e:	83 c2 03             	add    $0x3,%edx
  403721:	48 63 d2             	movslq %edx,%rdx
  403724:	85 c9                	test   %ecx,%ecx
  403726:	f2 0f 5c f4          	subsd  %xmm4,%xmm6
  40372a:	48 98                	cltq   
  40372c:	f2 44 0f 10 24 c5 00 	movsd  0x4a9a00(,%rax,8),%xmm12
  403733:	9a 4a 00 
  403736:	f2 0f 59 de          	mulsd  %xmm6,%xmm3
  40373a:	f2 0f 10 35 de 57 0a 	movsd  0xa57de(%rip),%xmm6        # 4a8f20 <big+0x30>
  403741:	00 
  403742:	f2 0f 58 d8          	addsd  %xmm0,%xmm3
  403746:	66 0f 28 c1          	movapd %xmm1,%xmm0
  40374a:	f2 41 0f 59 c0       	mulsd  %xmm8,%xmm0
  40374f:	f2 0f 5c c7          	subsd  %xmm7,%xmm0
  403753:	f2 0f 59 c1          	mulsd  %xmm1,%xmm0
  403757:	f2 0f 58 c6          	addsd  %xmm6,%xmm0
  40375b:	f2 0f 59 c1          	mulsd  %xmm1,%xmm0
  40375f:	f2 0f 10 0c d5 00 9a 	movsd  0x4a9a00(,%rdx,8),%xmm1
  403766:	4a 00 
  403768:	0f 8e 02 08 00 00    	jle    403f70 <__sin_sse2+0x9f0>
  40376e:	f2 0f 59 cb          	mulsd  %xmm3,%xmm1
  403772:	f2 41 0f 59 c2       	mulsd  %xmm10,%xmm0
  403777:	f2 41 0f 59 dc       	mulsd  %xmm12,%xmm3
  40377c:	f2 41 0f 58 cb       	addsd  %xmm11,%xmm1
  403781:	f2 0f 5c c8          	subsd  %xmm0,%xmm1
  403785:	66 41 0f 28 c2       	movapd %xmm10,%xmm0
  40378a:	f2 0f 58 cb          	addsd  %xmm3,%xmm1
  40378e:	66 41 0f 28 da       	movapd %xmm10,%xmm3
  403793:	f2 0f 58 d9          	addsd  %xmm1,%xmm3
  403797:	f2 0f 5c c3          	subsd  %xmm3,%xmm0
  40379b:	f2 0f 58 c1          	addsd  %xmm1,%xmm0
  40379f:	f2 0f 59 05 09 58 0a 	mulsd  0xa5809(%rip),%xmm0        # 4a8fb0 <hp1+0x68>
  4037a6:	00 
  4037a7:	f2 0f 58 c3          	addsd  %xmm3,%xmm0
  4037ab:	66 0f 2e c3          	ucomisd %xmm3,%xmm0
  4037af:	0f 8a 2b 06 00 00    	jp     403de0 <__sin_sse2+0x860>
  4037b5:	0f 85 25 06 00 00    	jne    403de0 <__sin_sse2+0x860>
  4037bb:	66 0f 28 d3          	movapd %xmm3,%xmm2
  4037bf:	e9 9c fe ff ff       	jmpq   403660 <__sin_sse2+0xe0>
  4037c4:	0f 1f 40 00          	nopl   0x0(%rax)
  4037c8:	3d fc 68 03 40       	cmp    $0x400368fc,%eax
  4037cd:	0f 8f 85 02 00 00    	jg     403a58 <__sin_sse2+0x4d8>
  4037d3:	85 c9                	test   %ecx,%ecx
  4037d5:	f2 44 0f 10 25 62 57 	movsd  0xa5762(%rip),%xmm12        # 4a8f40 <hp0>
  4037dc:	0a 00 
  4037de:	0f 8e eb 05 00 00    	jle    403dcf <__sin_sse2+0x84f>
  4037e4:	66 41 0f 28 c4       	movapd %xmm12,%xmm0
  4037e9:	f2 0f 5c c2          	subsd  %xmm2,%xmm0
  4037ed:	66 0f 57 db          	xorpd  %xmm3,%xmm3
  4037f1:	f2 44 0f 10 0d f6 56 	movsd  0xa56f6(%rip),%xmm9        # 4a8ef0 <big>
  4037f8:	0a 00 
  4037fa:	66 0f 2e c3          	ucomisd %xmm3,%xmm0
  4037fe:	0f 82 b4 09 00 00    	jb     4041b8 <__sin_sse2+0xc38>
  403804:	66 0f 28 c8          	movapd %xmm0,%xmm1
  403808:	f2 41 0f 58 c9       	addsd  %xmm9,%xmm1
  40380d:	66 0f 28 e1          	movapd %xmm1,%xmm4
  403811:	f2 41 0f 5c e1       	subsd  %xmm9,%xmm4
  403816:	f2 0f 5c c4          	subsd  %xmm4,%xmm0
  40381a:	f2 0f 58 05 26 57 0a 	addsd  0xa5726(%rip),%xmm0        # 4a8f48 <hp1>
  403821:	00 
  403822:	66 44 0f 28 d8       	movapd %xmm0,%xmm11
  403827:	f2 0f 11 0c 24       	movsd  %xmm1,(%rsp)
  40382c:	f2 0f 10 2d c4 56 0a 	movsd  0xa56c4(%rip),%xmm5        # 4a8ef8 <big+0x8>
  403833:	00 
  403834:	48 8b 14 24          	mov    (%rsp),%rdx
  403838:	f2 44 0f 59 d8       	mulsd  %xmm0,%xmm11
  40383d:	66 44 0f 28 d0       	movapd %xmm0,%xmm10
  403842:	f2 0f 10 25 b6 56 0a 	movsd  0xa56b6(%rip),%xmm4        # 4a8f00 <big+0x10>
  403849:	00 
  40384a:	c1 e2 02             	shl    $0x2,%edx
  40384d:	f2 44 0f 10 05 ba 56 	movsd  0xa56ba(%rip),%xmm8        # 4a8f10 <big+0x20>
  403854:	0a 00 
  403856:	8d 72 01             	lea    0x1(%rdx),%esi
  403859:	8d 42 02             	lea    0x2(%rdx),%eax
  40385c:	66 41 0f 28 cb       	movapd %xmm11,%xmm1
  403861:	f2 45 0f 59 d3       	mulsd  %xmm11,%xmm10
  403866:	48 63 f6             	movslq %esi,%rsi
  403869:	48 98                	cltq   
  40386b:	f2 0f 59 cd          	mulsd  %xmm5,%xmm1
  40386f:	f2 44 0f 10 2c c5 00 	movsd  0x4a9a00(,%rax,8),%xmm13
  403876:	9a 4a 00 
  403879:	8d 42 03             	lea    0x3(%rdx),%eax
  40387c:	48 63 d2             	movslq %edx,%rdx
  40387f:	f2 0f 10 3d 91 56 0a 	movsd  0xa5691(%rip),%xmm7        # 4a8f18 <big+0x28>
  403886:	00 
  403887:	48 98                	cltq   
  403889:	f2 0f 10 35 8f 56 0a 	movsd  0xa568f(%rip),%xmm6        # 4a8f20 <big+0x30>
  403890:	00 
  403891:	f2 0f 5c cc          	subsd  %xmm4,%xmm1
  403895:	f2 44 0f 59 d1       	mulsd  %xmm1,%xmm10
  40389a:	f2 0f 10 0c c5 00 9a 	movsd  0x4a9a00(,%rax,8),%xmm1
  4038a1:	4a 00 
  4038a3:	f2 44 0f 58 d0       	addsd  %xmm0,%xmm10
  4038a8:	f2 0f 10 04 f5 00 9a 	movsd  0x4a9a00(,%rsi,8),%xmm0
  4038af:	4a 00 
  4038b1:	f2 41 0f 59 c2       	mulsd  %xmm10,%xmm0
  4038b6:	f2 44 0f 59 14 d5 00 	mulsd  0x4a9a00(,%rdx,8),%xmm10
  4038bd:	9a 4a 00 
  4038c0:	f2 0f 5c c8          	subsd  %xmm0,%xmm1
  4038c4:	66 41 0f 28 c3       	movapd %xmm11,%xmm0
  4038c9:	f2 41 0f 59 c0       	mulsd  %xmm8,%xmm0
  4038ce:	f2 0f 5c c7          	subsd  %xmm7,%xmm0
  4038d2:	f2 41 0f 59 c3       	mulsd  %xmm11,%xmm0
  4038d7:	f2 0f 58 c6          	addsd  %xmm6,%xmm0
  4038db:	f2 41 0f 59 c3       	mulsd  %xmm11,%xmm0
  4038e0:	f2 41 0f 59 c5       	mulsd  %xmm13,%xmm0
  4038e5:	f2 0f 5c c8          	subsd  %xmm0,%xmm1
  4038e9:	66 41 0f 28 c5       	movapd %xmm13,%xmm0
  4038ee:	f2 41 0f 5c ca       	subsd  %xmm10,%xmm1
  4038f3:	66 45 0f 28 d5       	movapd %xmm13,%xmm10
  4038f8:	f2 44 0f 58 d1       	addsd  %xmm1,%xmm10
  4038fd:	f2 41 0f 5c c2       	subsd  %xmm10,%xmm0
  403902:	f2 0f 58 c1          	addsd  %xmm1,%xmm0
  403906:	f2 0f 59 05 2a 56 0a 	mulsd  0xa562a(%rip),%xmm0        # 4a8f38 <big+0x48>
  40390d:	00 
  40390e:	f2 41 0f 58 c2       	addsd  %xmm10,%xmm0
  403913:	66 41 0f 2e c2       	ucomisd %xmm10,%xmm0
  403918:	0f 8a b2 06 00 00    	jp     403fd0 <__sin_sse2+0xa50>
  40391e:	0f 85 ac 06 00 00    	jne    403fd0 <__sin_sse2+0xa50>
  403924:	85 c9                	test   %ecx,%ecx
  403926:	66 41 0f 28 d2       	movapd %xmm10,%xmm2
  40392b:	0f 8f 2f fd ff ff    	jg     403660 <__sin_sse2+0xe0>
  403931:	f2 0f 10 05 87 56 0a 	movsd  0xa5687(%rip),%xmm0        # 4a8fc0 <hp1+0x78>
  403938:	00 
  403939:	66 0f 57 d0          	xorpd  %xmm0,%xmm2
  40393d:	e9 1e fd ff ff       	jmpq   403660 <__sin_sse2+0xe0>
  403942:	66 0f 1f 44 00 00    	nopw   0x0(%rax,%rax,1)
  403948:	f2 0f 10 0d f8 54 0a 	movsd  0xa54f8(%rip),%xmm1        # 4a8e48 <_IO_stdin_used+0x8>
  40394f:	00 
  403950:	f2 0f 58 05 20 55 0a 	addsd  0xa5520(%rip),%xmm0        # 4a8e78 <_IO_stdin_used+0x38>
  403957:	00 
  403958:	66 0f 28 ea          	movapd %xmm2,%xmm5
  40395c:	f2 44 0f 10 05 eb 54 	movsd  0xa54eb(%rip),%xmm8        # 4a8e50 <_IO_stdin_used+0x10>
  403963:	0a 00 
  403965:	66 0f 28 fa          	movapd %xmm2,%xmm7
  403969:	f2 0f 58 e9          	addsd  %xmm1,%xmm5
  40396d:	66 0f 57 db          	xorpd  %xmm3,%xmm3
  403971:	f2 0f 59 c4          	mulsd  %xmm4,%xmm0
  403975:	66 41 0f 28 e0       	movapd %xmm8,%xmm4
  40397a:	f2 0f 5c e9          	subsd  %xmm1,%xmm5
  40397e:	66 0f 28 ca          	movapd %xmm2,%xmm1
  403982:	66 0f 28 f5          	movapd %xmm5,%xmm6
  403986:	f2 0f 5c fd          	subsd  %xmm5,%xmm7
  40398a:	f2 41 0f 59 f0       	mulsd  %xmm8,%xmm6
  40398f:	f2 0f 58 fb          	addsd  %xmm3,%xmm7
  403993:	f2 0f 59 f5          	mulsd  %xmm5,%xmm6
  403997:	f2 0f 59 e7          	mulsd  %xmm7,%xmm4
  40399b:	f2 0f 59 f5          	mulsd  %xmm5,%xmm6
  40399f:	f2 0f 59 2d d9 54 0a 	mulsd  0xa54d9(%rip),%xmm5        # 4a8e80 <_IO_stdin_used+0x40>
  4039a6:	00 
  4039a7:	f2 0f 59 e7          	mulsd  %xmm7,%xmm4
  4039ab:	f2 0f 58 ce          	addsd  %xmm6,%xmm1
  4039af:	f2 0f 59 ef          	mulsd  %xmm7,%xmm5
  4039b3:	f2 0f 59 e7          	mulsd  %xmm7,%xmm4
  4039b7:	f2 0f 58 c5          	addsd  %xmm5,%xmm0
  4039bb:	f2 0f 59 c2          	mulsd  %xmm2,%xmm0
  4039bf:	f2 0f 58 c4          	addsd  %xmm4,%xmm0
  4039c3:	66 0f 28 e2          	movapd %xmm2,%xmm4
  4039c7:	f2 0f 5c e1          	subsd  %xmm1,%xmm4
  4039cb:	f2 0f 58 c3          	addsd  %xmm3,%xmm0
  4039cf:	f2 0f 58 e6          	addsd  %xmm6,%xmm4
  4039d3:	f2 0f 58 c4          	addsd  %xmm4,%xmm0
  4039d7:	66 0f 28 e1          	movapd %xmm1,%xmm4
  4039db:	f2 0f 58 e0          	addsd  %xmm0,%xmm4
  4039df:	f2 0f 5c cc          	subsd  %xmm4,%xmm1
  4039e3:	f2 0f 58 c8          	addsd  %xmm0,%xmm1
  4039e7:	f2 0f 59 0d b9 55 0a 	mulsd  0xa55b9(%rip),%xmm1        # 4a8fa8 <hp1+0x60>
  4039ee:	00 
  4039ef:	f2 0f 58 cc          	addsd  %xmm4,%xmm1
  4039f3:	66 0f 2e e1          	ucomisd %xmm1,%xmm4
  4039f7:	0f 8b c3 03 00 00    	jnp    403dc0 <__sin_sse2+0x840>
  4039fd:	66 0f 2e d3          	ucomisd %xmm3,%xmm2
  403a01:	0f 86 00 08 00 00    	jbe    404207 <__sin_sse2+0xc87>
  403a07:	66 0f 28 cb          	movapd %xmm3,%xmm1
  403a0b:	48 8d 7c 24 50       	lea    0x50(%rsp),%rdi
  403a10:	66 0f 28 c2          	movapd %xmm2,%xmm0
  403a14:	f2 0f 11 14 24       	movsd  %xmm2,(%rsp)
  403a19:	e8 f2 1f 00 00       	callq  405a10 <__dubsin>
  403a1e:	f2 0f 10 4c 24 50    	movsd  0x50(%rsp),%xmm1
  403a24:	f2 0f 10 05 74 54 0a 	movsd  0xa5474(%rip),%xmm0        # 4a8ea0 <_IO_stdin_used+0x60>
  403a2b:	00 
  403a2c:	f2 0f 59 44 24 58    	mulsd  0x58(%rsp),%xmm0
  403a32:	f2 0f 10 14 24       	movsd  (%rsp),%xmm2
  403a37:	f2 0f 58 c1          	addsd  %xmm1,%xmm0
  403a3b:	66 0f 2e c8          	ucomisd %xmm0,%xmm1
  403a3f:	0f 8a 6b 05 00 00    	jp     403fb0 <__sin_sse2+0xa30>
  403a45:	0f 85 65 05 00 00    	jne    403fb0 <__sin_sse2+0xa30>
  403a4b:	66 0f 28 d1          	movapd %xmm1,%xmm2
  403a4f:	e9 0c fc ff ff       	jmpq   403660 <__sin_sse2+0xe0>
  403a54:	0f 1f 40 00          	nopl   0x0(%rax)
  403a58:	3d fa 21 99 41       	cmp    $0x419921fa,%eax
  403a5d:	0f 8f 9d 01 00 00    	jg     403c00 <__sin_sse2+0x680>
  403a63:	f2 0f 10 2d 4d 54 0a 	movsd  0xa544d(%rip),%xmm5        # 4a8eb8 <hpinv>
  403a6a:	00 
  403a6b:	f2 0f 10 05 4d 54 0a 	movsd  0xa544d(%rip),%xmm0        # 4a8ec0 <big>
  403a72:	00 
  403a73:	66 0f 28 e2          	movapd %xmm2,%xmm4
  403a77:	f2 0f 59 ea          	mulsd  %xmm2,%xmm5
  403a7b:	66 0f 57 db          	xorpd  %xmm3,%xmm3
  403a7f:	f2 0f 58 e8          	addsd  %xmm0,%xmm5
  403a83:	66 0f 28 f5          	movapd %xmm5,%xmm6
  403a87:	f2 0f 11 2c 24       	movsd  %xmm5,(%rsp)
  403a8c:	48 8b 04 24          	mov    (%rsp),%rax
  403a90:	f2 0f 5c f0          	subsd  %xmm0,%xmm6
  403a94:	f2 0f 10 05 2c 54 0a 	movsd  0xa542c(%rip),%xmm0        # 4a8ec8 <mp1>
  403a9b:	00 
  403a9c:	41 89 c4             	mov    %eax,%r12d
  403a9f:	83 e0 03             	and    $0x3,%eax
  403aa2:	66 0f 2e d3          	ucomisd %xmm3,%xmm2
  403aa6:	f2 0f 59 c6          	mulsd  %xmm6,%xmm0
  403aaa:	f2 0f 5c e0          	subsd  %xmm0,%xmm4
  403aae:	f2 0f 10 05 1a 54 0a 	movsd  0xa541a(%rip),%xmm0        # 4a8ed0 <mp1+0x8>
  403ab5:	00 
  403ab6:	f2 0f 59 c6          	mulsd  %xmm6,%xmm0
  403aba:	f2 0f 5c e0          	subsd  %xmm0,%xmm4
  403abe:	f2 0f 10 05 aa 54 0a 	movsd  0xa54aa(%rip),%xmm0        # 4a8f70 <hp1+0x28>
  403ac5:	00 
  403ac6:	f2 0f 59 c6          	mulsd  %xmm6,%xmm0
  403aca:	66 44 0f 28 cc       	movapd %xmm4,%xmm9
  403acf:	66 0f 28 cc          	movapd %xmm4,%xmm1
  403ad3:	f2 44 0f 5c c8       	subsd  %xmm0,%xmm9
  403ad8:	f2 41 0f 5c c9       	subsd  %xmm9,%xmm1
  403add:	f2 0f 5c c8          	subsd  %xmm0,%xmm1
  403ae1:	0f 86 8c 09 00 00    	jbe    404473 <__sin_sse2+0xef3>
  403ae7:	f2 44 0f 10 25 88 54 	movsd  0xa5488(%rip),%xmm12        # 4a8f78 <hp1+0x30>
  403aee:	0a 00 
  403af0:	f2 44 0f 59 e2       	mulsd  %xmm2,%xmm12
  403af5:	83 f8 01             	cmp    $0x1,%eax
  403af8:	0f 84 b7 07 00 00    	je     4042b5 <__sin_sse2+0xd35>
  403afe:	83 f8 03             	cmp    $0x3,%eax
  403b01:	0f 84 ae 07 00 00    	je     4042b5 <__sin_sse2+0xd35>
  403b07:	66 45 0f 28 e9       	movapd %xmm9,%xmm13
  403b0c:	85 c0                	test   %eax,%eax
  403b0e:	f2 45 0f 59 e9       	mulsd  %xmm9,%xmm13
  403b13:	74 11                	je     403b26 <__sin_sse2+0x5a6>
  403b15:	f2 0f 10 05 a3 54 0a 	movsd  0xa54a3(%rip),%xmm0        # 4a8fc0 <hp1+0x78>
  403b1c:	00 
  403b1d:	66 44 0f 57 c8       	xorpd  %xmm0,%xmm9
  403b22:	66 0f 57 c8          	xorpd  %xmm0,%xmm1
  403b26:	f2 0f 10 05 22 54 0a 	movsd  0xa5422(%rip),%xmm0        # 4a8f50 <hp1+0x8>
  403b2d:	00 
  403b2e:	66 41 0f 2e c5       	ucomisd %xmm13,%xmm0
  403b33:	0f 86 8c 0a 00 00    	jbe    4045c5 <__sin_sse2+0x1045>
  403b39:	66 45 0f 28 dd       	movapd %xmm13,%xmm11
  403b3e:	f2 44 0f 10 15 11 53 	movsd  0xa5311(%rip),%xmm10        # 4a8e58 <_IO_stdin_used+0x18>
  403b45:	0a 00 
  403b47:	f2 44 0f 10 05 10 53 	movsd  0xa5310(%rip),%xmm8        # 4a8e60 <_IO_stdin_used+0x20>
  403b4e:	0a 00 
  403b50:	f2 45 0f 59 da       	mulsd  %xmm10,%xmm11
  403b55:	f2 0f 10 3d 0b 53 0a 	movsd  0xa530b(%rip),%xmm7        # 4a8e68 <_IO_stdin_used+0x28>
  403b5c:	00 
  403b5d:	f2 0f 10 05 0b 53 0a 	movsd  0xa530b(%rip),%xmm0        # 4a8e70 <_IO_stdin_used+0x30>
  403b64:	00 
  403b65:	f2 44 0f 10 35 b2 53 	movsd  0xa53b2(%rip),%xmm14        # 4a8f20 <big+0x30>
  403b6c:	0a 00 
  403b6e:	f2 45 0f 58 d8       	addsd  %xmm8,%xmm11
  403b73:	f2 44 0f 59 f1       	mulsd  %xmm1,%xmm14
  403b78:	f2 45 0f 59 dd       	mulsd  %xmm13,%xmm11
  403b7d:	f2 44 0f 5c df       	subsd  %xmm7,%xmm11
  403b82:	f2 45 0f 59 dd       	mulsd  %xmm13,%xmm11
  403b87:	f2 44 0f 58 d8       	addsd  %xmm0,%xmm11
  403b8c:	f2 45 0f 59 dd       	mulsd  %xmm13,%xmm11
  403b91:	f2 44 0f 5c 1d be 53 	subsd  0xa53be(%rip),%xmm11        # 4a8f58 <hp1+0x10>
  403b98:	0a 00 
  403b9a:	f2 45 0f 59 d9       	mulsd  %xmm9,%xmm11
  403b9f:	f2 45 0f 5c de       	subsd  %xmm14,%xmm11
  403ba4:	66 45 0f 28 f1       	movapd %xmm9,%xmm14
  403ba9:	f2 45 0f 59 dd       	mulsd  %xmm13,%xmm11
  403bae:	66 45 0f 28 e9       	movapd %xmm9,%xmm13
  403bb3:	f2 44 0f 58 d9       	addsd  %xmm1,%xmm11
  403bb8:	f2 45 0f 58 f3       	addsd  %xmm11,%xmm14
  403bbd:	f2 45 0f 5c ee       	subsd  %xmm14,%xmm13
  403bc2:	f2 45 0f 58 eb       	addsd  %xmm11,%xmm13
  403bc7:	66 44 0f 2e eb       	ucomisd %xmm3,%xmm13
  403bcc:	f2 44 0f 59 2d 63 53 	mulsd  0xa5363(%rip),%xmm13        # 4a8f38 <big+0x48>
  403bd3:	0a 00 
  403bd5:	0f 86 8a 13 00 00    	jbe    404f65 <__sin_sse2+0x19e5>
  403bdb:	f2 45 0f 58 ec       	addsd  %xmm12,%xmm13
  403be0:	f2 45 0f 58 ee       	addsd  %xmm14,%xmm13
  403be5:	66 45 0f 2e f5       	ucomisd %xmm13,%xmm14
  403bea:	0f 8a 40 10 00 00    	jp     404c30 <__sin_sse2+0x16b0>
  403bf0:	0f 85 3a 10 00 00    	jne    404c30 <__sin_sse2+0x16b0>
  403bf6:	66 41 0f 28 d6       	movapd %xmm14,%xmm2
  403bfb:	e9 60 fa ff ff       	jmpq   403660 <__sin_sse2+0xe0>
  403c00:	3d ff ff ef 42       	cmp    $0x42efffff,%eax
  403c05:	0f 8f d4 05 00 00    	jg     4041df <__sin_sse2+0xc5f>
  403c0b:	f2 0f 10 05 a5 52 0a 	movsd  0xa52a5(%rip),%xmm0        # 4a8eb8 <hpinv>
  403c12:	00 
  403c13:	f2 0f 10 0d a5 52 0a 	movsd  0xa52a5(%rip),%xmm1        # 4a8ec0 <big>
  403c1a:	00 
  403c1b:	66 0f 28 da          	movapd %xmm2,%xmm3
  403c1f:	f2 0f 59 c2          	mulsd  %xmm2,%xmm0
  403c23:	f2 0f 10 35 9d 52 0a 	movsd  0xa529d(%rip),%xmm6        # 4a8ec8 <mp1>
  403c2a:	00 
  403c2b:	f2 0f 58 c1          	addsd  %xmm1,%xmm0
  403c2f:	66 0f 28 e0          	movapd %xmm0,%xmm4
  403c33:	f2 0f 11 04 24       	movsd  %xmm0,(%rsp)
  403c38:	48 8b 04 24          	mov    (%rsp),%rax
  403c3c:	f2 0f 5c e1          	subsd  %xmm1,%xmm4
  403c40:	f2 0f 10 0d 40 53 0a 	movsd  0xa5340(%rip),%xmm1        # 4a8f88 <hp1+0x40>
  403c47:	00 
  403c48:	89 c7                	mov    %eax,%edi
  403c4a:	89 c1                	mov    %eax,%ecx
  403c4c:	83 e7 03             	and    $0x3,%edi
  403c4f:	66 0f 28 c4          	movapd %xmm4,%xmm0
  403c53:	66 0f 28 ec          	movapd %xmm4,%xmm5
  403c57:	f2 0f 59 25 81 52 0a 	mulsd  0xa5281(%rip),%xmm4        # 4a8ee0 <mp1+0x18>
  403c5e:	00 
  403c5f:	83 ff 01             	cmp    $0x1,%edi
  403c62:	f2 0f 58 c1          	addsd  %xmm1,%xmm0
  403c66:	f2 0f 5c c1          	subsd  %xmm1,%xmm0
  403c6a:	66 0f 28 c8          	movapd %xmm0,%xmm1
  403c6e:	66 0f 28 f8          	movapd %xmm0,%xmm7
  403c72:	f2 0f 59 ce          	mulsd  %xmm6,%xmm1
  403c76:	f2 0f 5c e8          	subsd  %xmm0,%xmm5
  403c7a:	f2 0f 5c d9          	subsd  %xmm1,%xmm3
  403c7e:	f2 0f 10 0d 4a 52 0a 	movsd  0xa524a(%rip),%xmm1        # 4a8ed0 <mp1+0x8>
  403c85:	00 
  403c86:	f2 0f 59 f5          	mulsd  %xmm5,%xmm6
  403c8a:	f2 0f 59 f9          	mulsd  %xmm1,%xmm7
  403c8e:	f2 0f 59 cd          	mulsd  %xmm5,%xmm1
  403c92:	f2 0f 5c df          	subsd  %xmm7,%xmm3
  403c96:	f2 0f 5c de          	subsd  %xmm6,%xmm3
  403c9a:	f2 0f 10 35 36 52 0a 	movsd  0xa5236(%rip),%xmm6        # 4a8ed8 <mp1+0x10>
  403ca1:	00 
  403ca2:	f2 0f 59 c6          	mulsd  %xmm6,%xmm0
  403ca6:	f2 0f 59 ee          	mulsd  %xmm6,%xmm5
  403caa:	f2 0f 5c d9          	subsd  %xmm1,%xmm3
  403cae:	66 0f 28 cb          	movapd %xmm3,%xmm1
  403cb2:	f2 0f 5c c8          	subsd  %xmm0,%xmm1
  403cb6:	f2 0f 5c d9          	subsd  %xmm1,%xmm3
  403cba:	f2 0f 5c d8          	subsd  %xmm0,%xmm3
  403cbe:	66 0f 28 c1          	movapd %xmm1,%xmm0
  403cc2:	f2 0f 5c dd          	subsd  %xmm5,%xmm3
  403cc6:	f2 0f 5c dc          	subsd  %xmm4,%xmm3
  403cca:	f2 0f 58 c3          	addsd  %xmm3,%xmm0
  403cce:	f2 0f 5c c8          	subsd  %xmm0,%xmm1
  403cd2:	f2 0f 58 cb          	addsd  %xmm3,%xmm1
  403cd6:	0f 84 bc 07 00 00    	je     404498 <__sin_sse2+0xf18>
  403cdc:	83 ff 03             	cmp    $0x3,%edi
  403cdf:	0f 84 b3 07 00 00    	je     404498 <__sin_sse2+0xf18>
  403ce5:	66 0f 28 e0          	movapd %xmm0,%xmm4
  403ce9:	85 ff                	test   %edi,%edi
  403ceb:	f2 0f 59 e0          	mulsd  %xmm0,%xmm4
  403cef:	74 10                	je     403d01 <__sin_sse2+0x781>
  403cf1:	f2 0f 10 1d c7 52 0a 	movsd  0xa52c7(%rip),%xmm3        # 4a8fc0 <hp1+0x78>
  403cf8:	00 
  403cf9:	66 0f 57 c3          	xorpd  %xmm3,%xmm0
  403cfd:	66 0f 57 cb          	xorpd  %xmm3,%xmm1
  403d01:	f2 0f 10 1d 47 52 0a 	movsd  0xa5247(%rip),%xmm3        # 4a8f50 <hp1+0x8>
  403d08:	00 
  403d09:	66 0f 2e dc          	ucomisd %xmm4,%xmm3
  403d0d:	0f 86 1d 0d 00 00    	jbe    404a30 <__sin_sse2+0x14b0>
  403d13:	f2 0f 10 1d 3d 51 0a 	movsd  0xa513d(%rip),%xmm3        # 4a8e58 <_IO_stdin_used+0x18>
  403d1a:	00 
  403d1b:	f2 0f 10 2d fd 51 0a 	movsd  0xa51fd(%rip),%xmm5        # 4a8f20 <big+0x30>
  403d22:	00 
  403d23:	f2 0f 59 dc          	mulsd  %xmm4,%xmm3
  403d27:	f2 0f 59 e9          	mulsd  %xmm1,%xmm5
  403d2b:	f2 0f 58 1d 2d 51 0a 	addsd  0xa512d(%rip),%xmm3        # 4a8e60 <_IO_stdin_used+0x20>
  403d32:	00 
  403d33:	f2 0f 59 dc          	mulsd  %xmm4,%xmm3
  403d37:	f2 0f 5c 1d 29 51 0a 	subsd  0xa5129(%rip),%xmm3        # 4a8e68 <_IO_stdin_used+0x28>
  403d3e:	00 
  403d3f:	f2 0f 59 dc          	mulsd  %xmm4,%xmm3
  403d43:	f2 0f 58 1d 25 51 0a 	addsd  0xa5125(%rip),%xmm3        # 4a8e70 <_IO_stdin_used+0x30>
  403d4a:	00 
  403d4b:	f2 0f 59 dc          	mulsd  %xmm4,%xmm3
  403d4f:	f2 0f 5c 1d 01 52 0a 	subsd  0xa5201(%rip),%xmm3        # 4a8f58 <hp1+0x10>
  403d56:	00 
  403d57:	f2 0f 59 d8          	mulsd  %xmm0,%xmm3
  403d5b:	f2 0f 5c dd          	subsd  %xmm5,%xmm3
  403d5f:	66 0f 28 e8          	movapd %xmm0,%xmm5
  403d63:	f2 0f 59 dc          	mulsd  %xmm4,%xmm3
  403d67:	66 0f 28 e0          	movapd %xmm0,%xmm4
  403d6b:	f2 0f 58 d9          	addsd  %xmm1,%xmm3
  403d6f:	f2 0f 58 eb          	addsd  %xmm3,%xmm5
  403d73:	f2 0f 5c e5          	subsd  %xmm5,%xmm4
  403d77:	f2 0f 58 e3          	addsd  %xmm3,%xmm4
  403d7b:	66 0f 2e 25 05 51 0a 	ucomisd 0xa5105(%rip),%xmm4        # 4a8e88 <_IO_stdin_used+0x48>
  403d82:	00 
  403d83:	f2 0f 59 25 ad 51 0a 	mulsd  0xa51ad(%rip),%xmm4        # 4a8f38 <big+0x48>
  403d8a:	00 
  403d8b:	0f 86 86 12 00 00    	jbe    405017 <__sin_sse2+0x1a97>
  403d91:	f2 0f 58 25 f7 51 0a 	addsd  0xa51f7(%rip),%xmm4        # 4a8f90 <hp1+0x48>
  403d98:	00 
  403d99:	f2 0f 58 e5          	addsd  %xmm5,%xmm4
  403d9d:	66 0f 2e ec          	ucomisd %xmm4,%xmm5
  403da1:	7a 06                	jp     403da9 <__sin_sse2+0x829>
  403da3:	0f 84 ac f8 ff ff    	je     403655 <__sin_sse2+0xd5>
  403da9:	e8 92 d4 ff ff       	callq  401240 <bsloww>
  403dae:	66 0f 28 d0          	movapd %xmm0,%xmm2
  403db2:	e9 a9 f8 ff ff       	jmpq   403660 <__sin_sse2+0xe0>
  403db7:	66 0f 1f 84 00 00 00 	nopw   0x0(%rax,%rax,1)
  403dbe:	00 00 
  403dc0:	0f 85 37 fc ff ff    	jne    4039fd <__sin_sse2+0x47d>
  403dc6:	66 0f 28 d4          	movapd %xmm4,%xmm2
  403dca:	e9 91 f8 ff ff       	jmpq   403660 <__sin_sse2+0xe0>
  403dcf:	66 0f 28 c2          	movapd %xmm2,%xmm0
  403dd3:	f2 41 0f 58 c4       	addsd  %xmm12,%xmm0
  403dd8:	e9 10 fa ff ff       	jmpq   4037ed <__sin_sse2+0x26d>
  403ddd:	0f 1f 00             	nopl   (%rax)
  403de0:	66 0f 57 db          	xorpd  %xmm3,%xmm3
  403de4:	66 0f 28 ca          	movapd %xmm2,%xmm1
  403de8:	66 0f 2e d3          	ucomisd %xmm3,%xmm2
  403dec:	0f 86 23 06 00 00    	jbe    404415 <__sin_sse2+0xe95>
  403df2:	66 0f 28 c1          	movapd %xmm1,%xmm0
  403df6:	f2 41 0f 58 c1       	addsd  %xmm9,%xmm0
  403dfb:	f2 0f 11 04 24       	movsd  %xmm0,(%rsp)
  403e00:	f2 41 0f 5c c1       	subsd  %xmm9,%xmm0
  403e05:	48 8b 04 24          	mov    (%rsp),%rax
  403e09:	c1 e0 02             	shl    $0x2,%eax
  403e0c:	f2 0f 5c c8          	subsd  %xmm0,%xmm1
  403e10:	48 63 d0             	movslq %eax,%rdx
  403e13:	f2 44 0f 10 14 d5 00 	movsd  0x4a9a00(,%rdx,8),%xmm10
  403e1a:	9a 4a 00 
  403e1d:	8d 50 02             	lea    0x2(%rax),%edx
  403e20:	f2 0f 10 05 e0 50 0a 	movsd  0xa50e0(%rip),%xmm0        # 4a8f08 <big+0x18>
  403e27:	00 
  403e28:	48 63 d2             	movslq %edx,%rdx
  403e2b:	66 44 0f 28 c9       	movapd %xmm1,%xmm9
  403e30:	66 44 0f 28 e1       	movapd %xmm1,%xmm12
  403e35:	66 44 0f 28 d9       	movapd %xmm1,%xmm11
  403e3a:	f2 44 0f 59 c9       	mulsd  %xmm1,%xmm9
  403e3f:	f2 44 0f 58 d8       	addsd  %xmm0,%xmm11
  403e44:	f2 41 0f 59 e9       	mulsd  %xmm9,%xmm5
  403e49:	f2 45 0f 59 e1       	mulsd  %xmm9,%xmm12
  403e4e:	f2 44 0f 5c d8       	subsd  %xmm0,%xmm11
  403e53:	f2 45 0f 59 c1       	mulsd  %xmm9,%xmm8
  403e58:	f2 0f 5c ec          	subsd  %xmm4,%xmm5
  403e5c:	f2 44 0f 5c c7       	subsd  %xmm7,%xmm8
  403e61:	f2 44 0f 59 e5       	mulsd  %xmm5,%xmm12
  403e66:	f2 0f 10 2c d5 00 9a 	movsd  0x4a9a00(,%rdx,8),%xmm5
  403e6d:	4a 00 
  403e6f:	8d 50 03             	lea    0x3(%rax),%edx
  403e72:	83 c0 01             	add    $0x1,%eax
  403e75:	48 98                	cltq   
  403e77:	f2 45 0f 59 c1       	mulsd  %xmm9,%xmm8
  403e7c:	66 0f 28 e5          	movapd %xmm5,%xmm4
  403e80:	48 63 d2             	movslq %edx,%rdx
  403e83:	f2 44 0f 10 2c d5 00 	movsd  0x4a9a00(,%rdx,8),%xmm13
  403e8a:	9a 4a 00 
  403e8d:	f2 0f 58 e0          	addsd  %xmm0,%xmm4
  403e91:	f2 44 0f 58 c6       	addsd  %xmm6,%xmm8
  403e96:	f2 0f 5c e0          	subsd  %xmm0,%xmm4
  403e9a:	66 41 0f 28 c4       	movapd %xmm12,%xmm0
  403e9f:	f2 44 0f 59 e5       	mulsd  %xmm5,%xmm12
  403ea4:	f2 41 0f 59 c5       	mulsd  %xmm13,%xmm0
  403ea9:	f2 45 0f 59 c1       	mulsd  %xmm9,%xmm8
  403eae:	f2 0f 5c ec          	subsd  %xmm4,%xmm5
  403eb2:	f2 0f 58 04 c5 00 9a 	addsd  0x4a9a00(,%rax,8),%xmm0
  403eb9:	4a 00 
  403ebb:	f2 45 0f 59 c2       	mulsd  %xmm10,%xmm8
  403ec0:	f2 41 0f 58 ed       	addsd  %xmm13,%xmm5
  403ec5:	f2 41 0f 58 c4       	addsd  %xmm12,%xmm0
  403eca:	f2 0f 59 e9          	mulsd  %xmm1,%xmm5
  403ece:	f2 0f 58 c5          	addsd  %xmm5,%xmm0
  403ed2:	66 0f 28 e9          	movapd %xmm1,%xmm5
  403ed6:	f2 41 0f 59 ca       	mulsd  %xmm10,%xmm1
  403edb:	f2 41 0f 5c eb       	subsd  %xmm11,%xmm5
  403ee0:	f2 0f 59 cb          	mulsd  %xmm3,%xmm1
  403ee4:	f2 0f 58 eb          	addsd  %xmm3,%xmm5
  403ee8:	f2 0f 59 ec          	mulsd  %xmm4,%xmm5
  403eec:	f2 41 0f 59 e3       	mulsd  %xmm11,%xmm4
  403ef1:	f2 0f 58 c5          	addsd  %xmm5,%xmm0
  403ef5:	f2 0f 5c c1          	subsd  %xmm1,%xmm0
  403ef9:	66 41 0f 28 ca       	movapd %xmm10,%xmm1
  403efe:	f2 0f 58 cc          	addsd  %xmm4,%xmm1
  403f02:	f2 41 0f 5c c0       	subsd  %xmm8,%xmm0
  403f07:	f2 44 0f 5c d1       	subsd  %xmm1,%xmm10
  403f0c:	f2 44 0f 58 d4       	addsd  %xmm4,%xmm10
  403f11:	66 0f 28 e1          	movapd %xmm1,%xmm4
  403f15:	f2 41 0f 58 c2       	addsd  %xmm10,%xmm0
  403f1a:	f2 0f 58 e0          	addsd  %xmm0,%xmm4
  403f1e:	f2 0f 5c cc          	subsd  %xmm4,%xmm1
  403f22:	f2 0f 58 c8          	addsd  %xmm0,%xmm1
  403f26:	66 0f 2e cb          	ucomisd %xmm3,%xmm1
  403f2a:	f2 0f 59 0d 5e 4f 0a 	mulsd  0xa4f5e(%rip),%xmm1        # 4a8e90 <_IO_stdin_used+0x50>
  403f31:	00 
  403f32:	0f 86 c6 02 00 00    	jbe    4041fe <__sin_sse2+0xc7e>
  403f38:	f2 0f 58 cb          	addsd  %xmm3,%xmm1
  403f3c:	f2 0f 58 cc          	addsd  %xmm4,%xmm1
  403f40:	66 0f 2e cc          	ucomisd %xmm4,%xmm1
  403f44:	0f 8a 36 02 00 00    	jp     404180 <__sin_sse2+0xc00>
  403f4a:	0f 85 30 02 00 00    	jne    404180 <__sin_sse2+0xc00>
  403f50:	66 0f 2e d3          	ucomisd %xmm3,%xmm2
  403f54:	0f 87 6c fe ff ff    	ja     403dc6 <__sin_sse2+0x846>
  403f5a:	f2 0f 10 15 5e 50 0a 	movsd  0xa505e(%rip),%xmm2        # 4a8fc0 <hp1+0x78>
  403f61:	00 
  403f62:	66 0f 57 d4          	xorpd  %xmm4,%xmm2
  403f66:	e9 f5 f6 ff ff       	jmpq   403660 <__sin_sse2+0xe0>
  403f6b:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)
  403f70:	f2 44 0f 10 2d 47 50 	movsd  0xa5047(%rip),%xmm13        # 4a8fc0 <hp1+0x78>
  403f77:	0a 00 
  403f79:	66 45 0f 57 d5       	xorpd  %xmm13,%xmm10
  403f7e:	66 45 0f 57 dd       	xorpd  %xmm13,%xmm11
  403f83:	e9 e6 f7 ff ff       	jmpq   40376e <__sin_sse2+0x1ee>
  403f88:	0f 1f 84 00 00 00 00 	nopl   0x0(%rax,%rax,1)
  403f8f:	00 
  403f90:	66 41 0f 28 c9       	movapd %xmm9,%xmm1
  403f95:	f2 0f 5c ca          	subsd  %xmm2,%xmm1
  403f99:	66 0f 28 c1          	movapd %xmm1,%xmm0
  403f9d:	f2 41 0f 5c c1       	subsd  %xmm9,%xmm0
  403fa2:	f2 0f 58 c2          	addsd  %xmm2,%xmm0
  403fa6:	e9 0f f7 ff ff       	jmpq   4036ba <__sin_sse2+0x13a>
  403fab:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)
  403fb0:	66 0f 57 c9          	xorpd  %xmm1,%xmm1
  403fb4:	31 ff                	xor    %edi,%edi
  403fb6:	66 0f 28 c2          	movapd %xmm2,%xmm0
  403fba:	e8 31 44 00 00       	callq  4083f0 <__mpsin>
  403fbf:	66 0f 28 d0          	movapd %xmm0,%xmm2
  403fc3:	e9 98 f6 ff ff       	jmpq   403660 <__sin_sse2+0xe0>
  403fc8:	0f 1f 84 00 00 00 00 	nopl   0x0(%rax,%rax,1)
  403fcf:	00 
  403fd0:	66 0f 2e d3          	ucomisd %xmm3,%xmm2
  403fd4:	66 0f 28 c2          	movapd %xmm2,%xmm0
  403fd8:	0f 86 ab 07 00 00    	jbe    404789 <__sin_sse2+0x1209>
  403fde:	66 41 0f 28 cc       	movapd %xmm12,%xmm1
  403fe3:	f2 0f 5c c8          	subsd  %xmm0,%xmm1
  403fe7:	66 0f 2e cb          	ucomisd %xmm3,%xmm1
  403feb:	0f 82 1a 07 00 00    	jb     40470b <__sin_sse2+0x118b>
  403ff1:	66 44 0f 28 d1       	movapd %xmm1,%xmm10
  403ff6:	f2 44 0f 10 3d 49 4f 	movsd  0xa4f49(%rip),%xmm15        # 4a8f48 <hp1>
  403ffd:	0a 00 
  403fff:	f2 45 0f 58 d1       	addsd  %xmm9,%xmm10
  404004:	66 41 0f 28 c2       	movapd %xmm10,%xmm0
  404009:	f2 41 0f 5c c1       	subsd  %xmm9,%xmm0
  40400e:	66 44 0f 28 c8       	movapd %xmm0,%xmm9
  404013:	66 0f 28 c1          	movapd %xmm1,%xmm0
  404017:	f2 41 0f 5c c1       	subsd  %xmm9,%xmm0
  40401c:	66 44 0f 28 c8       	movapd %xmm0,%xmm9
  404021:	f2 44 0f 11 14 24    	movsd  %xmm10,(%rsp)
  404027:	48 8b 04 24          	mov    (%rsp),%rax
  40402b:	f2 44 0f 10 15 d4 4e 	movsd  0xa4ed4(%rip),%xmm10        # 4a8f08 <big+0x18>
  404032:	0a 00 
  404034:	f2 44 0f 59 c8       	mulsd  %xmm0,%xmm9
  404039:	66 44 0f 28 d8       	movapd %xmm0,%xmm11
  40403e:	c1 e0 02             	shl    $0x2,%eax
  404041:	f2 45 0f 58 da       	addsd  %xmm10,%xmm11
  404046:	48 63 d0             	movslq %eax,%rdx
  404049:	f2 45 0f 59 c1       	mulsd  %xmm9,%xmm8
  40404e:	f2 44 0f 10 34 d5 00 	movsd  0x4a9a00(,%rdx,8),%xmm14
  404055:	9a 4a 00 
  404058:	8d 50 02             	lea    0x2(%rax),%edx
  40405b:	f2 45 0f 5c da       	subsd  %xmm10,%xmm11
  404060:	f2 41 0f 59 e9       	mulsd  %xmm9,%xmm5
  404065:	66 41 0f 28 ce       	movapd %xmm14,%xmm1
  40406a:	48 63 d2             	movslq %edx,%rdx
  40406d:	f2 44 0f 5c c7       	subsd  %xmm7,%xmm8
  404072:	66 0f 28 f8          	movapd %xmm0,%xmm7
  404076:	f2 41 0f 58 ca       	addsd  %xmm10,%xmm1
  40407b:	f2 44 0f 10 2c d5 00 	movsd  0x4a9a00(,%rdx,8),%xmm13
  404082:	9a 4a 00 
  404085:	f2 41 0f 5c fb       	subsd  %xmm11,%xmm7
  40408a:	8d 50 03             	lea    0x3(%rax),%edx
  40408d:	83 c0 01             	add    $0x1,%eax
  404090:	48 98                	cltq   
  404092:	f2 0f 5c ec          	subsd  %xmm4,%xmm5
  404096:	f2 45 0f 59 c1       	mulsd  %xmm9,%xmm8
  40409b:	48 63 d2             	movslq %edx,%rdx
  40409e:	f2 41 0f 5c ca       	subsd  %xmm10,%xmm1
  4040a3:	66 44 0f 28 d0       	movapd %xmm0,%xmm10
  4040a8:	f2 41 0f 58 ff       	addsd  %xmm15,%xmm7
  4040ad:	f2 45 0f 59 d7       	mulsd  %xmm15,%xmm10
  4040b2:	f2 44 0f 58 c6       	addsd  %xmm6,%xmm8
  4040b7:	f2 0f 10 34 d5 00 9a 	movsd  0x4a9a00(,%rdx,8),%xmm6
  4040be:	4a 00 
  4040c0:	f2 0f 59 f9          	mulsd  %xmm1,%xmm7
  4040c4:	f2 45 0f 59 c1       	mulsd  %xmm9,%xmm8
  4040c9:	f2 45 0f 58 d0       	addsd  %xmm8,%xmm10
  4040ce:	f2 45 0f 59 d5       	mulsd  %xmm13,%xmm10
  4040d3:	f2 41 0f 5c f2       	subsd  %xmm10,%xmm6
  4040d8:	f2 0f 5c f7          	subsd  %xmm7,%xmm6
  4040dc:	66 41 0f 28 fe       	movapd %xmm14,%xmm7
  4040e1:	f2 0f 5c f9          	subsd  %xmm1,%xmm7
  4040e5:	f2 41 0f 59 cb       	mulsd  %xmm11,%xmm1
  4040ea:	f2 0f 58 3c c5 00 9a 	addsd  0x4a9a00(,%rax,8),%xmm7
  4040f1:	4a 00 
  4040f3:	f2 0f 59 f8          	mulsd  %xmm0,%xmm7
  4040f7:	f2 41 0f 59 c1       	mulsd  %xmm9,%xmm0
  4040fc:	f2 0f 5c f7          	subsd  %xmm7,%xmm6
  404100:	f2 0f 59 c5          	mulsd  %xmm5,%xmm0
  404104:	f2 41 0f 59 c6       	mulsd  %xmm14,%xmm0
  404109:	f2 0f 5c f0          	subsd  %xmm0,%xmm6
  40410d:	66 41 0f 28 c5       	movapd %xmm13,%xmm0
  404112:	f2 0f 5c c1          	subsd  %xmm1,%xmm0
  404116:	f2 44 0f 5c e8       	subsd  %xmm0,%xmm13
  40411b:	f2 44 0f 5c e9       	subsd  %xmm1,%xmm13
  404120:	66 0f 28 c8          	movapd %xmm0,%xmm1
  404124:	f2 41 0f 58 f5       	addsd  %xmm13,%xmm6
  404129:	f2 0f 58 ce          	addsd  %xmm6,%xmm1
  40412d:	f2 0f 5c c1          	subsd  %xmm1,%xmm0
  404131:	f2 0f 58 c6          	addsd  %xmm6,%xmm0
  404135:	66 0f 2e c3          	ucomisd %xmm3,%xmm0
  404139:	f2 0f 59 05 4f 4d 0a 	mulsd  0xa4d4f(%rip),%xmm0        # 4a8e90 <_IO_stdin_used+0x50>
  404140:	00 
  404141:	0f 86 48 03 00 00    	jbe    40448f <__sin_sse2+0xf0f>
  404147:	f2 0f 58 c3          	addsd  %xmm3,%xmm0
  40414b:	f2 0f 58 c1          	addsd  %xmm1,%xmm0
  40414f:	66 0f 2e c1          	ucomisd %xmm1,%xmm0
  404153:	0f 8a cd 02 00 00    	jp     404426 <__sin_sse2+0xea6>
  404159:	0f 85 c7 02 00 00    	jne    404426 <__sin_sse2+0xea6>
  40415f:	66 0f 2e d3          	ucomisd %xmm3,%xmm2
  404163:	0f 87 e2 f8 ff ff    	ja     403a4b <__sin_sse2+0x4cb>
  404169:	f2 0f 10 15 4f 4e 0a 	movsd  0xa4e4f(%rip),%xmm2        # 4a8fc0 <hp1+0x78>
  404170:	00 
  404171:	66 0f 57 d1          	xorpd  %xmm1,%xmm2
  404175:	e9 e6 f4 ff ff       	jmpq   403660 <__sin_sse2+0xe0>
  40417a:	66 0f 1f 44 00 00    	nopw   0x0(%rax,%rax,1)
  404180:	66 0f 2e d3          	ucomisd %xmm3,%xmm2
  404184:	0f 86 b3 05 00 00    	jbe    40473d <__sin_sse2+0x11bd>
  40418a:	66 0f 28 cb          	movapd %xmm3,%xmm1
  40418e:	48 8d 7c 24 50       	lea    0x50(%rsp),%rdi
  404193:	66 0f 28 c2          	movapd %xmm2,%xmm0
  404197:	f2 0f 11 14 24       	movsd  %xmm2,(%rsp)
  40419c:	e8 6f 18 00 00       	callq  405a10 <__dubsin>
  4041a1:	f2 0f 10 4c 24 50    	movsd  0x50(%rsp),%xmm1
  4041a7:	f2 0f 10 05 79 4d 0a 	movsd  0xa4d79(%rip),%xmm0        # 4a8f28 <big+0x38>
  4041ae:	00 
  4041af:	e9 78 f8 ff ff       	jmpq   403a2c <__sin_sse2+0x4ac>
  4041b4:	0f 1f 40 00          	nopl   0x0(%rax)
  4041b8:	66 41 0f 28 c9       	movapd %xmm9,%xmm1
  4041bd:	f2 0f 5c c8          	subsd  %xmm0,%xmm1
  4041c1:	66 0f 28 e1          	movapd %xmm1,%xmm4
  4041c5:	f2 41 0f 5c e1       	subsd  %xmm9,%xmm4
  4041ca:	f2 0f 58 e0          	addsd  %xmm0,%xmm4
  4041ce:	f2 0f 10 05 c2 4d 0a 	movsd  0xa4dc2(%rip),%xmm0        # 4a8f98 <hp1+0x50>
  4041d5:	00 
  4041d6:	f2 0f 5c c4          	subsd  %xmm4,%xmm0
  4041da:	e9 43 f6 ff ff       	jmpq   403822 <__sin_sse2+0x2a2>
  4041df:	3d ff ff ef 7f       	cmp    $0x7fefffff,%eax
  4041e4:	0f 8e b0 05 00 00    	jle    40479a <__sin_sse2+0x121a>
  4041ea:	3d 00 00 f0 7f       	cmp    $0x7ff00000,%eax
  4041ef:	0f 84 16 06 00 00    	je     40480b <__sin_sse2+0x128b>
  4041f5:	f2 0f 5e d2          	divsd  %xmm2,%xmm2
  4041f9:	e9 62 f4 ff ff       	jmpq   403660 <__sin_sse2+0xe0>
  4041fe:	f2 0f 5c cb          	subsd  %xmm3,%xmm1
  404202:	e9 35 fd ff ff       	jmpq   403f3c <__sin_sse2+0x9bc>
  404207:	f2 0f 10 3d b1 4d 0a 	movsd  0xa4db1(%rip),%xmm7        # 4a8fc0 <hp1+0x78>
  40420e:	00 
  40420f:	48 8d 7c 24 50       	lea    0x50(%rsp),%rdi
  404214:	66 0f 28 cb          	movapd %xmm3,%xmm1
  404218:	f2 0f 11 54 24 28    	movsd  %xmm2,0x28(%rsp)
  40421e:	66 0f 29 3c 24       	movapd %xmm7,(%rsp)
  404223:	66 0f 57 fa          	xorpd  %xmm2,%xmm7
  404227:	f2 0f 11 5c 24 20    	movsd  %xmm3,0x20(%rsp)
  40422d:	66 0f 28 ef          	movapd %xmm7,%xmm5
  404231:	66 0f 28 c5          	movapd %xmm5,%xmm0
  404235:	f2 0f 11 6c 24 18    	movsd  %xmm5,0x18(%rsp)
  40423b:	e8 d0 17 00 00       	callq  405a10 <__dubsin>
  404240:	f2 0f 10 64 24 50    	movsd  0x50(%rsp),%xmm4
  404246:	f2 0f 10 0d 52 4c 0a 	movsd  0xa4c52(%rip),%xmm1        # 4a8ea0 <_IO_stdin_used+0x60>
  40424d:	00 
  40424e:	f2 0f 59 4c 24 58    	mulsd  0x58(%rsp),%xmm1
  404254:	f2 0f 10 6c 24 18    	movsd  0x18(%rsp),%xmm5
  40425a:	f2 0f 10 5c 24 20    	movsd  0x20(%rsp),%xmm3
  404260:	f2 0f 10 54 24 28    	movsd  0x28(%rsp),%xmm2
  404266:	f2 0f 58 cc          	addsd  %xmm4,%xmm1
  40426a:	66 0f 2e e1          	ucomisd %xmm1,%xmm4
  40426e:	7a 1e                	jp     40428e <__sin_sse2+0xd0e>
  404270:	75 1c                	jne    40428e <__sin_sse2+0xd0e>
  404272:	66 0f 2e d3          	ucomisd %xmm3,%xmm2
  404276:	0f 87 4a fb ff ff    	ja     403dc6 <__sin_sse2+0x846>
  40427c:	66 0f 28 3c 24       	movapd (%rsp),%xmm7
  404281:	66 0f 57 fc          	xorpd  %xmm4,%xmm7
  404285:	66 0f 28 d7          	movapd %xmm7,%xmm2
  404289:	e9 d2 f3 ff ff       	jmpq   403660 <__sin_sse2+0xe0>
  40428e:	66 0f 2e d3          	ucomisd %xmm3,%xmm2
  404292:	0f 87 18 fd ff ff    	ja     403fb0 <__sin_sse2+0xa30>
  404298:	66 0f 28 cb          	movapd %xmm3,%xmm1
  40429c:	31 ff                	xor    %edi,%edi
  40429e:	66 0f 28 c5          	movapd %xmm5,%xmm0
  4042a2:	e8 49 41 00 00       	callq  4083f0 <__mpsin>
  4042a7:	66 0f 28 d0          	movapd %xmm0,%xmm2
  4042ab:	66 0f 57 14 24       	xorpd  (%rsp),%xmm2
  4042b0:	e9 ab f3 ff ff       	jmpq   403660 <__sin_sse2+0xe0>
  4042b5:	66 41 0f 2e d9       	ucomisd %xmm9,%xmm3
  4042ba:	0f 87 5a 07 00 00    	ja     404a1a <__sin_sse2+0x149a>
  4042c0:	f2 0f 10 05 28 4c 0a 	movsd  0xa4c28(%rip),%xmm0        # 4a8ef0 <big>
  4042c7:	00 
  4042c8:	66 41 0f 28 f9       	movapd %xmm9,%xmm7
  4042cd:	66 45 0f 28 f9       	movapd %xmm9,%xmm15
  4042d2:	f2 0f 10 2d 1e 4c 0a 	movsd  0xa4c1e(%rip),%xmm5        # 4a8ef8 <big+0x8>
  4042d9:	00 
  4042da:	f2 0f 58 f8          	addsd  %xmm0,%xmm7
  4042de:	f2 0f 10 25 1a 4c 0a 	movsd  0xa4c1a(%rip),%xmm4        # 4a8f00 <big+0x10>
  4042e5:	00 
  4042e6:	f2 44 0f 10 05 21 4c 	movsd  0xa4c21(%rip),%xmm8        # 4a8f10 <big+0x20>
  4042ed:	0a 00 
  4042ef:	f2 0f 11 3c 24       	movsd  %xmm7,(%rsp)
  4042f4:	48 8b 14 24          	mov    (%rsp),%rdx
  4042f8:	f2 0f 11 7c 24 18    	movsd  %xmm7,0x18(%rsp)
  4042fe:	f2 0f 5c f8          	subsd  %xmm0,%xmm7
  404302:	c1 e2 02             	shl    $0x2,%edx
  404305:	8d 4a 01             	lea    0x1(%rdx),%ecx
  404308:	8d 42 02             	lea    0x2(%rdx),%eax
  40430b:	f2 44 0f 5c ff       	subsd  %xmm7,%xmm15
  404310:	f2 0f 10 3d 00 4c 0a 	movsd  0xa4c00(%rip),%xmm7        # 4a8f18 <big+0x28>
  404317:	00 
  404318:	48 63 c9             	movslq %ecx,%rcx
  40431b:	48 98                	cltq   
  40431d:	f2 44 0f 10 34 c5 00 	movsd  0x4a9a00(,%rax,8),%xmm14
  404324:	9a 4a 00 
  404327:	8d 42 03             	lea    0x3(%rdx),%eax
  40432a:	48 63 d2             	movslq %edx,%rdx
  40432d:	66 41 0f 28 c7       	movapd %xmm15,%xmm0
  404332:	48 98                	cltq   
  404334:	f2 44 0f 10 14 c5 00 	movsd  0x4a9a00(,%rax,8),%xmm10
  40433b:	9a 4a 00 
  40433e:	f2 0f 58 c1          	addsd  %xmm1,%xmm0
  404342:	66 44 0f 28 e8       	movapd %xmm0,%xmm13
  404347:	66 44 0f 28 d8       	movapd %xmm0,%xmm11
  40434c:	f2 44 0f 59 e8       	mulsd  %xmm0,%xmm13
  404351:	66 41 0f 28 f5       	movapd %xmm13,%xmm6
  404356:	f2 45 0f 59 dd       	mulsd  %xmm13,%xmm11
  40435b:	f2 0f 59 f5          	mulsd  %xmm5,%xmm6
  40435f:	f2 0f 5c f4          	subsd  %xmm4,%xmm6
  404363:	f2 44 0f 59 de       	mulsd  %xmm6,%xmm11
  404368:	f2 0f 10 35 b0 4b 0a 	movsd  0xa4bb0(%rip),%xmm6        # 4a8f20 <big+0x30>
  40436f:	00 
  404370:	f2 44 0f 58 d8       	addsd  %xmm0,%xmm11
  404375:	f2 0f 10 04 cd 00 9a 	movsd  0x4a9a00(,%rcx,8),%xmm0
  40437c:	4a 00 
  40437e:	f2 41 0f 59 c3       	mulsd  %xmm11,%xmm0
  404383:	f2 44 0f 59 1c d5 00 	mulsd  0x4a9a00(,%rdx,8),%xmm11
  40438a:	9a 4a 00 
  40438d:	f2 44 0f 5c d0       	subsd  %xmm0,%xmm10
  404392:	66 41 0f 28 c5       	movapd %xmm13,%xmm0
  404397:	f2 41 0f 59 c0       	mulsd  %xmm8,%xmm0
  40439c:	f2 0f 5c c7          	subsd  %xmm7,%xmm0
  4043a0:	f2 41 0f 59 c5       	mulsd  %xmm13,%xmm0
  4043a5:	f2 0f 58 c6          	addsd  %xmm6,%xmm0
  4043a9:	f2 41 0f 59 c5       	mulsd  %xmm13,%xmm0
  4043ae:	f2 41 0f 59 c6       	mulsd  %xmm14,%xmm0
  4043b3:	f2 44 0f 5c d0       	subsd  %xmm0,%xmm10
  4043b8:	66 41 0f 28 c6       	movapd %xmm14,%xmm0
  4043bd:	f2 45 0f 5c d3       	subsd  %xmm11,%xmm10
  4043c2:	f2 41 0f 58 c2       	addsd  %xmm10,%xmm0
  4043c7:	f2 44 0f 5c f0       	subsd  %xmm0,%xmm14
  4043cc:	f2 45 0f 58 f2       	addsd  %xmm10,%xmm14
  4043d1:	66 44 0f 2e f3       	ucomisd %xmm3,%xmm14
  4043d6:	f2 44 0f 59 35 a1 4b 	mulsd  0xa4ba1(%rip),%xmm14        # 4a8f80 <hp1+0x38>
  4043dd:	0a 00 
  4043df:	0f 86 2b 06 00 00    	jbe    404a10 <__sin_sse2+0x1490>
  4043e5:	f2 45 0f 58 f4       	addsd  %xmm12,%xmm14
  4043ea:	f2 44 0f 58 f0       	addsd  %xmm0,%xmm14
  4043ef:	66 44 0f 2e f0       	ucomisd %xmm0,%xmm14
  4043f4:	0f 8a 2c 04 00 00    	jp     404826 <__sin_sse2+0x12a6>
  4043fa:	0f 85 26 04 00 00    	jne    404826 <__sin_sse2+0x12a6>
  404400:	41 83 e4 02          	and    $0x2,%r12d
  404404:	66 0f 28 d0          	movapd %xmm0,%xmm2
  404408:	0f 85 23 f5 ff ff    	jne    403931 <__sin_sse2+0x3b1>
  40440e:	66 90                	xchg   %ax,%ax
  404410:	e9 4b f2 ff ff       	jmpq   403660 <__sin_sse2+0xe0>
  404415:	f2 0f 10 0d a3 4b 0a 	movsd  0xa4ba3(%rip),%xmm1        # 4a8fc0 <hp1+0x78>
  40441c:	00 
  40441d:	66 0f 57 ca          	xorpd  %xmm2,%xmm1
  404421:	e9 cc f9 ff ff       	jmpq   403df2 <__sin_sse2+0x872>
  404426:	66 0f 2e d3          	ucomisd %xmm3,%xmm2
  40442a:	0f 86 5f 07 00 00    	jbe    404b8f <__sin_sse2+0x160f>
  404430:	66 0f 28 ca          	movapd %xmm2,%xmm1
  404434:	48 8d 7c 24 50       	lea    0x50(%rsp),%rdi
  404439:	f2 0f 10 1d 07 4b 0a 	movsd  0xa4b07(%rip),%xmm3        # 4a8f48 <hp1>
  404440:	00 
  404441:	f2 41 0f 5c cc       	subsd  %xmm12,%xmm1
  404446:	f2 0f 11 14 24       	movsd  %xmm2,(%rsp)
  40444b:	66 0f 28 c1          	movapd %xmm1,%xmm0
  40444f:	f2 0f 5c c3          	subsd  %xmm3,%xmm0
  404453:	f2 0f 5c c8          	subsd  %xmm0,%xmm1
  404457:	f2 0f 5c cb          	subsd  %xmm3,%xmm1
  40445b:	e8 40 2f 00 00       	callq  4073a0 <__docos>
  404460:	f2 0f 10 4c 24 50    	movsd  0x50(%rsp),%xmm1
  404466:	f2 0f 10 05 ba 4a 0a 	movsd  0xa4aba(%rip),%xmm0        # 4a8f28 <big+0x38>
  40446d:	00 
  40446e:	e9 b9 f5 ff ff       	jmpq   403a2c <__sin_sse2+0x4ac>
  404473:	f2 44 0f 10 25 44 4b 	movsd  0xa4b44(%rip),%xmm12        # 4a8fc0 <hp1+0x78>
  40447a:	0a 00 
  40447c:	66 44 0f 57 e2       	xorpd  %xmm2,%xmm12
  404481:	f2 44 0f 59 25 ee 4a 	mulsd  0xa4aee(%rip),%xmm12        # 4a8f78 <hp1+0x30>
  404488:	0a 00 
  40448a:	e9 66 f6 ff ff       	jmpq   403af5 <__sin_sse2+0x575>
  40448f:	f2 0f 5c c3          	subsd  %xmm3,%xmm0
  404493:	e9 b3 fc ff ff       	jmpq   40414b <__sin_sse2+0xbcb>
  404498:	66 0f 57 db          	xorpd  %xmm3,%xmm3
  40449c:	66 0f 2e d8          	ucomisd %xmm0,%xmm3
  4044a0:	0f 87 f9 0a 00 00    	ja     404f9f <__sin_sse2+0x1a1f>
  4044a6:	f2 0f 10 25 42 4a 0a 	movsd  0xa4a42(%rip),%xmm4        # 4a8ef0 <big>
  4044ad:	00 
  4044ae:	66 0f 28 e8          	movapd %xmm0,%xmm5
  4044b2:	f2 0f 58 ec          	addsd  %xmm4,%xmm5
  4044b6:	f2 0f 11 2c 24       	movsd  %xmm5,(%rsp)
  4044bb:	f2 0f 5c ec          	subsd  %xmm4,%xmm5
  4044bf:	48 8b 14 24          	mov    (%rsp),%rdx
  4044c3:	66 0f 28 e0          	movapd %xmm0,%xmm4
  4044c7:	c1 e2 02             	shl    $0x2,%edx
  4044ca:	f2 0f 5c e5          	subsd  %xmm5,%xmm4
  4044ce:	f2 0f 10 2d 22 4a 0a 	movsd  0xa4a22(%rip),%xmm5        # 4a8ef8 <big+0x8>
  4044d5:	00 
  4044d6:	8d 72 01             	lea    0x1(%rdx),%esi
  4044d9:	8d 42 02             	lea    0x2(%rdx),%eax
  4044dc:	48 63 f6             	movslq %esi,%rsi
  4044df:	48 98                	cltq   
  4044e1:	f2 0f 58 e1          	addsd  %xmm1,%xmm4
  4044e5:	f2 44 0f 10 04 c5 00 	movsd  0x4a9a00(,%rax,8),%xmm8
  4044ec:	9a 4a 00 
  4044ef:	8d 42 03             	lea    0x3(%rdx),%eax
  4044f2:	48 63 d2             	movslq %edx,%rdx
  4044f5:	48 98                	cltq   
  4044f7:	66 0f 28 fc          	movapd %xmm4,%xmm7
  4044fb:	66 0f 28 f4          	movapd %xmm4,%xmm6
  4044ff:	f2 0f 59 fc          	mulsd  %xmm4,%xmm7
  404503:	f2 0f 59 ef          	mulsd  %xmm7,%xmm5
  404507:	f2 0f 59 f7          	mulsd  %xmm7,%xmm6
  40450b:	f2 0f 5c 2d ed 49 0a 	subsd  0xa49ed(%rip),%xmm5        # 4a8f00 <big+0x10>
  404512:	00 
  404513:	f2 0f 59 f5          	mulsd  %xmm5,%xmm6
  404517:	f2 0f 10 2c c5 00 9a 	movsd  0x4a9a00(,%rax,8),%xmm5
  40451e:	4a 00 
  404520:	f2 0f 58 f4          	addsd  %xmm4,%xmm6
  404524:	f2 0f 10 24 f5 00 9a 	movsd  0x4a9a00(,%rsi,8),%xmm4
  40452b:	4a 00 
  40452d:	f2 0f 59 e6          	mulsd  %xmm6,%xmm4
  404531:	f2 0f 59 34 d5 00 9a 	mulsd  0x4a9a00(,%rdx,8),%xmm6
  404538:	4a 00 
  40453a:	f2 0f 5c ec          	subsd  %xmm4,%xmm5
  40453e:	f2 0f 10 25 ca 49 0a 	movsd  0xa49ca(%rip),%xmm4        # 4a8f10 <big+0x20>
  404545:	00 
  404546:	f2 0f 59 e7          	mulsd  %xmm7,%xmm4
  40454a:	f2 0f 5c 25 c6 49 0a 	subsd  0xa49c6(%rip),%xmm4        # 4a8f18 <big+0x28>
  404551:	00 
  404552:	f2 0f 59 e7          	mulsd  %xmm7,%xmm4
  404556:	f2 0f 58 25 c2 49 0a 	addsd  0xa49c2(%rip),%xmm4        # 4a8f20 <big+0x30>
  40455d:	00 
  40455e:	f2 0f 59 e7          	mulsd  %xmm7,%xmm4
  404562:	f2 41 0f 59 e0       	mulsd  %xmm8,%xmm4
  404567:	f2 0f 5c ec          	subsd  %xmm4,%xmm5
  40456b:	66 41 0f 28 e0       	movapd %xmm8,%xmm4
  404570:	f2 0f 5c ee          	subsd  %xmm6,%xmm5
  404574:	66 41 0f 28 f0       	movapd %xmm8,%xmm6
  404579:	f2 0f 58 f5          	addsd  %xmm5,%xmm6
  40457d:	f2 0f 5c e6          	subsd  %xmm6,%xmm4
  404581:	f2 0f 58 e5          	addsd  %xmm5,%xmm4
  404585:	66 0f 2e e3          	ucomisd %xmm3,%xmm4
  404589:	f2 0f 59 25 ef 49 0a 	mulsd  0xa49ef(%rip),%xmm4        # 4a8f80 <hp1+0x38>
  404590:	00 
  404591:	0f 86 fb 09 00 00    	jbe    404f92 <__sin_sse2+0x1a12>
  404597:	f2 0f 58 25 f1 49 0a 	addsd  0xa49f1(%rip),%xmm4        # 4a8f90 <hp1+0x48>
  40459e:	00 
  40459f:	f2 0f 58 e6          	addsd  %xmm6,%xmm4
  4045a3:	66 0f 2e e6          	ucomisd %xmm6,%xmm4
  4045a7:	0f 8a d4 05 00 00    	jp     404b81 <__sin_sse2+0x1601>
  4045ad:	0f 85 ce 05 00 00    	jne    404b81 <__sin_sse2+0x1601>
  4045b3:	83 e1 02             	and    $0x2,%ecx
  4045b6:	66 0f 28 d6          	movapd %xmm6,%xmm2
  4045ba:	0f 84 a0 f0 ff ff    	je     403660 <__sin_sse2+0xe0>
  4045c0:	e9 6c f3 ff ff       	jmpq   403931 <__sin_sse2+0x3b1>
  4045c5:	66 44 0f 2e cb       	ucomisd %xmm3,%xmm9
  4045ca:	41 bc 01 00 00 00    	mov    $0x1,%r12d
  4045d0:	0f 86 a3 09 00 00    	jbe    404f79 <__sin_sse2+0x19f9>
  4045d6:	f2 0f 10 05 12 49 0a 	movsd  0xa4912(%rip),%xmm0        # 4a8ef0 <big>
  4045dd:	00 
  4045de:	66 45 0f 28 d9       	movapd %xmm9,%xmm11
  4045e3:	66 41 0f 28 e9       	movapd %xmm9,%xmm5
  4045e8:	66 0f 28 f1          	movapd %xmm1,%xmm6
  4045ec:	f2 44 0f 58 d8       	addsd  %xmm0,%xmm11
  4045f1:	66 41 0f 28 fb       	movapd %xmm11,%xmm7
  4045f6:	f2 44 0f 11 1c 24    	movsd  %xmm11,(%rsp)
  4045fc:	48 8b 14 24          	mov    (%rsp),%rdx
  404600:	f2 0f 5c f8          	subsd  %xmm0,%xmm7
  404604:	f2 0f 10 05 ec 48 0a 	movsd  0xa48ec(%rip),%xmm0        # 4a8ef8 <big+0x8>
  40460b:	00 
  40460c:	c1 e2 02             	shl    $0x2,%edx
  40460f:	8d 4a 03             	lea    0x3(%rdx),%ecx
  404612:	48 63 c2             	movslq %edx,%rax
  404615:	f2 0f 5c ef          	subsd  %xmm7,%xmm5
  404619:	66 0f 28 f9          	movapd %xmm1,%xmm7
  40461d:	48 63 c9             	movslq %ecx,%rcx
  404620:	f2 44 0f 10 14 c5 00 	movsd  0x4a9a00(,%rax,8),%xmm10
  404627:	9a 4a 00 
  40462a:	8d 42 01             	lea    0x1(%rdx),%eax
  40462d:	66 0f 28 e5          	movapd %xmm5,%xmm4
  404631:	f2 0f 59 f5          	mulsd  %xmm5,%xmm6
  404635:	66 44 0f 28 c5       	movapd %xmm5,%xmm8
  40463a:	48 98                	cltq   
  40463c:	f2 0f 59 e5          	mulsd  %xmm5,%xmm4
  404640:	f2 0f 59 c4          	mulsd  %xmm4,%xmm0
  404644:	f2 44 0f 59 c4       	mulsd  %xmm4,%xmm8
  404649:	f2 0f 5c 05 af 48 0a 	subsd  0xa48af(%rip),%xmm0        # 4a8f00 <big+0x10>
  404650:	00 
  404651:	f2 44 0f 59 c0       	mulsd  %xmm0,%xmm8
  404656:	f2 0f 10 05 b2 48 0a 	movsd  0xa48b2(%rip),%xmm0        # 4a8f10 <big+0x20>
  40465d:	00 
  40465e:	f2 0f 59 c4          	mulsd  %xmm4,%xmm0
  404662:	f2 41 0f 58 f8       	addsd  %xmm8,%xmm7
  404667:	f2 0f 5c 05 a9 48 0a 	subsd  0xa48a9(%rip),%xmm0        # 4a8f18 <big+0x28>
  40466e:	00 
  40466f:	f2 0f 58 fd          	addsd  %xmm5,%xmm7
  404673:	f2 0f 59 c4          	mulsd  %xmm4,%xmm0
  404677:	f2 0f 58 05 a1 48 0a 	addsd  0xa48a1(%rip),%xmm0        # 4a8f20 <big+0x30>
  40467e:	00 
  40467f:	f2 0f 59 c4          	mulsd  %xmm4,%xmm0
  404683:	f2 0f 10 24 cd 00 9a 	movsd  0x4a9a00(,%rcx,8),%xmm4
  40468a:	4a 00 
  40468c:	f2 0f 59 e7          	mulsd  %xmm7,%xmm4
  404690:	f2 0f 58 f0          	addsd  %xmm0,%xmm6
  404694:	f2 0f 58 24 c5 00 9a 	addsd  0x4a9a00(,%rax,8),%xmm4
  40469b:	4a 00 
  40469d:	8d 42 02             	lea    0x2(%rdx),%eax
  4046a0:	f2 41 0f 59 f2       	mulsd  %xmm10,%xmm6
  4046a5:	48 98                	cltq   
  4046a7:	f2 0f 59 3c c5 00 9a 	mulsd  0x4a9a00(,%rax,8),%xmm7
  4046ae:	4a 00 
  4046b0:	f2 0f 5c e6          	subsd  %xmm6,%xmm4
  4046b4:	66 41 0f 28 f2       	movapd %xmm10,%xmm6
  4046b9:	f2 0f 58 e7          	addsd  %xmm7,%xmm4
  4046bd:	66 41 0f 28 fa       	movapd %xmm10,%xmm7
  4046c2:	f2 0f 58 fc          	addsd  %xmm4,%xmm7
  4046c6:	f2 0f 5c f7          	subsd  %xmm7,%xmm6
  4046ca:	f2 0f 58 f4          	addsd  %xmm4,%xmm6
  4046ce:	66 0f 2e f3          	ucomisd %xmm3,%xmm6
  4046d2:	f2 0f 59 35 8e 48 0a 	mulsd  0xa488e(%rip),%xmm6        # 4a8f68 <hp1+0x20>
  4046d9:	00 
  4046da:	0f 86 8f 08 00 00    	jbe    404f6f <__sin_sse2+0x19ef>
  4046e0:	f2 41 0f 58 f4       	addsd  %xmm12,%xmm6
  4046e5:	f2 0f 58 f7          	addsd  %xmm7,%xmm6
  4046e9:	66 0f 2e f7          	ucomisd %xmm7,%xmm6
  4046ed:	0f 8a 28 07 00 00    	jp     404e1b <__sin_sse2+0x189b>
  4046f3:	0f 85 22 07 00 00    	jne    404e1b <__sin_sse2+0x189b>
  4046f9:	45 85 e4             	test   %r12d,%r12d
  4046fc:	66 0f 28 d7          	movapd %xmm7,%xmm2
  404700:	0f 85 5a ef ff ff    	jne    403660 <__sin_sse2+0xe0>
  404706:	e9 26 f2 ff ff       	jmpq   403931 <__sin_sse2+0x3b1>
  40470b:	66 45 0f 28 d1       	movapd %xmm9,%xmm10
  404710:	f2 44 0f 10 3d 7f 48 	movsd  0xa487f(%rip),%xmm15        # 4a8f98 <hp1+0x50>
  404717:	0a 00 
  404719:	f2 44 0f 5c d1       	subsd  %xmm1,%xmm10
  40471e:	66 41 0f 28 c2       	movapd %xmm10,%xmm0
  404723:	f2 41 0f 5c c1       	subsd  %xmm9,%xmm0
  404728:	f2 0f 58 c1          	addsd  %xmm1,%xmm0
  40472c:	f2 0f 10 0d 8c 48 0a 	movsd  0xa488c(%rip),%xmm1        # 4a8fc0 <hp1+0x78>
  404733:	00 
  404734:	66 0f 57 c1          	xorpd  %xmm1,%xmm0
  404738:	e9 df f8 ff ff       	jmpq   40401c <__sin_sse2+0xa9c>
  40473d:	f2 0f 10 3d 7b 48 0a 	movsd  0xa487b(%rip),%xmm7        # 4a8fc0 <hp1+0x78>
  404744:	00 
  404745:	48 8d 7c 24 50       	lea    0x50(%rsp),%rdi
  40474a:	66 0f 28 cb          	movapd %xmm3,%xmm1
  40474e:	f2 0f 11 54 24 28    	movsd  %xmm2,0x28(%rsp)
  404754:	66 0f 29 3c 24       	movapd %xmm7,(%rsp)
  404759:	66 0f 57 fa          	xorpd  %xmm2,%xmm7
  40475d:	f2 0f 11 5c 24 20    	movsd  %xmm3,0x20(%rsp)
  404763:	66 0f 28 ef          	movapd %xmm7,%xmm5
  404767:	66 0f 28 c5          	movapd %xmm5,%xmm0
  40476b:	f2 0f 11 6c 24 18    	movsd  %xmm5,0x18(%rsp)
  404771:	e8 9a 12 00 00       	callq  405a10 <__dubsin>
  404776:	f2 0f 10 64 24 50    	movsd  0x50(%rsp),%xmm4
  40477c:	f2 0f 10 0d a4 47 0a 	movsd  0xa47a4(%rip),%xmm1        # 4a8f28 <big+0x38>
  404783:	00 
  404784:	e9 c5 fa ff ff       	jmpq   40424e <__sin_sse2+0xcce>
  404789:	f2 0f 10 05 2f 48 0a 	movsd  0xa482f(%rip),%xmm0        # 4a8fc0 <hp1+0x78>
  404790:	00 
  404791:	66 0f 57 c2          	xorpd  %xmm2,%xmm0
  404795:	e9 44 f8 ff ff       	jmpq   403fde <__sin_sse2+0xa5e>
  40479a:	48 8d 7c 24 40       	lea    0x40(%rsp),%rdi
  40479f:	66 0f 28 c2          	movapd %xmm2,%xmm0
  4047a3:	48 8d 74 24 50       	lea    0x50(%rsp),%rsi
  4047a8:	f2 0f 11 14 24       	movsd  %xmm2,(%rsp)
  4047ad:	e8 0e 0d 00 00       	callq  4054c0 <__branred>
  4047b2:	89 c7                	mov    %eax,%edi
  4047b4:	83 e0 03             	and    $0x3,%eax
  4047b7:	83 f8 02             	cmp    $0x2,%eax
  4047ba:	f2 0f 10 14 24       	movsd  (%rsp),%xmm2
  4047bf:	0f 84 ef 07 00 00    	je     404fb4 <__sin_sse2+0x1a34>
  4047c5:	83 f8 03             	cmp    $0x3,%eax
  4047c8:	0f 84 a7 03 00 00    	je     404b75 <__sin_sse2+0x15f5>
  4047ce:	83 f8 01             	cmp    $0x1,%eax
  4047d1:	0f 84 9e 03 00 00    	je     404b75 <__sin_sse2+0x15f5>
  4047d7:	f2 0f 10 44 24 40    	movsd  0x40(%rsp),%xmm0
  4047dd:	f2 0f 10 1d 6b 47 0a 	movsd  0xa476b(%rip),%xmm3        # 4a8f50 <hp1+0x8>
  4047e4:	00 
  4047e5:	66 0f 28 c8          	movapd %xmm0,%xmm1
  4047e9:	f2 0f 59 c8          	mulsd  %xmm0,%xmm1
  4047ed:	66 0f 2e d9          	ucomisd %xmm1,%xmm3
  4047f1:	f2 0f 10 4c 24 50    	movsd  0x50(%rsp),%xmm1
  4047f7:	0f 87 ac f5 ff ff    	ja     403da9 <__sin_sse2+0x829>
  4047fd:	e8 6e d4 ff ff       	callq  401c70 <bsloww1>
  404802:	66 0f 28 d0          	movapd %xmm0,%xmm2
  404806:	e9 55 ee ff ff       	jmpq   403660 <__sin_sse2+0xe0>
  40480b:	85 d2                	test   %edx,%edx
  40480d:	0f 85 e2 f9 ff ff    	jne    4041f5 <__sin_sse2+0xc75>
  404813:	48 c7 c0 c0 ff ff ff 	mov    $0xffffffffffffffc0,%rax
  40481a:	64 c7 00 21 00 00 00 	movl   $0x21,%fs:(%rax)
  404821:	e9 cf f9 ff ff       	jmpq   4041f5 <__sin_sse2+0xc75>
  404826:	66 0f 2e d3          	ucomisd %xmm3,%xmm2
  40482a:	48 8b 44 24 18       	mov    0x18(%rsp),%rax
  40482f:	0f 86 c4 07 00 00    	jbe    404ff9 <__sin_sse2+0x1a79>
  404835:	f2 0f 10 05 6b 46 0a 	movsd  0xa466b(%rip),%xmm0        # 4a8ea8 <_IO_stdin_used+0x68>
  40483c:	00 
  40483d:	f2 0f 59 c2          	mulsd  %xmm2,%xmm0
  404841:	f2 0f 11 04 24       	movsd  %xmm0,(%rsp)
  404846:	66 45 0f 28 d7       	movapd %xmm15,%xmm10
  40484b:	c1 e0 02             	shl    $0x2,%eax
  40484e:	48 63 d0             	movslq %eax,%rdx
  404851:	f2 44 0f 10 1d ae 46 	movsd  0xa46ae(%rip),%xmm11        # 4a8f08 <big+0x18>
  404858:	0a 00 
  40485a:	f2 45 0f 59 d7       	mulsd  %xmm15,%xmm10
  40485f:	66 45 0f 28 e7       	movapd %xmm15,%xmm12
  404864:	f2 44 0f 10 34 d5 00 	movsd  0x4a9a00(,%rdx,8),%xmm14
  40486b:	9a 4a 00 
  40486e:	8d 50 02             	lea    0x2(%rax),%edx
  404871:	f2 45 0f 58 e3       	addsd  %xmm11,%xmm12
  404876:	66 41 0f 28 c6       	movapd %xmm14,%xmm0
  40487b:	48 63 d2             	movslq %edx,%rdx
  40487e:	f2 45 0f 59 c2       	mulsd  %xmm10,%xmm8
  404883:	f2 41 0f 58 c3       	addsd  %xmm11,%xmm0
  404888:	f2 44 0f 10 2c d5 00 	movsd  0x4a9a00(,%rdx,8),%xmm13
  40488f:	9a 4a 00 
  404892:	f2 45 0f 5c e3       	subsd  %xmm11,%xmm12
  404897:	8d 50 03             	lea    0x3(%rax),%edx
  40489a:	83 c0 01             	add    $0x1,%eax
  40489d:	48 98                	cltq   
  40489f:	f2 41 0f 59 ea       	mulsd  %xmm10,%xmm5
  4048a4:	f2 44 0f 5c c7       	subsd  %xmm7,%xmm8
  4048a9:	66 41 0f 28 ff       	movapd %xmm15,%xmm7
  4048ae:	f2 41 0f 5c c3       	subsd  %xmm11,%xmm0
  4048b3:	66 44 0f 28 d9       	movapd %xmm1,%xmm11
  4048b8:	f2 41 0f 5c fc       	subsd  %xmm12,%xmm7
  4048bd:	48 63 d2             	movslq %edx,%rdx
  4048c0:	f2 45 0f 59 df       	mulsd  %xmm15,%xmm11
  4048c5:	f2 0f 5c ec          	subsd  %xmm4,%xmm5
  4048c9:	f2 45 0f 59 c2       	mulsd  %xmm10,%xmm8
  4048ce:	66 41 0f 28 e5       	movapd %xmm13,%xmm4
  4048d3:	f2 0f 58 f9          	addsd  %xmm1,%xmm7
  4048d7:	f2 44 0f 58 c6       	addsd  %xmm6,%xmm8
  4048dc:	f2 0f 10 34 d5 00 9a 	movsd  0x4a9a00(,%rdx,8),%xmm6
  4048e3:	4a 00 
  4048e5:	f2 0f 59 f8          	mulsd  %xmm0,%xmm7
  4048e9:	f2 45 0f 59 c2       	mulsd  %xmm10,%xmm8
  4048ee:	f2 45 0f 58 d8       	addsd  %xmm8,%xmm11
  4048f3:	f2 45 0f 59 dd       	mulsd  %xmm13,%xmm11
  4048f8:	f2 41 0f 5c f3       	subsd  %xmm11,%xmm6
  4048fd:	f2 0f 5c f7          	subsd  %xmm7,%xmm6
  404901:	66 41 0f 28 fe       	movapd %xmm14,%xmm7
  404906:	f2 0f 5c f8          	subsd  %xmm0,%xmm7
  40490a:	f2 41 0f 59 c4       	mulsd  %xmm12,%xmm0
  40490f:	f2 0f 58 3c c5 00 9a 	addsd  0x4a9a00(,%rax,8),%xmm7
  404916:	4a 00 
  404918:	f2 0f 5c e0          	subsd  %xmm0,%xmm4
  40491c:	f2 44 0f 5c ec       	subsd  %xmm4,%xmm13
  404921:	f2 41 0f 59 ff       	mulsd  %xmm15,%xmm7
  404926:	f2 44 0f 5c e8       	subsd  %xmm0,%xmm13
  40492b:	66 0f 28 c4          	movapd %xmm4,%xmm0
  40492f:	f2 0f 5c f7          	subsd  %xmm7,%xmm6
  404933:	66 41 0f 28 ff       	movapd %xmm15,%xmm7
  404938:	f2 41 0f 59 fa       	mulsd  %xmm10,%xmm7
  40493d:	f2 0f 59 fd          	mulsd  %xmm5,%xmm7
  404941:	f2 41 0f 59 fe       	mulsd  %xmm14,%xmm7
  404946:	f2 0f 5c f7          	subsd  %xmm7,%xmm6
  40494a:	f2 41 0f 58 f5       	addsd  %xmm13,%xmm6
  40494f:	f2 0f 58 c6          	addsd  %xmm6,%xmm0
  404953:	f2 0f 5c e0          	subsd  %xmm0,%xmm4
  404957:	f2 0f 58 e6          	addsd  %xmm6,%xmm4
  40495b:	66 0f 2e e3          	ucomisd %xmm3,%xmm4
  40495f:	f2 0f 59 25 29 45 0a 	mulsd  0xa4529(%rip),%xmm4        # 4a8e90 <_IO_stdin_used+0x50>
  404966:	00 
  404967:	0f 86 82 06 00 00    	jbe    404fef <__sin_sse2+0x1a6f>
  40496d:	f2 0f 58 24 24       	addsd  (%rsp),%xmm4
  404972:	f2 0f 58 e0          	addsd  %xmm0,%xmm4
  404976:	66 0f 2e e0          	ucomisd %xmm0,%xmm4
  40497a:	7a 06                	jp     404982 <__sin_sse2+0x1402>
  40497c:	0f 84 7e fa ff ff    	je     404400 <__sin_sse2+0xe80>
  404982:	66 41 0f 28 c1       	movapd %xmm9,%xmm0
  404987:	48 8d 7c 24 50       	lea    0x50(%rsp),%rdi
  40498c:	f2 0f 11 5c 24 18    	movsd  %xmm3,0x18(%rsp)
  404992:	f2 0f 11 14 24       	movsd  %xmm2,(%rsp)
  404997:	e8 04 2a 00 00       	callq  4073a0 <__docos>
  40499c:	f2 0f 10 44 24 58    	movsd  0x58(%rsp),%xmm0
  4049a2:	f2 0f 10 5c 24 18    	movsd  0x18(%rsp),%xmm3
  4049a8:	66 0f 28 c8          	movapd %xmm0,%xmm1
  4049ac:	f2 0f 10 14 24       	movsd  (%rsp),%xmm2
  4049b1:	66 0f 2e c3          	ucomisd %xmm3,%xmm0
  4049b5:	f2 0f 59 0d 6b 45 0a 	mulsd  0xa456b(%rip),%xmm1        # 4a8f28 <big+0x38>
  4049bc:	00 
  4049bd:	0f 86 5e 09 00 00    	jbe    405321 <__sin_sse2+0x1da1>
  4049c3:	66 0f 2e d3          	ucomisd %xmm3,%xmm2
  4049c7:	0f 86 f3 08 00 00    	jbe    4052c0 <__sin_sse2+0x1d40>
  4049cd:	f2 0f 10 05 db 44 0a 	movsd  0xa44db(%rip),%xmm0        # 4a8eb0 <_IO_stdin_used+0x70>
  4049d4:	00 
  4049d5:	f2 0f 59 c2          	mulsd  %xmm2,%xmm0
  4049d9:	f2 0f 58 c1          	addsd  %xmm1,%xmm0
  4049dd:	f2 0f 10 4c 24 50    	movsd  0x50(%rsp),%xmm1
  4049e3:	f2 0f 58 c1          	addsd  %xmm1,%xmm0
  4049e7:	66 0f 2e c8          	ucomisd %xmm0,%xmm1
  4049eb:	0f 8a 74 06 00 00    	jp     405065 <__sin_sse2+0x1ae5>
  4049f1:	0f 85 6e 06 00 00    	jne    405065 <__sin_sse2+0x1ae5>
  4049f7:	41 80 e4 02          	and    $0x2,%r12b
  4049fb:	66 0f 28 d1          	movapd %xmm1,%xmm2
  4049ff:	0f 85 2c ef ff ff    	jne    403931 <__sin_sse2+0x3b1>
  404a05:	e9 56 ec ff ff       	jmpq   403660 <__sin_sse2+0xe0>
  404a0a:	66 0f 1f 44 00 00    	nopw   0x0(%rax,%rax,1)
  404a10:	f2 45 0f 5c f4       	subsd  %xmm12,%xmm14
  404a15:	e9 d0 f9 ff ff       	jmpq   4043ea <__sin_sse2+0xe6a>
  404a1a:	f2 0f 10 05 9e 45 0a 	movsd  0xa459e(%rip),%xmm0        # 4a8fc0 <hp1+0x78>
  404a21:	00 
  404a22:	66 44 0f 57 c8       	xorpd  %xmm0,%xmm9
  404a27:	66 0f 57 c8          	xorpd  %xmm0,%xmm1
  404a2b:	e9 90 f8 ff ff       	jmpq   4042c0 <__sin_sse2+0xd40>
  404a30:	66 0f 57 db          	xorpd  %xmm3,%xmm3
  404a34:	66 0f 2e c3          	ucomisd %xmm3,%xmm0
  404a38:	0f 86 f3 05 00 00    	jbe    405031 <__sin_sse2+0x1ab1>
  404a3e:	66 0f 28 e0          	movapd %xmm0,%xmm4
  404a42:	be 01 00 00 00       	mov    $0x1,%esi
  404a47:	66 0f 28 f9          	movapd %xmm1,%xmm7
  404a4b:	f2 0f 10 2d 9d 44 0a 	movsd  0xa449d(%rip),%xmm5        # 4a8ef0 <big>
  404a52:	00 
  404a53:	66 0f 28 f4          	movapd %xmm4,%xmm6
  404a57:	f2 0f 58 f5          	addsd  %xmm5,%xmm6
  404a5b:	f2 0f 11 34 24       	movsd  %xmm6,(%rsp)
  404a60:	f2 0f 5c f5          	subsd  %xmm5,%xmm6
  404a64:	48 8b 14 24          	mov    (%rsp),%rdx
  404a68:	f2 0f 10 2d 88 44 0a 	movsd  0xa4488(%rip),%xmm5        # 4a8ef8 <big+0x8>
  404a6f:	00 
  404a70:	c1 e2 02             	shl    $0x2,%edx
  404a73:	f2 0f 5c e6          	subsd  %xmm6,%xmm4
  404a77:	8d 4a 03             	lea    0x3(%rdx),%ecx
  404a7a:	48 63 c2             	movslq %edx,%rax
  404a7d:	f2 44 0f 10 0c c5 00 	movsd  0x4a9a00(,%rax,8),%xmm9
  404a84:	9a 4a 00 
  404a87:	8d 42 01             	lea    0x1(%rdx),%eax
  404a8a:	48 63 c9             	movslq %ecx,%rcx
  404a8d:	48 98                	cltq   
  404a8f:	66 44 0f 28 c4       	movapd %xmm4,%xmm8
  404a94:	66 0f 28 f4          	movapd %xmm4,%xmm6
  404a98:	f2 44 0f 59 c4       	mulsd  %xmm4,%xmm8
  404a9d:	f2 41 0f 59 e8       	mulsd  %xmm8,%xmm5
  404aa2:	f2 41 0f 59 f0       	mulsd  %xmm8,%xmm6
  404aa7:	f2 0f 5c 2d 51 44 0a 	subsd  0xa4451(%rip),%xmm5        # 4a8f00 <big+0x10>
  404aae:	00 
  404aaf:	f2 0f 59 f5          	mulsd  %xmm5,%xmm6
  404ab3:	f2 0f 10 2c cd 00 9a 	movsd  0x4a9a00(,%rcx,8),%xmm5
  404aba:	4a 00 
  404abc:	f2 0f 58 f7          	addsd  %xmm7,%xmm6
  404ac0:	f2 0f 59 fc          	mulsd  %xmm4,%xmm7
  404ac4:	f2 0f 58 f4          	addsd  %xmm4,%xmm6
  404ac8:	f2 0f 10 25 40 44 0a 	movsd  0xa4440(%rip),%xmm4        # 4a8f10 <big+0x20>
  404acf:	00 
  404ad0:	f2 41 0f 59 e0       	mulsd  %xmm8,%xmm4
  404ad5:	f2 0f 59 ee          	mulsd  %xmm6,%xmm5
  404ad9:	f2 0f 5c 25 37 44 0a 	subsd  0xa4437(%rip),%xmm4        # 4a8f18 <big+0x28>
  404ae0:	00 
  404ae1:	f2 0f 58 2c c5 00 9a 	addsd  0x4a9a00(,%rax,8),%xmm5
  404ae8:	4a 00 
  404aea:	8d 42 02             	lea    0x2(%rdx),%eax
  404aed:	48 98                	cltq   
  404aef:	f2 0f 59 34 c5 00 9a 	mulsd  0x4a9a00(,%rax,8),%xmm6
  404af6:	4a 00 
  404af8:	f2 41 0f 59 e0       	mulsd  %xmm8,%xmm4
  404afd:	f2 0f 58 25 1b 44 0a 	addsd  0xa441b(%rip),%xmm4        # 4a8f20 <big+0x30>
  404b04:	00 
  404b05:	f2 41 0f 59 e0       	mulsd  %xmm8,%xmm4
  404b0a:	f2 0f 58 fc          	addsd  %xmm4,%xmm7
  404b0e:	66 41 0f 28 e1       	movapd %xmm9,%xmm4
  404b13:	f2 41 0f 59 f9       	mulsd  %xmm9,%xmm7
  404b18:	f2 0f 5c ef          	subsd  %xmm7,%xmm5
  404b1c:	f2 0f 58 ee          	addsd  %xmm6,%xmm5
  404b20:	66 41 0f 28 f1       	movapd %xmm9,%xmm6
  404b25:	f2 0f 58 f5          	addsd  %xmm5,%xmm6
  404b29:	f2 0f 5c e6          	subsd  %xmm6,%xmm4
  404b2d:	f2 0f 58 e5          	addsd  %xmm5,%xmm4
  404b31:	66 0f 2e e3          	ucomisd %xmm3,%xmm4
  404b35:	f2 0f 59 25 2b 44 0a 	mulsd  0xa442b(%rip),%xmm4        # 4a8f68 <hp1+0x20>
  404b3c:	00 
  404b3d:	0f 86 e1 04 00 00    	jbe    405024 <__sin_sse2+0x1aa4>
  404b43:	f2 0f 58 25 45 44 0a 	addsd  0xa4445(%rip),%xmm4        # 4a8f90 <hp1+0x48>
  404b4a:	00 
  404b4b:	f2 0f 58 e6          	addsd  %xmm6,%xmm4
  404b4f:	66 0f 2e e6          	ucomisd %xmm6,%xmm4
  404b53:	0f 8a a4 fc ff ff    	jp     4047fd <__sin_sse2+0x127d>
  404b59:	0f 85 9e fc ff ff    	jne    4047fd <__sin_sse2+0x127d>
  404b5f:	85 f6                	test   %esi,%esi
  404b61:	66 0f 28 d6          	movapd %xmm6,%xmm2
  404b65:	0f 85 f5 ea ff ff    	jne    403660 <__sin_sse2+0xe0>
  404b6b:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)
  404b70:	e9 bc ed ff ff       	jmpq   403931 <__sin_sse2+0x3b1>
  404b75:	f2 0f 10 4c 24 50    	movsd  0x50(%rsp),%xmm1
  404b7b:	f2 0f 10 44 24 40    	movsd  0x40(%rsp),%xmm0
  404b81:	e8 ea d3 ff ff       	callq  401f70 <bsloww2>
  404b86:	66 0f 28 d0          	movapd %xmm0,%xmm2
  404b8a:	e9 d1 ea ff ff       	jmpq   403660 <__sin_sse2+0xe0>
  404b8f:	f2 0f 10 3d 29 44 0a 	movsd  0xa4429(%rip),%xmm7        # 4a8fc0 <hp1+0x78>
  404b96:	00 
  404b97:	48 8d 7c 24 50       	lea    0x50(%rsp),%rdi
  404b9c:	f2 0f 10 25 a4 43 0a 	movsd  0xa43a4(%rip),%xmm4        # 4a8f48 <hp1>
  404ba3:	00 
  404ba4:	66 0f 29 3c 24       	movapd %xmm7,(%rsp)
  404ba9:	66 0f 57 fa          	xorpd  %xmm2,%xmm7
  404bad:	f2 0f 11 5c 24 28    	movsd  %xmm3,0x28(%rsp)
  404bb3:	f2 0f 11 54 24 20    	movsd  %xmm2,0x20(%rsp)
  404bb9:	66 0f 28 ef          	movapd %xmm7,%xmm5
  404bbd:	66 0f 28 cd          	movapd %xmm5,%xmm1
  404bc1:	f2 0f 11 6c 24 18    	movsd  %xmm5,0x18(%rsp)
  404bc7:	f2 41 0f 5c cc       	subsd  %xmm12,%xmm1
  404bcc:	66 0f 28 c1          	movapd %xmm1,%xmm0
  404bd0:	f2 0f 5c c4          	subsd  %xmm4,%xmm0
  404bd4:	f2 0f 5c c8          	subsd  %xmm0,%xmm1
  404bd8:	f2 0f 5c cc          	subsd  %xmm4,%xmm1
  404bdc:	e8 bf 27 00 00       	callq  4073a0 <__docos>
  404be1:	f2 0f 10 0d 3f 43 0a 	movsd  0xa433f(%rip),%xmm1        # 4a8f28 <big+0x38>
  404be8:	00 
  404be9:	f2 0f 10 64 24 50    	movsd  0x50(%rsp),%xmm4
  404bef:	f2 0f 59 4c 24 58    	mulsd  0x58(%rsp),%xmm1
  404bf5:	f2 0f 10 6c 24 18    	movsd  0x18(%rsp),%xmm5
  404bfb:	f2 0f 10 54 24 20    	movsd  0x20(%rsp),%xmm2
  404c01:	f2 0f 10 5c 24 28    	movsd  0x28(%rsp),%xmm3
  404c07:	f2 0f 58 cc          	addsd  %xmm4,%xmm1
  404c0b:	66 0f 2e e1          	ucomisd %xmm1,%xmm4
  404c0f:	0f 8a 79 f6 ff ff    	jp     40428e <__sin_sse2+0xd0e>
  404c15:	0f 85 73 f6 ff ff    	jne    40428e <__sin_sse2+0xd0e>
  404c1b:	66 0f 2e d3          	ucomisd %xmm3,%xmm2
  404c1f:	0f 86 57 f6 ff ff    	jbe    40427c <__sin_sse2+0xcfc>
  404c25:	e9 9c f1 ff ff       	jmpq   403dc6 <__sin_sse2+0x846>
  404c2a:	66 0f 1f 44 00 00    	nopw   0x0(%rax,%rax,1)
  404c30:	66 45 0f 28 f1       	movapd %xmm9,%xmm14
  404c35:	f2 44 0f 10 25 0a 42 	movsd  0xa420a(%rip),%xmm12        # 4a8e48 <_IO_stdin_used+0x8>
  404c3c:	0a 00 
  404c3e:	66 45 0f 28 d9       	movapd %xmm9,%xmm11
  404c43:	f2 45 0f 59 f1       	mulsd  %xmm9,%xmm14
  404c48:	66 45 0f 28 e9       	movapd %xmm9,%xmm13
  404c4d:	f2 45 0f 58 dc       	addsd  %xmm12,%xmm11
  404c52:	66 45 0f 28 f9       	movapd %xmm9,%xmm15
  404c57:	f2 45 0f 59 d6       	mulsd  %xmm14,%xmm10
  404c5c:	f2 45 0f 5c dc       	subsd  %xmm12,%xmm11
  404c61:	f2 44 0f 10 25 e6 41 	movsd  0xa41e6(%rip),%xmm12        # 4a8e50 <_IO_stdin_used+0x10>
  404c68:	0a 00 
  404c6a:	f2 45 0f 58 d0       	addsd  %xmm8,%xmm10
  404c6f:	f2 45 0f 59 e3       	mulsd  %xmm11,%xmm12
  404c74:	f2 45 0f 5c eb       	subsd  %xmm11,%xmm13
  404c79:	f2 45 0f 59 d6       	mulsd  %xmm14,%xmm10
  404c7e:	f2 45 0f 59 e3       	mulsd  %xmm11,%xmm12
  404c83:	f2 44 0f 58 e9       	addsd  %xmm1,%xmm13
  404c88:	f2 44 0f 5c d7       	subsd  %xmm7,%xmm10
  404c8d:	f2 45 0f 59 e3       	mulsd  %xmm11,%xmm12
  404c92:	f2 44 0f 59 1d e5 41 	mulsd  0xa41e5(%rip),%xmm11        # 4a8e80 <_IO_stdin_used+0x40>
  404c99:	0a 00 
  404c9b:	f2 45 0f 59 d6       	mulsd  %xmm14,%xmm10
  404ca0:	f2 45 0f 58 fc       	addsd  %xmm12,%xmm15
  404ca5:	f2 44 0f 58 d0       	addsd  %xmm0,%xmm10
  404caa:	f2 0f 10 05 9e 41 0a 	movsd  0xa419e(%rip),%xmm0        # 4a8e50 <_IO_stdin_used+0x10>
  404cb1:	00 
  404cb2:	f2 45 0f 59 dd       	mulsd  %xmm13,%xmm11
  404cb7:	f2 41 0f 59 c5       	mulsd  %xmm13,%xmm0
  404cbc:	f2 45 0f 59 d6       	mulsd  %xmm14,%xmm10
  404cc1:	f2 41 0f 59 c5       	mulsd  %xmm13,%xmm0
  404cc6:	f2 44 0f 58 15 a9 41 	addsd  0xa41a9(%rip),%xmm10        # 4a8e78 <_IO_stdin_used+0x38>
  404ccd:	0a 00 
  404ccf:	f2 41 0f 59 c5       	mulsd  %xmm13,%xmm0
  404cd4:	f2 45 0f 59 d6       	mulsd  %xmm14,%xmm10
  404cd9:	f2 45 0f 58 d3       	addsd  %xmm11,%xmm10
  404cde:	f2 45 0f 59 d1       	mulsd  %xmm9,%xmm10
  404ce3:	f2 44 0f 58 d0       	addsd  %xmm0,%xmm10
  404ce8:	66 41 0f 28 c1       	movapd %xmm9,%xmm0
  404ced:	f2 41 0f 5c c7       	subsd  %xmm15,%xmm0
  404cf2:	f2 44 0f 58 d1       	addsd  %xmm1,%xmm10
  404cf7:	f2 41 0f 58 c4       	addsd  %xmm12,%xmm0
  404cfc:	f2 44 0f 58 d0       	addsd  %xmm0,%xmm10
  404d01:	66 41 0f 28 c7       	movapd %xmm15,%xmm0
  404d06:	f2 41 0f 58 c2       	addsd  %xmm10,%xmm0
  404d0b:	f2 44 0f 5c f8       	subsd  %xmm0,%xmm15
  404d10:	f2 45 0f 58 fa       	addsd  %xmm10,%xmm15
  404d15:	66 44 0f 2e fb       	ucomisd %xmm3,%xmm15
  404d1a:	f2 44 0f 59 3d 6d 41 	mulsd  0xa416d(%rip),%xmm15        # 4a8e90 <_IO_stdin_used+0x50>
  404d21:	0a 00 
  404d23:	0f 86 21 05 00 00    	jbe    40524a <__sin_sse2+0x1cca>
  404d29:	66 0f 2e d3          	ucomisd %xmm3,%xmm2
  404d2d:	0f 86 3c 05 00 00    	jbe    40526f <__sin_sse2+0x1cef>
  404d33:	f2 0f 10 3d 6d 41 0a 	movsd  0xa416d(%rip),%xmm7        # 4a8ea8 <_IO_stdin_used+0x68>
  404d3a:	00 
  404d3b:	f2 0f 59 fa          	mulsd  %xmm2,%xmm7
  404d3f:	f2 41 0f 58 ff       	addsd  %xmm15,%xmm7
  404d44:	f2 0f 58 f8          	addsd  %xmm0,%xmm7
  404d48:	66 0f 2e c7          	ucomisd %xmm7,%xmm0
  404d4c:	0f 8b 03 03 00 00    	jnp    405055 <__sin_sse2+0x1ad5>
  404d52:	66 44 0f 2e cb       	ucomisd %xmm3,%xmm9
  404d57:	f2 0f 11 5c 24 38    	movsd  %xmm3,0x38(%rsp)
  404d5d:	4c 8d 64 24 50       	lea    0x50(%rsp),%r12
  404d62:	f2 0f 11 54 24 30    	movsd  %xmm2,0x30(%rsp)
  404d68:	f2 0f 11 64 24 28    	movsd  %xmm4,0x28(%rsp)
  404d6e:	f2 0f 11 74 24 20    	movsd  %xmm6,0x20(%rsp)
  404d74:	f2 0f 11 6c 24 18    	movsd  %xmm5,0x18(%rsp)
  404d7a:	0f 86 59 05 00 00    	jbe    4052d9 <__sin_sse2+0x1d59>
  404d80:	66 41 0f 28 c1       	movapd %xmm9,%xmm0
  404d85:	4c 89 e7             	mov    %r12,%rdi
  404d88:	f2 44 0f 11 0c 24    	movsd  %xmm9,(%rsp)
  404d8e:	e8 7d 0c 00 00       	callq  405a10 <__dubsin>
  404d93:	f2 44 0f 10 0c 24    	movsd  (%rsp),%xmm9
  404d99:	f2 0f 10 6c 24 18    	movsd  0x18(%rsp),%xmm5
  404d9f:	f2 0f 10 74 24 20    	movsd  0x20(%rsp),%xmm6
  404da5:	f2 0f 10 64 24 28    	movsd  0x28(%rsp),%xmm4
  404dab:	f2 0f 10 54 24 30    	movsd  0x30(%rsp),%xmm2
  404db1:	f2 0f 10 5c 24 38    	movsd  0x38(%rsp),%xmm3
  404db7:	f2 0f 10 44 24 58    	movsd  0x58(%rsp),%xmm0
  404dbd:	f2 0f 10 3d db 40 0a 	movsd  0xa40db(%rip),%xmm7        # 4a8ea0 <_IO_stdin_used+0x60>
  404dc4:	00 
  404dc5:	66 0f 2e c3          	ucomisd %xmm3,%xmm0
  404dc9:	f2 0f 59 c7          	mulsd  %xmm7,%xmm0
  404dcd:	0f 86 ce 04 00 00    	jbe    4052a1 <__sin_sse2+0x1d21>
  404dd3:	66 0f 2e d3          	ucomisd %xmm3,%xmm2
  404dd7:	0f 86 ab 04 00 00    	jbe    405288 <__sin_sse2+0x1d08>
  404ddd:	f2 0f 10 0d cb 40 0a 	movsd  0xa40cb(%rip),%xmm1        # 4a8eb0 <_IO_stdin_used+0x70>
  404de4:	00 
  404de5:	f2 0f 59 ca          	mulsd  %xmm2,%xmm1
  404de9:	f2 0f 58 c1          	addsd  %xmm1,%xmm0
  404ded:	f2 0f 10 4c 24 50    	movsd  0x50(%rsp),%xmm1
  404df3:	f2 0f 58 c1          	addsd  %xmm1,%xmm0
  404df7:	66 0f 2e c8          	ucomisd %xmm0,%xmm1
  404dfb:	0f 8a 7f 02 00 00    	jp     405080 <__sin_sse2+0x1b00>
  404e01:	0f 85 79 02 00 00    	jne    405080 <__sin_sse2+0x1b00>
  404e07:	66 44 0f 2e cb       	ucomisd %xmm3,%xmm9
  404e0c:	66 0f 28 d1          	movapd %xmm1,%xmm2
  404e10:	0f 87 4a e8 ff ff    	ja     403660 <__sin_sse2+0xe0>
  404e16:	e9 16 eb ff ff       	jmpq   403931 <__sin_sse2+0x3b1>
  404e1b:	66 0f 2e d3          	ucomisd %xmm3,%xmm2
  404e1f:	f2 44 0f 11 1c 24    	movsd  %xmm11,(%rsp)
  404e25:	48 8b 04 24          	mov    (%rsp),%rax
  404e29:	0f 86 02 04 00 00    	jbe    405231 <__sin_sse2+0x1cb1>
  404e2f:	f2 0f 10 35 71 40 0a 	movsd  0xa4071(%rip),%xmm6        # 4a8ea8 <_IO_stdin_used+0x68>
  404e36:	00 
  404e37:	f2 0f 59 f2          	mulsd  %xmm2,%xmm6
  404e3b:	c1 e0 02             	shl    $0x2,%eax
  404e3e:	f2 0f 10 25 c2 40 0a 	movsd  0xa40c2(%rip),%xmm4        # 4a8f08 <big+0x18>
  404e45:	00 
  404e46:	48 63 d0             	movslq %eax,%rdx
  404e49:	66 44 0f 28 dd       	movapd %xmm5,%xmm11
  404e4e:	f2 44 0f 10 14 d5 00 	movsd  0x4a9a00(,%rdx,8),%xmm10
  404e55:	9a 4a 00 
  404e58:	8d 50 02             	lea    0x2(%rax),%edx
  404e5b:	f2 44 0f 58 dc       	addsd  %xmm4,%xmm11
  404e60:	48 63 d2             	movslq %edx,%rdx
  404e63:	f2 41 0f 59 c2       	mulsd  %xmm10,%xmm0
  404e68:	f2 44 0f 10 24 d5 00 	movsd  0x4a9a00(,%rdx,8),%xmm12
  404e6f:	9a 4a 00 
  404e72:	8d 50 03             	lea    0x3(%rax),%edx
  404e75:	83 c0 01             	add    $0x1,%eax
  404e78:	48 98                	cltq   
  404e7a:	66 41 0f 28 fc       	movapd %xmm12,%xmm7
  404e7f:	48 63 d2             	movslq %edx,%rdx
  404e82:	f2 44 0f 5c dc       	subsd  %xmm4,%xmm11
  404e87:	f2 44 0f 10 2c d5 00 	movsd  0x4a9a00(,%rdx,8),%xmm13
  404e8e:	9a 4a 00 
  404e91:	f2 0f 58 fc          	addsd  %xmm4,%xmm7
  404e95:	f2 0f 5c fc          	subsd  %xmm4,%xmm7
  404e99:	66 41 0f 28 e0       	movapd %xmm8,%xmm4
  404e9e:	f2 45 0f 59 c4       	mulsd  %xmm12,%xmm8
  404ea3:	f2 41 0f 59 e5       	mulsd  %xmm13,%xmm4
  404ea8:	f2 44 0f 5c e7       	subsd  %xmm7,%xmm12
  404ead:	f2 0f 58 24 c5 00 9a 	addsd  0x4a9a00(,%rax,8),%xmm4
  404eb4:	4a 00 
  404eb6:	f2 41 0f 58 e0       	addsd  %xmm8,%xmm4
  404ebb:	66 45 0f 28 c4       	movapd %xmm12,%xmm8
  404ec0:	f2 45 0f 58 c5       	addsd  %xmm13,%xmm8
  404ec5:	f2 44 0f 59 c5       	mulsd  %xmm5,%xmm8
  404eca:	f2 41 0f 58 e0       	addsd  %xmm8,%xmm4
  404ecf:	66 44 0f 28 c5       	movapd %xmm5,%xmm8
  404ed4:	f2 41 0f 59 ea       	mulsd  %xmm10,%xmm5
  404ed9:	f2 45 0f 5c c3       	subsd  %xmm11,%xmm8
  404ede:	f2 0f 59 e9          	mulsd  %xmm1,%xmm5
  404ee2:	f2 44 0f 58 c1       	addsd  %xmm1,%xmm8
  404ee7:	f2 44 0f 59 c7       	mulsd  %xmm7,%xmm8
  404eec:	f2 41 0f 59 fb       	mulsd  %xmm11,%xmm7
  404ef1:	f2 41 0f 58 e0       	addsd  %xmm8,%xmm4
  404ef6:	f2 0f 5c e5          	subsd  %xmm5,%xmm4
  404efa:	f2 0f 5c e0          	subsd  %xmm0,%xmm4
  404efe:	66 41 0f 28 c2       	movapd %xmm10,%xmm0
  404f03:	f2 0f 58 c7          	addsd  %xmm7,%xmm0
  404f07:	f2 44 0f 5c d0       	subsd  %xmm0,%xmm10
  404f0c:	66 0f 28 e8          	movapd %xmm0,%xmm5
  404f10:	f2 44 0f 58 d7       	addsd  %xmm7,%xmm10
  404f15:	f2 41 0f 58 e2       	addsd  %xmm10,%xmm4
  404f1a:	f2 0f 58 ec          	addsd  %xmm4,%xmm5
  404f1e:	f2 0f 5c c5          	subsd  %xmm5,%xmm0
  404f22:	f2 0f 58 c4          	addsd  %xmm4,%xmm0
  404f26:	66 0f 2e c3          	ucomisd %xmm3,%xmm0
  404f2a:	f2 0f 59 05 5e 3f 0a 	mulsd  0xa3f5e(%rip),%xmm0        # 4a8e90 <_IO_stdin_used+0x50>
  404f31:	00 
  404f32:	0f 86 14 01 00 00    	jbe    40504c <__sin_sse2+0x1acc>
  404f38:	f2 0f 58 c6          	addsd  %xmm6,%xmm0
  404f3c:	f2 0f 58 c5          	addsd  %xmm5,%xmm0
  404f40:	66 0f 2e c5          	ucomisd %xmm5,%xmm0
  404f44:	0f 8a 2e 02 00 00    	jp     405178 <__sin_sse2+0x1bf8>
  404f4a:	0f 85 28 02 00 00    	jne    405178 <__sin_sse2+0x1bf8>
  404f50:	45 85 e4             	test   %r12d,%r12d
  404f53:	66 0f 28 d5          	movapd %xmm5,%xmm2
  404f57:	0f 85 03 e7 ff ff    	jne    403660 <__sin_sse2+0xe0>
  404f5d:	0f 1f 00             	nopl   (%rax)
  404f60:	e9 cc e9 ff ff       	jmpq   403931 <__sin_sse2+0x3b1>
  404f65:	f2 45 0f 5c ec       	subsd  %xmm12,%xmm13
  404f6a:	e9 71 ec ff ff       	jmpq   403be0 <__sin_sse2+0x660>
  404f6f:	f2 41 0f 5c f4       	subsd  %xmm12,%xmm6
  404f74:	e9 6c f7 ff ff       	jmpq   4046e5 <__sin_sse2+0x1165>
  404f79:	f2 0f 10 05 3f 40 0a 	movsd  0xa403f(%rip),%xmm0        # 4a8fc0 <hp1+0x78>
  404f80:	00 
  404f81:	45 30 e4             	xor    %r12b,%r12b
  404f84:	66 44 0f 57 c8       	xorpd  %xmm0,%xmm9
  404f89:	66 0f 57 c8          	xorpd  %xmm0,%xmm1
  404f8d:	e9 44 f6 ff ff       	jmpq   4045d6 <__sin_sse2+0x1056>
  404f92:	f2 0f 5c 25 f6 3f 0a 	subsd  0xa3ff6(%rip),%xmm4        # 4a8f90 <hp1+0x48>
  404f99:	00 
  404f9a:	e9 00 f6 ff ff       	jmpq   40459f <__sin_sse2+0x101f>
  404f9f:	f2 0f 10 25 19 40 0a 	movsd  0xa4019(%rip),%xmm4        # 4a8fc0 <hp1+0x78>
  404fa6:	00 
  404fa7:	66 0f 57 c4          	xorpd  %xmm4,%xmm0
  404fab:	66 0f 57 cc          	xorpd  %xmm4,%xmm1
  404faf:	e9 f2 f4 ff ff       	jmpq   4044a6 <__sin_sse2+0xf26>
  404fb4:	f2 0f 10 44 24 40    	movsd  0x40(%rsp),%xmm0
  404fba:	f2 0f 10 1d 8e 3f 0a 	movsd  0xa3f8e(%rip),%xmm3        # 4a8f50 <hp1+0x8>
  404fc1:	00 
  404fc2:	66 0f 28 c8          	movapd %xmm0,%xmm1
  404fc6:	f2 0f 59 c8          	mulsd  %xmm0,%xmm1
  404fca:	66 0f 2e d9          	ucomisd %xmm1,%xmm3
  404fce:	f2 0f 10 1d ea 3f 0a 	movsd  0xa3fea(%rip),%xmm3        # 4a8fc0 <hp1+0x78>
  404fd5:	00 
  404fd6:	f2 0f 10 4c 24 50    	movsd  0x50(%rsp),%xmm1
  404fdc:	66 0f 57 c3          	xorpd  %xmm3,%xmm0
  404fe0:	66 0f 57 cb          	xorpd  %xmm3,%xmm1
  404fe4:	0f 86 13 f8 ff ff    	jbe    4047fd <__sin_sse2+0x127d>
  404fea:	e9 ba ed ff ff       	jmpq   403da9 <__sin_sse2+0x829>
  404fef:	f2 0f 5c 24 24       	subsd  (%rsp),%xmm4
  404ff4:	e9 79 f9 ff ff       	jmpq   404972 <__sin_sse2+0x13f2>
  404ff9:	f2 0f 10 05 bf 3f 0a 	movsd  0xa3fbf(%rip),%xmm0        # 4a8fc0 <hp1+0x78>
  405000:	00 
  405001:	66 0f 57 c2          	xorpd  %xmm2,%xmm0
  405005:	f2 0f 59 05 9b 3e 0a 	mulsd  0xa3e9b(%rip),%xmm0        # 4a8ea8 <_IO_stdin_used+0x68>
  40500c:	00 
  40500d:	f2 0f 11 04 24       	movsd  %xmm0,(%rsp)
  405012:	e9 2f f8 ff ff       	jmpq   404846 <__sin_sse2+0x12c6>
  405017:	f2 0f 5c 25 71 3f 0a 	subsd  0xa3f71(%rip),%xmm4        # 4a8f90 <hp1+0x48>
  40501e:	00 
  40501f:	e9 75 ed ff ff       	jmpq   403d99 <__sin_sse2+0x819>
  405024:	f2 0f 5c 25 64 3f 0a 	subsd  0xa3f64(%rip),%xmm4        # 4a8f90 <hp1+0x48>
  40502b:	00 
  40502c:	e9 1a fb ff ff       	jmpq   404b4b <__sin_sse2+0x15cb>
  405031:	f2 0f 10 3d 87 3f 0a 	movsd  0xa3f87(%rip),%xmm7        # 4a8fc0 <hp1+0x78>
  405038:	00 
  405039:	31 f6                	xor    %esi,%esi
  40503b:	66 0f 28 e0          	movapd %xmm0,%xmm4
  40503f:	66 0f 57 e7          	xorpd  %xmm7,%xmm4
  405043:	66 0f 57 f9          	xorpd  %xmm1,%xmm7
  405047:	e9 ff f9 ff ff       	jmpq   404a4b <__sin_sse2+0x14cb>
  40504c:	f2 0f 5c c6          	subsd  %xmm6,%xmm0
  405050:	e9 e7 fe ff ff       	jmpq   404f3c <__sin_sse2+0x19bc>
  405055:	0f 85 f7 fc ff ff    	jne    404d52 <__sin_sse2+0x17d2>
  40505b:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)
  405060:	e9 21 fb ff ff       	jmpq   404b86 <__sin_sse2+0x1606>
  405065:	66 0f 57 c9          	xorpd  %xmm1,%xmm1
  405069:	bf 01 00 00 00       	mov    $0x1,%edi
  40506e:	66 0f 28 c2          	movapd %xmm2,%xmm0
  405072:	e8 79 33 00 00       	callq  4083f0 <__mpsin>
  405077:	66 0f 28 d0          	movapd %xmm0,%xmm2
  40507b:	e9 e0 e5 ff ff       	jmpq   403660 <__sin_sse2+0xe0>
  405080:	f2 0f 11 2c 24       	movsd  %xmm5,(%rsp)
  405085:	66 0f 28 c4          	movapd %xmm4,%xmm0
  405089:	f2 0f 10 2d 47 3e 0a 	movsd  0xa3e47(%rip),%xmm5        # 4a8ed8 <mp1+0x10>
  405090:	00 
  405091:	48 8b 04 24          	mov    (%rsp),%rax
  405095:	f2 0f 59 ee          	mulsd  %xmm6,%xmm5
  405099:	f2 0f 59 35 3f 3e 0a 	mulsd  0xa3e3f(%rip),%xmm6        # 4a8ee0 <mp1+0x18>
  4050a0:	00 
  4050a1:	a8 02                	test   $0x2,%al
  4050a3:	f2 0f 5c c5          	subsd  %xmm5,%xmm0
  4050a7:	f2 0f 5c e0          	subsd  %xmm0,%xmm4
  4050ab:	66 0f 28 cc          	movapd %xmm4,%xmm1
  4050af:	66 0f 28 e0          	movapd %xmm0,%xmm4
  4050b3:	f2 0f 5c cd          	subsd  %xmm5,%xmm1
  4050b7:	f2 0f 5c e6          	subsd  %xmm6,%xmm4
  4050bb:	f2 0f 5c c4          	subsd  %xmm4,%xmm0
  4050bf:	f2 0f 5c c6          	subsd  %xmm6,%xmm0
  4050c3:	f2 0f 58 c8          	addsd  %xmm0,%xmm1
  4050c7:	74 10                	je     4050d9 <__sin_sse2+0x1b59>
  4050c9:	f2 0f 10 05 ef 3e 0a 	movsd  0xa3eef(%rip),%xmm0        # 4a8fc0 <hp1+0x78>
  4050d0:	00 
  4050d1:	66 0f 57 e0          	xorpd  %xmm0,%xmm4
  4050d5:	66 0f 57 c8          	xorpd  %xmm0,%xmm1
  4050d9:	66 0f 2e e3          	ucomisd %xmm3,%xmm4
  4050dd:	f2 0f 11 5c 24 28    	movsd  %xmm3,0x28(%rsp)
  4050e3:	f2 0f 11 7c 24 20    	movsd  %xmm7,0x20(%rsp)
  4050e9:	f2 0f 11 54 24 18    	movsd  %xmm2,0x18(%rsp)
  4050ef:	0f 86 ea 02 00 00    	jbe    4053df <__sin_sse2+0x1e5f>
  4050f5:	66 0f 28 c4          	movapd %xmm4,%xmm0
  4050f9:	4c 89 e7             	mov    %r12,%rdi
  4050fc:	f2 0f 11 24 24       	movsd  %xmm4,(%rsp)
  405101:	e8 0a 09 00 00       	callq  405a10 <__dubsin>
  405106:	f2 0f 10 24 24       	movsd  (%rsp),%xmm4
  40510b:	f2 0f 10 54 24 18    	movsd  0x18(%rsp),%xmm2
  405111:	f2 0f 10 7c 24 20    	movsd  0x20(%rsp),%xmm7
  405117:	f2 0f 10 5c 24 28    	movsd  0x28(%rsp),%xmm3
  40511d:	f2 0f 10 44 24 58    	movsd  0x58(%rsp),%xmm0
  405123:	66 0f 2e c3          	ucomisd %xmm3,%xmm0
  405127:	f2 0f 59 c7          	mulsd  %xmm7,%xmm0
  40512b:	0f 86 93 02 00 00    	jbe    4053c4 <__sin_sse2+0x1e44>
  405131:	66 0f 2e d3          	ucomisd %xmm3,%xmm2
  405135:	0f 86 dd 02 00 00    	jbe    405418 <__sin_sse2+0x1e98>
  40513b:	f2 0f 10 0d a5 3d 0a 	movsd  0xa3da5(%rip),%xmm1        # 4a8ee8 <mp1+0x20>
  405142:	00 
  405143:	f2 0f 59 ca          	mulsd  %xmm2,%xmm1
  405147:	f2 0f 58 c1          	addsd  %xmm1,%xmm0
  40514b:	f2 0f 10 4c 24 50    	movsd  0x50(%rsp),%xmm1
  405151:	f2 0f 58 c1          	addsd  %xmm1,%xmm0
  405155:	66 0f 2e c8          	ucomisd %xmm0,%xmm1
  405159:	0f 8a 06 ff ff ff    	jp     405065 <__sin_sse2+0x1ae5>
  40515f:	0f 85 00 ff ff ff    	jne    405065 <__sin_sse2+0x1ae5>
  405165:	66 0f 2e e3          	ucomisd %xmm3,%xmm4
  405169:	66 0f 28 d1          	movapd %xmm1,%xmm2
  40516d:	0f 87 ed e4 ff ff    	ja     403660 <__sin_sse2+0xe0>
  405173:	e9 b9 e7 ff ff       	jmpq   403931 <__sin_sse2+0x3b1>
  405178:	66 41 0f 28 c1       	movapd %xmm9,%xmm0
  40517d:	48 8d 7c 24 50       	lea    0x50(%rsp),%rdi
  405182:	f2 0f 11 5c 24 18    	movsd  %xmm3,0x18(%rsp)
  405188:	f2 0f 11 14 24       	movsd  %xmm2,(%rsp)
  40518d:	e8 7e 08 00 00       	callq  405a10 <__dubsin>
  405192:	f2 0f 10 44 24 58    	movsd  0x58(%rsp),%xmm0
  405198:	f2 0f 10 5c 24 18    	movsd  0x18(%rsp),%xmm3
  40519e:	66 0f 28 c8          	movapd %xmm0,%xmm1
  4051a2:	f2 0f 10 14 24       	movsd  (%rsp),%xmm2
  4051a7:	66 0f 2e c3          	ucomisd %xmm3,%xmm0
  4051ab:	f2 0f 59 0d 75 3d 0a 	mulsd  0xa3d75(%rip),%xmm1        # 4a8f28 <big+0x38>
  4051b2:	00 
  4051b3:	0f 86 cf 01 00 00    	jbe    405388 <__sin_sse2+0x1e08>
  4051b9:	66 0f 2e d3          	ucomisd %xmm3,%xmm2
  4051bd:	0f 86 ac 01 00 00    	jbe    40536f <__sin_sse2+0x1def>
  4051c3:	f2 0f 10 05 e5 3c 0a 	movsd  0xa3ce5(%rip),%xmm0        # 4a8eb0 <_IO_stdin_used+0x70>
  4051ca:	00 
  4051cb:	f2 0f 59 c2          	mulsd  %xmm2,%xmm0
  4051cf:	f2 0f 58 c1          	addsd  %xmm1,%xmm0
  4051d3:	f2 0f 10 4c 24 50    	movsd  0x50(%rsp),%xmm1
  4051d9:	f2 0f 58 c1          	addsd  %xmm1,%xmm0
  4051dd:	66 0f 2e c8          	ucomisd %xmm0,%xmm1
  4051e1:	0f 8a 7e fe ff ff    	jp     405065 <__sin_sse2+0x1ae5>
  4051e7:	0f 85 78 fe ff ff    	jne    405065 <__sin_sse2+0x1ae5>
  4051ed:	41 83 ec 01          	sub    $0x1,%r12d
  4051f1:	66 0f 28 d1          	movapd %xmm1,%xmm2
  4051f5:	0f 84 65 e4 ff ff    	je     403660 <__sin_sse2+0xe0>
  4051fb:	e9 31 e7 ff ff       	jmpq   403931 <__sin_sse2+0x3b1>
  405200:	0f ae 54 24 50       	ldmxcsr 0x50(%rsp)
  405205:	bd 01 00 00 00       	mov    $0x1,%ebp
  40520a:	e9 99 e3 ff ff       	jmpq   4035a8 <__sin_sse2+0x28>
  40520f:	0f ae 5c 24 50       	stmxcsr 0x50(%rsp)
  405214:	8b 44 24 50          	mov    0x50(%rsp),%eax
  405218:	81 e3 00 60 00 00    	and    $0x6000,%ebx
  40521e:	80 e4 9f             	and    $0x9f,%ah
  405221:	09 c3                	or     %eax,%ebx
  405223:	89 5c 24 50          	mov    %ebx,0x50(%rsp)
  405227:	0f ae 54 24 50       	ldmxcsr 0x50(%rsp)
  40522c:	e9 38 e4 ff ff       	jmpq   403669 <__sin_sse2+0xe9>
  405231:	f2 0f 10 35 87 3d 0a 	movsd  0xa3d87(%rip),%xmm6        # 4a8fc0 <hp1+0x78>
  405238:	00 
  405239:	66 0f 57 f2          	xorpd  %xmm2,%xmm6
  40523d:	f2 0f 59 35 63 3c 0a 	mulsd  0xa3c63(%rip),%xmm6        # 4a8ea8 <_IO_stdin_used+0x68>
  405244:	00 
  405245:	e9 f1 fb ff ff       	jmpq   404e3b <__sin_sse2+0x18bb>
  40524a:	66 0f 2e d3          	ucomisd %xmm3,%xmm2
  40524e:	0f 86 57 01 00 00    	jbe    4053ab <__sin_sse2+0x1e2b>
  405254:	f2 0f 10 3d 4c 3c 0a 	movsd  0xa3c4c(%rip),%xmm7        # 4a8ea8 <_IO_stdin_used+0x68>
  40525b:	00 
  40525c:	f2 0f 59 fa          	mulsd  %xmm2,%xmm7
  405260:	f2 44 0f 5c ff       	subsd  %xmm7,%xmm15
  405265:	66 41 0f 28 ff       	movapd %xmm15,%xmm7
  40526a:	e9 d5 fa ff ff       	jmpq   404d44 <__sin_sse2+0x17c4>
  40526f:	f2 0f 10 3d 49 3d 0a 	movsd  0xa3d49(%rip),%xmm7        # 4a8fc0 <hp1+0x78>
  405276:	00 
  405277:	66 0f 57 fa          	xorpd  %xmm2,%xmm7
  40527b:	f2 0f 59 3d 25 3c 0a 	mulsd  0xa3c25(%rip),%xmm7        # 4a8ea8 <_IO_stdin_used+0x68>
  405282:	00 
  405283:	e9 b7 fa ff ff       	jmpq   404d3f <__sin_sse2+0x17bf>
  405288:	f2 0f 10 0d 30 3d 0a 	movsd  0xa3d30(%rip),%xmm1        # 4a8fc0 <hp1+0x78>
  40528f:	00 
  405290:	66 0f 57 ca          	xorpd  %xmm2,%xmm1
  405294:	f2 0f 59 0d 14 3c 0a 	mulsd  0xa3c14(%rip),%xmm1        # 4a8eb0 <_IO_stdin_used+0x70>
  40529b:	00 
  40529c:	e9 48 fb ff ff       	jmpq   404de9 <__sin_sse2+0x1869>
  4052a1:	66 0f 2e d3          	ucomisd %xmm3,%xmm2
  4052a5:	0f 86 95 00 00 00    	jbe    405340 <__sin_sse2+0x1dc0>
  4052ab:	f2 0f 10 0d fd 3b 0a 	movsd  0xa3bfd(%rip),%xmm1        # 4a8eb0 <_IO_stdin_used+0x70>
  4052b2:	00 
  4052b3:	f2 0f 59 ca          	mulsd  %xmm2,%xmm1
  4052b7:	f2 0f 5c c1          	subsd  %xmm1,%xmm0
  4052bb:	e9 2d fb ff ff       	jmpq   404ded <__sin_sse2+0x186d>
  4052c0:	f2 0f 10 05 f8 3c 0a 	movsd  0xa3cf8(%rip),%xmm0        # 4a8fc0 <hp1+0x78>
  4052c7:	00 
  4052c8:	66 0f 57 c2          	xorpd  %xmm2,%xmm0
  4052cc:	f2 0f 59 05 dc 3b 0a 	mulsd  0xa3bdc(%rip),%xmm0        # 4a8eb0 <_IO_stdin_used+0x70>
  4052d3:	00 
  4052d4:	e9 00 f7 ff ff       	jmpq   4049d9 <__sin_sse2+0x1459>
  4052d9:	f2 0f 10 05 df 3c 0a 	movsd  0xa3cdf(%rip),%xmm0        # 4a8fc0 <hp1+0x78>
  4052e0:	00 
  4052e1:	4c 89 e7             	mov    %r12,%rdi
  4052e4:	f2 44 0f 11 0c 24    	movsd  %xmm9,(%rsp)
  4052ea:	66 0f 57 c8          	xorpd  %xmm0,%xmm1
  4052ee:	66 41 0f 57 c1       	xorpd  %xmm9,%xmm0
  4052f3:	e8 18 07 00 00       	callq  405a10 <__dubsin>
  4052f8:	f2 0f 10 5c 24 38    	movsd  0x38(%rsp),%xmm3
  4052fe:	f2 0f 10 54 24 30    	movsd  0x30(%rsp),%xmm2
  405304:	f2 0f 10 64 24 28    	movsd  0x28(%rsp),%xmm4
  40530a:	f2 0f 10 74 24 20    	movsd  0x20(%rsp),%xmm6
  405310:	f2 0f 10 6c 24 18    	movsd  0x18(%rsp),%xmm5
  405316:	f2 44 0f 10 0c 24    	movsd  (%rsp),%xmm9
  40531c:	e9 96 fa ff ff       	jmpq   404db7 <__sin_sse2+0x1837>
  405321:	66 0f 2e d3          	ucomisd %xmm3,%xmm2
  405325:	76 32                	jbe    405359 <__sin_sse2+0x1dd9>
  405327:	f2 0f 10 05 81 3b 0a 	movsd  0xa3b81(%rip),%xmm0        # 4a8eb0 <_IO_stdin_used+0x70>
  40532e:	00 
  40532f:	f2 0f 59 c2          	mulsd  %xmm2,%xmm0
  405333:	f2 0f 5c c8          	subsd  %xmm0,%xmm1
  405337:	66 0f 28 c1          	movapd %xmm1,%xmm0
  40533b:	e9 9d f6 ff ff       	jmpq   4049dd <__sin_sse2+0x145d>
  405340:	f2 0f 10 0d 78 3c 0a 	movsd  0xa3c78(%rip),%xmm1        # 4a8fc0 <hp1+0x78>
  405347:	00 
  405348:	66 0f 57 ca          	xorpd  %xmm2,%xmm1
  40534c:	f2 0f 59 0d 5c 3b 0a 	mulsd  0xa3b5c(%rip),%xmm1        # 4a8eb0 <_IO_stdin_used+0x70>
  405353:	00 
  405354:	e9 5e ff ff ff       	jmpq   4052b7 <__sin_sse2+0x1d37>
  405359:	f2 0f 10 05 5f 3c 0a 	movsd  0xa3c5f(%rip),%xmm0        # 4a8fc0 <hp1+0x78>
  405360:	00 
  405361:	66 0f 57 c2          	xorpd  %xmm2,%xmm0
  405365:	f2 0f 59 05 43 3b 0a 	mulsd  0xa3b43(%rip),%xmm0        # 4a8eb0 <_IO_stdin_used+0x70>
  40536c:	00 
  40536d:	eb c4                	jmp    405333 <__sin_sse2+0x1db3>
  40536f:	f2 0f 10 05 49 3c 0a 	movsd  0xa3c49(%rip),%xmm0        # 4a8fc0 <hp1+0x78>
  405376:	00 
  405377:	66 0f 57 c2          	xorpd  %xmm2,%xmm0
  40537b:	f2 0f 59 05 2d 3b 0a 	mulsd  0xa3b2d(%rip),%xmm0        # 4a8eb0 <_IO_stdin_used+0x70>
  405382:	00 
  405383:	e9 47 fe ff ff       	jmpq   4051cf <__sin_sse2+0x1c4f>
  405388:	66 0f 2e d3          	ucomisd %xmm3,%xmm2
  40538c:	0f 86 b5 00 00 00    	jbe    405447 <__sin_sse2+0x1ec7>
  405392:	f2 0f 10 05 16 3b 0a 	movsd  0xa3b16(%rip),%xmm0        # 4a8eb0 <_IO_stdin_used+0x70>
  405399:	00 
  40539a:	f2 0f 59 c2          	mulsd  %xmm2,%xmm0
  40539e:	f2 0f 5c c8          	subsd  %xmm0,%xmm1
  4053a2:	66 0f 28 c1          	movapd %xmm1,%xmm0
  4053a6:	e9 28 fe ff ff       	jmpq   4051d3 <__sin_sse2+0x1c53>
  4053ab:	f2 0f 10 3d 0d 3c 0a 	movsd  0xa3c0d(%rip),%xmm7        # 4a8fc0 <hp1+0x78>
  4053b2:	00 
  4053b3:	66 0f 57 fa          	xorpd  %xmm2,%xmm7
  4053b7:	f2 0f 59 3d e9 3a 0a 	mulsd  0xa3ae9(%rip),%xmm7        # 4a8ea8 <_IO_stdin_used+0x68>
  4053be:	00 
  4053bf:	e9 9c fe ff ff       	jmpq   405260 <__sin_sse2+0x1ce0>
  4053c4:	66 0f 2e d3          	ucomisd %xmm3,%xmm2
  4053c8:	76 67                	jbe    405431 <__sin_sse2+0x1eb1>
  4053ca:	f2 0f 10 0d 16 3b 0a 	movsd  0xa3b16(%rip),%xmm1        # 4a8ee8 <mp1+0x20>
  4053d1:	00 
  4053d2:	f2 0f 59 ca          	mulsd  %xmm2,%xmm1
  4053d6:	f2 0f 5c c1          	subsd  %xmm1,%xmm0
  4053da:	e9 6c fd ff ff       	jmpq   40514b <__sin_sse2+0x1bcb>
  4053df:	f2 0f 10 05 d9 3b 0a 	movsd  0xa3bd9(%rip),%xmm0        # 4a8fc0 <hp1+0x78>
  4053e6:	00 
  4053e7:	4c 89 e7             	mov    %r12,%rdi
  4053ea:	f2 0f 11 24 24       	movsd  %xmm4,(%rsp)
  4053ef:	66 0f 57 c8          	xorpd  %xmm0,%xmm1
  4053f3:	66 0f 57 c4          	xorpd  %xmm4,%xmm0
  4053f7:	e8 14 06 00 00       	callq  405a10 <__dubsin>
  4053fc:	f2 0f 10 5c 24 28    	movsd  0x28(%rsp),%xmm3
  405402:	f2 0f 10 7c 24 20    	movsd  0x20(%rsp),%xmm7
  405408:	f2 0f 10 54 24 18    	movsd  0x18(%rsp),%xmm2
  40540e:	f2 0f 10 24 24       	movsd  (%rsp),%xmm4
  405413:	e9 05 fd ff ff       	jmpq   40511d <__sin_sse2+0x1b9d>
  405418:	f2 0f 10 0d a0 3b 0a 	movsd  0xa3ba0(%rip),%xmm1        # 4a8fc0 <hp1+0x78>
  40541f:	00 
  405420:	66 0f 57 ca          	xorpd  %xmm2,%xmm1
  405424:	f2 0f 59 0d bc 3a 0a 	mulsd  0xa3abc(%rip),%xmm1        # 4a8ee8 <mp1+0x20>
  40542b:	00 
  40542c:	e9 16 fd ff ff       	jmpq   405147 <__sin_sse2+0x1bc7>
  405431:	f2 0f 10 0d 87 3b 0a 	movsd  0xa3b87(%rip),%xmm1        # 4a8fc0 <hp1+0x78>
  405438:	00 
  405439:	66 0f 57 ca          	xorpd  %xmm2,%xmm1
  40543d:	f2 0f 59 0d a3 3a 0a 	mulsd  0xa3aa3(%rip),%xmm1        # 4a8ee8 <mp1+0x20>
  405444:	00 
  405445:	eb 8f                	jmp    4053d6 <__sin_sse2+0x1e56>
  405447:	f2 0f 10 05 71 3b 0a 	movsd  0xa3b71(%rip),%xmm0        # 4a8fc0 <hp1+0x78>
  40544e:	00 
  40544f:	66 0f 57 c2          	xorpd  %xmm2,%xmm0
  405453:	f2 0f 59 05 55 3a 0a 	mulsd  0xa3a55(%rip),%xmm0        # 4a8eb0 <_IO_stdin_used+0x70>
  40545a:	00 
  40545b:	e9 3e ff ff ff       	jmpq   40539e <__sin_sse2+0x1e1e>
~~~

~~~
000000000040fdf0 <__sin_avx>:
  40fdf0:	41 54                	push   %r12
  40fdf2:	c5 f9 28 d0          	vmovapd %xmm0,%xmm2
  40fdf6:	55                   	push   %rbp
  40fdf7:	53                   	push   %rbx
  40fdf8:	48 83 ec 60          	sub    $0x60,%rsp
  40fdfc:	c5 f8 ae 5c 24 40    	vstmxcsr 0x40(%rsp)
  40fe02:	8b 5c 24 40          	mov    0x40(%rsp),%ebx
  40fe06:	89 d8                	mov    %ebx,%eax
  40fe08:	80 e4 9f             	and    $0x9f,%ah
  40fe0b:	39 c3                	cmp    %eax,%ebx
  40fe0d:	89 44 24 50          	mov    %eax,0x50(%rsp)
  40fe11:	0f 85 aa 1b 00 00    	jne    4119c1 <__sin_avx+0x1bd1>
  40fe17:	31 ed                	xor    %ebp,%ebp
  40fe19:	c5 fb 11 14 24       	vmovsd %xmm2,(%rsp)
  40fe1e:	48 8b 14 24          	mov    (%rsp),%rdx
  40fe22:	48 89 d1             	mov    %rdx,%rcx
  40fe25:	48 c1 f9 20          	sar    $0x20,%rcx
  40fe29:	89 c8                	mov    %ecx,%eax
  40fe2b:	25 ff ff ff 7f       	and    $0x7fffffff,%eax
  40fe30:	3d ff ff 4f 3e       	cmp    $0x3e4fffff,%eax
  40fe35:	0f 8e 95 00 00 00    	jle    40fed0 <__sin_avx+0xe0>
  40fe3b:	3d ff ff cf 3f       	cmp    $0x3fcfffff,%eax
  40fe40:	0f 8f aa 00 00 00    	jg     40fef0 <__sin_avx+0x100>
  40fe46:	c5 f9 28 e2          	vmovapd %xmm2,%xmm4
  40fe4a:	c5 fb 10 05 06 90 09 	vmovsd 0x99006(%rip),%xmm0        # 4a8e58 <_IO_stdin_used+0x18>
  40fe51:	00 
  40fe52:	c5 f9 28 ea          	vmovapd %xmm2,%xmm5
  40fe56:	c5 db 59 e2          	vmulsd %xmm2,%xmm4,%xmm4
  40fe5a:	c5 fb 59 c4          	vmulsd %xmm4,%xmm0,%xmm0
  40fe5e:	c5 f9 28 cc          	vmovapd %xmm4,%xmm1
  40fe62:	c5 f3 59 ca          	vmulsd %xmm2,%xmm1,%xmm1
  40fe66:	c5 fb 58 05 f2 8f 09 	vaddsd 0x98ff2(%rip),%xmm0,%xmm0        # 4a8e60 <_IO_stdin_used+0x20>
  40fe6d:	00 
  40fe6e:	c5 fb 59 c4          	vmulsd %xmm4,%xmm0,%xmm0
  40fe72:	c5 fb 5c 05 ee 8f 09 	vsubsd 0x98fee(%rip),%xmm0,%xmm0        # 4a8e68 <_IO_stdin_used+0x28>
  40fe79:	00 
  40fe7a:	c5 fb 59 c4          	vmulsd %xmm4,%xmm0,%xmm0
  40fe7e:	c5 fb 58 05 ea 8f 09 	vaddsd 0x98fea(%rip),%xmm0,%xmm0        # 4a8e70 <_IO_stdin_used+0x30>
  40fe85:	00 
  40fe86:	c5 fb 59 c4          	vmulsd %xmm4,%xmm0,%xmm0
  40fe8a:	c5 f9 28 d8          	vmovapd %xmm0,%xmm3
  40fe8e:	c5 e3 5c 1d c2 90 09 	vsubsd 0x990c2(%rip),%xmm3,%xmm3        # 4a8f58 <hp1+0x10>
  40fe95:	00 
  40fe96:	c5 e3 59 d9          	vmulsd %xmm1,%xmm3,%xmm3
  40fe9a:	c5 f9 28 ca          	vmovapd %xmm2,%xmm1
  40fe9e:	c5 d3 58 eb          	vaddsd %xmm3,%xmm5,%xmm5
  40fea2:	c5 f3 5c cd          	vsubsd %xmm5,%xmm1,%xmm1
  40fea6:	c5 f3 58 cb          	vaddsd %xmm3,%xmm1,%xmm1
  40feaa:	c5 f3 59 0d ee 90 09 	vmulsd 0x990ee(%rip),%xmm1,%xmm1        # 4a8fa0 <hp1+0x58>
  40feb1:	00 
  40feb2:	c5 f3 58 cd          	vaddsd %xmm5,%xmm1,%xmm1
  40feb6:	c5 f9 2e cd          	vucomisd %xmm5,%xmm1
  40feba:	0f 8a e0 02 00 00    	jp     4101a0 <__sin_avx+0x3b0>
  40fec0:	0f 85 da 02 00 00    	jne    4101a0 <__sin_avx+0x3b0>
  40fec6:	c5 f9 28 d5          	vmovapd %xmm5,%xmm2
  40feca:	66 0f 1f 44 00 00    	nopw   0x0(%rax,%rax,1)
  40fed0:	40 84 ed             	test   %bpl,%bpl
  40fed3:	0f 85 f8 1a 00 00    	jne    4119d1 <__sin_avx+0x1be1>
  40fed9:	48 83 c4 60          	add    $0x60,%rsp
  40fedd:	c5 f9 28 c2          	vmovapd %xmm2,%xmm0
  40fee1:	5b                   	pop    %rbx
  40fee2:	5d                   	pop    %rbp
  40fee3:	41 5c                	pop    %r12
  40fee5:	c3                   	retq   
  40fee6:	66 2e 0f 1f 84 00 00 	nopw   %cs:0x0(%rax,%rax,1)
  40feed:	00 00 00 
  40fef0:	3d ff 5f eb 3f       	cmp    $0x3feb5fff,%eax
  40fef5:	0f 8f 35 01 00 00    	jg     410030 <__sin_avx+0x240>
  40fefb:	85 c9                	test   %ecx,%ecx
  40fefd:	c5 7b 10 0d eb 8f 09 	vmovsd 0x98feb(%rip),%xmm9        # 4a8ef0 <big>
  40ff04:	00 
  40ff05:	0f 8e c5 08 00 00    	jle    4107d0 <__sin_avx+0x9e0>
  40ff0b:	c5 f9 28 ca          	vmovapd %xmm2,%xmm1
  40ff0f:	c5 f9 28 fa          	vmovapd %xmm2,%xmm7
  40ff13:	c4 c1 73 58 c9       	vaddsd %xmm9,%xmm1,%xmm1
  40ff18:	c5 f9 28 c1          	vmovapd %xmm1,%xmm0
  40ff1c:	c4 c1 7b 5c c1       	vsubsd %xmm9,%xmm0,%xmm0
  40ff21:	c5 c3 5c f8          	vsubsd %xmm0,%xmm7,%xmm7
  40ff25:	c5 f9 28 c7          	vmovapd %xmm7,%xmm0
  40ff29:	c5 fb 11 0c 24       	vmovsd %xmm1,(%rsp)
  40ff2e:	c5 f9 28 c8          	vmovapd %xmm0,%xmm1
  40ff32:	c5 fb 10 2d be 8f 09 	vmovsd 0x98fbe(%rip),%xmm5        # 4a8ef8 <big+0x8>
  40ff39:	00 
  40ff3a:	48 8b 14 24          	mov    (%rsp),%rdx
  40ff3e:	c5 f3 59 c8          	vmulsd %xmm0,%xmm1,%xmm1
  40ff42:	c5 f9 28 d8          	vmovapd %xmm0,%xmm3
  40ff46:	c5 fb 10 25 b2 8f 09 	vmovsd 0x98fb2(%rip),%xmm4        # 4a8f00 <big+0x10>
  40ff4d:	00 
  40ff4e:	c5 7b 10 05 ba 8f 09 	vmovsd 0x98fba(%rip),%xmm8        # 4a8f10 <big+0x20>
  40ff55:	00 
  40ff56:	c1 e2 02             	shl    $0x2,%edx
  40ff59:	c5 fb 10 3d b7 8f 09 	vmovsd 0x98fb7(%rip),%xmm7        # 4a8f18 <big+0x28>
  40ff60:	00 
  40ff61:	48 63 c2             	movslq %edx,%rax
  40ff64:	c5 f9 28 f1          	vmovapd %xmm1,%xmm6
  40ff68:	c5 e3 59 d9          	vmulsd %xmm1,%xmm3,%xmm3
  40ff6c:	c5 7b 10 14 c5 00 9a 	vmovsd 0x4a9a00(,%rax,8),%xmm10
  40ff73:	4a 00 
  40ff75:	8d 42 01             	lea    0x1(%rdx),%eax
  40ff78:	c5 cb 59 f5          	vmulsd %xmm5,%xmm6,%xmm6
  40ff7c:	48 98                	cltq   
  40ff7e:	c5 7b 10 1c c5 00 9a 	vmovsd 0x4a9a00(,%rax,8),%xmm11
  40ff85:	4a 00 
  40ff87:	8d 42 02             	lea    0x2(%rdx),%eax
  40ff8a:	83 c2 03             	add    $0x3,%edx
  40ff8d:	48 63 d2             	movslq %edx,%rdx
  40ff90:	85 c9                	test   %ecx,%ecx
  40ff92:	c5 cb 5c f4          	vsubsd %xmm4,%xmm6,%xmm6
  40ff96:	48 98                	cltq   
  40ff98:	c5 7b 10 24 c5 00 9a 	vmovsd 0x4a9a00(,%rax,8),%xmm12
  40ff9f:	4a 00 
  40ffa1:	c5 e3 59 de          	vmulsd %xmm6,%xmm3,%xmm3
  40ffa5:	c5 fb 10 35 73 8f 09 	vmovsd 0x98f73(%rip),%xmm6        # 4a8f20 <big+0x30>
  40ffac:	00 
  40ffad:	c5 e3 58 d8          	vaddsd %xmm0,%xmm3,%xmm3
  40ffb1:	c5 f9 28 c1          	vmovapd %xmm1,%xmm0
  40ffb5:	c4 c1 7b 59 c0       	vmulsd %xmm8,%xmm0,%xmm0
  40ffba:	c5 fb 5c c7          	vsubsd %xmm7,%xmm0,%xmm0
  40ffbe:	c5 fb 59 c1          	vmulsd %xmm1,%xmm0,%xmm0
  40ffc2:	c5 fb 58 c6          	vaddsd %xmm6,%xmm0,%xmm0
  40ffc6:	c5 fb 59 c1          	vmulsd %xmm1,%xmm0,%xmm0
  40ffca:	c5 fb 10 0c d5 00 9a 	vmovsd 0x4a9a00(,%rdx,8),%xmm1
  40ffd1:	4a 00 
  40ffd3:	0f 8e d7 07 00 00    	jle    4107b0 <__sin_avx+0x9c0>
  40ffd9:	c5 f3 59 cb          	vmulsd %xmm3,%xmm1,%xmm1
  40ffdd:	c4 c1 7b 59 c2       	vmulsd %xmm10,%xmm0,%xmm0
  40ffe2:	c4 c1 63 59 dc       	vmulsd %xmm12,%xmm3,%xmm3
  40ffe7:	c4 c1 73 58 cb       	vaddsd %xmm11,%xmm1,%xmm1
  40ffec:	c5 f3 5c c8          	vsubsd %xmm0,%xmm1,%xmm1
  40fff0:	c5 79 29 d0          	vmovapd %xmm10,%xmm0
  40fff4:	c5 f3 58 cb          	vaddsd %xmm3,%xmm1,%xmm1
  40fff8:	c5 79 29 d3          	vmovapd %xmm10,%xmm3
  40fffc:	c5 e3 58 d9          	vaddsd %xmm1,%xmm3,%xmm3
  410000:	c5 fb 5c c3          	vsubsd %xmm3,%xmm0,%xmm0
  410004:	c5 fb 58 c1          	vaddsd %xmm1,%xmm0,%xmm0
  410008:	c5 fb 59 05 a0 8f 09 	vmulsd 0x98fa0(%rip),%xmm0,%xmm0        # 4a8fb0 <hp1+0x68>
  41000f:	00 
  410010:	c5 fb 58 c3          	vaddsd %xmm3,%xmm0,%xmm0
  410014:	c5 f9 2e c3          	vucomisd %xmm3,%xmm0
  410018:	0f 8a 12 06 00 00    	jp     410630 <__sin_avx+0x840>
  41001e:	0f 85 0c 06 00 00    	jne    410630 <__sin_avx+0x840>
  410024:	c5 f9 28 d3          	vmovapd %xmm3,%xmm2
  410028:	e9 a3 fe ff ff       	jmpq   40fed0 <__sin_avx+0xe0>
  41002d:	0f 1f 00             	nopl   (%rax)
  410030:	3d fc 68 03 40       	cmp    $0x400368fc,%eax
  410035:	0f 8f 75 02 00 00    	jg     4102b0 <__sin_avx+0x4c0>
  41003b:	85 c9                	test   %ecx,%ecx
  41003d:	c5 7b 10 25 fb 8e 09 	vmovsd 0x98efb(%rip),%xmm12        # 4a8f40 <hp0>
  410044:	00 
  410045:	0f 8e d4 05 00 00    	jle    41061f <__sin_avx+0x82f>
  41004b:	c5 79 29 e0          	vmovapd %xmm12,%xmm0
  41004f:	c5 fb 5c c2          	vsubsd %xmm2,%xmm0,%xmm0
  410053:	c5 e1 57 db          	vxorpd %xmm3,%xmm3,%xmm3
  410057:	c5 7b 10 0d 91 8e 09 	vmovsd 0x98e91(%rip),%xmm9        # 4a8ef0 <big>
  41005e:	00 
  41005f:	c5 f9 2e c3          	vucomisd %xmm3,%xmm0
  410063:	0f 82 7f 09 00 00    	jb     4109e8 <__sin_avx+0xbf8>
  410069:	c5 f9 28 c8          	vmovapd %xmm0,%xmm1
  41006d:	c4 c1 73 58 c9       	vaddsd %xmm9,%xmm1,%xmm1
  410072:	c5 f9 28 e1          	vmovapd %xmm1,%xmm4
  410076:	c4 c1 5b 5c e1       	vsubsd %xmm9,%xmm4,%xmm4
  41007b:	c5 fb 5c c4          	vsubsd %xmm4,%xmm0,%xmm0
  41007f:	c5 fb 58 05 c1 8e 09 	vaddsd 0x98ec1(%rip),%xmm0,%xmm0        # 4a8f48 <hp1>
  410086:	00 
  410087:	c5 79 28 d8          	vmovapd %xmm0,%xmm11
  41008b:	c5 fb 11 0c 24       	vmovsd %xmm1,(%rsp)
  410090:	c5 fb 10 2d 60 8e 09 	vmovsd 0x98e60(%rip),%xmm5        # 4a8ef8 <big+0x8>
  410097:	00 
  410098:	48 8b 14 24          	mov    (%rsp),%rdx
  41009c:	c5 23 59 d8          	vmulsd %xmm0,%xmm11,%xmm11
  4100a0:	c5 79 28 d0          	vmovapd %xmm0,%xmm10
  4100a4:	c5 fb 10 25 54 8e 09 	vmovsd 0x98e54(%rip),%xmm4        # 4a8f00 <big+0x10>
  4100ab:	00 
  4100ac:	c1 e2 02             	shl    $0x2,%edx
  4100af:	c5 7b 10 05 59 8e 09 	vmovsd 0x98e59(%rip),%xmm8        # 4a8f10 <big+0x20>
  4100b6:	00 
  4100b7:	8d 72 01             	lea    0x1(%rdx),%esi
  4100ba:	8d 42 02             	lea    0x2(%rdx),%eax
  4100bd:	c5 79 29 d9          	vmovapd %xmm11,%xmm1
  4100c1:	c4 41 2b 59 d3       	vmulsd %xmm11,%xmm10,%xmm10
  4100c6:	48 63 f6             	movslq %esi,%rsi
  4100c9:	48 98                	cltq   
  4100cb:	c5 f3 59 cd          	vmulsd %xmm5,%xmm1,%xmm1
  4100cf:	c5 7b 10 2c c5 00 9a 	vmovsd 0x4a9a00(,%rax,8),%xmm13
  4100d6:	4a 00 
  4100d8:	8d 42 03             	lea    0x3(%rdx),%eax
  4100db:	48 63 d2             	movslq %edx,%rdx
  4100de:	c5 fb 10 3d 32 8e 09 	vmovsd 0x98e32(%rip),%xmm7        # 4a8f18 <big+0x28>
  4100e5:	00 
  4100e6:	48 98                	cltq   
  4100e8:	c5 fb 10 35 30 8e 09 	vmovsd 0x98e30(%rip),%xmm6        # 4a8f20 <big+0x30>
  4100ef:	00 
  4100f0:	c5 f3 5c cc          	vsubsd %xmm4,%xmm1,%xmm1
  4100f4:	c5 2b 59 d1          	vmulsd %xmm1,%xmm10,%xmm10
  4100f8:	c5 fb 10 0c c5 00 9a 	vmovsd 0x4a9a00(,%rax,8),%xmm1
  4100ff:	4a 00 
  410101:	c5 2b 58 d0          	vaddsd %xmm0,%xmm10,%xmm10
  410105:	c5 fb 10 04 f5 00 9a 	vmovsd 0x4a9a00(,%rsi,8),%xmm0
  41010c:	4a 00 
  41010e:	c4 c1 7b 59 c2       	vmulsd %xmm10,%xmm0,%xmm0
  410113:	c5 2b 59 14 d5 00 9a 	vmulsd 0x4a9a00(,%rdx,8),%xmm10,%xmm10
  41011a:	4a 00 
  41011c:	c5 f3 5c c8          	vsubsd %xmm0,%xmm1,%xmm1
  410120:	c5 79 29 d8          	vmovapd %xmm11,%xmm0
  410124:	c4 c1 7b 59 c0       	vmulsd %xmm8,%xmm0,%xmm0
  410129:	c5 fb 5c c7          	vsubsd %xmm7,%xmm0,%xmm0
  41012d:	c4 c1 7b 59 c3       	vmulsd %xmm11,%xmm0,%xmm0
  410132:	c5 fb 58 c6          	vaddsd %xmm6,%xmm0,%xmm0
  410136:	c4 c1 7b 59 c3       	vmulsd %xmm11,%xmm0,%xmm0
  41013b:	c4 c1 7b 59 c5       	vmulsd %xmm13,%xmm0,%xmm0
  410140:	c5 f3 5c c8          	vsubsd %xmm0,%xmm1,%xmm1
  410144:	c5 79 29 e8          	vmovapd %xmm13,%xmm0
  410148:	c4 c1 73 5c ca       	vsubsd %xmm10,%xmm1,%xmm1
  41014d:	c4 41 79 28 d5       	vmovapd %xmm13,%xmm10
  410152:	c5 2b 58 d1          	vaddsd %xmm1,%xmm10,%xmm10
  410156:	c4 c1 7b 5c c2       	vsubsd %xmm10,%xmm0,%xmm0
  41015b:	c5 fb 58 c1          	vaddsd %xmm1,%xmm0,%xmm0
  41015f:	c5 fb 59 05 d1 8d 09 	vmulsd 0x98dd1(%rip),%xmm0,%xmm0        # 4a8f38 <big+0x48>
  410166:	00 
  410167:	c4 c1 7b 58 c2       	vaddsd %xmm10,%xmm0,%xmm0
  41016c:	c4 c1 79 2e c2       	vucomisd %xmm10,%xmm0
  410171:	0f 8a 99 06 00 00    	jp     410810 <__sin_avx+0xa20>
  410177:	0f 85 93 06 00 00    	jne    410810 <__sin_avx+0xa20>
  41017d:	85 c9                	test   %ecx,%ecx
  41017f:	c5 79 29 d2          	vmovapd %xmm10,%xmm2
  410183:	0f 8f 47 fd ff ff    	jg     40fed0 <__sin_avx+0xe0>
  410189:	c5 fb 10 05 2f 8e 09 	vmovsd 0x98e2f(%rip),%xmm0        # 4a8fc0 <hp1+0x78>
  410190:	00 
  410191:	c5 e9 57 d0          	vxorpd %xmm0,%xmm2,%xmm2
  410195:	e9 36 fd ff ff       	jmpq   40fed0 <__sin_avx+0xe0>
  41019a:	66 0f 1f 44 00 00    	nopw   0x0(%rax,%rax,1)
  4101a0:	c5 fb 10 0d a0 8c 09 	vmovsd 0x98ca0(%rip),%xmm1        # 4a8e48 <_IO_stdin_used+0x8>
  4101a7:	00 
  4101a8:	c5 fb 58 05 c8 8c 09 	vaddsd 0x98cc8(%rip),%xmm0,%xmm0        # 4a8e78 <_IO_stdin_used+0x38>
  4101af:	00 
  4101b0:	c5 f9 28 ea          	vmovapd %xmm2,%xmm5
  4101b4:	c5 7b 10 05 94 8c 09 	vmovsd 0x98c94(%rip),%xmm8        # 4a8e50 <_IO_stdin_used+0x10>
  4101bb:	00 
  4101bc:	c5 f9 28 fa          	vmovapd %xmm2,%xmm7
  4101c0:	c5 d3 58 e9          	vaddsd %xmm1,%xmm5,%xmm5
  4101c4:	c5 e1 57 db          	vxorpd %xmm3,%xmm3,%xmm3
  4101c8:	c5 fb 59 c4          	vmulsd %xmm4,%xmm0,%xmm0
  4101cc:	c5 79 29 c4          	vmovapd %xmm8,%xmm4
  4101d0:	c5 d3 5c e9          	vsubsd %xmm1,%xmm5,%xmm5
  4101d4:	c5 f9 28 ca          	vmovapd %xmm2,%xmm1
  4101d8:	c5 f9 28 f5          	vmovapd %xmm5,%xmm6
  4101dc:	c5 c3 5c fd          	vsubsd %xmm5,%xmm7,%xmm7
  4101e0:	c4 c1 4b 59 f0       	vmulsd %xmm8,%xmm6,%xmm6
  4101e5:	c5 c3 58 fb          	vaddsd %xmm3,%xmm7,%xmm7
  4101e9:	c5 cb 59 f5          	vmulsd %xmm5,%xmm6,%xmm6
  4101ed:	c5 db 59 e7          	vmulsd %xmm7,%xmm4,%xmm4
  4101f1:	c5 cb 59 f5          	vmulsd %xmm5,%xmm6,%xmm6
  4101f5:	c5 d3 59 2d 83 8c 09 	vmulsd 0x98c83(%rip),%xmm5,%xmm5        # 4a8e80 <_IO_stdin_used+0x40>
  4101fc:	00 
  4101fd:	c5 db 59 e7          	vmulsd %xmm7,%xmm4,%xmm4
  410201:	c5 f3 58 ce          	vaddsd %xmm6,%xmm1,%xmm1
  410205:	c5 d3 59 ef          	vmulsd %xmm7,%xmm5,%xmm5
  410209:	c5 db 59 e7          	vmulsd %xmm7,%xmm4,%xmm4
  41020d:	c5 fb 58 c5          	vaddsd %xmm5,%xmm0,%xmm0
  410211:	c5 fb 59 c2          	vmulsd %xmm2,%xmm0,%xmm0
  410215:	c5 fb 58 c4          	vaddsd %xmm4,%xmm0,%xmm0
  410219:	c5 f9 28 e2          	vmovapd %xmm2,%xmm4
  41021d:	c5 db 5c e1          	vsubsd %xmm1,%xmm4,%xmm4
  410221:	c5 fb 58 c3          	vaddsd %xmm3,%xmm0,%xmm0
  410225:	c5 db 58 e6          	vaddsd %xmm6,%xmm4,%xmm4
  410229:	c5 fb 58 c4          	vaddsd %xmm4,%xmm0,%xmm0
  41022d:	c5 f9 28 e1          	vmovapd %xmm1,%xmm4
  410231:	c5 db 58 e0          	vaddsd %xmm0,%xmm4,%xmm4
  410235:	c5 f3 5c cc          	vsubsd %xmm4,%xmm1,%xmm1
  410239:	c5 f3 58 c8          	vaddsd %xmm0,%xmm1,%xmm1
  41023d:	c5 f3 59 0d 63 8d 09 	vmulsd 0x98d63(%rip),%xmm1,%xmm1        # 4a8fa8 <hp1+0x60>
  410244:	00 
  410245:	c5 f3 58 cc          	vaddsd %xmm4,%xmm1,%xmm1
  410249:	c5 f9 2e e1          	vucomisd %xmm1,%xmm4
  41024d:	0f 8b bd 03 00 00    	jnp    410610 <__sin_avx+0x820>
  410253:	c5 f9 2e d3          	vucomisd %xmm3,%xmm2
  410257:	0f 86 d9 07 00 00    	jbe    410a36 <__sin_avx+0xc46>
  41025d:	c5 f9 28 cb          	vmovapd %xmm3,%xmm1
  410261:	48 8d 7c 24 50       	lea    0x50(%rsp),%rdi
  410266:	c5 f9 28 c2          	vmovapd %xmm2,%xmm0
  41026a:	c5 fb 11 14 24       	vmovsd %xmm2,(%rsp)
  41026f:	e8 9c 57 ff ff       	callq  405a10 <__dubsin>
  410274:	c5 fb 10 4c 24 50    	vmovsd 0x50(%rsp),%xmm1
  41027a:	c5 fb 10 05 1e 8c 09 	vmovsd 0x98c1e(%rip),%xmm0        # 4a8ea0 <_IO_stdin_used+0x60>
  410281:	00 
  410282:	c5 fb 59 44 24 58    	vmulsd 0x58(%rsp),%xmm0,%xmm0
  410288:	c5 fb 10 14 24       	vmovsd (%rsp),%xmm2
  41028d:	c5 fb 58 c1          	vaddsd %xmm1,%xmm0,%xmm0
  410291:	c5 f9 2e c8          	vucomisd %xmm0,%xmm1
  410295:	0f 8a 55 05 00 00    	jp     4107f0 <__sin_avx+0xa00>
  41029b:	0f 85 4f 05 00 00    	jne    4107f0 <__sin_avx+0xa00>
  4102a1:	c5 f9 28 d1          	vmovapd %xmm1,%xmm2
  4102a5:	e9 26 fc ff ff       	jmpq   40fed0 <__sin_avx+0xe0>
  4102aa:	66 0f 1f 44 00 00    	nopw   0x0(%rax,%rax,1)
  4102b0:	3d fa 21 99 41       	cmp    $0x419921fa,%eax
  4102b5:	0f 8f 95 01 00 00    	jg     410450 <__sin_avx+0x660>
  4102bb:	c5 fb 10 2d f5 8b 09 	vmovsd 0x98bf5(%rip),%xmm5        # 4a8eb8 <hpinv>
  4102c2:	00 
  4102c3:	c5 fb 10 05 f5 8b 09 	vmovsd 0x98bf5(%rip),%xmm0        # 4a8ec0 <big>
  4102ca:	00 
  4102cb:	c5 f9 28 e2          	vmovapd %xmm2,%xmm4
  4102cf:	c5 d3 59 ea          	vmulsd %xmm2,%xmm5,%xmm5
  4102d3:	c5 e1 57 db          	vxorpd %xmm3,%xmm3,%xmm3
  4102d7:	c5 d3 58 e8          	vaddsd %xmm0,%xmm5,%xmm5
  4102db:	c5 f9 28 f5          	vmovapd %xmm5,%xmm6
  4102df:	c5 fb 11 2c 24       	vmovsd %xmm5,(%rsp)
  4102e4:	48 8b 04 24          	mov    (%rsp),%rax
  4102e8:	c5 cb 5c f0          	vsubsd %xmm0,%xmm6,%xmm6
  4102ec:	c5 fb 10 05 d4 8b 09 	vmovsd 0x98bd4(%rip),%xmm0        # 4a8ec8 <mp1>
  4102f3:	00 
  4102f4:	41 89 c4             	mov    %eax,%r12d
  4102f7:	83 e0 03             	and    $0x3,%eax
  4102fa:	c5 f9 2e d3          	vucomisd %xmm3,%xmm2
  4102fe:	c5 fb 59 c6          	vmulsd %xmm6,%xmm0,%xmm0
  410302:	c5 db 5c e0          	vsubsd %xmm0,%xmm4,%xmm4
  410306:	c5 fb 10 05 c2 8b 09 	vmovsd 0x98bc2(%rip),%xmm0        # 4a8ed0 <mp1+0x8>
  41030d:	00 
  41030e:	c5 fb 59 c6          	vmulsd %xmm6,%xmm0,%xmm0
  410312:	c5 db 5c e0          	vsubsd %xmm0,%xmm4,%xmm4
  410316:	c5 fb 10 05 52 8c 09 	vmovsd 0x98c52(%rip),%xmm0        # 4a8f70 <hp1+0x28>
  41031d:	00 
  41031e:	c5 fb 59 c6          	vmulsd %xmm6,%xmm0,%xmm0
  410322:	c5 79 28 cc          	vmovapd %xmm4,%xmm9
  410326:	c5 f9 28 cc          	vmovapd %xmm4,%xmm1
  41032a:	c5 33 5c c8          	vsubsd %xmm0,%xmm9,%xmm9
  41032e:	c4 c1 73 5c c9       	vsubsd %xmm9,%xmm1,%xmm1
  410333:	c5 f3 5c c8          	vsubsd %xmm0,%xmm1,%xmm1
  410337:	0f 86 4d 09 00 00    	jbe    410c8a <__sin_avx+0xe9a>
  41033d:	c5 7b 10 25 33 8c 09 	vmovsd 0x98c33(%rip),%xmm12        # 4a8f78 <hp1+0x30>
  410344:	00 
  410345:	c5 1b 59 e2          	vmulsd %xmm2,%xmm12,%xmm12
  410349:	83 f8 01             	cmp    $0x1,%eax
  41034c:	0f 84 92 07 00 00    	je     410ae4 <__sin_avx+0xcf4>
  410352:	83 f8 03             	cmp    $0x3,%eax
  410355:	0f 84 89 07 00 00    	je     410ae4 <__sin_avx+0xcf4>
  41035b:	c4 41 79 28 e9       	vmovapd %xmm9,%xmm13
  410360:	85 c0                	test   %eax,%eax
  410362:	c4 41 13 59 e9       	vmulsd %xmm9,%xmm13,%xmm13
  410367:	74 10                	je     410379 <__sin_avx+0x589>
  410369:	c5 fb 10 05 4f 8c 09 	vmovsd 0x98c4f(%rip),%xmm0        # 4a8fc0 <hp1+0x78>
  410370:	00 
  410371:	c5 31 57 c8          	vxorpd %xmm0,%xmm9,%xmm9
  410375:	c5 f1 57 c8          	vxorpd %xmm0,%xmm1,%xmm1
  410379:	c5 fb 10 05 cf 8b 09 	vmovsd 0x98bcf(%rip),%xmm0        # 4a8f50 <hp1+0x8>
  410380:	00 
  410381:	c4 c1 79 2e c5       	vucomisd %xmm13,%xmm0
  410386:	0f 86 4a 0a 00 00    	jbe    410dd6 <__sin_avx+0xfe6>
  41038c:	c4 41 79 28 dd       	vmovapd %xmm13,%xmm11
  410391:	c5 7b 10 15 bf 8a 09 	vmovsd 0x98abf(%rip),%xmm10        # 4a8e58 <_IO_stdin_used+0x18>
  410398:	00 
  410399:	c5 7b 10 05 bf 8a 09 	vmovsd 0x98abf(%rip),%xmm8        # 4a8e60 <_IO_stdin_used+0x20>
  4103a0:	00 
  4103a1:	c4 41 23 59 da       	vmulsd %xmm10,%xmm11,%xmm11
  4103a6:	c5 fb 10 3d ba 8a 09 	vmovsd 0x98aba(%rip),%xmm7        # 4a8e68 <_IO_stdin_used+0x28>
  4103ad:	00 
  4103ae:	c5 fb 10 05 ba 8a 09 	vmovsd 0x98aba(%rip),%xmm0        # 4a8e70 <_IO_stdin_used+0x30>
  4103b5:	00 
  4103b6:	c5 7b 10 35 62 8b 09 	vmovsd 0x98b62(%rip),%xmm14        # 4a8f20 <big+0x30>
  4103bd:	00 
  4103be:	c4 41 23 58 d8       	vaddsd %xmm8,%xmm11,%xmm11
  4103c3:	c5 0b 59 f1          	vmulsd %xmm1,%xmm14,%xmm14
  4103c7:	c4 41 23 59 dd       	vmulsd %xmm13,%xmm11,%xmm11
  4103cc:	c5 23 5c df          	vsubsd %xmm7,%xmm11,%xmm11
  4103d0:	c4 41 23 59 dd       	vmulsd %xmm13,%xmm11,%xmm11
  4103d5:	c5 23 58 d8          	vaddsd %xmm0,%xmm11,%xmm11
  4103d9:	c4 41 23 59 dd       	vmulsd %xmm13,%xmm11,%xmm11
  4103de:	c5 23 5c 1d 72 8b 09 	vsubsd 0x98b72(%rip),%xmm11,%xmm11        # 4a8f58 <hp1+0x10>
  4103e5:	00 
  4103e6:	c4 41 23 59 d9       	vmulsd %xmm9,%xmm11,%xmm11
  4103eb:	c4 41 23 5c de       	vsubsd %xmm14,%xmm11,%xmm11
  4103f0:	c4 41 79 28 f1       	vmovapd %xmm9,%xmm14
  4103f5:	c4 41 23 59 dd       	vmulsd %xmm13,%xmm11,%xmm11
  4103fa:	c4 41 79 28 e9       	vmovapd %xmm9,%xmm13
  4103ff:	c5 23 58 d9          	vaddsd %xmm1,%xmm11,%xmm11
  410403:	c4 41 0b 58 f3       	vaddsd %xmm11,%xmm14,%xmm14
  410408:	c4 41 13 5c ee       	vsubsd %xmm14,%xmm13,%xmm13
  41040d:	c4 41 13 58 eb       	vaddsd %xmm11,%xmm13,%xmm13
  410412:	c5 79 2e eb          	vucomisd %xmm3,%xmm13
  410416:	c5 13 59 2d 1a 8b 09 	vmulsd 0x98b1a(%rip),%xmm13,%xmm13        # 4a8f38 <big+0x48>
  41041d:	00 
  41041e:	0f 86 09 13 00 00    	jbe    41172d <__sin_avx+0x193d>
  410424:	c4 41 13 58 ec       	vaddsd %xmm12,%xmm13,%xmm13
  410429:	c4 41 13 58 ee       	vaddsd %xmm14,%xmm13,%xmm13
  41042e:	c4 41 79 2e f5       	vucomisd %xmm13,%xmm14
  410433:	0f 8a e7 0f 00 00    	jp     411420 <__sin_avx+0x1630>
  410439:	0f 85 e1 0f 00 00    	jne    411420 <__sin_avx+0x1630>
  41043f:	c5 79 29 f2          	vmovapd %xmm14,%xmm2
  410443:	e9 88 fa ff ff       	jmpq   40fed0 <__sin_avx+0xe0>
  410448:	0f 1f 84 00 00 00 00 	nopl   0x0(%rax,%rax,1)
  41044f:	00 
  410450:	3d ff ff ef 42       	cmp    $0x42efffff,%eax
  410455:	0f 8f b3 05 00 00    	jg     410a0e <__sin_avx+0xc1e>
  41045b:	c5 fb 10 05 55 8a 09 	vmovsd 0x98a55(%rip),%xmm0        # 4a8eb8 <hpinv>
  410462:	00 
  410463:	c5 fb 10 0d 55 8a 09 	vmovsd 0x98a55(%rip),%xmm1        # 4a8ec0 <big>
  41046a:	00 
  41046b:	c5 f9 28 da          	vmovapd %xmm2,%xmm3
  41046f:	c5 fb 59 c2          	vmulsd %xmm2,%xmm0,%xmm0
  410473:	c5 fb 10 35 4d 8a 09 	vmovsd 0x98a4d(%rip),%xmm6        # 4a8ec8 <mp1>
  41047a:	00 
  41047b:	c5 fb 58 c1          	vaddsd %xmm1,%xmm0,%xmm0
  41047f:	c5 f9 28 e0          	vmovapd %xmm0,%xmm4
  410483:	c5 fb 11 04 24       	vmovsd %xmm0,(%rsp)
  410488:	48 8b 04 24          	mov    (%rsp),%rax
  41048c:	c5 db 5c e1          	vsubsd %xmm1,%xmm4,%xmm4
  410490:	c5 fb 10 0d f0 8a 09 	vmovsd 0x98af0(%rip),%xmm1        # 4a8f88 <hp1+0x40>
  410497:	00 
  410498:	89 c7                	mov    %eax,%edi
  41049a:	89 c1                	mov    %eax,%ecx
  41049c:	83 e7 03             	and    $0x3,%edi
  41049f:	c5 f9 28 c4          	vmovapd %xmm4,%xmm0
  4104a3:	c5 f9 28 ec          	vmovapd %xmm4,%xmm5
  4104a7:	c5 db 59 25 31 8a 09 	vmulsd 0x98a31(%rip),%xmm4,%xmm4        # 4a8ee0 <mp1+0x18>
  4104ae:	00 
  4104af:	83 ff 01             	cmp    $0x1,%edi
  4104b2:	c5 fb 58 c1          	vaddsd %xmm1,%xmm0,%xmm0
  4104b6:	c5 fb 5c c1          	vsubsd %xmm1,%xmm0,%xmm0
  4104ba:	c5 f9 28 c8          	vmovapd %xmm0,%xmm1
  4104be:	c5 f9 28 f8          	vmovapd %xmm0,%xmm7
  4104c2:	c5 f3 59 ce          	vmulsd %xmm6,%xmm1,%xmm1
  4104c6:	c5 d3 5c e8          	vsubsd %xmm0,%xmm5,%xmm5
  4104ca:	c5 e3 5c d9          	vsubsd %xmm1,%xmm3,%xmm3
  4104ce:	c5 fb 10 0d fa 89 09 	vmovsd 0x989fa(%rip),%xmm1        # 4a8ed0 <mp1+0x8>
  4104d5:	00 
  4104d6:	c5 cb 59 f5          	vmulsd %xmm5,%xmm6,%xmm6
  4104da:	c5 c3 59 f9          	vmulsd %xmm1,%xmm7,%xmm7
  4104de:	c5 f3 59 cd          	vmulsd %xmm5,%xmm1,%xmm1
  4104e2:	c5 e3 5c df          	vsubsd %xmm7,%xmm3,%xmm3
  4104e6:	c5 e3 5c de          	vsubsd %xmm6,%xmm3,%xmm3
  4104ea:	c5 fb 10 35 e6 89 09 	vmovsd 0x989e6(%rip),%xmm6        # 4a8ed8 <mp1+0x10>
  4104f1:	00 
  4104f2:	c5 fb 59 c6          	vmulsd %xmm6,%xmm0,%xmm0
  4104f6:	c5 d3 59 ee          	vmulsd %xmm6,%xmm5,%xmm5
  4104fa:	c5 e3 5c d9          	vsubsd %xmm1,%xmm3,%xmm3
  4104fe:	c5 f9 28 cb          	vmovapd %xmm3,%xmm1
  410502:	c5 f3 5c c8          	vsubsd %xmm0,%xmm1,%xmm1
  410506:	c5 e3 5c d9          	vsubsd %xmm1,%xmm3,%xmm3
  41050a:	c5 e3 5c d8          	vsubsd %xmm0,%xmm3,%xmm3
  41050e:	c5 f9 28 c1          	vmovapd %xmm1,%xmm0
  410512:	c5 e3 5c dd          	vsubsd %xmm5,%xmm3,%xmm3
  410516:	c5 e3 5c dc          	vsubsd %xmm4,%xmm3,%xmm3
  41051a:	c5 fb 58 c3          	vaddsd %xmm3,%xmm0,%xmm0
  41051e:	c5 f3 5c c8          	vsubsd %xmm0,%xmm1,%xmm1
  410522:	c5 f3 58 cb          	vaddsd %xmm3,%xmm1,%xmm1
  410526:	0f 84 80 07 00 00    	je     410cac <__sin_avx+0xebc>
  41052c:	83 ff 03             	cmp    $0x3,%edi
  41052f:	0f 84 77 07 00 00    	je     410cac <__sin_avx+0xebc>
  410535:	c5 f9 28 e0          	vmovapd %xmm0,%xmm4
  410539:	85 ff                	test   %edi,%edi
  41053b:	c5 db 59 e0          	vmulsd %xmm0,%xmm4,%xmm4
  41053f:	74 10                	je     410551 <__sin_avx+0x761>
  410541:	c5 fb 10 1d 77 8a 09 	vmovsd 0x98a77(%rip),%xmm3        # 4a8fc0 <hp1+0x78>
  410548:	00 
  410549:	c5 f9 57 c3          	vxorpd %xmm3,%xmm0,%xmm0
  41054d:	c5 f1 57 cb          	vxorpd %xmm3,%xmm1,%xmm1
  410551:	c5 fb 10 1d f7 89 09 	vmovsd 0x989f7(%rip),%xmm3        # 4a8f50 <hp1+0x8>
  410558:	00 
  410559:	c5 f9 2e dc          	vucomisd %xmm4,%xmm3
  41055d:	0f 86 c4 0c 00 00    	jbe    411227 <__sin_avx+0x1437>
  410563:	c5 fb 10 1d ed 88 09 	vmovsd 0x988ed(%rip),%xmm3        # 4a8e58 <_IO_stdin_used+0x18>
  41056a:	00 
  41056b:	c5 fb 10 2d ad 89 09 	vmovsd 0x989ad(%rip),%xmm5        # 4a8f20 <big+0x30>
  410572:	00 
  410573:	c5 e3 59 dc          	vmulsd %xmm4,%xmm3,%xmm3
  410577:	c5 d3 59 e9          	vmulsd %xmm1,%xmm5,%xmm5
  41057b:	c5 e3 58 1d dd 88 09 	vaddsd 0x988dd(%rip),%xmm3,%xmm3        # 4a8e60 <_IO_stdin_used+0x20>
  410582:	00 
  410583:	c5 e3 59 dc          	vmulsd %xmm4,%xmm3,%xmm3
  410587:	c5 e3 5c 1d d9 88 09 	vsubsd 0x988d9(%rip),%xmm3,%xmm3        # 4a8e68 <_IO_stdin_used+0x28>
  41058e:	00 
  41058f:	c5 e3 59 dc          	vmulsd %xmm4,%xmm3,%xmm3
  410593:	c5 e3 58 1d d5 88 09 	vaddsd 0x988d5(%rip),%xmm3,%xmm3        # 4a8e70 <_IO_stdin_used+0x30>
  41059a:	00 
  41059b:	c5 e3 59 dc          	vmulsd %xmm4,%xmm3,%xmm3
  41059f:	c5 e3 5c 1d b1 89 09 	vsubsd 0x989b1(%rip),%xmm3,%xmm3        # 4a8f58 <hp1+0x10>
  4105a6:	00 
  4105a7:	c5 e3 59 d8          	vmulsd %xmm0,%xmm3,%xmm3
  4105ab:	c5 e3 5c dd          	vsubsd %xmm5,%xmm3,%xmm3
  4105af:	c5 f9 28 e8          	vmovapd %xmm0,%xmm5
  4105b3:	c5 e3 59 dc          	vmulsd %xmm4,%xmm3,%xmm3
  4105b7:	c5 f9 28 e0          	vmovapd %xmm0,%xmm4
  4105bb:	c5 e3 58 d9          	vaddsd %xmm1,%xmm3,%xmm3
  4105bf:	c5 d3 58 eb          	vaddsd %xmm3,%xmm5,%xmm5
  4105c3:	c5 db 5c e5          	vsubsd %xmm5,%xmm4,%xmm4
  4105c7:	c5 db 58 e3          	vaddsd %xmm3,%xmm4,%xmm4
  4105cb:	c5 f9 2e 25 b5 88 09 	vucomisd 0x988b5(%rip),%xmm4        # 4a8e88 <_IO_stdin_used+0x48>
  4105d2:	00 
  4105d3:	c5 db 59 25 5d 89 09 	vmulsd 0x9895d(%rip),%xmm4,%xmm4        # 4a8f38 <big+0x48>
  4105da:	00 
  4105db:	0f 86 fd 11 00 00    	jbe    4117de <__sin_avx+0x19ee>
  4105e1:	c5 db 58 25 a7 89 09 	vaddsd 0x989a7(%rip),%xmm4,%xmm4        # 4a8f90 <hp1+0x48>
  4105e8:	00 
  4105e9:	c5 db 58 e5          	vaddsd %xmm5,%xmm4,%xmm4
  4105ed:	c5 f9 2e ec          	vucomisd %xmm4,%xmm5
  4105f1:	7a 06                	jp     4105f9 <__sin_avx+0x809>
  4105f3:	0f 84 cd f8 ff ff    	je     40fec6 <__sin_avx+0xd6>
  4105f9:	e8 22 e8 ff ff       	callq  40ee20 <bsloww>
  4105fe:	c5 f9 28 d0          	vmovapd %xmm0,%xmm2
  410602:	e9 c9 f8 ff ff       	jmpq   40fed0 <__sin_avx+0xe0>
  410607:	66 0f 1f 84 00 00 00 	nopw   0x0(%rax,%rax,1)
  41060e:	00 00 
  410610:	0f 85 3d fc ff ff    	jne    410253 <__sin_avx+0x463>
  410616:	c5 f9 28 d4          	vmovapd %xmm4,%xmm2
  41061a:	e9 b1 f8 ff ff       	jmpq   40fed0 <__sin_avx+0xe0>
  41061f:	c5 f9 28 c2          	vmovapd %xmm2,%xmm0
  410623:	c4 c1 7b 58 c4       	vaddsd %xmm12,%xmm0,%xmm0
  410628:	e9 26 fa ff ff       	jmpq   410053 <__sin_avx+0x263>
  41062d:	0f 1f 00             	nopl   (%rax)
  410630:	c5 e1 57 db          	vxorpd %xmm3,%xmm3,%xmm3
  410634:	c5 f9 28 ca          	vmovapd %xmm2,%xmm1
  410638:	c5 f9 2e d3          	vucomisd %xmm3,%xmm2
  41063c:	0f 86 ea 05 00 00    	jbe    410c2c <__sin_avx+0xe3c>
  410642:	c5 f9 28 c1          	vmovapd %xmm1,%xmm0
  410646:	c4 c1 7b 58 c1       	vaddsd %xmm9,%xmm0,%xmm0
  41064b:	c5 fb 11 04 24       	vmovsd %xmm0,(%rsp)
  410650:	c4 c1 7b 5c c1       	vsubsd %xmm9,%xmm0,%xmm0
  410655:	48 8b 04 24          	mov    (%rsp),%rax
  410659:	c1 e0 02             	shl    $0x2,%eax
  41065c:	c5 f3 5c c8          	vsubsd %xmm0,%xmm1,%xmm1
  410660:	48 63 d0             	movslq %eax,%rdx
  410663:	c5 7b 10 14 d5 00 9a 	vmovsd 0x4a9a00(,%rdx,8),%xmm10
  41066a:	4a 00 
  41066c:	8d 50 02             	lea    0x2(%rax),%edx
  41066f:	c5 fb 10 05 91 88 09 	vmovsd 0x98891(%rip),%xmm0        # 4a8f08 <big+0x18>
  410676:	00 
  410677:	48 63 d2             	movslq %edx,%rdx
  41067a:	c5 79 28 c9          	vmovapd %xmm1,%xmm9
  41067e:	c5 79 28 e1          	vmovapd %xmm1,%xmm12
  410682:	c5 79 28 d9          	vmovapd %xmm1,%xmm11
  410686:	c5 33 59 c9          	vmulsd %xmm1,%xmm9,%xmm9
  41068a:	c5 23 58 d8          	vaddsd %xmm0,%xmm11,%xmm11
  41068e:	c4 c1 53 59 e9       	vmulsd %xmm9,%xmm5,%xmm5
  410693:	c4 41 1b 59 e1       	vmulsd %xmm9,%xmm12,%xmm12
  410698:	c5 23 5c d8          	vsubsd %xmm0,%xmm11,%xmm11
  41069c:	c4 41 3b 59 c1       	vmulsd %xmm9,%xmm8,%xmm8
  4106a1:	c5 d3 5c ec          	vsubsd %xmm4,%xmm5,%xmm5
  4106a5:	c5 3b 5c c7          	vsubsd %xmm7,%xmm8,%xmm8
  4106a9:	c5 1b 59 e5          	vmulsd %xmm5,%xmm12,%xmm12
  4106ad:	c5 fb 10 2c d5 00 9a 	vmovsd 0x4a9a00(,%rdx,8),%xmm5
  4106b4:	4a 00 
  4106b6:	8d 50 03             	lea    0x3(%rax),%edx
  4106b9:	83 c0 01             	add    $0x1,%eax
  4106bc:	48 98                	cltq   
  4106be:	c4 41 3b 59 c1       	vmulsd %xmm9,%xmm8,%xmm8
  4106c3:	c5 f9 28 e5          	vmovapd %xmm5,%xmm4
  4106c7:	48 63 d2             	movslq %edx,%rdx
  4106ca:	c5 7b 10 2c d5 00 9a 	vmovsd 0x4a9a00(,%rdx,8),%xmm13
  4106d1:	4a 00 
  4106d3:	c5 db 58 e0          	vaddsd %xmm0,%xmm4,%xmm4
  4106d7:	c5 3b 58 c6          	vaddsd %xmm6,%xmm8,%xmm8
  4106db:	c5 db 5c e0          	vsubsd %xmm0,%xmm4,%xmm4
  4106df:	c5 79 29 e0          	vmovapd %xmm12,%xmm0
  4106e3:	c5 1b 59 e5          	vmulsd %xmm5,%xmm12,%xmm12
  4106e7:	c4 c1 7b 59 c5       	vmulsd %xmm13,%xmm0,%xmm0
  4106ec:	c4 41 3b 59 c1       	vmulsd %xmm9,%xmm8,%xmm8
  4106f1:	c5 d3 5c ec          	vsubsd %xmm4,%xmm5,%xmm5
  4106f5:	c5 fb 58 04 c5 00 9a 	vaddsd 0x4a9a00(,%rax,8),%xmm0,%xmm0
  4106fc:	4a 00 
  4106fe:	c4 41 3b 59 c2       	vmulsd %xmm10,%xmm8,%xmm8
  410703:	c4 c1 53 58 ed       	vaddsd %xmm13,%xmm5,%xmm5
  410708:	c4 c1 7b 58 c4       	vaddsd %xmm12,%xmm0,%xmm0
  41070d:	c5 d3 59 e9          	vmulsd %xmm1,%xmm5,%xmm5
  410711:	c5 fb 58 c5          	vaddsd %xmm5,%xmm0,%xmm0
  410715:	c5 f9 28 e9          	vmovapd %xmm1,%xmm5
  410719:	c4 c1 73 59 ca       	vmulsd %xmm10,%xmm1,%xmm1
  41071e:	c4 c1 53 5c eb       	vsubsd %xmm11,%xmm5,%xmm5
  410723:	c5 f3 59 cb          	vmulsd %xmm3,%xmm1,%xmm1
  410727:	c5 d3 58 eb          	vaddsd %xmm3,%xmm5,%xmm5
  41072b:	c5 d3 59 ec          	vmulsd %xmm4,%xmm5,%xmm5
  41072f:	c4 c1 5b 59 e3       	vmulsd %xmm11,%xmm4,%xmm4
  410734:	c5 fb 58 c5          	vaddsd %xmm5,%xmm0,%xmm0
  410738:	c5 fb 5c c1          	vsubsd %xmm1,%xmm0,%xmm0
  41073c:	c5 79 29 d1          	vmovapd %xmm10,%xmm1
  410740:	c5 f3 58 cc          	vaddsd %xmm4,%xmm1,%xmm1
  410744:	c4 c1 7b 5c c0       	vsubsd %xmm8,%xmm0,%xmm0
  410749:	c5 2b 5c d1          	vsubsd %xmm1,%xmm10,%xmm10
  41074d:	c5 2b 58 d4          	vaddsd %xmm4,%xmm10,%xmm10
  410751:	c5 f9 28 e1          	vmovapd %xmm1,%xmm4
  410755:	c4 c1 7b 58 c2       	vaddsd %xmm10,%xmm0,%xmm0
  41075a:	c5 db 58 e0          	vaddsd %xmm0,%xmm4,%xmm4
  41075e:	c5 f3 5c cc          	vsubsd %xmm4,%xmm1,%xmm1
  410762:	c5 f3 58 c8          	vaddsd %xmm0,%xmm1,%xmm1
  410766:	c5 f9 2e cb          	vucomisd %xmm3,%xmm1
  41076a:	c5 f3 59 0d 1e 87 09 	vmulsd 0x9871e(%rip),%xmm1,%xmm1        # 4a8e90 <_IO_stdin_used+0x50>
  410771:	00 
  410772:	0f 86 b5 02 00 00    	jbe    410a2d <__sin_avx+0xc3d>
  410778:	c5 f3 58 cb          	vaddsd %xmm3,%xmm1,%xmm1
  41077c:	c5 f3 58 cc          	vaddsd %xmm4,%xmm1,%xmm1
  410780:	c5 f9 2e cc          	vucomisd %xmm4,%xmm1
  410784:	0f 8a 26 02 00 00    	jp     4109b0 <__sin_avx+0xbc0>
  41078a:	0f 85 20 02 00 00    	jne    4109b0 <__sin_avx+0xbc0>
  410790:	c5 f9 2e d3          	vucomisd %xmm3,%xmm2
  410794:	0f 87 7c fe ff ff    	ja     410616 <__sin_avx+0x826>
  41079a:	c5 fb 10 15 1e 88 09 	vmovsd 0x9881e(%rip),%xmm2        # 4a8fc0 <hp1+0x78>
  4107a1:	00 
  4107a2:	c5 e9 57 d4          	vxorpd %xmm4,%xmm2,%xmm2
  4107a6:	e9 25 f7 ff ff       	jmpq   40fed0 <__sin_avx+0xe0>
  4107ab:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)
  4107b0:	c5 7b 10 2d 08 88 09 	vmovsd 0x98808(%rip),%xmm13        # 4a8fc0 <hp1+0x78>
  4107b7:	00 
  4107b8:	c4 41 29 57 d5       	vxorpd %xmm13,%xmm10,%xmm10
  4107bd:	c4 41 21 57 dd       	vxorpd %xmm13,%xmm11,%xmm11
  4107c2:	e9 12 f8 ff ff       	jmpq   40ffd9 <__sin_avx+0x1e9>
  4107c7:	66 0f 1f 84 00 00 00 	nopw   0x0(%rax,%rax,1)
  4107ce:	00 00 
  4107d0:	c5 79 29 c9          	vmovapd %xmm9,%xmm1
  4107d4:	c5 f3 5c ca          	vsubsd %xmm2,%xmm1,%xmm1
  4107d8:	c5 f9 28 c1          	vmovapd %xmm1,%xmm0
  4107dc:	c4 c1 7b 5c c1       	vsubsd %xmm9,%xmm0,%xmm0
  4107e1:	c5 fb 58 c2          	vaddsd %xmm2,%xmm0,%xmm0
  4107e5:	e9 3f f7 ff ff       	jmpq   40ff29 <__sin_avx+0x139>
  4107ea:	66 0f 1f 44 00 00    	nopw   0x0(%rax,%rax,1)
  4107f0:	c5 f1 57 c9          	vxorpd %xmm1,%xmm1,%xmm1
  4107f4:	31 ff                	xor    %edi,%edi
  4107f6:	c5 f9 28 c2          	vmovapd %xmm2,%xmm0
  4107fa:	e8 f1 7b ff ff       	callq  4083f0 <__mpsin>
  4107ff:	c5 f9 28 d0          	vmovapd %xmm0,%xmm2
  410803:	e9 c8 f6 ff ff       	jmpq   40fed0 <__sin_avx+0xe0>
  410808:	0f 1f 84 00 00 00 00 	nopl   0x0(%rax,%rax,1)
  41080f:	00 
  410810:	c5 f9 2e d3          	vucomisd %xmm3,%xmm2
  410814:	c5 f9 28 c2          	vmovapd %xmm2,%xmm0
  410818:	0f 86 72 07 00 00    	jbe    410f90 <__sin_avx+0x11a0>
  41081e:	c5 79 29 e1          	vmovapd %xmm12,%xmm1
  410822:	c5 f3 5c c8          	vsubsd %xmm0,%xmm1,%xmm1
  410826:	c5 f9 2e cb          	vucomisd %xmm3,%xmm1
  41082a:	0f 82 e5 06 00 00    	jb     410f15 <__sin_avx+0x1125>
  410830:	c5 79 28 d1          	vmovapd %xmm1,%xmm10
  410834:	c5 7b 10 3d 0c 87 09 	vmovsd 0x9870c(%rip),%xmm15        # 4a8f48 <hp1>
  41083b:	00 
  41083c:	c4 41 2b 58 d1       	vaddsd %xmm9,%xmm10,%xmm10
  410841:	c5 79 29 d0          	vmovapd %xmm10,%xmm0
  410845:	c4 c1 7b 5c c1       	vsubsd %xmm9,%xmm0,%xmm0
  41084a:	c5 79 28 c8          	vmovapd %xmm0,%xmm9
  41084e:	c5 f9 28 c1          	vmovapd %xmm1,%xmm0
  410852:	c4 c1 7b 5c c1       	vsubsd %xmm9,%xmm0,%xmm0
  410857:	c5 79 28 c8          	vmovapd %xmm0,%xmm9
  41085b:	c5 7b 11 14 24       	vmovsd %xmm10,(%rsp)
  410860:	48 8b 04 24          	mov    (%rsp),%rax
  410864:	c5 7b 10 15 9c 86 09 	vmovsd 0x9869c(%rip),%xmm10        # 4a8f08 <big+0x18>
  41086b:	00 
  41086c:	c5 33 59 c8          	vmulsd %xmm0,%xmm9,%xmm9
  410870:	c5 79 28 d8          	vmovapd %xmm0,%xmm11
  410874:	c1 e0 02             	shl    $0x2,%eax
  410877:	c4 41 23 58 da       	vaddsd %xmm10,%xmm11,%xmm11
  41087c:	48 63 d0             	movslq %eax,%rdx
  41087f:	c4 41 3b 59 c1       	vmulsd %xmm9,%xmm8,%xmm8
  410884:	c5 7b 10 34 d5 00 9a 	vmovsd 0x4a9a00(,%rdx,8),%xmm14
  41088b:	4a 00 
  41088d:	8d 50 02             	lea    0x2(%rax),%edx
  410890:	c4 41 23 5c da       	vsubsd %xmm10,%xmm11,%xmm11
  410895:	c4 c1 53 59 e9       	vmulsd %xmm9,%xmm5,%xmm5
  41089a:	c5 79 29 f1          	vmovapd %xmm14,%xmm1
  41089e:	48 63 d2             	movslq %edx,%rdx
  4108a1:	c5 3b 5c c7          	vsubsd %xmm7,%xmm8,%xmm8
  4108a5:	c5 f9 28 f8          	vmovapd %xmm0,%xmm7
  4108a9:	c4 c1 73 58 ca       	vaddsd %xmm10,%xmm1,%xmm1
  4108ae:	c5 7b 10 2c d5 00 9a 	vmovsd 0x4a9a00(,%rdx,8),%xmm13
  4108b5:	4a 00 
  4108b7:	c4 c1 43 5c fb       	vsubsd %xmm11,%xmm7,%xmm7
  4108bc:	8d 50 03             	lea    0x3(%rax),%edx
  4108bf:	83 c0 01             	add    $0x1,%eax
  4108c2:	48 98                	cltq   
  4108c4:	c5 d3 5c ec          	vsubsd %xmm4,%xmm5,%xmm5
  4108c8:	c4 41 3b 59 c1       	vmulsd %xmm9,%xmm8,%xmm8
  4108cd:	48 63 d2             	movslq %edx,%rdx
  4108d0:	c4 c1 73 5c ca       	vsubsd %xmm10,%xmm1,%xmm1
  4108d5:	c5 79 28 d0          	vmovapd %xmm0,%xmm10
  4108d9:	c4 c1 43 58 ff       	vaddsd %xmm15,%xmm7,%xmm7
  4108de:	c4 41 2b 59 d7       	vmulsd %xmm15,%xmm10,%xmm10
  4108e3:	c5 3b 58 c6          	vaddsd %xmm6,%xmm8,%xmm8
  4108e7:	c5 fb 10 34 d5 00 9a 	vmovsd 0x4a9a00(,%rdx,8),%xmm6
  4108ee:	4a 00 
  4108f0:	c5 c3 59 f9          	vmulsd %xmm1,%xmm7,%xmm7
  4108f4:	c4 41 3b 59 c1       	vmulsd %xmm9,%xmm8,%xmm8
  4108f9:	c4 41 2b 58 d0       	vaddsd %xmm8,%xmm10,%xmm10
  4108fe:	c4 41 2b 59 d5       	vmulsd %xmm13,%xmm10,%xmm10
  410903:	c4 c1 4b 5c f2       	vsubsd %xmm10,%xmm6,%xmm6
  410908:	c5 cb 5c f7          	vsubsd %xmm7,%xmm6,%xmm6
  41090c:	c5 79 29 f7          	vmovapd %xmm14,%xmm7
  410910:	c5 c3 5c f9          	vsubsd %xmm1,%xmm7,%xmm7
  410914:	c4 c1 73 59 cb       	vmulsd %xmm11,%xmm1,%xmm1
  410919:	c5 c3 58 3c c5 00 9a 	vaddsd 0x4a9a00(,%rax,8),%xmm7,%xmm7
  410920:	4a 00 
  410922:	c5 c3 59 f8          	vmulsd %xmm0,%xmm7,%xmm7
  410926:	c4 c1 7b 59 c1       	vmulsd %xmm9,%xmm0,%xmm0
  41092b:	c5 cb 5c f7          	vsubsd %xmm7,%xmm6,%xmm6
  41092f:	c5 fb 59 c5          	vmulsd %xmm5,%xmm0,%xmm0
  410933:	c4 c1 7b 59 c6       	vmulsd %xmm14,%xmm0,%xmm0
  410938:	c5 cb 5c f0          	vsubsd %xmm0,%xmm6,%xmm6
  41093c:	c5 79 29 e8          	vmovapd %xmm13,%xmm0
  410940:	c5 fb 5c c1          	vsubsd %xmm1,%xmm0,%xmm0
  410944:	c5 13 5c e8          	vsubsd %xmm0,%xmm13,%xmm13
  410948:	c5 13 5c e9          	vsubsd %xmm1,%xmm13,%xmm13
  41094c:	c5 f9 28 c8          	vmovapd %xmm0,%xmm1
  410950:	c4 c1 4b 58 f5       	vaddsd %xmm13,%xmm6,%xmm6
  410955:	c5 f3 58 ce          	vaddsd %xmm6,%xmm1,%xmm1
  410959:	c5 fb 5c c1          	vsubsd %xmm1,%xmm0,%xmm0
  41095d:	c5 fb 58 c6          	vaddsd %xmm6,%xmm0,%xmm0
  410961:	c5 f9 2e c3          	vucomisd %xmm3,%xmm0
  410965:	c5 fb 59 05 23 85 09 	vmulsd 0x98523(%rip),%xmm0,%xmm0        # 4a8e90 <_IO_stdin_used+0x50>
  41096c:	00 
  41096d:	0f 86 30 03 00 00    	jbe    410ca3 <__sin_avx+0xeb3>
  410973:	c5 fb 58 c3          	vaddsd %xmm3,%xmm0,%xmm0
  410977:	c5 fb 58 c1          	vaddsd %xmm1,%xmm0,%xmm0
  41097b:	c5 f9 2e c1          	vucomisd %xmm1,%xmm0
  41097f:	0f 8a b8 02 00 00    	jp     410c3d <__sin_avx+0xe4d>
  410985:	0f 85 b2 02 00 00    	jne    410c3d <__sin_avx+0xe4d>
  41098b:	c5 f9 2e d3          	vucomisd %xmm3,%xmm2
  41098f:	0f 87 0c f9 ff ff    	ja     4102a1 <__sin_avx+0x4b1>
  410995:	c5 fb 10 15 23 86 09 	vmovsd 0x98623(%rip),%xmm2        # 4a8fc0 <hp1+0x78>
  41099c:	00 
  41099d:	c5 e9 57 d1          	vxorpd %xmm1,%xmm2,%xmm2
  4109a1:	e9 2a f5 ff ff       	jmpq   40fed0 <__sin_avx+0xe0>
  4109a6:	66 2e 0f 1f 84 00 00 	nopw   %cs:0x0(%rax,%rax,1)
  4109ad:	00 00 00 
  4109b0:	c5 f9 2e d3          	vucomisd %xmm3,%xmm2
  4109b4:	0f 86 8a 05 00 00    	jbe    410f44 <__sin_avx+0x1154>
  4109ba:	c5 f9 28 cb          	vmovapd %xmm3,%xmm1
  4109be:	48 8d 7c 24 50       	lea    0x50(%rsp),%rdi
  4109c3:	c5 f9 28 c2          	vmovapd %xmm2,%xmm0
  4109c7:	c5 fb 11 14 24       	vmovsd %xmm2,(%rsp)
  4109cc:	e8 3f 50 ff ff       	callq  405a10 <__dubsin>
  4109d1:	c5 fb 10 4c 24 50    	vmovsd 0x50(%rsp),%xmm1
  4109d7:	c5 fb 10 05 49 85 09 	vmovsd 0x98549(%rip),%xmm0        # 4a8f28 <big+0x38>
  4109de:	00 
  4109df:	e9 9e f8 ff ff       	jmpq   410282 <__sin_avx+0x492>
  4109e4:	0f 1f 40 00          	nopl   0x0(%rax)
  4109e8:	c5 79 29 c9          	vmovapd %xmm9,%xmm1
  4109ec:	c5 f3 5c c8          	vsubsd %xmm0,%xmm1,%xmm1
  4109f0:	c5 f9 28 e1          	vmovapd %xmm1,%xmm4
  4109f4:	c4 c1 5b 5c e1       	vsubsd %xmm9,%xmm4,%xmm4
  4109f9:	c5 db 58 e0          	vaddsd %xmm0,%xmm4,%xmm4
  4109fd:	c5 fb 10 05 93 85 09 	vmovsd 0x98593(%rip),%xmm0        # 4a8f98 <hp1+0x50>
  410a04:	00 
  410a05:	c5 fb 5c c4          	vsubsd %xmm4,%xmm0,%xmm0
  410a09:	e9 79 f6 ff ff       	jmpq   410087 <__sin_avx+0x297>
  410a0e:	3d ff ff ef 7f       	cmp    $0x7fefffff,%eax
  410a13:	0f 8e 88 05 00 00    	jle    410fa1 <__sin_avx+0x11b1>
  410a19:	3d 00 00 f0 7f       	cmp    $0x7ff00000,%eax
  410a1e:	0f 84 ee 05 00 00    	je     411012 <__sin_avx+0x1222>
  410a24:	c5 eb 5e d2          	vdivsd %xmm2,%xmm2,%xmm2
  410a28:	e9 a3 f4 ff ff       	jmpq   40fed0 <__sin_avx+0xe0>
  410a2d:	c5 f3 5c cb          	vsubsd %xmm3,%xmm1,%xmm1
  410a31:	e9 46 fd ff ff       	jmpq   41077c <__sin_avx+0x98c>
  410a36:	c5 fb 10 3d 82 85 09 	vmovsd 0x98582(%rip),%xmm7        # 4a8fc0 <hp1+0x78>
  410a3d:	00 
  410a3e:	48 8d 7c 24 50       	lea    0x50(%rsp),%rdi
  410a43:	c5 f9 28 cb          	vmovapd %xmm3,%xmm1
  410a47:	c5 fb 11 54 24 28    	vmovsd %xmm2,0x28(%rsp)
  410a4d:	c5 f9 29 3c 24       	vmovapd %xmm7,(%rsp)
  410a52:	c5 c1 57 fa          	vxorpd %xmm2,%xmm7,%xmm7
  410a56:	c5 fb 11 5c 24 20    	vmovsd %xmm3,0x20(%rsp)
  410a5c:	c5 f9 28 ef          	vmovapd %xmm7,%xmm5
  410a60:	c5 f9 28 c5          	vmovapd %xmm5,%xmm0
  410a64:	c5 fb 11 6c 24 18    	vmovsd %xmm5,0x18(%rsp)
  410a6a:	e8 a1 4f ff ff       	callq  405a10 <__dubsin>
  410a6f:	c5 fb 10 64 24 50    	vmovsd 0x50(%rsp),%xmm4
  410a75:	c5 fb 10 0d 23 84 09 	vmovsd 0x98423(%rip),%xmm1        # 4a8ea0 <_IO_stdin_used+0x60>
  410a7c:	00 
  410a7d:	c5 f3 59 4c 24 58    	vmulsd 0x58(%rsp),%xmm1,%xmm1
  410a83:	c5 fb 10 6c 24 18    	vmovsd 0x18(%rsp),%xmm5
  410a89:	c5 fb 10 5c 24 20    	vmovsd 0x20(%rsp),%xmm3
  410a8f:	c5 fb 10 54 24 28    	vmovsd 0x28(%rsp),%xmm2
  410a95:	c5 f3 58 cc          	vaddsd %xmm4,%xmm1,%xmm1
  410a99:	c5 f9 2e e1          	vucomisd %xmm1,%xmm4
  410a9d:	7a 1e                	jp     410abd <__sin_avx+0xccd>
  410a9f:	75 1c                	jne    410abd <__sin_avx+0xccd>
  410aa1:	c5 f9 2e d3          	vucomisd %xmm3,%xmm2
  410aa5:	0f 87 6b fb ff ff    	ja     410616 <__sin_avx+0x826>
  410aab:	c5 f9 28 3c 24       	vmovapd (%rsp),%xmm7
  410ab0:	c5 c1 57 fc          	vxorpd %xmm4,%xmm7,%xmm7
  410ab4:	c5 f9 28 d7          	vmovapd %xmm7,%xmm2
  410ab8:	e9 13 f4 ff ff       	jmpq   40fed0 <__sin_avx+0xe0>
  410abd:	c5 f9 2e d3          	vucomisd %xmm3,%xmm2
  410ac1:	0f 87 29 fd ff ff    	ja     4107f0 <__sin_avx+0xa00>
  410ac7:	c5 f9 28 cb          	vmovapd %xmm3,%xmm1
  410acb:	31 ff                	xor    %edi,%edi
  410acd:	c5 f9 28 c5          	vmovapd %xmm5,%xmm0
  410ad1:	e8 1a 79 ff ff       	callq  4083f0 <__mpsin>
  410ad6:	c5 f9 28 d0          	vmovapd %xmm0,%xmm2
  410ada:	c5 e9 57 14 24       	vxorpd (%rsp),%xmm2,%xmm2
  410adf:	e9 ec f3 ff ff       	jmpq   40fed0 <__sin_avx+0xe0>
  410ae4:	c4 c1 79 2e d9       	vucomisd %xmm9,%xmm3
  410ae9:	0f 87 23 07 00 00    	ja     411212 <__sin_avx+0x1422>
  410aef:	c5 fb 10 05 f9 83 09 	vmovsd 0x983f9(%rip),%xmm0        # 4a8ef0 <big>
  410af6:	00 
  410af7:	c5 79 29 cf          	vmovapd %xmm9,%xmm7
  410afb:	c4 41 79 28 f9       	vmovapd %xmm9,%xmm15
  410b00:	c5 fb 10 2d f0 83 09 	vmovsd 0x983f0(%rip),%xmm5        # 4a8ef8 <big+0x8>
  410b07:	00 
  410b08:	c5 c3 58 f8          	vaddsd %xmm0,%xmm7,%xmm7
  410b0c:	c5 fb 10 25 ec 83 09 	vmovsd 0x983ec(%rip),%xmm4        # 4a8f00 <big+0x10>
  410b13:	00 
  410b14:	c5 7b 10 05 f4 83 09 	vmovsd 0x983f4(%rip),%xmm8        # 4a8f10 <big+0x20>
  410b1b:	00 
  410b1c:	c5 fb 11 3c 24       	vmovsd %xmm7,(%rsp)
  410b21:	48 8b 14 24          	mov    (%rsp),%rdx
  410b25:	c5 fb 11 7c 24 18    	vmovsd %xmm7,0x18(%rsp)
  410b2b:	c5 c3 5c f8          	vsubsd %xmm0,%xmm7,%xmm7
  410b2f:	c1 e2 02             	shl    $0x2,%edx
  410b32:	8d 4a 01             	lea    0x1(%rdx),%ecx
  410b35:	8d 42 02             	lea    0x2(%rdx),%eax
  410b38:	c5 03 5c ff          	vsubsd %xmm7,%xmm15,%xmm15
  410b3c:	c5 fb 10 3d d4 83 09 	vmovsd 0x983d4(%rip),%xmm7        # 4a8f18 <big+0x28>
  410b43:	00 
  410b44:	48 63 c9             	movslq %ecx,%rcx
  410b47:	48 98                	cltq   
  410b49:	c5 7b 10 34 c5 00 9a 	vmovsd 0x4a9a00(,%rax,8),%xmm14
  410b50:	4a 00 
  410b52:	8d 42 03             	lea    0x3(%rdx),%eax
  410b55:	48 63 d2             	movslq %edx,%rdx
  410b58:	c5 79 29 f8          	vmovapd %xmm15,%xmm0
  410b5c:	48 98                	cltq   
  410b5e:	c5 7b 10 14 c5 00 9a 	vmovsd 0x4a9a00(,%rax,8),%xmm10
  410b65:	4a 00 
  410b67:	c5 fb 58 c1          	vaddsd %xmm1,%xmm0,%xmm0
  410b6b:	c5 79 28 e8          	vmovapd %xmm0,%xmm13
  410b6f:	c5 79 28 d8          	vmovapd %xmm0,%xmm11
  410b73:	c5 13 59 e8          	vmulsd %xmm0,%xmm13,%xmm13
  410b77:	c5 79 29 ee          	vmovapd %xmm13,%xmm6
  410b7b:	c4 41 23 59 dd       	vmulsd %xmm13,%xmm11,%xmm11
  410b80:	c5 cb 59 f5          	vmulsd %xmm5,%xmm6,%xmm6
  410b84:	c5 cb 5c f4          	vsubsd %xmm4,%xmm6,%xmm6
  410b88:	c5 23 59 de          	vmulsd %xmm6,%xmm11,%xmm11
  410b8c:	c5 fb 10 35 8c 83 09 	vmovsd 0x9838c(%rip),%xmm6        # 4a8f20 <big+0x30>
  410b93:	00 
  410b94:	c5 23 58 d8          	vaddsd %xmm0,%xmm11,%xmm11
  410b98:	c5 fb 10 04 cd 00 9a 	vmovsd 0x4a9a00(,%rcx,8),%xmm0
  410b9f:	4a 00 
  410ba1:	c4 c1 7b 59 c3       	vmulsd %xmm11,%xmm0,%xmm0
  410ba6:	c5 23 59 1c d5 00 9a 	vmulsd 0x4a9a00(,%rdx,8),%xmm11,%xmm11
  410bad:	4a 00 
  410baf:	c5 2b 5c d0          	vsubsd %xmm0,%xmm10,%xmm10
  410bb3:	c5 79 29 e8          	vmovapd %xmm13,%xmm0
  410bb7:	c4 c1 7b 59 c0       	vmulsd %xmm8,%xmm0,%xmm0
  410bbc:	c5 fb 5c c7          	vsubsd %xmm7,%xmm0,%xmm0
  410bc0:	c4 c1 7b 59 c5       	vmulsd %xmm13,%xmm0,%xmm0
  410bc5:	c5 fb 58 c6          	vaddsd %xmm6,%xmm0,%xmm0
  410bc9:	c4 c1 7b 59 c5       	vmulsd %xmm13,%xmm0,%xmm0
  410bce:	c4 c1 7b 59 c6       	vmulsd %xmm14,%xmm0,%xmm0
  410bd3:	c5 2b 5c d0          	vsubsd %xmm0,%xmm10,%xmm10
  410bd7:	c5 79 29 f0          	vmovapd %xmm14,%xmm0
  410bdb:	c4 41 2b 5c d3       	vsubsd %xmm11,%xmm10,%xmm10
  410be0:	c4 c1 7b 58 c2       	vaddsd %xmm10,%xmm0,%xmm0
  410be5:	c5 0b 5c f0          	vsubsd %xmm0,%xmm14,%xmm14
  410be9:	c4 41 0b 58 f2       	vaddsd %xmm10,%xmm14,%xmm14
  410bee:	c5 79 2e f3          	vucomisd %xmm3,%xmm14
  410bf2:	c5 0b 59 35 86 83 09 	vmulsd 0x98386(%rip),%xmm14,%xmm14        # 4a8f80 <hp1+0x38>
  410bf9:	00 
  410bfa:	0f 86 08 06 00 00    	jbe    411208 <__sin_avx+0x1418>
  410c00:	c4 41 0b 58 f4       	vaddsd %xmm12,%xmm14,%xmm14
  410c05:	c5 0b 58 f0          	vaddsd %xmm0,%xmm14,%xmm14
  410c09:	c5 79 2e f0          	vucomisd %xmm0,%xmm14
  410c0d:	0f 8a 1a 04 00 00    	jp     41102d <__sin_avx+0x123d>
  410c13:	0f 85 14 04 00 00    	jne    41102d <__sin_avx+0x123d>
  410c19:	41 83 e4 02          	and    $0x2,%r12d
  410c1d:	c5 f9 28 d0          	vmovapd %xmm0,%xmm2
  410c21:	0f 85 62 f5 ff ff    	jne    410189 <__sin_avx+0x399>
  410c27:	e9 a4 f2 ff ff       	jmpq   40fed0 <__sin_avx+0xe0>
  410c2c:	c5 fb 10 0d 8c 83 09 	vmovsd 0x9838c(%rip),%xmm1        # 4a8fc0 <hp1+0x78>
  410c33:	00 
  410c34:	c5 f1 57 ca          	vxorpd %xmm2,%xmm1,%xmm1
  410c38:	e9 05 fa ff ff       	jmpq   410642 <__sin_avx+0x852>
  410c3d:	c5 f9 2e d3          	vucomisd %xmm3,%xmm2
  410c41:	0f 86 38 07 00 00    	jbe    41137f <__sin_avx+0x158f>
  410c47:	c5 f9 28 ca          	vmovapd %xmm2,%xmm1
  410c4b:	48 8d 7c 24 50       	lea    0x50(%rsp),%rdi
  410c50:	c5 fb 10 1d f0 82 09 	vmovsd 0x982f0(%rip),%xmm3        # 4a8f48 <hp1>
  410c57:	00 
  410c58:	c4 c1 73 5c cc       	vsubsd %xmm12,%xmm1,%xmm1
  410c5d:	c5 fb 11 14 24       	vmovsd %xmm2,(%rsp)
  410c62:	c5 f9 28 c1          	vmovapd %xmm1,%xmm0
  410c66:	c5 fb 5c c3          	vsubsd %xmm3,%xmm0,%xmm0
  410c6a:	c5 f3 5c c8          	vsubsd %xmm0,%xmm1,%xmm1
  410c6e:	c5 f3 5c cb          	vsubsd %xmm3,%xmm1,%xmm1
  410c72:	e8 29 67 ff ff       	callq  4073a0 <__docos>
  410c77:	c5 fb 10 4c 24 50    	vmovsd 0x50(%rsp),%xmm1
  410c7d:	c5 fb 10 05 a3 82 09 	vmovsd 0x982a3(%rip),%xmm0        # 4a8f28 <big+0x38>
  410c84:	00 
  410c85:	e9 f8 f5 ff ff       	jmpq   410282 <__sin_avx+0x492>
  410c8a:	c5 7b 10 25 2e 83 09 	vmovsd 0x9832e(%rip),%xmm12        # 4a8fc0 <hp1+0x78>
  410c91:	00 
  410c92:	c5 19 57 e2          	vxorpd %xmm2,%xmm12,%xmm12
  410c96:	c5 1b 59 25 da 82 09 	vmulsd 0x982da(%rip),%xmm12,%xmm12        # 4a8f78 <hp1+0x30>
  410c9d:	00 
  410c9e:	e9 a6 f6 ff ff       	jmpq   410349 <__sin_avx+0x559>
  410ca3:	c5 fb 5c c3          	vsubsd %xmm3,%xmm0,%xmm0
  410ca7:	e9 cb fc ff ff       	jmpq   410977 <__sin_avx+0xb87>
  410cac:	c5 e1 57 db          	vxorpd %xmm3,%xmm3,%xmm3
  410cb0:	c5 f9 2e d8          	vucomisd %xmm0,%xmm3
  410cb4:	0f 87 ac 0a 00 00    	ja     411766 <__sin_avx+0x1976>
  410cba:	c5 fb 10 25 2e 82 09 	vmovsd 0x9822e(%rip),%xmm4        # 4a8ef0 <big>
  410cc1:	00 
  410cc2:	c5 f9 28 e8          	vmovapd %xmm0,%xmm5
  410cc6:	c5 d3 58 ec          	vaddsd %xmm4,%xmm5,%xmm5
  410cca:	c5 fb 11 2c 24       	vmovsd %xmm5,(%rsp)
  410ccf:	c5 d3 5c ec          	vsubsd %xmm4,%xmm5,%xmm5
  410cd3:	48 8b 14 24          	mov    (%rsp),%rdx
  410cd7:	c5 f9 28 e0          	vmovapd %xmm0,%xmm4
  410cdb:	c1 e2 02             	shl    $0x2,%edx
  410cde:	c5 db 5c e5          	vsubsd %xmm5,%xmm4,%xmm4
  410ce2:	c5 fb 10 2d 0e 82 09 	vmovsd 0x9820e(%rip),%xmm5        # 4a8ef8 <big+0x8>
  410ce9:	00 
  410cea:	8d 72 01             	lea    0x1(%rdx),%esi
  410ced:	8d 42 02             	lea    0x2(%rdx),%eax
  410cf0:	48 63 f6             	movslq %esi,%rsi
  410cf3:	48 98                	cltq   
  410cf5:	c5 db 58 e1          	vaddsd %xmm1,%xmm4,%xmm4
  410cf9:	c5 7b 10 04 c5 00 9a 	vmovsd 0x4a9a00(,%rax,8),%xmm8
  410d00:	4a 00 
  410d02:	8d 42 03             	lea    0x3(%rdx),%eax
  410d05:	48 63 d2             	movslq %edx,%rdx
  410d08:	48 98                	cltq   
  410d0a:	c5 f9 28 fc          	vmovapd %xmm4,%xmm7
  410d0e:	c5 f9 28 f4          	vmovapd %xmm4,%xmm6
  410d12:	c5 c3 59 fc          	vmulsd %xmm4,%xmm7,%xmm7
  410d16:	c5 d3 59 ef          	vmulsd %xmm7,%xmm5,%xmm5
  410d1a:	c5 cb 59 f7          	vmulsd %xmm7,%xmm6,%xmm6
  410d1e:	c5 d3 5c 2d da 81 09 	vsubsd 0x981da(%rip),%xmm5,%xmm5        # 4a8f00 <big+0x10>
  410d25:	00 
  410d26:	c5 cb 59 f5          	vmulsd %xmm5,%xmm6,%xmm6
  410d2a:	c5 fb 10 2c c5 00 9a 	vmovsd 0x4a9a00(,%rax,8),%xmm5
  410d31:	4a 00 
  410d33:	c5 cb 58 f4          	vaddsd %xmm4,%xmm6,%xmm6
  410d37:	c5 fb 10 24 f5 00 9a 	vmovsd 0x4a9a00(,%rsi,8),%xmm4
  410d3e:	4a 00 
  410d40:	c5 db 59 e6          	vmulsd %xmm6,%xmm4,%xmm4
  410d44:	c5 cb 59 34 d5 00 9a 	vmulsd 0x4a9a00(,%rdx,8),%xmm6,%xmm6
  410d4b:	4a 00 
  410d4d:	c5 d3 5c ec          	vsubsd %xmm4,%xmm5,%xmm5
  410d51:	c5 fb 10 25 b7 81 09 	vmovsd 0x981b7(%rip),%xmm4        # 4a8f10 <big+0x20>
  410d58:	00 
  410d59:	c5 db 59 e7          	vmulsd %xmm7,%xmm4,%xmm4
  410d5d:	c5 db 5c 25 b3 81 09 	vsubsd 0x981b3(%rip),%xmm4,%xmm4        # 4a8f18 <big+0x28>
  410d64:	00 
  410d65:	c5 db 59 e7          	vmulsd %xmm7,%xmm4,%xmm4
  410d69:	c5 db 58 25 af 81 09 	vaddsd 0x981af(%rip),%xmm4,%xmm4        # 4a8f20 <big+0x30>
  410d70:	00 
  410d71:	c5 db 59 e7          	vmulsd %xmm7,%xmm4,%xmm4
  410d75:	c4 c1 5b 59 e0       	vmulsd %xmm8,%xmm4,%xmm4
  410d7a:	c5 d3 5c ec          	vsubsd %xmm4,%xmm5,%xmm5
  410d7e:	c5 79 29 c4          	vmovapd %xmm8,%xmm4
  410d82:	c5 d3 5c ee          	vsubsd %xmm6,%xmm5,%xmm5
  410d86:	c5 79 29 c6          	vmovapd %xmm8,%xmm6
  410d8a:	c5 cb 58 f5          	vaddsd %xmm5,%xmm6,%xmm6
  410d8e:	c5 db 5c e6          	vsubsd %xmm6,%xmm4,%xmm4
  410d92:	c5 db 58 e5          	vaddsd %xmm5,%xmm4,%xmm4
  410d96:	c5 f9 2e e3          	vucomisd %xmm3,%xmm4
  410d9a:	c5 db 59 25 de 81 09 	vmulsd 0x981de(%rip),%xmm4,%xmm4        # 4a8f80 <hp1+0x38>
  410da1:	00 
  410da2:	0f 86 b1 09 00 00    	jbe    411759 <__sin_avx+0x1969>
  410da8:	c5 db 58 25 e0 81 09 	vaddsd 0x981e0(%rip),%xmm4,%xmm4        # 4a8f90 <hp1+0x48>
  410daf:	00 
  410db0:	c5 db 58 e6          	vaddsd %xmm6,%xmm4,%xmm4
  410db4:	c5 f9 2e e6          	vucomisd %xmm6,%xmm4
  410db8:	0f 8a b3 05 00 00    	jp     411371 <__sin_avx+0x1581>
  410dbe:	0f 85 ad 05 00 00    	jne    411371 <__sin_avx+0x1581>
  410dc4:	83 e1 02             	and    $0x2,%ecx
  410dc7:	c5 f9 28 d6          	vmovapd %xmm6,%xmm2
  410dcb:	0f 84 ff f0 ff ff    	je     40fed0 <__sin_avx+0xe0>
  410dd1:	e9 b3 f3 ff ff       	jmpq   410189 <__sin_avx+0x399>
  410dd6:	c5 79 2e cb          	vucomisd %xmm3,%xmm9
  410dda:	41 bc 01 00 00 00    	mov    $0x1,%r12d
  410de0:	0f 86 5b 09 00 00    	jbe    411741 <__sin_avx+0x1951>
  410de6:	c5 fb 10 05 02 81 09 	vmovsd 0x98102(%rip),%xmm0        # 4a8ef0 <big>
  410ded:	00 
  410dee:	c4 41 79 28 d9       	vmovapd %xmm9,%xmm11
  410df3:	c5 79 29 cd          	vmovapd %xmm9,%xmm5
  410df7:	c5 f9 28 f1          	vmovapd %xmm1,%xmm6
  410dfb:	c5 23 58 d8          	vaddsd %xmm0,%xmm11,%xmm11
  410dff:	c5 79 29 df          	vmovapd %xmm11,%xmm7
  410e03:	c5 7b 11 1c 24       	vmovsd %xmm11,(%rsp)
  410e08:	48 8b 14 24          	mov    (%rsp),%rdx
  410e0c:	c5 c3 5c f8          	vsubsd %xmm0,%xmm7,%xmm7
  410e10:	c5 fb 10 05 e0 80 09 	vmovsd 0x980e0(%rip),%xmm0        # 4a8ef8 <big+0x8>
  410e17:	00 
  410e18:	c1 e2 02             	shl    $0x2,%edx
  410e1b:	8d 4a 03             	lea    0x3(%rdx),%ecx
  410e1e:	48 63 c2             	movslq %edx,%rax
  410e21:	c5 d3 5c ef          	vsubsd %xmm7,%xmm5,%xmm5
  410e25:	c5 f9 28 f9          	vmovapd %xmm1,%xmm7
  410e29:	48 63 c9             	movslq %ecx,%rcx
  410e2c:	c5 7b 10 14 c5 00 9a 	vmovsd 0x4a9a00(,%rax,8),%xmm10
  410e33:	4a 00 
  410e35:	8d 42 01             	lea    0x1(%rdx),%eax
  410e38:	c5 f9 28 e5          	vmovapd %xmm5,%xmm4
  410e3c:	c5 cb 59 f5          	vmulsd %xmm5,%xmm6,%xmm6
  410e40:	c5 79 28 c5          	vmovapd %xmm5,%xmm8
  410e44:	48 98                	cltq   
  410e46:	c5 db 59 e5          	vmulsd %xmm5,%xmm4,%xmm4
  410e4a:	c5 fb 59 c4          	vmulsd %xmm4,%xmm0,%xmm0
  410e4e:	c5 3b 59 c4          	vmulsd %xmm4,%xmm8,%xmm8
  410e52:	c5 fb 5c 05 a6 80 09 	vsubsd 0x980a6(%rip),%xmm0,%xmm0        # 4a8f00 <big+0x10>
  410e59:	00 
  410e5a:	c5 3b 59 c0          	vmulsd %xmm0,%xmm8,%xmm8
  410e5e:	c5 fb 10 05 aa 80 09 	vmovsd 0x980aa(%rip),%xmm0        # 4a8f10 <big+0x20>
  410e65:	00 
  410e66:	c5 fb 59 c4          	vmulsd %xmm4,%xmm0,%xmm0
  410e6a:	c4 c1 43 58 f8       	vaddsd %xmm8,%xmm7,%xmm7
  410e6f:	c5 fb 5c 05 a1 80 09 	vsubsd 0x980a1(%rip),%xmm0,%xmm0        # 4a8f18 <big+0x28>
  410e76:	00 
  410e77:	c5 c3 58 fd          	vaddsd %xmm5,%xmm7,%xmm7
  410e7b:	c5 fb 59 c4          	vmulsd %xmm4,%xmm0,%xmm0
  410e7f:	c5 fb 58 05 99 80 09 	vaddsd 0x98099(%rip),%xmm0,%xmm0        # 4a8f20 <big+0x30>
  410e86:	00 
  410e87:	c5 fb 59 c4          	vmulsd %xmm4,%xmm0,%xmm0
  410e8b:	c5 fb 10 24 cd 00 9a 	vmovsd 0x4a9a00(,%rcx,8),%xmm4
  410e92:	4a 00 
  410e94:	c5 db 59 e7          	vmulsd %xmm7,%xmm4,%xmm4
  410e98:	c5 cb 58 f0          	vaddsd %xmm0,%xmm6,%xmm6
  410e9c:	c5 db 58 24 c5 00 9a 	vaddsd 0x4a9a00(,%rax,8),%xmm4,%xmm4
  410ea3:	4a 00 
  410ea5:	8d 42 02             	lea    0x2(%rdx),%eax
  410ea8:	c4 c1 4b 59 f2       	vmulsd %xmm10,%xmm6,%xmm6
  410ead:	48 98                	cltq   
  410eaf:	c5 c3 59 3c c5 00 9a 	vmulsd 0x4a9a00(,%rax,8),%xmm7,%xmm7
  410eb6:	4a 00 
  410eb8:	c5 db 5c e6          	vsubsd %xmm6,%xmm4,%xmm4
  410ebc:	c5 79 29 d6          	vmovapd %xmm10,%xmm6
  410ec0:	c5 db 58 e7          	vaddsd %xmm7,%xmm4,%xmm4
  410ec4:	c5 79 29 d7          	vmovapd %xmm10,%xmm7
  410ec8:	c5 c3 58 fc          	vaddsd %xmm4,%xmm7,%xmm7
  410ecc:	c5 cb 5c f7          	vsubsd %xmm7,%xmm6,%xmm6
  410ed0:	c5 cb 58 f4          	vaddsd %xmm4,%xmm6,%xmm6
  410ed4:	c5 f9 2e f3          	vucomisd %xmm3,%xmm6
  410ed8:	c5 cb 59 35 88 80 09 	vmulsd 0x98088(%rip),%xmm6,%xmm6        # 4a8f68 <hp1+0x20>
  410edf:	00 
  410ee0:	0f 86 51 08 00 00    	jbe    411737 <__sin_avx+0x1947>
  410ee6:	c4 c1 4b 58 f4       	vaddsd %xmm12,%xmm6,%xmm6
  410eeb:	c5 cb 58 f7          	vaddsd %xmm7,%xmm6,%xmm6
  410eef:	c5 f9 2e f7          	vucomisd %xmm7,%xmm6
  410ef3:	0f 8a fe 06 00 00    	jp     4115f7 <__sin_avx+0x1807>
  410ef9:	0f 85 f8 06 00 00    	jne    4115f7 <__sin_avx+0x1807>
  410eff:	45 85 e4             	test   %r12d,%r12d
  410f02:	c5 f9 28 d7          	vmovapd %xmm7,%xmm2
  410f06:	0f 85 c4 ef ff ff    	jne    40fed0 <__sin_avx+0xe0>
  410f0c:	0f 1f 40 00          	nopl   0x0(%rax)
  410f10:	e9 74 f2 ff ff       	jmpq   410189 <__sin_avx+0x399>
  410f15:	c4 41 79 28 d1       	vmovapd %xmm9,%xmm10
  410f1a:	c5 7b 10 3d 76 80 09 	vmovsd 0x98076(%rip),%xmm15        # 4a8f98 <hp1+0x50>
  410f21:	00 
  410f22:	c5 2b 5c d1          	vsubsd %xmm1,%xmm10,%xmm10
  410f26:	c5 79 29 d0          	vmovapd %xmm10,%xmm0
  410f2a:	c4 c1 7b 5c c1       	vsubsd %xmm9,%xmm0,%xmm0
  410f2f:	c5 fb 58 c1          	vaddsd %xmm1,%xmm0,%xmm0
  410f33:	c5 fb 10 0d 85 80 09 	vmovsd 0x98085(%rip),%xmm1        # 4a8fc0 <hp1+0x78>
  410f3a:	00 
  410f3b:	c5 f9 57 c1          	vxorpd %xmm1,%xmm0,%xmm0
  410f3f:	e9 13 f9 ff ff       	jmpq   410857 <__sin_avx+0xa67>
  410f44:	c5 fb 10 3d 74 80 09 	vmovsd 0x98074(%rip),%xmm7        # 4a8fc0 <hp1+0x78>
  410f4b:	00 
  410f4c:	48 8d 7c 24 50       	lea    0x50(%rsp),%rdi
  410f51:	c5 f9 28 cb          	vmovapd %xmm3,%xmm1
  410f55:	c5 fb 11 54 24 28    	vmovsd %xmm2,0x28(%rsp)
  410f5b:	c5 f9 29 3c 24       	vmovapd %xmm7,(%rsp)
  410f60:	c5 c1 57 fa          	vxorpd %xmm2,%xmm7,%xmm7
  410f64:	c5 fb 11 5c 24 20    	vmovsd %xmm3,0x20(%rsp)
  410f6a:	c5 f9 28 ef          	vmovapd %xmm7,%xmm5
  410f6e:	c5 f9 28 c5          	vmovapd %xmm5,%xmm0
  410f72:	c5 fb 11 6c 24 18    	vmovsd %xmm5,0x18(%rsp)
  410f78:	e8 93 4a ff ff       	callq  405a10 <__dubsin>
  410f7d:	c5 fb 10 64 24 50    	vmovsd 0x50(%rsp),%xmm4
  410f83:	c5 fb 10 0d 9d 7f 09 	vmovsd 0x97f9d(%rip),%xmm1        # 4a8f28 <big+0x38>
  410f8a:	00 
  410f8b:	e9 ed fa ff ff       	jmpq   410a7d <__sin_avx+0xc8d>
  410f90:	c5 fb 10 05 28 80 09 	vmovsd 0x98028(%rip),%xmm0        # 4a8fc0 <hp1+0x78>
  410f97:	00 
  410f98:	c5 f9 57 c2          	vxorpd %xmm2,%xmm0,%xmm0
  410f9c:	e9 7d f8 ff ff       	jmpq   41081e <__sin_avx+0xa2e>
  410fa1:	48 8d 7c 24 40       	lea    0x40(%rsp),%rdi
  410fa6:	c5 f9 28 c2          	vmovapd %xmm2,%xmm0
  410faa:	48 8d 74 24 50       	lea    0x50(%rsp),%rsi
  410faf:	c5 fb 11 14 24       	vmovsd %xmm2,(%rsp)
  410fb4:	e8 07 45 ff ff       	callq  4054c0 <__branred>
  410fb9:	89 c7                	mov    %eax,%edi
  410fbb:	83 e0 03             	and    $0x3,%eax
  410fbe:	83 f8 02             	cmp    $0x2,%eax
  410fc1:	c5 fb 10 14 24       	vmovsd (%rsp),%xmm2
  410fc6:	0f 84 af 07 00 00    	je     41177b <__sin_avx+0x198b>
  410fcc:	83 f8 03             	cmp    $0x3,%eax
  410fcf:	0f 84 90 03 00 00    	je     411365 <__sin_avx+0x1575>
  410fd5:	83 f8 01             	cmp    $0x1,%eax
  410fd8:	0f 84 87 03 00 00    	je     411365 <__sin_avx+0x1575>
  410fde:	c5 fb 10 44 24 40    	vmovsd 0x40(%rsp),%xmm0
  410fe4:	c5 fb 10 1d 64 7f 09 	vmovsd 0x97f64(%rip),%xmm3        # 4a8f50 <hp1+0x8>
  410feb:	00 
  410fec:	c5 f9 28 c8          	vmovapd %xmm0,%xmm1
  410ff0:	c5 f3 59 c8          	vmulsd %xmm0,%xmm1,%xmm1
  410ff4:	c5 f9 2e d9          	vucomisd %xmm1,%xmm3
  410ff8:	c5 fb 10 4c 24 50    	vmovsd 0x50(%rsp),%xmm1
  410ffe:	0f 87 f5 f5 ff ff    	ja     4105f9 <__sin_avx+0x809>
  411004:	e8 37 e8 ff ff       	callq  40f840 <bsloww1>
  411009:	c5 f9 28 d0          	vmovapd %xmm0,%xmm2
  41100d:	e9 be ee ff ff       	jmpq   40fed0 <__sin_avx+0xe0>
  411012:	85 d2                	test   %edx,%edx
  411014:	0f 85 0a fa ff ff    	jne    410a24 <__sin_avx+0xc34>
  41101a:	48 c7 c0 c0 ff ff ff 	mov    $0xffffffffffffffc0,%rax
  411021:	64 c7 00 21 00 00 00 	movl   $0x21,%fs:(%rax)
  411028:	e9 f7 f9 ff ff       	jmpq   410a24 <__sin_avx+0xc34>
  41102d:	c5 f9 2e d3          	vucomisd %xmm3,%xmm2
  411031:	48 8b 44 24 18       	mov    0x18(%rsp),%rax
  411036:	0f 86 84 07 00 00    	jbe    4117c0 <__sin_avx+0x19d0>
  41103c:	c5 fb 10 05 64 7e 09 	vmovsd 0x97e64(%rip),%xmm0        # 4a8ea8 <_IO_stdin_used+0x68>
  411043:	00 
  411044:	c5 fb 59 c2          	vmulsd %xmm2,%xmm0,%xmm0
  411048:	c5 fb 11 04 24       	vmovsd %xmm0,(%rsp)
  41104d:	c4 41 79 28 d7       	vmovapd %xmm15,%xmm10
  411052:	c1 e0 02             	shl    $0x2,%eax
  411055:	48 63 d0             	movslq %eax,%rdx
  411058:	c5 7b 10 1d a8 7e 09 	vmovsd 0x97ea8(%rip),%xmm11        # 4a8f08 <big+0x18>
  41105f:	00 
  411060:	c4 41 2b 59 d7       	vmulsd %xmm15,%xmm10,%xmm10
  411065:	c4 41 79 28 e7       	vmovapd %xmm15,%xmm12
  41106a:	c5 7b 10 34 d5 00 9a 	vmovsd 0x4a9a00(,%rdx,8),%xmm14
  411071:	4a 00 
  411073:	8d 50 02             	lea    0x2(%rax),%edx
  411076:	c4 41 1b 58 e3       	vaddsd %xmm11,%xmm12,%xmm12
  41107b:	c5 79 29 f0          	vmovapd %xmm14,%xmm0
  41107f:	48 63 d2             	movslq %edx,%rdx
  411082:	c4 41 3b 59 c2       	vmulsd %xmm10,%xmm8,%xmm8
  411087:	c4 c1 7b 58 c3       	vaddsd %xmm11,%xmm0,%xmm0
  41108c:	c5 7b 10 2c d5 00 9a 	vmovsd 0x4a9a00(,%rdx,8),%xmm13
  411093:	4a 00 
  411095:	c4 41 1b 5c e3       	vsubsd %xmm11,%xmm12,%xmm12
  41109a:	8d 50 03             	lea    0x3(%rax),%edx
  41109d:	83 c0 01             	add    $0x1,%eax
  4110a0:	48 98                	cltq   
  4110a2:	c4 c1 53 59 ea       	vmulsd %xmm10,%xmm5,%xmm5
  4110a7:	c5 3b 5c c7          	vsubsd %xmm7,%xmm8,%xmm8
  4110ab:	c5 79 29 ff          	vmovapd %xmm15,%xmm7
  4110af:	c4 c1 7b 5c c3       	vsubsd %xmm11,%xmm0,%xmm0
  4110b4:	c5 79 28 d9          	vmovapd %xmm1,%xmm11
  4110b8:	c4 c1 43 5c fc       	vsubsd %xmm12,%xmm7,%xmm7
  4110bd:	48 63 d2             	movslq %edx,%rdx
  4110c0:	c4 41 23 59 df       	vmulsd %xmm15,%xmm11,%xmm11
  4110c5:	c5 d3 5c ec          	vsubsd %xmm4,%xmm5,%xmm5
  4110c9:	c4 41 3b 59 c2       	vmulsd %xmm10,%xmm8,%xmm8
  4110ce:	c5 79 29 ec          	vmovapd %xmm13,%xmm4
  4110d2:	c5 c3 58 f9          	vaddsd %xmm1,%xmm7,%xmm7
  4110d6:	c5 3b 58 c6          	vaddsd %xmm6,%xmm8,%xmm8
  4110da:	c5 fb 10 34 d5 00 9a 	vmovsd 0x4a9a00(,%rdx,8),%xmm6
  4110e1:	4a 00 
  4110e3:	c5 c3 59 f8          	vmulsd %xmm0,%xmm7,%xmm7
  4110e7:	c4 41 3b 59 c2       	vmulsd %xmm10,%xmm8,%xmm8
  4110ec:	c4 41 23 58 d8       	vaddsd %xmm8,%xmm11,%xmm11
  4110f1:	c4 41 23 59 dd       	vmulsd %xmm13,%xmm11,%xmm11
  4110f6:	c4 c1 4b 5c f3       	vsubsd %xmm11,%xmm6,%xmm6
  4110fb:	c5 cb 5c f7          	vsubsd %xmm7,%xmm6,%xmm6
  4110ff:	c5 79 29 f7          	vmovapd %xmm14,%xmm7
  411103:	c5 c3 5c f8          	vsubsd %xmm0,%xmm7,%xmm7
  411107:	c4 c1 7b 59 c4       	vmulsd %xmm12,%xmm0,%xmm0
  41110c:	c5 c3 58 3c c5 00 9a 	vaddsd 0x4a9a00(,%rax,8),%xmm7,%xmm7
  411113:	4a 00 
  411115:	c5 db 5c e0          	vsubsd %xmm0,%xmm4,%xmm4
  411119:	c5 13 5c ec          	vsubsd %xmm4,%xmm13,%xmm13
  41111d:	c4 c1 43 59 ff       	vmulsd %xmm15,%xmm7,%xmm7
  411122:	c5 13 5c e8          	vsubsd %xmm0,%xmm13,%xmm13
  411126:	c5 f9 28 c4          	vmovapd %xmm4,%xmm0
  41112a:	c5 cb 5c f7          	vsubsd %xmm7,%xmm6,%xmm6
  41112e:	c5 79 29 ff          	vmovapd %xmm15,%xmm7
  411132:	c4 c1 43 59 fa       	vmulsd %xmm10,%xmm7,%xmm7
  411137:	c5 c3 59 fd          	vmulsd %xmm5,%xmm7,%xmm7
  41113b:	c4 c1 43 59 fe       	vmulsd %xmm14,%xmm7,%xmm7
  411140:	c5 cb 5c f7          	vsubsd %xmm7,%xmm6,%xmm6
  411144:	c4 c1 4b 58 f5       	vaddsd %xmm13,%xmm6,%xmm6
  411149:	c5 fb 58 c6          	vaddsd %xmm6,%xmm0,%xmm0
  41114d:	c5 db 5c e0          	vsubsd %xmm0,%xmm4,%xmm4
  411151:	c5 db 58 e6          	vaddsd %xmm6,%xmm4,%xmm4
  411155:	c5 f9 2e e3          	vucomisd %xmm3,%xmm4
  411159:	c5 db 59 25 2f 7d 09 	vmulsd 0x97d2f(%rip),%xmm4,%xmm4        # 4a8e90 <_IO_stdin_used+0x50>
  411160:	00 
  411161:	0f 86 4f 06 00 00    	jbe    4117b6 <__sin_avx+0x19c6>
  411167:	c5 db 58 24 24       	vaddsd (%rsp),%xmm4,%xmm4
  41116c:	c5 db 58 e0          	vaddsd %xmm0,%xmm4,%xmm4
  411170:	c5 f9 2e e0          	vucomisd %xmm0,%xmm4
  411174:	7a 06                	jp     41117c <__sin_avx+0x138c>
  411176:	0f 84 9d fa ff ff    	je     410c19 <__sin_avx+0xe29>
  41117c:	c5 79 29 c8          	vmovapd %xmm9,%xmm0
  411180:	48 8d 7c 24 50       	lea    0x50(%rsp),%rdi
  411185:	c5 fb 11 5c 24 18    	vmovsd %xmm3,0x18(%rsp)
  41118b:	c5 fb 11 14 24       	vmovsd %xmm2,(%rsp)
  411190:	e8 0b 62 ff ff       	callq  4073a0 <__docos>
  411195:	c5 fb 10 44 24 58    	vmovsd 0x58(%rsp),%xmm0
  41119b:	c5 fb 10 5c 24 18    	vmovsd 0x18(%rsp),%xmm3
  4111a1:	c5 f9 28 c8          	vmovapd %xmm0,%xmm1
  4111a5:	c5 fb 10 14 24       	vmovsd (%rsp),%xmm2
  4111aa:	c5 f9 2e c3          	vucomisd %xmm3,%xmm0
  4111ae:	c5 f3 59 0d 72 7d 09 	vmulsd 0x97d72(%rip),%xmm1,%xmm1        # 4a8f28 <big+0x38>
  4111b5:	00 
  4111b6:	0f 86 25 09 00 00    	jbe    411ae1 <__sin_avx+0x1cf1>
  4111bc:	c5 f9 2e d3          	vucomisd %xmm3,%xmm2
  4111c0:	0f 86 bc 08 00 00    	jbe    411a82 <__sin_avx+0x1c92>
  4111c6:	c5 fb 10 05 e2 7c 09 	vmovsd 0x97ce2(%rip),%xmm0        # 4a8eb0 <_IO_stdin_used+0x70>
  4111cd:	00 
  4111ce:	c5 fb 59 c2          	vmulsd %xmm2,%xmm0,%xmm0
  4111d2:	c5 fb 58 c1          	vaddsd %xmm1,%xmm0,%xmm0
  4111d6:	c5 fb 10 4c 24 50    	vmovsd 0x50(%rsp),%xmm1
  4111dc:	c5 fb 58 c1          	vaddsd %xmm1,%xmm0,%xmm0
  4111e0:	c5 f9 2e c8          	vucomisd %xmm0,%xmm1
  4111e4:	0f 8a 3d 06 00 00    	jp     411827 <__sin_avx+0x1a37>
  4111ea:	0f 85 37 06 00 00    	jne    411827 <__sin_avx+0x1a37>
  4111f0:	41 80 e4 02          	and    $0x2,%r12b
  4111f4:	c5 f9 28 d1          	vmovapd %xmm1,%xmm2
  4111f8:	0f 85 8b ef ff ff    	jne    410189 <__sin_avx+0x399>
  4111fe:	66 90                	xchg   %ax,%ax
  411200:	e9 cb ec ff ff       	jmpq   40fed0 <__sin_avx+0xe0>
  411205:	0f 1f 00             	nopl   (%rax)
  411208:	c4 41 0b 5c f4       	vsubsd %xmm12,%xmm14,%xmm14
  41120d:	e9 f3 f9 ff ff       	jmpq   410c05 <__sin_avx+0xe15>
  411212:	c5 fb 10 05 a6 7d 09 	vmovsd 0x97da6(%rip),%xmm0        # 4a8fc0 <hp1+0x78>
  411219:	00 
  41121a:	c5 31 57 c8          	vxorpd %xmm0,%xmm9,%xmm9
  41121e:	c5 f1 57 c8          	vxorpd %xmm0,%xmm1,%xmm1
  411222:	e9 c8 f8 ff ff       	jmpq   410aef <__sin_avx+0xcff>
  411227:	c5 e1 57 db          	vxorpd %xmm3,%xmm3,%xmm3
  41122b:	c5 f9 2e c3          	vucomisd %xmm3,%xmm0
  41122f:	0f 86 c3 05 00 00    	jbe    4117f8 <__sin_avx+0x1a08>
  411235:	c5 f9 28 e0          	vmovapd %xmm0,%xmm4
  411239:	be 01 00 00 00       	mov    $0x1,%esi
  41123e:	c5 f9 28 f9          	vmovapd %xmm1,%xmm7
  411242:	c5 fb 10 2d a6 7c 09 	vmovsd 0x97ca6(%rip),%xmm5        # 4a8ef0 <big>
  411249:	00 
  41124a:	c5 f9 28 f4          	vmovapd %xmm4,%xmm6
  41124e:	c5 cb 58 f5          	vaddsd %xmm5,%xmm6,%xmm6
  411252:	c5 fb 11 34 24       	vmovsd %xmm6,(%rsp)
  411257:	c5 cb 5c f5          	vsubsd %xmm5,%xmm6,%xmm6
  41125b:	48 8b 14 24          	mov    (%rsp),%rdx
  41125f:	c5 fb 10 2d 91 7c 09 	vmovsd 0x97c91(%rip),%xmm5        # 4a8ef8 <big+0x8>
  411266:	00 
  411267:	c1 e2 02             	shl    $0x2,%edx
  41126a:	c5 db 5c e6          	vsubsd %xmm6,%xmm4,%xmm4
  41126e:	8d 4a 03             	lea    0x3(%rdx),%ecx
  411271:	48 63 c2             	movslq %edx,%rax
  411274:	c5 7b 10 0c c5 00 9a 	vmovsd 0x4a9a00(,%rax,8),%xmm9
  41127b:	4a 00 
  41127d:	8d 42 01             	lea    0x1(%rdx),%eax
  411280:	48 63 c9             	movslq %ecx,%rcx
  411283:	48 98                	cltq   
  411285:	c5 79 28 c4          	vmovapd %xmm4,%xmm8
  411289:	c5 f9 28 f4          	vmovapd %xmm4,%xmm6
  41128d:	c5 3b 59 c4          	vmulsd %xmm4,%xmm8,%xmm8
  411291:	c4 c1 53 59 e8       	vmulsd %xmm8,%xmm5,%xmm5
  411296:	c4 c1 4b 59 f0       	vmulsd %xmm8,%xmm6,%xmm6
  41129b:	c5 d3 5c 2d 5d 7c 09 	vsubsd 0x97c5d(%rip),%xmm5,%xmm5        # 4a8f00 <big+0x10>
  4112a2:	00 
  4112a3:	c5 cb 59 f5          	vmulsd %xmm5,%xmm6,%xmm6
  4112a7:	c5 fb 10 2c cd 00 9a 	vmovsd 0x4a9a00(,%rcx,8),%xmm5
  4112ae:	4a 00 
  4112b0:	c5 cb 58 f7          	vaddsd %xmm7,%xmm6,%xmm6
  4112b4:	c5 c3 59 fc          	vmulsd %xmm4,%xmm7,%xmm7
  4112b8:	c5 cb 58 f4          	vaddsd %xmm4,%xmm6,%xmm6
  4112bc:	c5 fb 10 25 4c 7c 09 	vmovsd 0x97c4c(%rip),%xmm4        # 4a8f10 <big+0x20>
  4112c3:	00 
  4112c4:	c4 c1 5b 59 e0       	vmulsd %xmm8,%xmm4,%xmm4
  4112c9:	c5 d3 59 ee          	vmulsd %xmm6,%xmm5,%xmm5
  4112cd:	c5 db 5c 25 43 7c 09 	vsubsd 0x97c43(%rip),%xmm4,%xmm4        # 4a8f18 <big+0x28>
  4112d4:	00 
  4112d5:	c5 d3 58 2c c5 00 9a 	vaddsd 0x4a9a00(,%rax,8),%xmm5,%xmm5
  4112dc:	4a 00 
  4112de:	8d 42 02             	lea    0x2(%rdx),%eax
  4112e1:	48 98                	cltq   
  4112e3:	c5 cb 59 34 c5 00 9a 	vmulsd 0x4a9a00(,%rax,8),%xmm6,%xmm6
  4112ea:	4a 00 
  4112ec:	c4 c1 5b 59 e0       	vmulsd %xmm8,%xmm4,%xmm4
  4112f1:	c5 db 58 25 27 7c 09 	vaddsd 0x97c27(%rip),%xmm4,%xmm4        # 4a8f20 <big+0x30>
  4112f8:	00 
  4112f9:	c4 c1 5b 59 e0       	vmulsd %xmm8,%xmm4,%xmm4
  4112fe:	c5 c3 58 fc          	vaddsd %xmm4,%xmm7,%xmm7
  411302:	c5 79 29 cc          	vmovapd %xmm9,%xmm4
  411306:	c4 c1 43 59 f9       	vmulsd %xmm9,%xmm7,%xmm7
  41130b:	c5 d3 5c ef          	vsubsd %xmm7,%xmm5,%xmm5
  41130f:	c5 d3 58 ee          	vaddsd %xmm6,%xmm5,%xmm5
  411313:	c5 79 29 ce          	vmovapd %xmm9,%xmm6
  411317:	c5 cb 58 f5          	vaddsd %xmm5,%xmm6,%xmm6
  41131b:	c5 db 5c e6          	vsubsd %xmm6,%xmm4,%xmm4
  41131f:	c5 db 58 e5          	vaddsd %xmm5,%xmm4,%xmm4
  411323:	c5 f9 2e e3          	vucomisd %xmm3,%xmm4
  411327:	c5 db 59 25 39 7c 09 	vmulsd 0x97c39(%rip),%xmm4,%xmm4        # 4a8f68 <hp1+0x20>
  41132e:	00 
  41132f:	0f 86 b6 04 00 00    	jbe    4117eb <__sin_avx+0x19fb>
  411335:	c5 db 58 25 53 7c 09 	vaddsd 0x97c53(%rip),%xmm4,%xmm4        # 4a8f90 <hp1+0x48>
  41133c:	00 
  41133d:	c5 db 58 e6          	vaddsd %xmm6,%xmm4,%xmm4
  411341:	c5 f9 2e e6          	vucomisd %xmm6,%xmm4
  411345:	0f 8a b9 fc ff ff    	jp     411004 <__sin_avx+0x1214>
  41134b:	0f 85 b3 fc ff ff    	jne    411004 <__sin_avx+0x1214>
  411351:	85 f6                	test   %esi,%esi
  411353:	c5 f9 28 d6          	vmovapd %xmm6,%xmm2
  411357:	0f 85 73 eb ff ff    	jne    40fed0 <__sin_avx+0xe0>
  41135d:	0f 1f 00             	nopl   (%rax)
  411360:	e9 24 ee ff ff       	jmpq   410189 <__sin_avx+0x399>
  411365:	c5 fb 10 4c 24 50    	vmovsd 0x50(%rsp),%xmm1
  41136b:	c5 fb 10 44 24 40    	vmovsd 0x40(%rsp),%xmm0
  411371:	e8 ba e7 ff ff       	callq  40fb30 <bsloww2>
  411376:	c5 f9 28 d0          	vmovapd %xmm0,%xmm2
  41137a:	e9 51 eb ff ff       	jmpq   40fed0 <__sin_avx+0xe0>
  41137f:	c5 fb 10 3d 39 7c 09 	vmovsd 0x97c39(%rip),%xmm7        # 4a8fc0 <hp1+0x78>
  411386:	00 
  411387:	48 8d 7c 24 50       	lea    0x50(%rsp),%rdi
  41138c:	c5 fb 10 25 b4 7b 09 	vmovsd 0x97bb4(%rip),%xmm4        # 4a8f48 <hp1>
  411393:	00 
  411394:	c5 f9 29 3c 24       	vmovapd %xmm7,(%rsp)
  411399:	c5 c1 57 fa          	vxorpd %xmm2,%xmm7,%xmm7
  41139d:	c5 fb 11 5c 24 28    	vmovsd %xmm3,0x28(%rsp)
  4113a3:	c5 fb 11 54 24 20    	vmovsd %xmm2,0x20(%rsp)
  4113a9:	c5 f9 28 ef          	vmovapd %xmm7,%xmm5
  4113ad:	c5 f9 28 cd          	vmovapd %xmm5,%xmm1
  4113b1:	c5 fb 11 6c 24 18    	vmovsd %xmm5,0x18(%rsp)
  4113b7:	c4 c1 73 5c cc       	vsubsd %xmm12,%xmm1,%xmm1
  4113bc:	c5 f9 28 c1          	vmovapd %xmm1,%xmm0
  4113c0:	c5 fb 5c c4          	vsubsd %xmm4,%xmm0,%xmm0
  4113c4:	c5 f3 5c c8          	vsubsd %xmm0,%xmm1,%xmm1
  4113c8:	c5 f3 5c cc          	vsubsd %xmm4,%xmm1,%xmm1
  4113cc:	e8 cf 5f ff ff       	callq  4073a0 <__docos>
  4113d1:	c5 fb 10 0d 4f 7b 09 	vmovsd 0x97b4f(%rip),%xmm1        # 4a8f28 <big+0x38>
  4113d8:	00 
  4113d9:	c5 fb 10 64 24 50    	vmovsd 0x50(%rsp),%xmm4
  4113df:	c5 f3 59 4c 24 58    	vmulsd 0x58(%rsp),%xmm1,%xmm1
  4113e5:	c5 fb 10 6c 24 18    	vmovsd 0x18(%rsp),%xmm5
  4113eb:	c5 fb 10 54 24 20    	vmovsd 0x20(%rsp),%xmm2
  4113f1:	c5 fb 10 5c 24 28    	vmovsd 0x28(%rsp),%xmm3
  4113f7:	c5 f3 58 cc          	vaddsd %xmm4,%xmm1,%xmm1
  4113fb:	c5 f9 2e e1          	vucomisd %xmm1,%xmm4
  4113ff:	0f 8a b8 f6 ff ff    	jp     410abd <__sin_avx+0xccd>
  411405:	0f 85 b2 f6 ff ff    	jne    410abd <__sin_avx+0xccd>
  41140b:	c5 f9 2e d3          	vucomisd %xmm3,%xmm2
  41140f:	0f 86 96 f6 ff ff    	jbe    410aab <__sin_avx+0xcbb>
  411415:	e9 fc f1 ff ff       	jmpq   410616 <__sin_avx+0x826>
  41141a:	66 0f 1f 44 00 00    	nopw   0x0(%rax,%rax,1)
  411420:	c4 41 79 28 f1       	vmovapd %xmm9,%xmm14
  411425:	c5 7b 10 25 1b 7a 09 	vmovsd 0x97a1b(%rip),%xmm12        # 4a8e48 <_IO_stdin_used+0x8>
  41142c:	00 
  41142d:	c4 41 79 28 d9       	vmovapd %xmm9,%xmm11
  411432:	c4 41 0b 59 f1       	vmulsd %xmm9,%xmm14,%xmm14
  411437:	c4 41 79 28 e9       	vmovapd %xmm9,%xmm13
  41143c:	c4 41 23 58 dc       	vaddsd %xmm12,%xmm11,%xmm11
  411441:	c4 41 79 28 f9       	vmovapd %xmm9,%xmm15
  411446:	c4 41 2b 59 d6       	vmulsd %xmm14,%xmm10,%xmm10
  41144b:	c4 41 23 5c dc       	vsubsd %xmm12,%xmm11,%xmm11
  411450:	c5 7b 10 25 f8 79 09 	vmovsd 0x979f8(%rip),%xmm12        # 4a8e50 <_IO_stdin_used+0x10>
  411457:	00 
  411458:	c4 41 2b 58 d0       	vaddsd %xmm8,%xmm10,%xmm10
  41145d:	c4 41 1b 59 e3       	vmulsd %xmm11,%xmm12,%xmm12
  411462:	c4 41 13 5c eb       	vsubsd %xmm11,%xmm13,%xmm13
  411467:	c4 41 2b 59 d6       	vmulsd %xmm14,%xmm10,%xmm10
  41146c:	c4 41 1b 59 e3       	vmulsd %xmm11,%xmm12,%xmm12
  411471:	c5 13 58 e9          	vaddsd %xmm1,%xmm13,%xmm13
  411475:	c5 2b 5c d7          	vsubsd %xmm7,%xmm10,%xmm10
  411479:	c4 41 1b 59 e3       	vmulsd %xmm11,%xmm12,%xmm12
  41147e:	c5 23 59 1d fa 79 09 	vmulsd 0x979fa(%rip),%xmm11,%xmm11        # 4a8e80 <_IO_stdin_used+0x40>
  411485:	00 
  411486:	c4 41 2b 59 d6       	vmulsd %xmm14,%xmm10,%xmm10
  41148b:	c4 41 03 58 fc       	vaddsd %xmm12,%xmm15,%xmm15
  411490:	c5 2b 58 d0          	vaddsd %xmm0,%xmm10,%xmm10
  411494:	c5 fb 10 05 b4 79 09 	vmovsd 0x979b4(%rip),%xmm0        # 4a8e50 <_IO_stdin_used+0x10>
  41149b:	00 
  41149c:	c4 41 23 59 dd       	vmulsd %xmm13,%xmm11,%xmm11
  4114a1:	c4 c1 7b 59 c5       	vmulsd %xmm13,%xmm0,%xmm0
  4114a6:	c4 41 2b 59 d6       	vmulsd %xmm14,%xmm10,%xmm10
  4114ab:	c4 c1 7b 59 c5       	vmulsd %xmm13,%xmm0,%xmm0
  4114b0:	c5 2b 58 15 c0 79 09 	vaddsd 0x979c0(%rip),%xmm10,%xmm10        # 4a8e78 <_IO_stdin_used+0x38>
  4114b7:	00 
  4114b8:	c4 c1 7b 59 c5       	vmulsd %xmm13,%xmm0,%xmm0
  4114bd:	c4 41 2b 59 d6       	vmulsd %xmm14,%xmm10,%xmm10
  4114c2:	c4 41 2b 58 d3       	vaddsd %xmm11,%xmm10,%xmm10
  4114c7:	c4 41 2b 59 d1       	vmulsd %xmm9,%xmm10,%xmm10
  4114cc:	c5 2b 58 d0          	vaddsd %xmm0,%xmm10,%xmm10
  4114d0:	c5 79 29 c8          	vmovapd %xmm9,%xmm0
  4114d4:	c4 c1 7b 5c c7       	vsubsd %xmm15,%xmm0,%xmm0
  4114d9:	c5 2b 58 d1          	vaddsd %xmm1,%xmm10,%xmm10
  4114dd:	c4 c1 7b 58 c4       	vaddsd %xmm12,%xmm0,%xmm0
  4114e2:	c5 2b 58 d0          	vaddsd %xmm0,%xmm10,%xmm10
  4114e6:	c5 79 29 f8          	vmovapd %xmm15,%xmm0
  4114ea:	c4 c1 7b 58 c2       	vaddsd %xmm10,%xmm0,%xmm0
  4114ef:	c5 03 5c f8          	vsubsd %xmm0,%xmm15,%xmm15
  4114f3:	c4 41 03 58 fa       	vaddsd %xmm10,%xmm15,%xmm15
  4114f8:	c5 79 2e fb          	vucomisd %xmm3,%xmm15
  4114fc:	c5 03 59 3d 8c 79 09 	vmulsd 0x9798c(%rip),%xmm15,%xmm15        # 4a8e90 <_IO_stdin_used+0x50>
  411503:	00 
  411504:	0f 86 04 05 00 00    	jbe    411a0e <__sin_avx+0x1c1e>
  41150a:	c5 f9 2e d3          	vucomisd %xmm3,%xmm2
  41150e:	0f 86 1d 05 00 00    	jbe    411a31 <__sin_avx+0x1c41>
  411514:	c5 fb 10 3d 8c 79 09 	vmovsd 0x9798c(%rip),%xmm7        # 4a8ea8 <_IO_stdin_used+0x68>
  41151b:	00 
  41151c:	c5 c3 59 fa          	vmulsd %xmm2,%xmm7,%xmm7
  411520:	c4 c1 43 58 ff       	vaddsd %xmm15,%xmm7,%xmm7
  411525:	c5 c3 58 f8          	vaddsd %xmm0,%xmm7,%xmm7
  411529:	c5 f9 2e c7          	vucomisd %xmm7,%xmm0
  41152d:	0f 8b e9 02 00 00    	jnp    41181c <__sin_avx+0x1a2c>
  411533:	c5 79 2e cb          	vucomisd %xmm3,%xmm9
  411537:	c5 fb 11 5c 24 38    	vmovsd %xmm3,0x38(%rsp)
  41153d:	4c 8d 64 24 50       	lea    0x50(%rsp),%r12
  411542:	c5 fb 11 54 24 30    	vmovsd %xmm2,0x30(%rsp)
  411548:	c5 fb 11 64 24 28    	vmovsd %xmm4,0x28(%rsp)
  41154e:	c5 fb 11 74 24 20    	vmovsd %xmm6,0x20(%rsp)
  411554:	c5 fb 11 6c 24 18    	vmovsd %xmm5,0x18(%rsp)
  41155a:	0f 86 3b 05 00 00    	jbe    411a9b <__sin_avx+0x1cab>
  411560:	c5 79 29 c8          	vmovapd %xmm9,%xmm0
  411564:	4c 89 e7             	mov    %r12,%rdi
  411567:	c5 7b 11 0c 24       	vmovsd %xmm9,(%rsp)
  41156c:	e8 9f 44 ff ff       	callq  405a10 <__dubsin>
  411571:	c5 7b 10 0c 24       	vmovsd (%rsp),%xmm9
  411576:	c5 fb 10 6c 24 18    	vmovsd 0x18(%rsp),%xmm5
  41157c:	c5 fb 10 74 24 20    	vmovsd 0x20(%rsp),%xmm6
  411582:	c5 fb 10 64 24 28    	vmovsd 0x28(%rsp),%xmm4
  411588:	c5 fb 10 54 24 30    	vmovsd 0x30(%rsp),%xmm2
  41158e:	c5 fb 10 5c 24 38    	vmovsd 0x38(%rsp),%xmm3
  411594:	c5 fb 10 44 24 58    	vmovsd 0x58(%rsp),%xmm0
  41159a:	c5 fb 10 3d fe 78 09 	vmovsd 0x978fe(%rip),%xmm7        # 4a8ea0 <_IO_stdin_used+0x60>
  4115a1:	00 
  4115a2:	c5 f9 2e c3          	vucomisd %xmm3,%xmm0
  4115a6:	c5 fb 59 c7          	vmulsd %xmm7,%xmm0,%xmm0
  4115aa:	0f 86 b3 04 00 00    	jbe    411a63 <__sin_avx+0x1c73>
  4115b0:	c5 f9 2e d3          	vucomisd %xmm3,%xmm2
  4115b4:	0f 86 90 04 00 00    	jbe    411a4a <__sin_avx+0x1c5a>
  4115ba:	c5 fb 10 0d ee 78 09 	vmovsd 0x978ee(%rip),%xmm1        # 4a8eb0 <_IO_stdin_used+0x70>
  4115c1:	00 
  4115c2:	c5 f3 59 ca          	vmulsd %xmm2,%xmm1,%xmm1
  4115c6:	c5 fb 58 c1          	vaddsd %xmm1,%xmm0,%xmm0
  4115ca:	c5 fb 10 4c 24 50    	vmovsd 0x50(%rsp),%xmm1
  4115d0:	c5 fb 58 c1          	vaddsd %xmm1,%xmm0,%xmm0
  4115d4:	c5 f9 2e c8          	vucomisd %xmm0,%xmm1
  4115d8:	0f 8a 64 02 00 00    	jp     411842 <__sin_avx+0x1a52>
  4115de:	0f 85 5e 02 00 00    	jne    411842 <__sin_avx+0x1a52>
  4115e4:	c5 79 2e cb          	vucomisd %xmm3,%xmm9
  4115e8:	c5 f9 28 d1          	vmovapd %xmm1,%xmm2
  4115ec:	0f 87 de e8 ff ff    	ja     40fed0 <__sin_avx+0xe0>
  4115f2:	e9 92 eb ff ff       	jmpq   410189 <__sin_avx+0x399>
  4115f7:	c5 f9 2e d3          	vucomisd %xmm3,%xmm2
  4115fb:	c5 7b 11 1c 24       	vmovsd %xmm11,(%rsp)
  411600:	48 8b 04 24          	mov    (%rsp),%rax
  411604:	0f 86 eb 03 00 00    	jbe    4119f5 <__sin_avx+0x1c05>
  41160a:	c5 fb 10 35 96 78 09 	vmovsd 0x97896(%rip),%xmm6        # 4a8ea8 <_IO_stdin_used+0x68>
  411611:	00 
  411612:	c5 cb 59 f2          	vmulsd %xmm2,%xmm6,%xmm6
  411616:	c1 e0 02             	shl    $0x2,%eax
  411619:	c5 fb 10 25 e7 78 09 	vmovsd 0x978e7(%rip),%xmm4        # 4a8f08 <big+0x18>
  411620:	00 
  411621:	48 63 d0             	movslq %eax,%rdx
  411624:	c5 79 28 dd          	vmovapd %xmm5,%xmm11
  411628:	c5 7b 10 14 d5 00 9a 	vmovsd 0x4a9a00(,%rdx,8),%xmm10
  41162f:	4a 00 
  411631:	8d 50 02             	lea    0x2(%rax),%edx
  411634:	c5 23 58 dc          	vaddsd %xmm4,%xmm11,%xmm11
  411638:	48 63 d2             	movslq %edx,%rdx
  41163b:	c4 c1 7b 59 c2       	vmulsd %xmm10,%xmm0,%xmm0
  411640:	c5 7b 10 24 d5 00 9a 	vmovsd 0x4a9a00(,%rdx,8),%xmm12
  411647:	4a 00 
  411649:	8d 50 03             	lea    0x3(%rax),%edx
  41164c:	83 c0 01             	add    $0x1,%eax
  41164f:	48 98                	cltq   
  411651:	c5 79 29 e7          	vmovapd %xmm12,%xmm7
  411655:	48 63 d2             	movslq %edx,%rdx
  411658:	c5 23 5c dc          	vsubsd %xmm4,%xmm11,%xmm11
  41165c:	c5 7b 10 2c d5 00 9a 	vmovsd 0x4a9a00(,%rdx,8),%xmm13
  411663:	4a 00 
  411665:	c5 c3 58 fc          	vaddsd %xmm4,%xmm7,%xmm7
  411669:	c5 c3 5c fc          	vsubsd %xmm4,%xmm7,%xmm7
  41166d:	c5 79 29 c4          	vmovapd %xmm8,%xmm4
  411671:	c4 41 3b 59 c4       	vmulsd %xmm12,%xmm8,%xmm8
  411676:	c4 c1 5b 59 e5       	vmulsd %xmm13,%xmm4,%xmm4
  41167b:	c5 1b 5c e7          	vsubsd %xmm7,%xmm12,%xmm12
  41167f:	c5 db 58 24 c5 00 9a 	vaddsd 0x4a9a00(,%rax,8),%xmm4,%xmm4
  411686:	4a 00 
  411688:	c4 c1 5b 58 e0       	vaddsd %xmm8,%xmm4,%xmm4
  41168d:	c4 41 79 28 c4       	vmovapd %xmm12,%xmm8
  411692:	c4 41 3b 58 c5       	vaddsd %xmm13,%xmm8,%xmm8
  411697:	c5 3b 59 c5          	vmulsd %xmm5,%xmm8,%xmm8
  41169b:	c4 c1 5b 58 e0       	vaddsd %xmm8,%xmm4,%xmm4
  4116a0:	c5 79 28 c5          	vmovapd %xmm5,%xmm8
  4116a4:	c4 c1 53 59 ea       	vmulsd %xmm10,%xmm5,%xmm5
  4116a9:	c4 41 3b 5c c3       	vsubsd %xmm11,%xmm8,%xmm8
  4116ae:	c5 d3 59 e9          	vmulsd %xmm1,%xmm5,%xmm5
  4116b2:	c5 3b 58 c1          	vaddsd %xmm1,%xmm8,%xmm8
  4116b6:	c5 3b 59 c7          	vmulsd %xmm7,%xmm8,%xmm8
  4116ba:	c4 c1 43 59 fb       	vmulsd %xmm11,%xmm7,%xmm7
  4116bf:	c4 c1 5b 58 e0       	vaddsd %xmm8,%xmm4,%xmm4
  4116c4:	c5 db 5c e5          	vsubsd %xmm5,%xmm4,%xmm4
  4116c8:	c5 db 5c e0          	vsubsd %xmm0,%xmm4,%xmm4
  4116cc:	c5 79 29 d0          	vmovapd %xmm10,%xmm0
  4116d0:	c5 fb 58 c7          	vaddsd %xmm7,%xmm0,%xmm0
  4116d4:	c5 2b 5c d0          	vsubsd %xmm0,%xmm10,%xmm10
  4116d8:	c5 f9 28 e8          	vmovapd %xmm0,%xmm5
  4116dc:	c5 2b 58 d7          	vaddsd %xmm7,%xmm10,%xmm10
  4116e0:	c4 c1 5b 58 e2       	vaddsd %xmm10,%xmm4,%xmm4
  4116e5:	c5 d3 58 ec          	vaddsd %xmm4,%xmm5,%xmm5
  4116e9:	c5 fb 5c c5          	vsubsd %xmm5,%xmm0,%xmm0
  4116ed:	c5 fb 58 c4          	vaddsd %xmm4,%xmm0,%xmm0
  4116f1:	c5 f9 2e c3          	vucomisd %xmm3,%xmm0
  4116f5:	c5 fb 59 05 93 77 09 	vmulsd 0x97793(%rip),%xmm0,%xmm0        # 4a8e90 <_IO_stdin_used+0x50>
  4116fc:	00 
  4116fd:	0f 86 10 01 00 00    	jbe    411813 <__sin_avx+0x1a23>
  411703:	c5 fb 58 c6          	vaddsd %xmm6,%xmm0,%xmm0
  411707:	c5 fb 58 c5          	vaddsd %xmm5,%xmm0,%xmm0
  41170b:	c5 f9 2e c5          	vucomisd %xmm5,%xmm0
  41170f:	0f 8a 25 02 00 00    	jp     41193a <__sin_avx+0x1b4a>
  411715:	0f 85 1f 02 00 00    	jne    41193a <__sin_avx+0x1b4a>
  41171b:	45 85 e4             	test   %r12d,%r12d
  41171e:	c5 f9 28 d5          	vmovapd %xmm5,%xmm2
  411722:	0f 85 a8 e7 ff ff    	jne    40fed0 <__sin_avx+0xe0>
  411728:	e9 5c ea ff ff       	jmpq   410189 <__sin_avx+0x399>
  41172d:	c4 41 13 5c ec       	vsubsd %xmm12,%xmm13,%xmm13
  411732:	e9 f2 ec ff ff       	jmpq   410429 <__sin_avx+0x639>
  411737:	c4 c1 4b 5c f4       	vsubsd %xmm12,%xmm6,%xmm6
  41173c:	e9 aa f7 ff ff       	jmpq   410eeb <__sin_avx+0x10fb>
  411741:	c5 fb 10 05 77 78 09 	vmovsd 0x97877(%rip),%xmm0        # 4a8fc0 <hp1+0x78>
  411748:	00 
  411749:	45 30 e4             	xor    %r12b,%r12b
  41174c:	c5 31 57 c8          	vxorpd %xmm0,%xmm9,%xmm9
  411750:	c5 f1 57 c8          	vxorpd %xmm0,%xmm1,%xmm1
  411754:	e9 8d f6 ff ff       	jmpq   410de6 <__sin_avx+0xff6>
  411759:	c5 db 5c 25 2f 78 09 	vsubsd 0x9782f(%rip),%xmm4,%xmm4        # 4a8f90 <hp1+0x48>
  411760:	00 
  411761:	e9 4a f6 ff ff       	jmpq   410db0 <__sin_avx+0xfc0>
  411766:	c5 fb 10 25 52 78 09 	vmovsd 0x97852(%rip),%xmm4        # 4a8fc0 <hp1+0x78>
  41176d:	00 
  41176e:	c5 f9 57 c4          	vxorpd %xmm4,%xmm0,%xmm0
  411772:	c5 f1 57 cc          	vxorpd %xmm4,%xmm1,%xmm1
  411776:	e9 3f f5 ff ff       	jmpq   410cba <__sin_avx+0xeca>
  41177b:	c5 fb 10 44 24 40    	vmovsd 0x40(%rsp),%xmm0
  411781:	c5 fb 10 1d c7 77 09 	vmovsd 0x977c7(%rip),%xmm3        # 4a8f50 <hp1+0x8>
  411788:	00 
  411789:	c5 f9 28 c8          	vmovapd %xmm0,%xmm1
  41178d:	c5 f3 59 c8          	vmulsd %xmm0,%xmm1,%xmm1
  411791:	c5 f9 2e d9          	vucomisd %xmm1,%xmm3
  411795:	c5 fb 10 1d 23 78 09 	vmovsd 0x97823(%rip),%xmm3        # 4a8fc0 <hp1+0x78>
  41179c:	00 
  41179d:	c5 fb 10 4c 24 50    	vmovsd 0x50(%rsp),%xmm1
  4117a3:	c5 f9 57 c3          	vxorpd %xmm3,%xmm0,%xmm0
  4117a7:	c5 f1 57 cb          	vxorpd %xmm3,%xmm1,%xmm1
  4117ab:	0f 86 53 f8 ff ff    	jbe    411004 <__sin_avx+0x1214>
  4117b1:	e9 43 ee ff ff       	jmpq   4105f9 <__sin_avx+0x809>
  4117b6:	c5 db 5c 24 24       	vsubsd (%rsp),%xmm4,%xmm4
  4117bb:	e9 ac f9 ff ff       	jmpq   41116c <__sin_avx+0x137c>
  4117c0:	c5 fb 10 05 f8 77 09 	vmovsd 0x977f8(%rip),%xmm0        # 4a8fc0 <hp1+0x78>
  4117c7:	00 
  4117c8:	c5 f9 57 c2          	vxorpd %xmm2,%xmm0,%xmm0
  4117cc:	c5 fb 59 05 d4 76 09 	vmulsd 0x976d4(%rip),%xmm0,%xmm0        # 4a8ea8 <_IO_stdin_used+0x68>
  4117d3:	00 
  4117d4:	c5 fb 11 04 24       	vmovsd %xmm0,(%rsp)
  4117d9:	e9 6f f8 ff ff       	jmpq   41104d <__sin_avx+0x125d>
  4117de:	c5 db 5c 25 aa 77 09 	vsubsd 0x977aa(%rip),%xmm4,%xmm4        # 4a8f90 <hp1+0x48>
  4117e5:	00 
  4117e6:	e9 fe ed ff ff       	jmpq   4105e9 <__sin_avx+0x7f9>
  4117eb:	c5 db 5c 25 9d 77 09 	vsubsd 0x9779d(%rip),%xmm4,%xmm4        # 4a8f90 <hp1+0x48>
  4117f2:	00 
  4117f3:	e9 45 fb ff ff       	jmpq   41133d <__sin_avx+0x154d>
  4117f8:	c5 fb 10 3d c0 77 09 	vmovsd 0x977c0(%rip),%xmm7        # 4a8fc0 <hp1+0x78>
  4117ff:	00 
  411800:	31 f6                	xor    %esi,%esi
  411802:	c5 f9 28 e0          	vmovapd %xmm0,%xmm4
  411806:	c5 d9 57 e7          	vxorpd %xmm7,%xmm4,%xmm4
  41180a:	c5 c1 57 f9          	vxorpd %xmm1,%xmm7,%xmm7
  41180e:	e9 2f fa ff ff       	jmpq   411242 <__sin_avx+0x1452>
  411813:	c5 fb 5c c6          	vsubsd %xmm6,%xmm0,%xmm0
  411817:	e9 eb fe ff ff       	jmpq   411707 <__sin_avx+0x1917>
  41181c:	0f 85 11 fd ff ff    	jne    411533 <__sin_avx+0x1743>
  411822:	e9 4f fb ff ff       	jmpq   411376 <__sin_avx+0x1586>
  411827:	c5 f1 57 c9          	vxorpd %xmm1,%xmm1,%xmm1
  41182b:	bf 01 00 00 00       	mov    $0x1,%edi
  411830:	c5 f9 28 c2          	vmovapd %xmm2,%xmm0
  411834:	e8 b7 6b ff ff       	callq  4083f0 <__mpsin>
  411839:	c5 f9 28 d0          	vmovapd %xmm0,%xmm2
  41183d:	e9 8e e6 ff ff       	jmpq   40fed0 <__sin_avx+0xe0>
  411842:	c5 fb 11 2c 24       	vmovsd %xmm5,(%rsp)
  411847:	c5 f9 28 c4          	vmovapd %xmm4,%xmm0
  41184b:	c5 fb 10 2d 85 76 09 	vmovsd 0x97685(%rip),%xmm5        # 4a8ed8 <mp1+0x10>
  411852:	00 
  411853:	48 8b 04 24          	mov    (%rsp),%rax
  411857:	c5 d3 59 ee          	vmulsd %xmm6,%xmm5,%xmm5
  41185b:	c5 cb 59 35 7d 76 09 	vmulsd 0x9767d(%rip),%xmm6,%xmm6        # 4a8ee0 <mp1+0x18>
  411862:	00 
  411863:	a8 02                	test   $0x2,%al
  411865:	c5 fb 5c c5          	vsubsd %xmm5,%xmm0,%xmm0
  411869:	c5 db 5c e0          	vsubsd %xmm0,%xmm4,%xmm4
  41186d:	c5 f9 28 cc          	vmovapd %xmm4,%xmm1
  411871:	c5 f9 28 e0          	vmovapd %xmm0,%xmm4
  411875:	c5 f3 5c cd          	vsubsd %xmm5,%xmm1,%xmm1
  411879:	c5 db 5c e6          	vsubsd %xmm6,%xmm4,%xmm4
  41187d:	c5 fb 5c c4          	vsubsd %xmm4,%xmm0,%xmm0
  411881:	c5 fb 5c c6          	vsubsd %xmm6,%xmm0,%xmm0
  411885:	c5 f3 58 c8          	vaddsd %xmm0,%xmm1,%xmm1
  411889:	74 10                	je     41189b <__sin_avx+0x1aab>
  41188b:	c5 fb 10 05 2d 77 09 	vmovsd 0x9772d(%rip),%xmm0        # 4a8fc0 <hp1+0x78>
  411892:	00 
  411893:	c5 d9 57 e0          	vxorpd %xmm0,%xmm4,%xmm4
  411897:	c5 f1 57 c8          	vxorpd %xmm0,%xmm1,%xmm1
  41189b:	c5 f9 2e e3          	vucomisd %xmm3,%xmm4
  41189f:	c5 fb 11 5c 24 28    	vmovsd %xmm3,0x28(%rsp)
  4118a5:	c5 fb 11 7c 24 20    	vmovsd %xmm7,0x20(%rsp)
  4118ab:	c5 fb 11 54 24 18    	vmovsd %xmm2,0x18(%rsp)
  4118b1:	0f 86 e8 02 00 00    	jbe    411b9f <__sin_avx+0x1daf>
  4118b7:	c5 f9 28 c4          	vmovapd %xmm4,%xmm0
  4118bb:	4c 89 e7             	mov    %r12,%rdi
  4118be:	c5 fb 11 24 24       	vmovsd %xmm4,(%rsp)
  4118c3:	e8 48 41 ff ff       	callq  405a10 <__dubsin>
  4118c8:	c5 fb 10 24 24       	vmovsd (%rsp),%xmm4
  4118cd:	c5 fb 10 54 24 18    	vmovsd 0x18(%rsp),%xmm2
  4118d3:	c5 fb 10 7c 24 20    	vmovsd 0x20(%rsp),%xmm7
  4118d9:	c5 fb 10 5c 24 28    	vmovsd 0x28(%rsp),%xmm3
  4118df:	c5 fb 10 44 24 58    	vmovsd 0x58(%rsp),%xmm0
  4118e5:	c5 f9 2e c3          	vucomisd %xmm3,%xmm0
  4118e9:	c5 fb 59 c7          	vmulsd %xmm7,%xmm0,%xmm0
  4118ed:	0f 86 91 02 00 00    	jbe    411b84 <__sin_avx+0x1d94>
  4118f3:	c5 f9 2e d3          	vucomisd %xmm3,%xmm2
  4118f7:	0f 86 db 02 00 00    	jbe    411bd8 <__sin_avx+0x1de8>
  4118fd:	c5 fb 10 0d e3 75 09 	vmovsd 0x975e3(%rip),%xmm1        # 4a8ee8 <mp1+0x20>
  411904:	00 
  411905:	c5 f3 59 ca          	vmulsd %xmm2,%xmm1,%xmm1
  411909:	c5 fb 58 c1          	vaddsd %xmm1,%xmm0,%xmm0
  41190d:	c5 fb 10 4c 24 50    	vmovsd 0x50(%rsp),%xmm1
  411913:	c5 fb 58 c1          	vaddsd %xmm1,%xmm0,%xmm0
  411917:	c5 f9 2e c8          	vucomisd %xmm0,%xmm1
  41191b:	0f 8a 06 ff ff ff    	jp     411827 <__sin_avx+0x1a37>
  411921:	0f 85 00 ff ff ff    	jne    411827 <__sin_avx+0x1a37>
  411927:	c5 f9 2e e3          	vucomisd %xmm3,%xmm4
  41192b:	c5 f9 28 d1          	vmovapd %xmm1,%xmm2
  41192f:	0f 87 9b e5 ff ff    	ja     40fed0 <__sin_avx+0xe0>
  411935:	e9 4f e8 ff ff       	jmpq   410189 <__sin_avx+0x399>
  41193a:	c5 79 29 c8          	vmovapd %xmm9,%xmm0
  41193e:	48 8d 7c 24 50       	lea    0x50(%rsp),%rdi
  411943:	c5 fb 11 5c 24 18    	vmovsd %xmm3,0x18(%rsp)
  411949:	c5 fb 11 14 24       	vmovsd %xmm2,(%rsp)
  41194e:	e8 bd 40 ff ff       	callq  405a10 <__dubsin>
  411953:	c5 fb 10 44 24 58    	vmovsd 0x58(%rsp),%xmm0
  411959:	c5 fb 10 5c 24 18    	vmovsd 0x18(%rsp),%xmm3
  41195f:	c5 f9 28 c8          	vmovapd %xmm0,%xmm1
  411963:	c5 fb 10 14 24       	vmovsd (%rsp),%xmm2
  411968:	c5 f9 2e c3          	vucomisd %xmm3,%xmm0
  41196c:	c5 f3 59 0d b4 75 09 	vmulsd 0x975b4(%rip),%xmm1,%xmm1        # 4a8f28 <big+0x38>
  411973:	00 
  411974:	0f 86 ce 01 00 00    	jbe    411b48 <__sin_avx+0x1d58>
  41197a:	c5 f9 2e d3          	vucomisd %xmm3,%xmm2
  41197e:	0f 86 ab 01 00 00    	jbe    411b2f <__sin_avx+0x1d3f>
  411984:	c5 fb 10 05 24 75 09 	vmovsd 0x97524(%rip),%xmm0        # 4a8eb0 <_IO_stdin_used+0x70>
  41198b:	00 
  41198c:	c5 fb 59 c2          	vmulsd %xmm2,%xmm0,%xmm0
  411990:	c5 fb 58 c1          	vaddsd %xmm1,%xmm0,%xmm0
  411994:	c5 fb 10 4c 24 50    	vmovsd 0x50(%rsp),%xmm1
  41199a:	c5 fb 58 c1          	vaddsd %xmm1,%xmm0,%xmm0
  41199e:	c5 f9 2e c8          	vucomisd %xmm0,%xmm1
  4119a2:	0f 8a 7f fe ff ff    	jp     411827 <__sin_avx+0x1a37>
  4119a8:	0f 85 79 fe ff ff    	jne    411827 <__sin_avx+0x1a37>
  4119ae:	41 83 ec 01          	sub    $0x1,%r12d
  4119b2:	c5 f9 28 d1          	vmovapd %xmm1,%xmm2
  4119b6:	0f 84 14 e5 ff ff    	je     40fed0 <__sin_avx+0xe0>
  4119bc:	e9 c8 e7 ff ff       	jmpq   410189 <__sin_avx+0x399>
  4119c1:	c5 f8 ae 54 24 50    	vldmxcsr 0x50(%rsp)
  4119c7:	bd 01 00 00 00       	mov    $0x1,%ebp
  4119cc:	e9 48 e4 ff ff       	jmpq   40fe19 <__sin_avx+0x29>
  4119d1:	c5 f8 ae 5c 24 50    	vstmxcsr 0x50(%rsp)
  4119d7:	8b 44 24 50          	mov    0x50(%rsp),%eax
  4119db:	81 e3 00 60 00 00    	and    $0x6000,%ebx
  4119e1:	80 e4 9f             	and    $0x9f,%ah
  4119e4:	09 c3                	or     %eax,%ebx
  4119e6:	89 5c 24 50          	mov    %ebx,0x50(%rsp)
  4119ea:	c5 f8 ae 54 24 50    	vldmxcsr 0x50(%rsp)
  4119f0:	e9 e4 e4 ff ff       	jmpq   40fed9 <__sin_avx+0xe9>
  4119f5:	c5 fb 10 35 c3 75 09 	vmovsd 0x975c3(%rip),%xmm6        # 4a8fc0 <hp1+0x78>
  4119fc:	00 
  4119fd:	c5 c9 57 f2          	vxorpd %xmm2,%xmm6,%xmm6
  411a01:	c5 cb 59 35 9f 74 09 	vmulsd 0x9749f(%rip),%xmm6,%xmm6        # 4a8ea8 <_IO_stdin_used+0x68>
  411a08:	00 
  411a09:	e9 08 fc ff ff       	jmpq   411616 <__sin_avx+0x1826>
  411a0e:	c5 f9 2e d3          	vucomisd %xmm3,%xmm2
  411a12:	0f 86 53 01 00 00    	jbe    411b6b <__sin_avx+0x1d7b>
  411a18:	c5 fb 10 3d 88 74 09 	vmovsd 0x97488(%rip),%xmm7        # 4a8ea8 <_IO_stdin_used+0x68>
  411a1f:	00 
  411a20:	c5 c3 59 fa          	vmulsd %xmm2,%xmm7,%xmm7
  411a24:	c5 03 5c ff          	vsubsd %xmm7,%xmm15,%xmm15
  411a28:	c5 79 29 ff          	vmovapd %xmm15,%xmm7
  411a2c:	e9 f4 fa ff ff       	jmpq   411525 <__sin_avx+0x1735>
  411a31:	c5 fb 10 3d 87 75 09 	vmovsd 0x97587(%rip),%xmm7        # 4a8fc0 <hp1+0x78>
  411a38:	00 
  411a39:	c5 c1 57 fa          	vxorpd %xmm2,%xmm7,%xmm7
  411a3d:	c5 c3 59 3d 63 74 09 	vmulsd 0x97463(%rip),%xmm7,%xmm7        # 4a8ea8 <_IO_stdin_used+0x68>
  411a44:	00 
  411a45:	e9 d6 fa ff ff       	jmpq   411520 <__sin_avx+0x1730>
  411a4a:	c5 fb 10 0d 6e 75 09 	vmovsd 0x9756e(%rip),%xmm1        # 4a8fc0 <hp1+0x78>
  411a51:	00 
  411a52:	c5 f1 57 ca          	vxorpd %xmm2,%xmm1,%xmm1
  411a56:	c5 f3 59 0d 52 74 09 	vmulsd 0x97452(%rip),%xmm1,%xmm1        # 4a8eb0 <_IO_stdin_used+0x70>
  411a5d:	00 
  411a5e:	e9 63 fb ff ff       	jmpq   4115c6 <__sin_avx+0x17d6>
  411a63:	c5 f9 2e d3          	vucomisd %xmm3,%xmm2
  411a67:	0f 86 93 00 00 00    	jbe    411b00 <__sin_avx+0x1d10>
  411a6d:	c5 fb 10 0d 3b 74 09 	vmovsd 0x9743b(%rip),%xmm1        # 4a8eb0 <_IO_stdin_used+0x70>
  411a74:	00 
  411a75:	c5 f3 59 ca          	vmulsd %xmm2,%xmm1,%xmm1
  411a79:	c5 fb 5c c1          	vsubsd %xmm1,%xmm0,%xmm0
  411a7d:	e9 48 fb ff ff       	jmpq   4115ca <__sin_avx+0x17da>
  411a82:	c5 fb 10 05 36 75 09 	vmovsd 0x97536(%rip),%xmm0        # 4a8fc0 <hp1+0x78>
  411a89:	00 
  411a8a:	c5 f9 57 c2          	vxorpd %xmm2,%xmm0,%xmm0
  411a8e:	c5 fb 59 05 1a 74 09 	vmulsd 0x9741a(%rip),%xmm0,%xmm0        # 4a8eb0 <_IO_stdin_used+0x70>
  411a95:	00 
  411a96:	e9 37 f7 ff ff       	jmpq   4111d2 <__sin_avx+0x13e2>
  411a9b:	c5 fb 10 05 1d 75 09 	vmovsd 0x9751d(%rip),%xmm0        # 4a8fc0 <hp1+0x78>
  411aa2:	00 
  411aa3:	4c 89 e7             	mov    %r12,%rdi
  411aa6:	c5 7b 11 0c 24       	vmovsd %xmm9,(%rsp)
  411aab:	c5 f1 57 c8          	vxorpd %xmm0,%xmm1,%xmm1
  411aaf:	c4 c1 79 57 c1       	vxorpd %xmm9,%xmm0,%xmm0
  411ab4:	e8 57 3f ff ff       	callq  405a10 <__dubsin>
  411ab9:	c5 fb 10 5c 24 38    	vmovsd 0x38(%rsp),%xmm3
  411abf:	c5 fb 10 54 24 30    	vmovsd 0x30(%rsp),%xmm2
  411ac5:	c5 fb 10 64 24 28    	vmovsd 0x28(%rsp),%xmm4
  411acb:	c5 fb 10 74 24 20    	vmovsd 0x20(%rsp),%xmm6
  411ad1:	c5 fb 10 6c 24 18    	vmovsd 0x18(%rsp),%xmm5
  411ad7:	c5 7b 10 0c 24       	vmovsd (%rsp),%xmm9
  411adc:	e9 b3 fa ff ff       	jmpq   411594 <__sin_avx+0x17a4>
  411ae1:	c5 f9 2e d3          	vucomisd %xmm3,%xmm2
  411ae5:	76 32                	jbe    411b19 <__sin_avx+0x1d29>
  411ae7:	c5 fb 10 05 c1 73 09 	vmovsd 0x973c1(%rip),%xmm0        # 4a8eb0 <_IO_stdin_used+0x70>
  411aee:	00 
  411aef:	c5 fb 59 c2          	vmulsd %xmm2,%xmm0,%xmm0
  411af3:	c5 f3 5c c8          	vsubsd %xmm0,%xmm1,%xmm1
  411af7:	c5 f9 28 c1          	vmovapd %xmm1,%xmm0
  411afb:	e9 d6 f6 ff ff       	jmpq   4111d6 <__sin_avx+0x13e6>
  411b00:	c5 fb 10 0d b8 74 09 	vmovsd 0x974b8(%rip),%xmm1        # 4a8fc0 <hp1+0x78>
  411b07:	00 
  411b08:	c5 f1 57 ca          	vxorpd %xmm2,%xmm1,%xmm1
  411b0c:	c5 f3 59 0d 9c 73 09 	vmulsd 0x9739c(%rip),%xmm1,%xmm1        # 4a8eb0 <_IO_stdin_used+0x70>
  411b13:	00 
  411b14:	e9 60 ff ff ff       	jmpq   411a79 <__sin_avx+0x1c89>
  411b19:	c5 fb 10 05 9f 74 09 	vmovsd 0x9749f(%rip),%xmm0        # 4a8fc0 <hp1+0x78>
  411b20:	00 
  411b21:	c5 f9 57 c2          	vxorpd %xmm2,%xmm0,%xmm0
  411b25:	c5 fb 59 05 83 73 09 	vmulsd 0x97383(%rip),%xmm0,%xmm0        # 4a8eb0 <_IO_stdin_used+0x70>
  411b2c:	00 
  411b2d:	eb c4                	jmp    411af3 <__sin_avx+0x1d03>
  411b2f:	c5 fb 10 05 89 74 09 	vmovsd 0x97489(%rip),%xmm0        # 4a8fc0 <hp1+0x78>
  411b36:	00 
  411b37:	c5 f9 57 c2          	vxorpd %xmm2,%xmm0,%xmm0
  411b3b:	c5 fb 59 05 6d 73 09 	vmulsd 0x9736d(%rip),%xmm0,%xmm0        # 4a8eb0 <_IO_stdin_used+0x70>
  411b42:	00 
  411b43:	e9 48 fe ff ff       	jmpq   411990 <__sin_avx+0x1ba0>
  411b48:	c5 f9 2e d3          	vucomisd %xmm3,%xmm2
  411b4c:	0f 86 b5 00 00 00    	jbe    411c07 <__sin_avx+0x1e17>
  411b52:	c5 fb 10 05 56 73 09 	vmovsd 0x97356(%rip),%xmm0        # 4a8eb0 <_IO_stdin_used+0x70>
  411b59:	00 
  411b5a:	c5 fb 59 c2          	vmulsd %xmm2,%xmm0,%xmm0
  411b5e:	c5 f3 5c c8          	vsubsd %xmm0,%xmm1,%xmm1
  411b62:	c5 f9 28 c1          	vmovapd %xmm1,%xmm0
  411b66:	e9 29 fe ff ff       	jmpq   411994 <__sin_avx+0x1ba4>
  411b6b:	c5 fb 10 3d 4d 74 09 	vmovsd 0x9744d(%rip),%xmm7        # 4a8fc0 <hp1+0x78>
  411b72:	00 
  411b73:	c5 c1 57 fa          	vxorpd %xmm2,%xmm7,%xmm7
  411b77:	c5 c3 59 3d 29 73 09 	vmulsd 0x97329(%rip),%xmm7,%xmm7        # 4a8ea8 <_IO_stdin_used+0x68>
  411b7e:	00 
  411b7f:	e9 a0 fe ff ff       	jmpq   411a24 <__sin_avx+0x1c34>
  411b84:	c5 f9 2e d3          	vucomisd %xmm3,%xmm2
  411b88:	76 67                	jbe    411bf1 <__sin_avx+0x1e01>
  411b8a:	c5 fb 10 0d 56 73 09 	vmovsd 0x97356(%rip),%xmm1        # 4a8ee8 <mp1+0x20>
  411b91:	00 
  411b92:	c5 f3 59 ca          	vmulsd %xmm2,%xmm1,%xmm1
  411b96:	c5 fb 5c c1          	vsubsd %xmm1,%xmm0,%xmm0
  411b9a:	e9 6e fd ff ff       	jmpq   41190d <__sin_avx+0x1b1d>
  411b9f:	c5 fb 10 05 19 74 09 	vmovsd 0x97419(%rip),%xmm0        # 4a8fc0 <hp1+0x78>
  411ba6:	00 
  411ba7:	4c 89 e7             	mov    %r12,%rdi
  411baa:	c5 fb 11 24 24       	vmovsd %xmm4,(%rsp)
  411baf:	c5 f1 57 c8          	vxorpd %xmm0,%xmm1,%xmm1
  411bb3:	c5 f9 57 c4          	vxorpd %xmm4,%xmm0,%xmm0
  411bb7:	e8 54 3e ff ff       	callq  405a10 <__dubsin>
  411bbc:	c5 fb 10 5c 24 28    	vmovsd 0x28(%rsp),%xmm3
  411bc2:	c5 fb 10 7c 24 20    	vmovsd 0x20(%rsp),%xmm7
  411bc8:	c5 fb 10 54 24 18    	vmovsd 0x18(%rsp),%xmm2
  411bce:	c5 fb 10 24 24       	vmovsd (%rsp),%xmm4
  411bd3:	e9 07 fd ff ff       	jmpq   4118df <__sin_avx+0x1aef>
  411bd8:	c5 fb 10 0d e0 73 09 	vmovsd 0x973e0(%rip),%xmm1        # 4a8fc0 <hp1+0x78>
  411bdf:	00 
  411be0:	c5 f1 57 ca          	vxorpd %xmm2,%xmm1,%xmm1
  411be4:	c5 f3 59 0d fc 72 09 	vmulsd 0x972fc(%rip),%xmm1,%xmm1        # 4a8ee8 <mp1+0x20>
  411beb:	00 
  411bec:	e9 18 fd ff ff       	jmpq   411909 <__sin_avx+0x1b19>
  411bf1:	c5 fb 10 0d c7 73 09 	vmovsd 0x973c7(%rip),%xmm1        # 4a8fc0 <hp1+0x78>
  411bf8:	00 
  411bf9:	c5 f1 57 ca          	vxorpd %xmm2,%xmm1,%xmm1
  411bfd:	c5 f3 59 0d e3 72 09 	vmulsd 0x972e3(%rip),%xmm1,%xmm1        # 4a8ee8 <mp1+0x20>
  411c04:	00 
  411c05:	eb 8f                	jmp    411b96 <__sin_avx+0x1da6>
  411c07:	c5 fb 10 05 b1 73 09 	vmovsd 0x973b1(%rip),%xmm0        # 4a8fc0 <hp1+0x78>
  411c0e:	00 
  411c0f:	c5 f9 57 c2          	vxorpd %xmm2,%xmm0,%xmm0
  411c13:	c5 fb 59 05 95 72 09 	vmulsd 0x97295(%rip),%xmm0,%xmm0        # 4a8eb0 <_IO_stdin_used+0x70>
  411c1a:	00 
  411c1b:	e9 3e ff ff ff       	jmpq   411b5e <__sin_avx+0x1d6e>
~~~

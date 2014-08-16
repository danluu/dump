; RUN: llvm-as < %s | \
; RUN: llc -march=x86-64 -mattr=+64bit,+sse3

declare <2 x double> @llvm.x86.sse2.min.pd(<2 x double>, <2 x double>)

define <2 x double> @foo(<2 x double> %f) {
  %t = call <2 x double> @llvm.x86.sse2.min.pd(<2 x double> %f, <2 x double> %f)
  ret <2 x double> %t
}

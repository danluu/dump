using Base.llvmcall

# This was an experiment to try getting the initial llvmcall implementation to work. Turns out, there's still a bug, which is why getting this to work required modifying llvmcall.

# llvmcall(ir, (rettypes...), (argtypes...), args...)

# function add1234(x::(Int32,Int32,Int32,Int32))
#     llvmcall("""%3 = add <4 x i32> %1, %0
#              ret <4 x i32> %3""",
#              (Int32,Int32,Int32,Int32),
#              ((Int32,Int32,Int32,Int32),(Int32,Int32,Int32,Int32)),
#              (int32(1),int32(2),int32(3),int32(4)),
#              x)
# end

# # llvmcall(ir, (rettypes...), (argtypes...), args...)

# function add_simd(x::(Int32,Int32,Int32,Int32), y::(Int32, Int32, Int32, Int32))
#     llvmcall("""%3 = add <4 x i32> %1, add <4 x i32> %0
#              ret <4 x i32> %3""",
#              (Int32,Int32,Int32,Int32),
#              ((Int32,Int32,Int32,Int32),(Int32,Int32,Int32,Int32)),
#              x,
#              y)
# end


# function add_simd(x::(Int64,Int64,Int64,Int64), y::(Int64, Int64, Int64, Int64))
#     llvmcall("""%3 = add <4 x i64> %1, %0
#              ret <4 x i64> %3""",
#              (Int64,Int64,Int64,Int64),
#              ((Int64,Int64,Int64,Int64),(Int64,Int64,Int64,Int64)),
#              x,
#              y)
# end

# print(add_simd((2,4,6,8),(10,100,1000,10000)))

# function fadd_simd(x::(Float64,Float64), y::(Float64, Float64))
#     llvmcall("""%3 = fadd <2 x double> %1, %0
#              ret <2 x double> %3""",
#              (Float64,Float64),
#              ((Float64,Float64),(Float64,Float64)),
#              x,y)
# end

# print(fadd_simd((2.0,4.0),(10.0,100.0)))

# function fmac(x::(Float64), y::(Float64), z::(Float64))
#     llvmcall("""
#              %4 = call double @llvm.fmuladd.f64(double %2, double %1, double %0)
#              ret double %4""",
#              (Float64),
#              ((Float64),(Float64),(Float64)),
#              x,y,z)
# end

# print(fmac((2.0),(4.0),(10.0)))


# declare <2 x double> @llvm.x86.sse2.min.pd(<2 x double>, <2 x double>)
# %3 = call <2 x double> @llvm.x86.sse2.min.pd(<2 x double> %1, <2 x double> %0)
# works if I add the following line to llvmcall itself:
#		  << "declare <2 x double> @llvm.x86.sse2.min.pd(<2 x double>, <2 x double>)" << "\n"

function min_simd(x::(Float64,Float64), y::(Float64, Float64))
    llvmcall("""%3 = call <2 x double> @llvm.x86.sse2.min.pd(<2 x double> %1, <2 x double> %0)
             ret <2 x double> %3""",
             (Float64,Float64),
             ((Float64,Float64),(Float64,Float64)),
             x,
             y)
end

function wat()
    print(min_simd((2.0,4.0),(10.0,100.0)))
end

wat()

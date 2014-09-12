function (times){T}(A::StridedMatrix{T}, B::StridedMatrix{T})
    A_mul_B!(similar(B,T,(size(A,1),size(B,2))),A,B)
end

# function (times){T}(A::StridedMatrix{T}, B::StridedMatrix{T})
#     C = similar(B,T,(size(A,1),size(B,2)))
#     gemm_wrapper!(C, 'N', 'N', A, B)
#     return C
# end

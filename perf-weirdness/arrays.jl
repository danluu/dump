function setup(a::Array, n::Int)
    for k in 1:n, j in 1:n, i in 1:n
        a[i,j,k] = 11*i*j*k + 2i + 7j
    end
end

function sum_array(a::Array, n::Int)
    # 3 should be 2
    for k in 3:n, j in 1:n, i in 1:n
        #a[i,j,k] = min(a[i,j,k-1],
        #               a[i,k,k-1] + a[k,j,k-1])
        a[i,j,k] = a[i,j,k] < 100 ? a[i,j,k] : 100
        #a[i,j,k] = min(a[i,j,k],100)
    end
end

function main(n::Int)    
    a = Array(Int, n, n, n)
    setup(a,n)

    @elapsed sum_array(a, n)    
end

println(median([main(900) for x=1:10]))

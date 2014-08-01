function setup(a::Array, n::Int)
    for k in 1:n, j in 1:n, i in 1:n
        a[i,j,k] = i*3j*5k + 2i + 7j
    end
end

function sum_array(a::Array, n::Int)
    sum = 0
    for k in 2:n, j in 1:n, i in 1:n
        a[i,j,k] = min(a[i,j,k-1],
                       a[i,k,k-1] + a[k,j,k-1])
    end
    return sum
end

function main(n::Int)    
    a = Array(Int, n, n, n)
    setup(a,n)

    @time result = sum_array(a, n)
    return result
end

main(1000)


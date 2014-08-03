function return_int32(n::Int)
    return int32((1 << n) - 1)
end

function use_int32(k::Int32, n::Int, m::Int)
    return k
end

function initial_perm(n::Int)
    return int32((1 << n) - 1)
end

function next_perm(current::Int32, n::Int ,k::Int)
    lowest_bit = current & -current
    propogate = lowest_bit + current
    next = div((current $ propogate) >> 2,lowest_bit) | propogate
    if next >= (1 << n)
        next = 0
    end
    return next
end

function call_fns()
    d = Dict{Int32, Float32}()
    p = initial_perm(4)
    num_cities = 4
    while p != 0
        d[p] = float32(1)
        next_perm(p, num_cities, 1)
    end
end

call_fns()

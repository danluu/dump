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
    return int32(next)
end

function tsp_cost()
    d = Dict{Int32, Float32}()
    # do we really need to special case the base case?
    p = initial_perm(1)
    while p != 0
        d[p] = float32(1)
        p = next_perm(p, 4, 1)
    end
end

tsp_cost()

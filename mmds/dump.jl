function page_rank(m, beta)
    assert(size(m,1) == size(m,2))
    s = size(m,1)
    spray = ones(size(m)) / s
    r = ones(s)

    x = beta * m + (1-beta) * spray
    for i in 1:6
        println(r)
        r = x * r
    end
    return r
end

# println("1")
# page_rank([0 0 0; .5 0 0; .5 1 1], .7)
# println("2")
# page_rank([0 0 1; .5 0 0; .5 1 0], .85)
# println("3")
# page_rank([0 0 1; .5 0 0; .5 1 0], 1.0)

function prime_sum(m)
    h = Dict{Int, Int}()
    for x in m
        for (k,_) in factor(x)
            if !haskey(h, k)
                h[k] = x
            else
                h[k] += x
            end
        end
    end
    return h
end

# print(prime_sum([15, 21, 24, 30, 49]))

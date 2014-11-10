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

function shingle(s::ASCIIString, n::Int)
    h = Set{ASCIIString}()
    idx_delta = n-1
    for i in 1:(length(s) - idx_delta)
        end_idx = i + idx_delta
        push!(h, s[i:end_idx])
    end
    return h
end

function shingle_stuff()
    test0 = shingle("ABRACADABRA", 2)
    test1 = shingle("BRICABRAC", 2)
    common = intersect(test0, test1)
    total = union(test0, test1)
    println(test0)
    println(test1)
    println(common)
    println(length(common) / length(total))
end

# shingle_stuff()

function distance(p)
    l1a = norm(p - [0,0], 1)
    l2a = norm(p - [0,0], 2)
    l1b = norm(p - [100,40], 1)
    l2b = norm(p - [100,40], 2)
    return l1a < l1b && l2a > l2b
end

# println(distance([53,18]))
# println(distance([56,13]))
# println(distance([66,5]))
# println(distance([50,18]))

# Center is a vector and not a tuple so we can use vector functions. 
# Length of center should always be the dimension, which should always be 2.

type Centroid
    center::Vector{Int}
    points::Set{Vector{Int}}
end

function make_initial_centroids()
    initial_centers = Array[[25,125], [44,105], [29,97], [35,63], [55,63], [42,57], [23,40], [64,37], [33,22], [55,20]]
    
end

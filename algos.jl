# Some code for Tim Roughgarden's algorithms part 2 course

function read_jobs(fname)
    f = open(fname)
    line = readline(f)
    numjobs = int(line)
    a = Array((Int, Int), numjobs)
    for i in 1:numjobs
        # tuple is (weight, length)
        line = readline(f)
        a[i] = tuple(map(int, split(line))...)
    end
    return a
end

function compare_difference(x, y)
    if x[1] - x[2] > y[1] - y[2] 
        return true
    elseif x[1] - x[2] < y[1] - y[2] 
        return false
    else 
        return x[1] > y[1] 
    end
end

function compare_ratio(x, y)
    return x[1] / x[2] > y[1] / y[2]
end

# 'correct' uses the ratio between the weight and the length
# incorrect uses the difference
function order_jobs(a::Array, correct::Bool)
    if (correct) 
        ordered = sort(a, lt=compare_ratio)
    else
        ordered = sort(a, lt=compare_difference)
    end
    return ordered
end

function compute_weighted_sum(a::Array)
    time = 0
    sum = 0
    for x in a
        time += x[2]
        sum += x[1] * time
    end
    return sum
end

function problem1(fname::String, correct::Bool)
    raw_data = read_jobs(fname)
    ordered_jobs = order_jobs(raw_data, correct)
    sum = compute_weighted_sum(ordered_jobs)
    return sum
end

assert(compute_weighted_sum([(3,1), (2,2), (1,3)]) == 15)
assert(problem1("1-1.txt", false) == 11336)
assert(problem1("1-1.txt", true) == 10548)
assert(problem1("1-2.txt", false) == 145924)
assert(problem1("1-2.txt", true) == 138232)
print("Problem 1: $(problem1("jobs.txt", false))\n")
print("Problem 2: $(problem1("jobs.txt", true))\n")

function read_edges(fname)
    f = open(fname)
    line = readline(f)
    vertices, edges = tuple(map(int, split(line))...)
    d = Dict()
    # d could be an array -- the graph is connected, so we know every
    # vertex has at least one edge.
    for i in 1:edges
        # tuple is (vertex, vertex, weight)
        line = readline(f)
        v1, v2, weight = tuple(map(int, split(line))...)
        if !haskey(d, v1)
            d[v1] = Dict()
        end
        
        if !haskey(d, v2)
            d[v2] = Dict()
        end

        d[v1][v2] = weight
        d[v2][v1] = weight
    end
    return d
end

function compute_mst_naive(g)
    # Assume graph is connected, so we can start with any node.
    not_done = Dict()
    weight = 0
    for k in keys(g)
        not_done[k] = true
    end
    done = {1 => true}
    delete!(not_done, 1)

    while !isempty(not_done)
        existing, new = find_cheapest(done, g)       
        weight += g[existing][new]
        done[new] = true
        delete!(not_done, new)
    end

    return weight
end

function find_cheapest(done, g)
    cost = typemax(Int)
    cheapest = (0, 0)
    for v1 in keys(done)
        for v2 in keys(g[v1])
            if !haskey(done, v2) && g[v1][v2] < cost
                cost = g[v1][v2]
                cheapest = (v1, v2)
            end
        end
    end
    assert(cheapest != (0,0))
    return cheapest
end

g = read_edges("1-3.txt")
assert(compute_mst_naive(g) == 2624)

g = read_edges("edges.txt")
print("Problem 3: $(compute_mst_naive(g))\n")

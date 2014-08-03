# Read a text file with the following format
# numjobs
# weight length
# weight length
# ...
# return an array with (weight, length) tuples
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

# return true if weight(x) - length(x) > weight(y) - length(y)
# ties are broken by largest weight
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

# is_correct uses the ratio between the weight and the length
# not is_correct uses the difference
function order_jobs(v::Vector{(Int, Int)}, is_correct::Bool)
    if (is_correct) 
        ordered = sort(v, lt=compare_ratio)
    else
        ordered = sort(v, lt=compare_difference)
    end
    return ordered
end

function compute_weighted_sum(v::Vector{(Int, Int)})
    time = 0
    sum = 0
    for x in v
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

# print("Problem 1: $(problem1("jobs.txt", false))\n")
# print("Problem 2: $(problem1("jobs.txt", true))\n")

function read_edges(fname::String, directed::Bool)
    f = open(fname)
    line = readline(f)
    vertices, edges = tuple(map(int, split(line))...)
    d = Dict{Int, Dict{Int, Int}}()
    # d could be an array -- the graph is connected, so we know every
    # vertex has at least one edge.
    for i in 1:edges
        # tuple is (vertex, vertex, weight)
        line = readline(f)
        v1, v2, weight = tuple(map(int, split(line))...)
        if !haskey(d, v1)
            d[v1] = Dict{Int, Int}()
        end
        
        if !haskey(d, v2) && !directed
            d[v2] = Dict{Int, Int}()
        end

        d[v1][v2] = weight
        if !directed
            d[v2][v1] = weight
        end
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

# g = read_edges("edges.txt", false)
# print("Problem 3: $(compute_mst_naive(g))\n")

function read_clusters(fname::String)
    f = open(fname)
    line = readline(f)
    num_vertices = int(line)
    a = Array((Int, Int, Int), 0)    

    line = readline(f)
    while line != ""
        # tuple is (vertex, vertex, weight)
        push!(a, tuple(map(int, split(line))...))       
        line = readline(f)
    end
    return (a, num_vertices)
end

function read_clusters_binary(fname::String)
    f = open(fname)
    line = readline(f)
    num_vertices, num_bits = tuple(map(int, split(line))...)
    d = Dict{Int, Bool}()

    line = readline(f)
    while line != ""
        num = 0
        line = chomp(line)
        for c in line
            if c != ' '
                num = (num << 1) | parseint(c)
            end
        end
        d[num] = true

        line = readline(f)
    end   
    return d
end

function clustering_compare_edges(x, y)
    return x[3] < y[3]
end

function sort_by_edge_weight(v::Vector{(Int, Int, Int)})
    # put smallest edges on top
    sort(v, lt=clustering_compare_edges)
end

include("union-find.jl")

function find_cluster_distance(fname::String)
    unsorted_edges, num_vertices = read_clusters(fname)
    sorted_edges = sort_by_edge_weight(unsorted_edges)
    u = make_union(num_vertices)
    done = false
    for (v1, v2, distance) in sorted_edges
        if length(u) <= 4
            done = true
        end
        
        if find(u, v1) != find(u, v2)
            if !done
                union(u, find(u, v1), find(u, v2))
            else
                return distance
                break
            end
        end
    end
end

function single_bits(num_bits::Int)
    max_shift = num_bits - 1
    d = Dict{Int, Bool}()
    for i in 0:max_shift
        d[1 << i] = true
    end
    return d
end

function double_bits(num_bits::Int)
    # this gets single and double bits.
    max_shift = num_bits - 1
    d = Dict{Int, Bool}()
    bits = single_bits(num_bits)
    for x in keys(bits)
        for y in keys(bits)
            d[x | y] = true
        end
    end
    return d
end

function find_num_big_clusters()
#    vertices = read_clusters_binary("clustering_small.txt")
    vertices = read_clusters_binary("clustering_big.txt")
    u = UF(Dict{Int, Int}(), Dict{Int, Vector{Int}}())

    # make a hash of all vertices
    for v in keys(vertices)
        push!(u, v)
    end

    # generate all double bit pairs up to length 24
    all_bits = double_bits(24)
    
    # create clusters for everything within hamming distance 2
    for v1 in keys(vertices)
        for b in keys(all_bits)
            v2 = v1 $ b
            if haskey(vertices, v2)
                union(u, find(u, v1), find(u, v2))
            end
        end
    end

    return length(u)
end

# print(find_cluster_distance("clustering1.txt"))
# print(read_clusters_binary("clustering_small.txt"))
# print(find_num_big_clusters())

function max_knapsack_value(fname::String, memoize::Bool)
    # Note that we don't have a weight = 0 dimension in the array to work around
    # julia's 1 indexed arrays without kluding up every array access. This should
    # be fine except for degenerate cases.

    function read_items(fname::String)
        f = open(fname)
        line = readline(f)
        capacity, num_items = tuple(map(int, split(line))...)
        a = Array((Int, Int), num_items)

        max_weight = 0
        for i in 1:num_items
            # tuple is (value, weight)
            line = readline(f)
            value, weight = tuple(map(int, split(line))...)
            if weight > max_weight
                max_weight = weight
            end
            a[i] = (value, weight)
        end
        return (a, capacity, max_weight)
    end

    function max_without_item(a::Array, i, j)
        # this would be more effficient if we made the array one larger and avoided
        # this branch all the time, but julia's 1-indexing makes that less readable.
        if i-1 > 0
            return a[i-1, j]
        else
            return 0
        end
    end

    function max_with_item(a::Array, i, j, value, weight)
        # nonsense function to deal with julia's 1-based arrays
        if i-1 < 1 && j-weight >= 0 || j-weight == 0
            return value 
        elseif j-weight < 1 || i-1 < 1
            return 0
        else
            return a[i-1, j-weight] + value
        end
    end

    function find_max_value(h, all_items, i, j)
        if haskey(h, (i,j))
            return h[(i,j)]
        elseif i <= 0 || j <= 0
            return 0
        else
            value, weight = all_items[i]
            if (j-weight < 0)
                h[(i,j)] = find_max_value(h, all_items, i-1, j)
            else 
                h[(i,j)] = max(find_max_value(h, all_items, i-1, j),
                               find_max_value(h, all_items, i-1, j-weight) + value)
            end
            return h[(i,j)]
        end        
    end

    all_items, capacity, max_weight = read_items(fname)

    if !memoize
        a = Array(Int, length(all_items), capacity)

        for i in 1:length(all_items)
            for j in 1:capacity
                value, weight = all_items[i]
                a[i, j] = max_without_item(a, i, j) > max_with_item(a, i, j, value, weight) ?
                max_without_item(a, i, j) : max_with_item(a, i, j, value, weight)
            end
        end

        return a[length(all_items), capacity]
    else
        # (item, capacity) -> value
        h = Dict{(Int, Int), Int}()
        return find_max_value(h, all_items, length(all_items), capacity)
    end
end

# print("$(max_knapsack_value("knapsack1.txt", true))\n")
# print("$(max_knapsack_value("knapsack_big.txt", true))\n")

function calculated_cost(a, m, n)
    if n > size(a)[2] || m > size(a)[1] || n <= 0 || m <= 0 || m > n
        return 0
    else
        return a[m,n]
    end
end

function min_over_range(a::Array, input::Array, i, s)
    min = typemax(Int)
    for r in i:(i+s)
        cost = sum(input[i:i+s]) + 
        calculated_cost(a, i, r-1) + 
        calculated_cost(a, r+1, i+s)
        min = cost < min ? cost : min
    end
    return min
end

function optimal_bst(input::Array)
    assert(sum(input) == 1)
    n = length(input)
    a = Array(Float64, n, n)
    for s in 0:n-1 
        for i in 1:n
            # s = j - i
            # i = j + s
            if i+s <= n
                a[i, i+s] = min_over_range(a, input, i, s)
            end
        end
    end
    return a[1,n]
end

assert(optimal_bst([.1, .3, .6]) == 1.5)
# print(optimal_bst([.05, .4, .08, .04, .1, .1, .23]))

# format is
# num_vertices num_edges
# v1 v2 length
# v1 v2 length
# ...

function read_graph4(fname::String, directed::Bool)
    # This is similar to read_edges, but we can't quite re-use read_edges.
    # TODO: refactor this and read_edges into one function.
    f = open(fname)
    line = readline(f)
    vertices, edges = tuple(map(int, split(line))...)
    d = Dict{Int, Dict{Int, Int}}()
    # d could be an array -- the graph is connected, so we know every
    # vertex has at least one edge.
    for i in 1:edges
        # tuple is (vertex, vertex, weight)
        line = readline(f)
        v1, v2, weight = tuple(map(int, split(line))...)
        if !haskey(d, v1)
            d[v1] = Dict{Int, Int}()
        end
        
        if !haskey(d, v2) && !directed
            d[v2] = Dict{Int, Int}()
        end

        d[v1][v2] = weight
        if !directed
            d[v2][v1] = weight
        end
     end
    return d, vertices
end

function find_shortest_path(fname::String)
    # this function works around Julia's 1-based array. It's awkward not to be
    # be able to index from 0 for this, so we simply return the correct value 
    # for iteration 0.
    # Also, k is the last index of the array because that makes julia pretty
    # print the result in a reasonable fashion.
    function lookup_fw_value(a::Array, g, k, i, j)
        if k == 0
            if i == j
                return 0
            elseif haskey(g, i) && haskey(g[i], j)
                return g[i][j]
            else
                return div(typemax(Int),4)
            end
        else
            return a[i, j, k]
        end
    end

    # either the value from the previous iteration (i to j), or value from i to k plus k to j.
    function fw_minimum(a::Array, g, k, i, j)
        return min(lookup_fw_value(a, g, k-1, i, j),
                   lookup_fw_value(a, g, k-1, i, k) + lookup_fw_value(a, g, k-1, k, j))
    end

    g, num_vertices = read_graph4(fname, true)
    a = Array(Int, num_vertices, num_vertices, num_vertices)
    
    # Using Floyd-Warshall. Initialization is handled by lookup_fw_value.
    for k in 1:num_vertices
        for i in 1:num_vertices
            for j in 1:num_vertices
                a[i, j, k] = fw_minimum(a, g, k, i, j)
            end
        end
    end

    shortest_distance = typemax(Int)
    for i in 1:num_vertices
        for j in 1:num_vertices
            shortest_distance = a[i,j,num_vertices] < shortest_distance ? a[i,j,num_vertices] : shortest_distance
        end
    end

    has_cycle = false
    for i in 1:num_vertices
        if a[i,i,num_vertices] < 0
            has_cycle = true
        end
    end

    return (shortest_distance, has_cycle)
end
    
# print(find_shortest_path("g1.txt"))
# print(find_shortest_path("g2.txt"))
# print(find_shortest_path("g3.txt"))

function next_perm(current::Int32, n::Int ,k::Int)
    lowest_bit = current & -current
    propogate = lowest_bit + current
    next = div((current $ propogate) >> 2,lowest_bit) | propogate
    if next >= (1 << n)
        next = 0
    end
    return next
end

assert(next_perm(int32(1), 4, 1) == 2)
assert(next_perm(int32(2), 4, 1) == 4)
assert(next_perm(int32(4), 4, 1) == 8)
assert(next_perm(int32(8), 4, 1) == 0)

assert(next_perm(int32(3), 4, 2) == 5)
assert(next_perm(int32(5), 4, 2) == 6)
assert(next_perm(int32(6), 4, 2) == 9)
assert(next_perm(int32(9), 4, 2) == 10)
assert(next_perm(int32(10), 4, 2) == 12)
assert(next_perm(int32(12), 4, 2) == 0)

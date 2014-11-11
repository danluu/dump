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
    center::Vector{Float64}
    points::Set{Vector{Int}}
end

function print_centroids(centroids::Array{Centroid})
    for c in centroids
        println("Center: $(c.center)")
        println("Points: $(c.points)")
    end
end

function find_closest_centroid(cents::Array{Centroid}, point::Vector{Int})
    min_dist = typemax(Float64)
    closest = nothing
    for c in cents
        dist = norm(c.center - point)
        if dist < min_dist
            min_dist = dist
            closest = c
            # println("Distance from $point to $c is $dist")
        end
    end
    closest
end

function recompute_center(centroid::Centroid)
    average = [0,0]
    for p in centroid.points
        average += p
    end
    centroid.center = average / length(centroid.points)
end

function recompute_centers(centroids::Vector{Centroid})
    for c in centroids
        recompute_center(c)
    end
end

function reassign_point(to::Centroid, from::Centroid, point)
    push!(to.points, point)
    delete!(from.points, point)
end

function reassign_points(centroids::Vector{Centroid})
    for cent in centroids
        for p in cent.points
            closest = find_closest_centroid(centroids, p)
            if closest != cent
                println("Reassigning $p from $cent to $closest")
                reassign_point(closest, cent, p)
            end
        end
    end
end

# naive algo that recomputes a ton of stuff. Should be ok for the number of points we have.
function make_initial_centroids(initial_centers, initial_free_points)
    


    centroids = Array(Centroid,0)

    # Add initial centers
    for c in initial_centers
        new_list = Set{Vector{Int}}()
        push!(new_list, c)
        new_cent = Centroid(c, new_list)
        push!(centroids, new_cent)
    end

    # Add initial non-centers
    for p in initial_free_points
        closest = find_closest_centroid(centroids, p)
        push!(closest.points, p)
    end

    centroids
end

function crappy_knn(initial_centers, initial_free_points, initial::Bool)
    cents = make_initial_centroids(initial_centers, initial_free_points)
    if initial
        print_centroids(cents)
    end
    recompute_centers(cents)
    if !initial
        print_centroids(cents)
    end
    println("")
    return # blow away stuff below this.
    reassign_points(cents)
    # print_centroids(cents)
    recompute_centers(cents)
    # print_centroids(cents)
end

 # crappy_knn(
 #     Array[[25,125], [44,105], [29,97], [35,63], [55,63], [42,57], [23,40], [64,37], [33,22], [55,20]], 
 #     Array[[28,145],[50,130],[65,140],[38,115],[55,118],[50,90],[43,83],[63,88],[50,60],[50,30]], false)


# crappy_knn(Array[[5,10], [20,5]], Array[[3,3],[10,1],[15,14],[20,10]], true)
# crappy_knn(Array[[5,10], [20,5]], Array[[6,7],[11,14],[11,5],[17,2]], true)
# crappy_knn(Array[[5,10], [20,5]], Array[[7,8],[12,5],[13,10],[16,4]], true)
# crappy_knn(Array[[5,10], [20,5]], Array[[3,3],[10,1],[13,10],[16,4]], true)

# crappy_knn(Array[[5,10], [20,5]], Array[[6,15],[13,7],[16,19],[25,12]], true)
# crappy_knn(Array[[5,10], [20,5]], Array[[7,12],[12,8],[16,16],[18,5]], true)
# crappy_knn(Array[[5,10], [20,5]], Array[[7,8],[12,5],[15,14],[20,10]], true)
# crappy_knn(Array[[5,10], [20,5]], Array[[7,8],[12,5],[13,10],[16,4]], true)


# Return indices of bits set in Int
# Starts at 1 because julia is 1-indexed
function index_of_bits(x::Int)
    assert(x >= 0)
    set_bits = Array(Int,0)
    
    i = 1
    current_idx = 1
    while x != 0
        if x & 1 == 1
            push!(set_bits, i)
        end
        x >>= 1
        i += 1
    end
    set_bits
end

# brute force. Slow implementation. Lots of copying + GC.
function set_cover_brutal(input)
    sets = map(x -> Set(x), input)
    cover = union(sets...)
    minimal_set = Int
    minimal_size = typemax(Int)

    num_bits = length(sets)
    for i in 1:(2^num_bits-1)
        indices = index_of_bits(i)
        working_set = Set{Char}()
        for idx in indices
            union!(working_set, sets[idx])
        end
        
        # Replace minimal set if we have a smaller cover.
        if working_set == cover
            if count_ones(i) < minimal_size
                minimal_set = i
                minimal_size = count_ones(minimal_set)
            end
        end
    end

    minimal_set
end

# brutal_size = count_ones(set_cover_brutal(["AB", "BC", "CD", "DE", "EF", "FG", "GH", "AH", "ADG", "ADF"]))

# Slack formula: y * (dot(w,x) + b) >= 1 - slack
# y is our "positive" var
function compute_slack(point::Array{Int}, positive::Bool)
    res = dot([-1,1],point) - 2
    res = positive ? res : -res
    return -(res - 1)
end

function compute_all_slacks(pos, neg)
    for point in pos
        slack = compute_slack(point, true)
        println("$point $slack")
    end
    for point in neg
        slack = compute_slack(point, false)
        println("$point $slack")
    end     
end

compute_all_slacks(
Array[[5,10],[7,0],[1,8],[3,8],[7,8],[1,6],[3,6],[3,4]],
Array[[5,8],[5,6],[7,6],[1,4],[5,4],[7,4],[1,2],[3,2]]
)
 
function classify_with_decision_tree(point::Array{Int})
    # [age, salary]
    assert(length(point) == 2)
    if point[1] < 45 
        if point[2] < 110
            return false
        else
            return true
        end
    else
        if point[2] < 75
            return false
        else
            return true
        end        
    end
end

function decision_tree_fixed(yes, no)
    # should buy. false means misclassified
    for point in yes
        if !classify_with_decision_tree(point)
            println("$point should buy, didn't")
        end
    end

    for point in no
        if classify_with_decision_tree(point)
            println("$point should buy, didn't")
        end
    end 
end

decision_tree_fixed(
    Array[[28,145], [38,115], [43,83], [50,130], [50,90], [50,60], [50,30], [55,118], [63,88], [65,140]],
    Array[[23,40], [25,125], [29,97], [33,22], [35,63], [42,57], [44, 105], [55,63], [55,20], [64,37]]
)


include("algos.jl")

assert(compute_weighted_sum([(3,1), (2,2), (1,3)]) == 15)
assert(problem1("1-1.txt", false) == 11336)
assert(problem1("1-1.txt", true) == 10548)
assert(problem1("1-2.txt", false) == 145924)
assert(problem1("1-2.txt", true) == 138232)

g = read_edges("1-3.txt", false)
assert(compute_mst_naive(g) == 2624)

assert(find_cluster_distance("3-1-a.txt")==134365)
assert(find_cluster_distance("3-1-b.txt")==7)

assert(max_knapsack_value("knapsack-test-1.txt", false) == 60)
assert(max_knapsack_value("knapsack-test-1b.txt", false) == 60)
assert(max_knapsack_value("knapsack-test-1c.txt", false) == 60)
assert(max_knapsack_value("knapsack-test-2.txt", false) == 2700)
assert(max_knapsack_value("knapsack-test-2b.txt", false) == 27000)
assert(max_knapsack_value("knapsack-test-2c.txt", false) == 27000)
assert(max_knapsack_value("knapsack-test-1.txt", true) == 60)
assert(max_knapsack_value("knapsack-test-1b.txt", true) == 60)
assert(max_knapsack_value("knapsack-test-1c.txt", true) == 60)
assert(max_knapsack_value("knapsack-test-2.txt", true) == 2700)
assert(max_knapsack_value("knapsack-test-2b.txt", true) == 27000)
assert(max_knapsack_value("knapsack-test-2c.txt", true) == 27000)

assert(optimal_bst([.1, .3, .6]) == 1.5)
assert(find_shortest_path("4-1.txt") == (-1, false))
assert(find_shortest_path("4-2.txt") == (-1, false))

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

assert(one_indices(int32(3)) == [1,2])
assert(one_indices(int32(4)) == [3])
assert(one_indices(int32(5)) == [1,3])

assert(tsp_cost("5-1.txt") == 4)
assert(int(floor(tsp_cost("5-2.txt"))) == 10)
assert(int(floor(tsp_cost("5-3.txt"))) == 26714)

assert(all(scc_count("scc-2.txt") .== [4, 3, 3, 1, 0]))
assert(all(scc_count("scc-4.txt") .== [3, 3, 2, 0, 0]))
assert(all(scc_count("scc-7.txt") .== [36, 7, 1, 1, 1]))

assert(scc_2sat("6-1.txt") == true)
assert(scc_2sat("6-2.txt") == false)

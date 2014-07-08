type UF
    parent::Dict{Int, Int}
    children::Dict{Int, Vector{Int}}
end

function make_union(num::Int)
    u = UF(Dict{Int, Int}(), Dict{Int, Vector{Int}}())
    for i in 1:num
        u.parent[i] = i
        u.children[i] = [i]
    end
    return u
end

function union(u::UF, x::Int, y::Int)
    if length(u.children[x]) > length(u.children[y]) 
        union_helper(u, x, y)
    else
        union_helper(u, y, x)
    end
end

function union_helper(u::UF, x::Int, y::Int)
    for c in u.children[y]
        u.parent[c] = x
        push!(u.children[x], c)
    end
    delete!(u.children, y)
end

function Base.find(u::UF, x::Int)
    return u.parent[x]
end

function Base.length(u::UF)
    return length(u.children)
end

n0 = 4
u0 = make_union(n0)
assert(length(u0) == 4)
for i in n0
    assert(u0.parent[i] == i)
    assert(find(u0, i) == i)
    assert(u0.children[i] == [i])
end
union(u0, 1, 2)
assert(length(u0) == 3)
assert(find(u0, 1) == find(u0, 2))
assert(find(u0, 2) != find(u0, 3))
assert(find(u0, 3) != find(u0, 4))
union(u0, 3, 4)
assert(length(u0) == 2)
assert(find(u0, 1) == find(u0, 2))
assert(find(u0, 2) != find(u0, 3))
assert(find(u0, 3) == find(u0, 4))
union(u0, find(u0, 3), find(u0, 2))
assert(length(u0) == 1)
assert(find(u0, 1) == find(u0, 2))
assert(find(u0, 2) == find(u0, 3))
assert(find(u0, 3) == find(u0, 4))

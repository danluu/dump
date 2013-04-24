# Trying out various features of julia by solving easy toy problems that require
# some use of basic language features and libraries

function string_is_perm(a::String, b::String)
    count = Dict{Char,Int}()
    
    for c = a
        has(count,c) ? (count[c] += 1) : (count[c] = 1)
    end
    
    for c = b
        has(count,c) ? count[c] -= 1 : return false
    end

    for (k,v) = count
        if v != 0 return false end
    end
    return true
end
    
assert(string_is_perm("foo","foo") == true)
assert(string_is_perm("foo","oof") == true)
assert(string_is_perm("foo","foof") == false)
assert(string_is_perm("foo","moof") == false)
assert(string_is_perm("foo","moo") == false)

function sub_spaces(x::String)
    replace(x," ", "%20")
end

assert(sub_spaces("this is a string   --yep") == "this%20is%20a%20string%20%20%20--yep")

function is_rotation(x::String, y::String)
    return length(x)==length(y) && ismatch(Regex(y),"$x$x")
end

assert(is_rotation("waterbottle", "erbottlewat") == true)
assert(is_rotation("waterbottle", "trbottlewae") == false)
assert(is_rotation("f", "ff") == false)
assert(is_rotation("ff", "f") == false)

type DLLBlock{T}
    data::T
    prev::Union(Nothing,DLLBlock{T})
    next::Union(Nothing,DLLBlock{T})
end

type DLL{T}
    length::Int
    head::DLLBlock{T}
    rear::DLLBlock{T}
end

function makeDLL{T}(x::T)
    y = DLLBlock(x,nothing,nothing)
    return DLL{T}(1,y,y)
end

begin
    a = makeDLL(10)
end

type LLBlock{T}
    data::T
    next::Union(Nothing,LLBlock{T})
end

type LL{T}
    length::Int
    head::LLBlock{T}
end

function makeLL{T}(x::T)
    y = LLBlock(x,nothing)
    return LL{T}(1,y)
end

function cons{T}(x::T, xs::LL{T})
    block = LLBlock(x, nothing)
    block.next = xs.head
    xs.length += 1
    xs.head = block
end

# Note: begin/end doesn't define a new scope

begin
    a = makeLL(10)
    b = cons(20,a)
end

# Stacks are supported by the Vector type in Julia, which is just a 1-d array
function sort_stack(s::Array{Int})
    len = length(s)
    new_s = Array(Int,0)
    while(length(new_s) < len)
        assert(length(new_s) + length(s) == len)
        temp = pop!(s)
        while(length(new_s) != 0 && temp > last(new_s))
            push!(s, pop!(new_s))
        end
        push!(new_s,temp)
    end
    return new_s
end

assert(sort_stack([1,2,3,4,5]) == [5,4,3,2,1])
assert(sort_stack([5,4,3,2,1]) == [5,4,3,2,1])

# Solution from Leah
function subsets{T}(xs::Array{T,1})
    if length(xs) == 0
        return Array(Array{T,1},0)
    else
        subrest = subsets(xs[2:])
        ours = [x for x=[unshift!(z,xs[1]) for z=[copy(ys) for ys=subrest]]]
            append!(subrest,ours)
            push!(subrest,[xs[1]])
            return subrest
   end
end

@show subsets([1,2,3])

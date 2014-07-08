# Mutable heap.

type ArrayHeap{T}
    a::Vector{T}
    # need some sort of index for elements.
end

function ArrayHeap(T)
    return ArrayHeap{T}(Array(T, 0))
end

function top(h::ArrayHeap) 
    return h.a[1]
end

function swap(h::ArrayHeap, i::Int, j::Int)
    temp = h.a[i]
    h.a[i] = h.a[j]
    h.a[j] = temp
end

function parent(i::Int)
    return div(i,2)
end

function left(i::Int)
    return 2*i
end

function right(i::Int)
    return 2*i+1
end

function Base.push!{T}(h::ArrayHeap{T}, x::T)
    # Push onto the end and then bubble up to correct position
    push!(h.a, x)
    i = length(h.a)
    while (i > 1 && h.a[parent(i)] > h.a[i])
        swap(h, parent(i), i)
        i = parent(i)
    end
end

function Base.pop!{T}(h::ArrayHeap{T})
    # Swap top with bottom and then bubble down
    swap(h, 1, length(h.a))
    top = pop!(h.a)
    i = 1
    while ((left(i)  <= length(h.a) && h.a[i] > h.a[left(i)]) ||
           (right(i) <= length(h.a) && h.a[i] > h.a[right(i)]))
        if left(i) == length(h.a) || h.a[left(i)] < h.a[right(i)]
            swap(h, i, left(i))
            i = left(i)
        else
            swap(h, i, right(i))
            i = right(i)
        end
    end
    return top
end

h = ArrayHeap(Int)
push!(h, 2)
push!(h, 3)
push!(h, 1)
push!(h, 4)
assert(pop!(h) == 1)
assert(pop!(h) == 2)
assert(pop!(h) == 3)
assert(pop!(h) == 4)

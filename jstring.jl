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

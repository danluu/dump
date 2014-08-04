ILLEGAL_IDX = -1
MAX_HT_LOAD_FACTOR = 0.7

# TODO: make this generic.
immutable KV
    key::Int32
    value::Float32
end

type DenseDict
    table::Array{KV}
    num_elements::Int
    num_deleted::Int
    max_size::Int
    empty_key::Int32
    deleted_key::Int32
end


function set_empty_key(h::DenseDict, key)
    k.empty_key = key
end

function empty_key(h)
    return h.empty_key
end

function hash_fn(key)
    # TODO: actually hash.
    return key
end

function resize_and_reset(h::DenseDict, size::Int)
    h.table = Array(KV, size)
    h.num_elements = 0
    h.num_deleted = 0
    h.max_size = size # TODO: need to account for load factor.
    h.empty_key = typemin(Int32)
    h.deleted_key = typemin(Int32) + 1

    for i in 1:length(h.table)
        h.table[i] = KV(h.empty_key, 0.0)
    end
end

# Use quadratic probing.
function reprobe(key, num_probes)
    # TODO: try doing linear hashing (i.e., always return 1)
    return num_probes
end

function getindex(h::DenseDict, key)
    return find(h, key)
end

function find(h, key)
    if size(h) == 0 
        return nothing
    end
    idx, insert_idx = find_idx(h, key)
    if idx == ILLEGAL_IDX
        return nothing
    else
        return h.table[idx].value
    end
end

function find_idx(h, key)
    # TODO: replace mod1 with bit manipulation to speed this up.
    # This is somewhat annoying to do in Julia because of the 1-based indexing. 
    # If we & with a mask we can get 0. Simplest solution is to basically 0 index,
    # do all index modifying operations, and then add 1.

    num_probes = 0           # number of times we've probed
    insert_idx = ILLEGAL_IDX # where we'd insert
    # TODO: assert this where we re-size, to avoid adding the check to every lookup.
    assert(count_ones(h.max_size) == 1)
    # Maybe do this masking in the hash function?    
    idx = mod1(hash_fn(key), max_size(h))
    while true
        if test_empty(h, idx)            
            return insert_idx == ILLEGAL_IDX ? (ILLEGAL_IDX, idx) : (ILLEGAL_IDX, insert_idx)
        elseif test_deleted(h, idx) # keep looking, but mark entry for insertion.
            insert_idx == ILLEGAL_IDX ? idx : insert_idx
        elseif key == get_key(h, idx)
            return (idx, ILLEGAL_IDX)
        end
        num_probes += 1
        idx = mod1(idx + reprobe(key, num_probes), max_size(h))
    end
end

function get_key(h, idx)
    return h.table[idx].key
end

function setindex!(h::DenseDict, val, key)
    insert(h, key, val)
end

function insert(h, key, val)
    # resize_delta(h, 1) # TODO: add resizing.
    return insert_noresize(h, key, val)
end

function insert_noresize(h, key, val)
    assert(key != h.empty_key)
    assert(key != h.deleted_key)
    idx, insert_idx = find_idx(h, key)
    if idx != ILLEGAL_IDX # element was already in table.
        return false      # false: didn't insert.
    else
        return insert_at(h, key, val, insert_idx)
    end
end

function insert_at(h, key, val, idx)
    if size(h) > max_size(h)
        throw(OverflowError())
    end
    if test_deleted(h, idx)
        # replace old entry.
        assert(h.num_deleted > 0)
        h.num_deleted -= 1
    else
        h.num_elements += 1
    end
    h.table[idx] = KV(key, val)
end

function test_deleted(h, index::Int)
    h.num_deleted > 0 && h.deleted_key == h.table[index]
end

function test_empty(h, index::Int)
    return h.empty_key == get_key(h, index)
end


function size(h)
    return h.num_elements - h.num_deleted
end

function max_size(h)
    return h.max_size
end

function empty(h)
    return size(h) == 0
end

function num_buckets(h)
end





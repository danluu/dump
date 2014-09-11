# Screwing around. Little to nothing in this file makes sense.

const NUM_LEVELS = 3
const BLOCK_SIZE = 2^NUM_LEVELS
const NUM_LEAVES = 2^(NUM_LEVELS-1)
const BASE_OFFSET = BLOCK_SIZE * NUM_LEAVES

# note: this means that the root is block 0. Maybe want it to be block 3 or something weird like that to simplify some math.
# note: we assume that index 0 within a block is empty, so the calculation for block 1
# is something between 33 and 39
function block_number(offset:Int)
    iceil(offset - base_offset/BLOCK_SIZE)
end

function parent(offset:Int)
    
end

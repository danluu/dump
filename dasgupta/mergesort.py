# inputs: two sorted lists
# output: a sorted list
# WARNING: this implementation is probably slow because we pop off the front of a list
# instead of keeping an index.
def merge(aa, bb):
    assert(abs(len(aa) - len(bb)) <= 1)

    res = []
    while len(aa) > 0 and len(bb) > 0:
        if (aa[0] < bb[0]):
            res.append(aa.pop(0))
        else:
            res.append(bb.pop(0))

    if (len(aa) > 0):
        res += aa

    if (len(bb) > 0):
        res += bb

    return res


def mergesort(aa):
    if (len(aa) <= 1):
        return(aa)

    fst = 0
    mid = len(aa) // 2
    end = len(aa)
    
    return merge(mergesort(aa[fst:mid]),mergesort(aa[mid:end]))
            

assert(merge([0,1,2], [3,4,5]) == [0,1,2,3,4,5])
assert(merge([3,4,5], [0,1,2])  == [0,1,2,3,4,5])

assert(merge([0,2,4], [1,3,5])  == [0,1,2,3,4,5])
assert(merge([1,3,5], [0,2,4])  == [0,1,2,3,4,5])

assert(mergesort([0,1,2,3,4]) == [0,1,2,3,4])
assert(mergesort([0,1,2,3,4,5]) == [0,1,2,3,4,5])
assert(mergesort([5,4,3,2,1,0]) == [0,1,2,3,4,5])

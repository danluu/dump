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


# with open('rosalind_ms.txt') as f:
with open('/home/danluu/Downloads/rosalind_ms.txt') as f:
    alen = int(f.readline())
    a_str = f.readline().split()
    assert(alen == len(a_str))

    a = [int(x) for x in a_str]

    res = " ".join([str(x) for x in mergesort(a)])

    # with open('ms_out.txt','w') as outf:
    with open('/home/danluu/Downloads/ms_out.txt','w') as outf:
        outf.write(res)

    

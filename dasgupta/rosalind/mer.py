def merge(aa, bb):

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

# with open('rosalind_mer.txt') as f:
with open('/home/danluu/Downloads/rosalind_mer.txt') as f:
    len1 = int(f.readline())
    a1_str = f.readline().split()
    a1 = [int(x) for x in a1_str]
    assert(len1 == len(a1))

    len2 = int(f.readline())
    a2_str = f.readline().split()
    a2 = [int(x) for x in a2_str]
    assert(len2 == len(a2))
    
    res = merge(a1, a2)
    res_str = [str(x) for x in res]

    # with open('mer_out.txt','w') as outf:
    with open('/home/danluu/Downloads/mer_out.txt','w') as outf:
        outf.write(" ".join(res_str))

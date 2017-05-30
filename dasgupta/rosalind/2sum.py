def find2(a):
    d = dict()
    for i in range(len(a)):
        if -a[i] in d:
            return [str(d[-a[i]]+1), str(i+1)]
        else:
            d[a[i]] = i
    return [str(-1)]
    

# with open('rosalind_2sum.txt') as f:
with open('/home/danluu/Downloads/rosalind_2sum.txt') as f:
    header = f.readline().split()
    assert(len(header) == 2)
    alen = int(header[1])

    res = []
    for line in f:
        a = [int(x) for x in line.split()]
        assert(len(a) == alen)
        res.append(" ".join(find2(a)))

    # with open('2sum_out.txt','w') as outf:
    with open('/home/danluu/Downloads/2sum_out.txt','w') as outf:
        outf.write("\n".join(res))

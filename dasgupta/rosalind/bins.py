def bsearch(x, values):
    lb = 0
    ub = len(values) - 1
    while (ub >= lb):
        span = ub - lb
        halfspan = span // 2
        if (halfspan == 0):
            if values[lb] == x:
                return lb
            elif values[ub] == x:
                return ub
            else:
                return -2
        mididx = lb + halfspan
        midvalue = values[mididx]
        if x == midvalue:
            return mididx
        elif x > midvalue:
            lb = mididx + 1
        else:
            ub = mididx - 1

    return -2
        

def bins():
    l = []
    with open('/home/danluu/Downloads/rosalind_bins.txt') as f:
    # with open('bins.txt') as f:
        l = f.readlines()

    n = int(l[0].strip())
    m = int(l[1].strip())

    values_str = l[2].split()
    search_str = l[3].split()

    print(n)
    print(m)

    assert(len(values_str) == n)
    assert(len(search_str) == m)

    values = [int(x) for x in values_str]
    search = [int(x) for x in search_str]

    res = []
    for x in search:
        my_ans = bsearch(x, values) + 1
        python_ans = -200
        try:
            python_ans = values.index(x) + 1
            if my_ans == -1:
                print(x, my_ans, python_ans)
        except ValueError:
            python_ans = -1
            if my_ans != -1:
                print(x, my_ans, python_ans)
        # if my_ans != python_ans:
        #     print(x, my_ans, python_ans)

        res.append(my_ans)

    return res


with open('/home/danluu/Downloads/bins_out.txt','w') as outf:
# with open('bins_out.txt','w') as outf:
    l = bins()
    lstr = [str(x) for x in l]
    outf.write(" ".join(lstr))


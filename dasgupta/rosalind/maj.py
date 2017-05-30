from statistics import median

def maj(a):
    candidate = int(median(a))
    count = 0

    for x in a:
        if candidate == x:
            count += 1

    if count > (len(a) / 2):
        return candidate
    else:
        return -1

# with open('rosalind_maj.txt') as f:
with open('/home/danluu/Downloads/rosalind_maj.txt') as f:
    res = []

    header = f.readline().split()
    num_problems = int(header[0])
    array_len = int(header[1])

    for line in f:
        parts = line.split()
        a = [int(x) for x in parts]
        res.append(str(maj(a)))


    # with open('maj_out.txt','w') as outf:
    with open('/home/danluu/Downloads/maj_out.txt','w') as outf:
        outf.write(" ".join(res))



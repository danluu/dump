def read_graph():
    gr = dict()
    firstline = True
    # with open('rosalind_ddeg.txt') as f:
    with open('/home/danluu/Downloads/rosalind_ddeg.txt') as f:
        for line in f:
            
            parts = line.split()
            assert(len(parts) == 2)
                            
            n1 = int(parts[0])
            n2 = int(parts[1])
            if firstline:
                firstline = False
                # Create empty list for each node
                for i in range(1, n1+1):
                    gr[i] = []
            else:
                gr[n1].append(n2)
                gr[n2].append(n1)
    return gr

def enumerate_degree(gr):
    res = []
    for n1 in sorted(gr):
        second_deg = 0
        for n2 in gr[n1]:
            second_deg += len(gr[n2])
        res.append(str(second_deg))
    return res

gr = read_graph()
res = enumerate_degree(gr)
# with open('ddeg_out.txt','w') as outf:
with open('/home/danluu/Downloads/ddeg_out.txt','w') as outf:
    outf.write(" ".join(enumerate_degree(gr)))

from collections import defaultdict

def read_graph():
    gr = defaultdict(list)
    firstline = True
    # with open('rosalind_deg.txt') as f:
    with open('/home/danluu/Downloads/rosalind_deg.txt') as f:
        num_nodes = -1
        for line in f:
            
            parts = line.split()
            assert(len(parts) == 2)
                            
            n1 = int(parts[0])
            n2 = int(parts[1])
            if firstline:
                firstline = False
                num_nodes = n1
            else:
                gr[n1].append(n2)
                gr[n2].append(n1)
    assert(num_nodes == len(gr))
    return gr

def enumerate_degree(gr):
    res = []
    for n1 in sorted(gr):
        res.append(str(len(gr[n1])))
    return res

gr = read_graph()
res = enumerate_degree(gr)
# with open('deg_out.txt','w') as outf:
with open('/home/danluu/Downloads/deg_out.txt','w') as outf:
    outf.write(" ".join(enumerate_degree(gr)))

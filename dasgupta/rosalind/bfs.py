import collections

def read_directed_graph():
    gr = dict()
    firstline = True
    # with open('rosalind_bfs.txt') as f:
    with open('/home/danluu/Downloads/rosalind_bfs.txt') as f:
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
    return gr

def bfs1(gr):
    q = collections.deque()
    seen = set()
    res = [-1] * (len(gr) + 1)

    q.append(1)
    seen.add(1)
    res[1] = 0

    while q:
        node = q.popleft()
        for neighbor in gr[node]:
            if not neighbor in seen:
                seen.add(neighbor)
                res[neighbor] = res[node] + 1
                q.append(neighbor)
    return res[1:]
                

gr = read_directed_graph()
print(" ".join([str(x) for x in bfs1(gr)]))

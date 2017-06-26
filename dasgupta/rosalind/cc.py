# Start with a set of unvisited nodes.
# while the set is not empty, remove an arbitrary element from the set and run dfs.
# In the dfs, visit every unvisited node.
from collections import defaultdict

def read_graph():
    gr = defaultdict(list)
    # with open('rosalind_cc.txt') as f:
    with open('/Users/danluu/Downloads/rosalind_cc.txt') as f:
        for line in f:            
            parts = line.split()
            if len(parts) != 2:
                raise Exception("ERROR: unparsable line: %s" % parts)
            
            n1, n2 = map(int, parts)
            gr[n1].append(n2)
            gr[n2].append(n1)
    return gr

def dfs(node, unvisited):
    for neighbor in gr[node]:
        if neighbor in unvisited:
            unvisited.remove(neighbor)
            dfs(neighbor, unvisited)
    return

gr = read_graph()
unvisited = set(gr.keys())

num_cc = 0
while unvisited:
    node = unvisited.pop()
    num_cc += 1
    dfs(node, unvisited)

print(num_cc)

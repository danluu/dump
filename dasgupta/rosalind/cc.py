# Start with a set of unvisited nodes.
# while the set is not empty, remove an arbitrary element from the set and run dfs.
# In the dfs, visit every unvisited node.

def read_graph():
    gr = dict()
    header = True
    # with open('rosalind_cc.txt') as f:
    with open('/Users/danluu/Downloads/rosalind_cc.txt') as f:
        for line in f:
            
            parts = line.split()
            if (len(parts) != 2):
                print("ERROR: unparsable line: ", parts)
                assert(False)
                            
            n1 = int(parts[0])
            n2 = int(parts[1])
            if header:
                header = False
                # Create empty list for each node
                for i in range(1, n1+1):
                    gr[i] = []
            else:
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
unvisited = set()
for node in gr:
    unvisited.add(node)

num_cc = 0
while len(unvisited) != 0:
    node = unvisited.pop()
    num_cc += 1
    dfs(node, unvisited)

print(num_cc)

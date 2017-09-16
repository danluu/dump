# http://rosalind.info/problems/bip/

import collections

def solve(g):
    color = {}
    stack = []
    for node in g:
        if not node in color:
            stack.append(node)
            color[node] = 0

        while len(stack) > 0:
            node = stack.pop()
            for neighbor in g[node]:
                if neighbor not in color:
                    color[neighbor] = color[node] ^ 1
                    stack.append(neighbor)
                else:
                    if color[neighbor] == color[node]:
                        return -1

    return 1

graph = collections.defaultdict(list)
# with open('rosalind_bip.txt') as f:
with open('/Users/danluu/Downloads/rosalind_bip.txt') as f:
    results = ""
    num_graphs = int(f.readline().strip())
    for line in f:
        line = line.strip()

        if line == '':
            # New graph.
            # Note: we don't actually create a node for every node!
            header = f.readline()
            num_graphs -= 1
            if len(graph) != 0:
                results += ' {}'.format(solve(graph))
            graph = collections.defaultdict(list)
        else:
            # node in existing graph.
            nodes = [int(x) for x in line.split(' ')]
            graph[nodes[0]].append(nodes[1])
            graph[nodes[1]].append(nodes[0])

    results += ' {}'.format(solve(graph))
    assert(num_graphs == 0)
    
print(results.strip())

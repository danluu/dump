import collections

def dfs(g, node, seen, node_stack):
    # print('dfs {}'.format(node))
    node_stack.add(node)
    # print('stack add {}'.format(node))
    for neighbor in g[node]:
        if neighbor in node_stack:
            return -1
        if not neighbor in seen:
            seen.add(neighbor)
            if dfs(g, neighbor, seen, node_stack) == -1:
                return -1
                
    node_stack.remove(node)
    # print('stack remove {}'.format(node))
    return 1


def solve(g):
    seen = set()
    node_stack = set()
    for node in g:
        if not node in seen:
            assert(len(node_stack) == 0)
            if dfs(g, node, seen, node_stack) == -1:
                return -1
    return 1

graph = {}
reverse_graph = {}

with open('/Users/danluu/Downloads/rosalind_dag.txt') as f:
# with open('rosalind_dag.txt') as f:
    results = ""
    num_graphs = int(f.readline().strip())
    for line in f:
        line = line.strip()

        if line == '':
            # New graph.
            header = f.readline().split(' ')
            num_nodes = int(header[0])
            num_edges = int(header[1])

            num_graphs -= 1
            if len(graph) != 0:
                # print(graph)
                # print(reverse_graph)
                results += ' {}'.format(solve(graph))

            graph = {}
            reverse_graph = {}
            for node in range(1, num_nodes+1):
                graph[node] = []
                reverse_graph[node] = []
        else:
            # node in existing graph.
            nodes = [int(x) for x in line.split(' ')]
            graph[nodes[0]].append(nodes[1])
            reverse_graph[nodes[1]].append(nodes[0])
            num_edges -= 1

    # print(graph)
    # print(reverse_graph)
    results += ' {}'.format(solve(graph))
    assert(num_graphs == 0)
    
print(results.strip())

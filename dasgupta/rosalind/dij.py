import collections
import heapq

def solve(graph, num_nodes):
    result = [-1 for _ in range(num_nodes+1)]
    potential = []

    # for neighbor in graph[node]:
    #     heapq.heappush(potential, (graph[node][neighbor],neighbor))
    heapq.heappush(potential,(0,1))
    # print('push ({},{})'.format(0,1))
    # print(potential)

        
    while potential:
        dist, node = heapq.heappop(potential)
        # print('pop ({},{})'.format(dist, node))
        # print(potential)
        if result[node] != -1:
            # We check for a duplicate pop because heapq doesn't have
            # a replace operation, so we may draw the same element off
            # the heap multiple times.
            #
            # An alterate solution would be to grab the element off
            # the heap and modify the heap, but grabbing the element
            # is linear time.
            assert(dist >= result[node])
            # print('skip {} {}:{}'.format(node,result[node],dist))
            continue
        result[node] = dist
        for neighbor in graph[node]:
            alt = dist + graph[node][neighbor]
            assert(alt != -1)
            if alt < result[neighbor] or result[neighbor] == -1:
                heapq.heappush(potential, (alt, neighbor))
                # print('push ({},{})'.format(alt,neighbor))
                # print(potential)

    return result[1:]

# with open('rosalind_dij.txt') as f:
with open('/Users/danluu/Downloads/rosalind_dij.txt') as f:
    graph = collections.defaultdict(dict)

    header_str = f.readline().strip().split(' ')
    header = [int(x) for x in header_str]
    num_nodes = header[0]

    for line in f:
        parts = [int(x) for x in line.split(' ')]
        if parts[0] in graph and parts[1] in graph[parts[0]]:
            old = graph[parts[0]][parts[1]]
            if parts[2] < old:
                graph[parts[0]][parts[1]] = parts[2]
        else:
            graph[parts[0]][parts[1]] = parts[2]                

    print(' '.join([str(x) for x in solve(graph, num_nodes)]))


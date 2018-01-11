import unittest

class Cyclic(Exception):
    pass

def tsort(g, rev):
    no_incoming = []
    for node, incoming in rev.items():
        if not incoming:
            no_incoming.append(node)

    if not no_incoming:
        raise Cyclic

    res = []
    while no_incoming:
        node = no_incoming.pop()
        res.append(node)
        for outgoing in g[node]:
            rev[outgoing].remove(node)
            if not rev[outgoing]:
                no_incoming.append(outgoing)

    return res

def reverse_graph(g):
    rev = dict()
    for head in g:
        rev[head] = set()

    for head, tail in g.items():
        for node in tail:
            rev[node].add(head)

    return rev

def load_graph(filename):
    g = dict()
    with open(filename) as f:
        header = f.readline().strip().split(' ')
        num_nodes = int(header[0])

        for i in range(1, num_nodes+1):
            g[i] = []

        for line in f:
            parts = line.strip().split(' ')
            g[int(parts[0])].append(int(parts[1]))

    return g

class TestAdd(unittest.TestCase):
    def test_trivial(self):
        self.assertEqual(True,True)
        self.assertEqual(False,False)

    def test_rosalind_load(self):
        g = load_graph('rosalind_ts.txt')
        self.assertEqual(len(g), 4)
        self.assertEqual(len(g[1]), 1)
        self.assertEqual(len(g[2]), 0)
        self.assertEqual(len(g[4]), 2)

    def test_rosalind_sample(self):
        g = load_graph('rosalind_ts.txt')
        rev = reverse_graph(g)
        res = tsort(g,rev)
        print(res)
        self.assertEqual(res, [4,3,1,2])
        

if __name__ == '__main__':
    unittest.main()
        

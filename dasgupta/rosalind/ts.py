import unittest

class Cyclic(Exception):
    pass

def tsort(rev):
    no_outgoing = []
    for node, outgoing in rev.items():
        if not outgoing:
            no_outgoing.append(node)

    if not no_outgoing:
        raise Cyclic

    while no_outgoing:
        node = no_outgoing.pop()
        # TODO: fill this in.

def reverse_graph(g):
    rev = dict()
    for head in g:
        rev[head] = []

    for head, tail in g.items():
        rev[tail].append(head)

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
            g[int(parts[0])].append((parts[1]))

    return g

class TestAdd(unittest.TestCase):
    def test_trivial(self):
        self.assertEqual(True,True)
        self.assertEqual(False,False)

    def test_rosalind_sample(self):
        g = load_graph('rosalind_ts.txt')
        self.assertEqual(len(g), 4)
        self.assertEqual(len(g[1]), 1)
        self.assertEqual(len(g[2]), 0)
        self.assertEqual(len(g[4]), 2)
        
        

if __name__ == '__main__':
    unittest.main()
        

from collections import defaultdict
import os
import sys

sys.path.append(os.path.abspath("../common"))
from common import Fasta

heads = defaultdict(list)

def grph(f):
    fastas = Fasta(f)
    for name, data in fastas:
        heads[data[0:3]].append(name)
    fastas.reset()

    for name, data in fastas:
        for name2 in heads[data[-3:]]:
            if (name != name2):
                print("{} {}".format(name, name2))

with open('/Users/visualstudio/Downloads/rosalind_grph.txt') as f:
    grph(f)

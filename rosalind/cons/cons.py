import os
import sys

sys.path.append(os.path.abspath("../common"))
from common import Fasta

def increment_count(data, count):
    for i in range(len(data.rstrip())):
        count[data[i]][i] += 1

def display_letter_count(letter, count):
    count_str = [str(x) for x in count[letter]]
    count_joined = ' '.join(count_str)
    print("{}: {}".format(letter, count_joined))


def cons(f):
    fastas = Fasta(f)
    name, data = next(fastas)

    count = {}
    count['A'] = [0] * len(data)
    count['C'] = [0] * len(data)
    count['T'] = [0] * len(data)
    count['G'] = [0] * len(data)

    # print(name)
    increment_count(data, count)
    # TODO: how do you create an iterator in Python?
    for name, data in fastas:
        increment_count(data, count)

    most_common = ""
    for i in range(len(count['A'])):
        most_common_ch = ""
        most_common_count = 0
        for letter in ['A', 'C', 'T', 'G']:
            if count[letter][i] > most_common_count:
                most_common_ch = letter
                most_common_count = count[letter][i]
        most_common += most_common_ch

    print(most_common)
    for letter in ['A', 'C', 'T', 'G']:
        display_letter_count(letter, count)

with open('/Users/visualstudio/Downloads/rosalind_cons.txt') as f:
    cons(f)

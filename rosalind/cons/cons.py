class Fasta:
    def __init__(self, file):
        self.file = file

    def __iter__(self):
        return self

    def __next__(self):
        name, data = Fasta.read_fasta(f)
        if name == "":
            raise StopIteration
        return name, data

    def read_fasta(f):
        name = f.readline().rstrip()[1:]
        data = ""

        # Loop until we run into the next name or the file is finished. If we
        # ran into the next name, rewind so that the next time we're called we
        # get the start of the name.
        while True:
            ch = f.read(1)
            if not ch:
                break
            if ch == '>':
                f.seek(f.tell()-1)
                break
            data += ch
            data += f.readline().rstrip()
        return name, data

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

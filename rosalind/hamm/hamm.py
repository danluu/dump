def hamm(s1, s2):
    assert len(s1) == len(s2)
    distance = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            distance += 1
    return distance

s1 = "GAGCCTACTAACGGGAT"
s2 = "CATCGTAATGACGGCCT"

assert hamm(s1, s2) == 7

with open('/Users/visualstudio/Downloads/rosalind_hamm.txt') as f:
    s1 = f.readline()
    s2 = f.readline()
    print(hamm(s1, s2))

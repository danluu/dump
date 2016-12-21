def revc(dna):
    rev = ""
    for x in reversed(dna):
        if (x == 'A'):
            rev += 'T'
        elif (x == 'T'):
            rev += 'A'
        elif (x == 'C'):
            rev += 'G'
        elif (x == 'G'):
            rev += 'C'
    return rev

assert revc('AAAACCCGGT') == 'ACCGGGTTTT'

with open('/Users/visualstudio/Downloads/rosalind_revc.txt') as f:
    line = f.readline()
    print(revc(line))

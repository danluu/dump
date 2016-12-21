def rna(dna):
    return dna.replace('T', 'U')

assert rna('GATGGAACTTGACTACGTAAATT') == 'GAUGGAACUUGACUACGUAAAUU'

with open('/Users/visualstudio/Downloads/rosalind_rna.txt') as f:
    line = f.readline()
    print(rna(line))

def dna(dd):
    count = [0, 0, 0, 0]
    sum_count = 0
    for cc in dd:
        sum_count += 1
        if cc == 'A':
            count[0] += 1
        elif cc == 'C':
            count[1] += 1
        elif cc == 'G':
            count[2] += 1
        elif cc == 'T':
            count[3] += 1
        else:
            print(cc)

    result = ' '.join(str(x) for x in count)
    print(sum_count)
    print(sum(count))
    print(result)

dna('AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC')

with open('/Users/visualstudio/Downloads/rosalind_dna.txt') as f:
    line = f.readline()
    dna(line)

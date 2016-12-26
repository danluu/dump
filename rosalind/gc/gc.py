def gc_content(dna):
    gc_count = 0
    other_count = 0
    for x in dna:
        if (x == 'C' or x == 'G'):
            gc_count += 1
        elif(x == 'A' or x == 'T'):
            other_count += 1
    return gc_count, other_count

def gc(ss):
    lines = ss.split()
    gc_total = 0
    other_total = 0
    highest_gc_perc = 0.0
    highest_name = ""
    current_name = ""
    for l in lines:
        # print(l)
        if l[0] == '>':
            print("NAME {}".format(current_name))
            if (gc_total > 0):
                gc_perc = gc_total / (other_total + gc_total)
                if gc_perc > highest_gc_perc:
                    print("New winner {} {}".format(current_name, gc_perc))
                    highest_gc_perc = gc_perc
                    highest_name = current_name
                else:
                    print("Loser {} {}".format(current_name, gc_perc))
            gc_total = 0
            other_total = 0
            current_name = l[1:]
        else:
            gc_count, other_count = gc_content(l)
            gc_total += gc_count
            other_total += other_count
            # print(gc_count, other_count)
            # print(gc_total, other_total)

    if (gc_total > 0):
        gc_perc = gc_total / (other_total + gc_total)
        if gc_perc > highest_gc_perc:
            print("New winner {} {}".format(current_name, gc_perc))
            highest_gc_perc = gc_perc
            highest_name = current_name
        else:
            print("Loser {} {}".format(current_name, gc_perc))
    return highest_name, highest_gc_perc * 100

sample = """>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT"""

assert gc_content("AGCTATAG") == (3, 5)
assert gc_content("GGGG") == (4, 0)
assert gc_content("CCCCC") == (5, 0)
assert gc_content("AACC") == (2, 2)
assert gc_content("ACAC") == (2, 2)
assert gc_content("CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC") == (37,23)
assert gc_content("TGGGAACCTGCGGGCAGTAGGTGGAAT") == (16, 11)
top = 37+16
bot = 23 + 11 + top

# print(gc(sample))

with open('/Users/visualstudio/Downloads/rosalind_gc.txt') as f:
    all = f.read()
    name, num = gc(all)
    print(name)
    print(num)

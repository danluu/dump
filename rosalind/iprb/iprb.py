# Probability of producing a dominant gene = 1 - probability of two recessive genes.
def iprb(dd, dr, rr):
    # Note that pairs of a group with themselves are divided by two.
    # If we have A_0 A_1 as one group and B_0 B_1 as another group,
    # (A_0,A_1) is the same as (A_1,A_0).
    total = dd*(dd-1)/2 + dd*dr + dd*rr +\
            dr*(dr-1)/2 + dr*rr +\
            rr*(rr-1)/2
    recessive = rr*(rr-1)/2 + (dr*rr)/2 + (dr*(dr-1))/8
    pdom = 1 - recessive / total
    return pdom

# print(iprb(20, 20, 20))


with open('/Users/visualstudio/Downloads/rosalind_iprb.txt') as f:
    line = f.readline()
    numbers = [int(i) for i in line.split()]
    print(iprb(*numbers))

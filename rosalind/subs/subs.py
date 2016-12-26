# Naive n^2 substring

def subs(ss, tt):
    results = []
    for i in range(len(ss)):
        if subs_helper(ss, tt, i):
            results.append(i+1)
    return results

def subs_helper(ss, tt, ii):
    for i in range(len(tt)):
        if ii+i >= len(ss):
            return False
        if ss[ii+i] != tt[i]:
            return False
    return True

assert subs('GATATATGCATATACTT', 'ATAT') == [2, 4, 10]

with open('/Users/visualstudio/Downloads/rosalind_subs.txt') as f:
    line0 = f.readline().rstrip()
    line1 = f.readline().rstrip()
    result = subs(line0, line1)
    str_result = [str(x) for x in result]
    print(' '.join(str_result))

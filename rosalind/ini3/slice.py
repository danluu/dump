def rosalind_slice(ss, aa, bb, cc, dd):
    return ss[aa: bb+1] + ' ' + ss[cc:dd+1]

print(rosalind_slice('HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain.', 22, 27, 97, 102))

with open('/Users/visualstudio/Downloads/rosalind_ini3.txt') as f:
    line = f.readline()
    line2 = f.readline()
    a, b, c, d = line2.split()
    print(rosalind_slice(line, int(a), int(b), int(c), int(d)))

def sum_squares(a, b):
    return a**2 + b**2

print(sum_squares(3, 5))

with open('/Users/visualstudio/Downloads/rosalind_ini2.txt') as f:
    line = f.readline()
    a, b = line.split()
    print(sum_squares(int(a), int(b)))

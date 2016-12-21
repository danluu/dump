def fib(nn, kk):
    x0 = 1
    x1 = 1
    for i in range(nn-2):
        temp = x1
        x1 = kk * x0 + x1
        x0 = temp
    return x1

assert fib(5, 3) == 19

with open('/Users/visualstudio/Downloads/rosalind_fib.txt') as f:
    line = f.readline()
    a, b = line.split()
    print(fib(int(a), int(b)))

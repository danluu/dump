def parent(i):
    # print("p {}:{}".format(i, ((i+1) // 2) - 1))
    return ((i+1) // 2) - 1

def swap(a, i, j):
    a[i], a[j] = a[j], a[i]

def bubble_up(a, i):
    # print(a)
    while i > 0:
        p = parent(i)
        if a[p] < a[i]:            
            # print("bubble {} -- {}:{}".format(i, p, i))
            swap(a, p, i)
            # print(a)
            i = p
        else:
            return
        
def solve(a):
    # print(a)
    # for i in range(len(a)-1, -1, -1):
    for i in range(len(a)):
        bubble_up(a, i)
    return a

# with open('rosalind_hea.txt') as f:
with open('/Users/danluu/Downloads/rosalind_hea.txt') as f:
    num = int(f.readline())
    raw_a = f.readline().split()
    assert(num == len(raw_a))
    a = [int(x) for x in raw_a]
    res = solve(a)
    print(' '.join([str(x) for x in res]))

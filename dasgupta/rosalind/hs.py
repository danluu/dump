def parent(i):
    # print("p {}:{}".format(i, ((i+1) // 2) - 1))
    return ((i+1) // 2) - 1

def children(i):
    return [2*i + 1, 2*i + 2]

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

# Note: could refactor compare and swap code into single fn.
def sift_down(a, i):
    while 2*i+1 < len(a):
        if 2*i+1 == len(a) - 1:
            if a[2*i+1] > a[i]:
                swap(a, 2*i+1, i)
                i = 2*i+1
            else:
                return
        elif 2*i+2 < len(a):
            if a[2*i+1] > a[2*i+2]:
                if a[2*i+1] > a[i]:
                    swap(a, 2*i+1, i)
                    i = 2*i+1
                else:
                    return
            else:
                if a[2*i+2] > a[i]:
                    swap(a, 2*i+2, i)
                    i = 2*i+2
                else:
                    return

def is_heap(a):
    for i in range(1,len(a)):
        if a[parent(i)] < a[i]:
            print(a)
            print('heap violation {}:{} -- {}:{}'.format(i, parent(i), a[i], a[parent(i)]))
            return False
    return True

def insert(a, x):
    a.append(x)
    bubble_up(a, len(a) - 1)
    # assert(is_heap(a))

def remove(a):
    swap(a, 0, len(a) - 1)
    item = a.pop()
    sift_down(a, 0)
    # assert(is_heap(a))
    return item
    

def solve(inp):
    a = []
    result = []
    for x in inp:
        insert(a, x)
    while a:
        result.append(remove(a))

    for x in reversed(result):
        print(str(x) + ' ',end='')
    
        

# with open('rosalind_hs.txt') as f:
with open('/Users/danluu/Downloads/rosalind_hs.txt') as f:
    num_elements = int(f.readline().strip())
    inp = [int(x) for x in  f.readline().split(' ')]
    assert(len(inp) == num_elements)

    solve(inp)

    
        

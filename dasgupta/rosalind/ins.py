def read_data():
    # with open('rosalind_ins.txt') as f:
    with open('/home/danluu/Downloads/rosalind_ins.txt') as f:
        n = int(f.readline())
        l = f.readline().split()
        assert(n == len(l))
        res = [int(x) for x in l]
    return res

def swap(a,i,j):
    tmp = a[i]
    a[i] = a[j]
    a[j] = tmp

def count_ins(a):
    num_swaps = 0
    for i in range(1,len(a)):
        k = i
        while k > 0 and a[k] < a[k-1]:
            swap(a,k-1,k)
            num_swaps += 1
            k -= 1
    return num_swaps


a = read_data()
print(count_ins(a))
        
    

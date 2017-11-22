def merge(raw0, raw1):
    a0 = ms(raw0)
    a1 = ms(raw1)
    
    res = []

    i0 = 0
    i1 = 0
    
    while i0 < len(a0) or i1 < len(a1):
        if i0 >= len(a0):
            res.append(a1[i1])
            i1 += 1
        elif i1 >= len(a1):
            res.append(a0[i0])
            i0 += 1
        elif a1[i1] < a0[i0]:
            res.append(a1[i1])
            i1 += 1
        else:
            res.append(a0[i0])
            i0 += 1
            
    return res

def ms(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    return merge(arr[:mid],arr[mid:])

with open('rosalind_inv.txt') as f:
    num_entries = int(f.readline().strip())
    arr = [int(x) for x in f.readline().strip().split(' ')]

print(arr)
print(ms(arr))

def swap(aa, i, j):
    tmp = aa[i]
    aa[i] = aa[j]
    aa[j] = tmp

def partition(aa):
    cur = 1
    gt_ptr = len(aa)

    target = aa[0]

    while cur < gt_ptr:
        if aa[cur] <= target:
            cur += 1
        else:
            gt_ptr -= 1
            swap(aa, cur, gt_ptr)

    swap(aa, 0, cur-1)
    return aa

# print(partition([3,1,2,4,5,6]))
# print(partition([3,6,5,4,2,1]))
# print(partition([7,2,5,6,1,3,9,4,8]))

with open('/Users/danluu/Downloads/rosalind_par.txt') as f:
    num_entries = f.readline().strip()
    line = f.readline().strip()
    aa = [int(x) for x in line.split(' ')]
    # assert(len(aa) == num_entries)

    with open('/Users/danluu/Downloads/par_result.txt','w') as outf:        
        int_res = partition(aa)
        res = ' '.join([str(x) for x in int_res])
        print(res, file=outf)

        

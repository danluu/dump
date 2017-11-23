def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp

    return arr

def rotate(arr, i, j, k):
    tmp = arr[k]
    arr[k] = arr[j]
    arr[j] = arr[i]
    arr[i] = tmp

    return arr

def partition(arr):
    low = 0
    mid = 0
    hgh = 1

    while hgh < len(arr) - 1:
        nxt = hgh + 1
        if arr[nxt] == arr[low]:
            swap(arr, mid + 1, nxt)
            # print('swap {}'.format(arr))
            mid += 1
        elif arr[nxt] > arr[low]:
            pass
        elif arr[nxt] < arr[low]:
            rotate(arr, low, mid + 1, nxt)
            # print('rotate {}'.format(arr))
            low += 1
            mid += 1
        else:
            assert(False)

        hgh += 1
    

# with open('rosalind_par3.txt') as f:
with open('/home/danluu/Downloads/rosalind_par3.txt') as f:
    num_elements = int(f.readline().strip())
    arr = [int(x) for x in f.readline().strip().split(' ')]
    assert(num_elements) == len(arr)

# print(arr)
partition(arr)
print(' '.join([str(x) for x in arr]))


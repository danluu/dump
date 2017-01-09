import math

def perm(xx):
    print(math.factorial(xx))
    input = list(range(1, xx+1))
    perm_helper(input, [])

def perm_helper(input, result):
    # print("{}:{}".format(input, result))
    if input == []:
        print(' '.join(str(x) for x in result))
    else:
        for i in range(len(input)):
            head = input[:i]
            tail = input[i+1:]
            joined = head + tail
            result_copy = result[:]
            result_copy.append(input[i])
            perm_helper(joined, result_copy)

perm(7)

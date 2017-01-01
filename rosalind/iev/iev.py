def iev(input):
    transfer = [2, 2, 2, 1.5, 1, 0]

    str_weights = input.split(' ')
    weights = [int(x) for x in str_weights]
    sum = 0.0
    for i in range(len(weights)):
        sum += weights[i] * transfer[i]
    return sum

assert iev("1 0 0 1 0 1") == 3.5

with open('/Users/visualstudio/Downloads/rosalind_iev.txt') as f:
    line = f.readline()
    print(iev(line))

import collections

# Create a set of inverse of all numbers in xs.
# For every pair of numbers, check to see if the pair sums to inverse of any number.
def solve(xs):
    candidates = collections.defaultdict(list)
    for i in range(len(xs)):
        candidates[-xs[i]].append(i)

    for i in range(len(xs)):
        for j in range(len(xs)):
            if i != j and (xs[i] + xs[j]) in candidates:
                return "{} {} {}".format(i+1,
                                         j+1,
                                         candidates[xs[i]+xs[j]][0]+1)
               

    return -1

# with open('rosalind_3sum.txt') as f:
with open('/Users/danluu/Downloads/rosalind_3sum.txt') as f:
    num_lines_s, num_entries_per_line_s = f.readline().strip().split(' ')
    num_lines = int(num_lines_s)
    num_entries_per_line = int(num_entries_per_line_s)
    for line in f:
        num_lines -= 1
        numbers = [int(x) for x in line.strip().split(' ')]
        assert(len(numbers) == num_entries_per_line)
        print(solve(numbers))

    assert(num_lines == 0)


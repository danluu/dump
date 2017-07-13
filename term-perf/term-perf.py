import collections
import csv
import math
import os
import sys

def sort_results(raw_results):
    for name in raw_results:
        raw_results[name].sort()

def get_results_by_type(fname):
    raw_results = collections.defaultdict(list)
    with open(fname) as csvf:
        reader = csv.reader(csvf)
        header = next(reader)
        for row in reader:
            for i in range(len(header)):
                name = header[i]
                raw_results[name].append(float(row[i]))

    sort_results(raw_results)
    return raw_results

def get_min_max(raw_results):
    max_val = 0
    min_val = float('inf')
    for name in raw_results:
        for value in raw_results[name]:
            if value > max_val:
                max_val = value
            if value < min_val:
                min_val = value
    return min_val, max_val

def output_csv(raw_results):
    print("latency.ms, terminal")
    for name in raw_results:
        for value in raw_results[name]:
            print("{},{}".format(value, name))

def float_range(start, stop, step):
    assert step > 0.0
    total = start
    compo = 0.0
    while total < stop:
        yield total
        y = step - compo
        temp = total + y
        compo = (temp - total) - y
        total = temp

def output_percentile(raw_results, filename):
    with open(filename,'w') as f:
        f.write("nines,latency.ms,terminal\n")
        for name in raw_results:
            total = len(raw_results[name])
            i = 0
            delta = 0.01
            percentile_50th = 0.3
            for x in float_range(percentile_50th, 3.0 + delta, delta):
                cur_fraction = percentile(x) * total
                while i < cur_fraction:
                    i += 1
                f.write("{},{},{}\n".format(x,raw_results[name][i],name))
                # print("DEBUG: i {} cur_fraction {} percentile {}".format(i,cur_fraction,percentile(x)))

# (10**x - 1) / (10**x)
def p90_percentile(x):
    # assert(x >= 1.0)
    tentox = math.pow(10, x)
    return (tentox - 1) / tentox

def interpolate_percentile(x):
    assert(x <= 1.0)
    return 0.9 * x

# log scale for p90 and above
# currently linear for 0 to 90, but it should probably also be log.
def percentile(x):
    return p90_percentile(x)
    # if x >= 1.0:
    #     return p90_percentile(x)
    # else:
    #     return interpolate_percentile(x)

input_fname = sys.argv[1]
no_extension = os.path.splitext(input_fname)[0]
output_fname = no_extension + "-percentile.csv"
    
raw_results = get_results_by_type(input_fname)
# output_csv(raw_results)
output_percentile(raw_results, output_fname)

# print(p90_percentile(1))
# print(p90_percentile(2))
# print(p90_percentile(3))


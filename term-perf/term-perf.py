import collections
import csv

def get_results_by_type():
    raw_results = collections.defaultdict(list)
    with open('results.csv') as csvf:
        reader = csv.reader(csvf)
        header = next(reader)
        for row in reader:
            for i in range(len(header)):
                name = header[i]
                raw_results[name].append(float(row[i]))
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
    print("latency (ms), terminal")
    for name in raw_results:
        for value in raw_results[name]:
            print("{},{}".format(value, name))
    
raw_results = get_results_by_type()
output_csv(raw_results)


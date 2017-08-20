import csv

# Take a branch prediction accuracy and return the cpi
# Assumes 80% non-branch, 20% branch
# CPI 1 for non-branch or correctly predicted branch
# CPI 20 for incorrectly predicted branch
def cpi(pct):
    return (0.8 + 0.2 * pct) + 0.2 * (1 - pct) * 20

def show_list():
    with open('input.csv') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        for row in reader:
            scheme = row[0]
            pct = float(row[1])
            cycles = cpi(pct)
            print("{},{},{}".format(scheme,pct,cycles))


show_list()        

import csv

# Take a branch prediction accuracy and return the cpi
# Assumes 80% non-branch, 20% branch
# CPI 1 for non-branch or correctly predicted branch
# CPI 20 for incorrectly predicted branch
def cpi(pct):
    return (0.8 + 0.2 * pct) + 0.2 * (1 - pct) * 20

# Position in plot
# No prediction (4.8 cpi) is at absolute position 200
# Perfect prediction (1.0 cpi) is at absolute position 1200
def position(cpi):
    base = 200
    offset = (cpi - 4.8) * (1000 / -3.8)
    return base + offset

def show_list():
    with open('input.csv') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        for row in reader:
            scheme = row[0]
            pct = float(row[1])
            cycles = cpi(pct)
            pixel = position(cycles)
            print("{},{},{},{}".format(scheme,pct,cycles,pixel))


show_list()        

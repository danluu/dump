import collections
import csv
import datetime
import math

release_date = {}
share = collections.defaultdict(dict)

average_month = 30.44
first_date = datetime.datetime.strptime('2009-02-09', '%Y-%m-%d')
last_date = datetime.datetime.strptime('2017-10-02', '%Y-%m-%d')
date_range = last_date - first_date
max_buckets = math.ceil((date_range.days + 1) / average_month)

buckets = collections.defaultdict(lambda: [0.0] * max_buckets)
max_months_seen = 0

with open('version-history.csv') as vh_file:
    vh_reader = csv.reader(vh_file)
    for row in vh_reader:
        date = datetime.datetime.strptime(row[1], "%Y-%m-%d")
        version = int(row[0])
        release_date[version] = date

with open('historical-share.csv') as hs_file:
    hs_reader = csv.DictReader(hs_file)
    for row in hs_reader:
        if row['date'] == '':
            continue
        date = datetime.datetime.strptime(row['date'], "%Y-%m-%d")
        for version in row:
            if version != 'date':
                share[date][int(version)] = float(row[version])

# Convert from input data to ggplot2 friendly format.
for date in share:
    for version in share[date]:
        if version < len(release_date):
            maybe_age = date - release_date[version+1]
            if (maybe_age < datetime.timedelta(0)):
                age = datetime.timedelta(0)
            else:
                age = maybe_age
        else:
            age = datetime.timedelta(0)
        current_share = share[date][version]
        # if age < datetime.timedelta(0):
        #     assert(current_share == 0.0)
        #     continue

        bidx = math.floor(age.days / average_month)
        buckets[date][bidx] += current_share

sp_header = ['date','months','percent']
with open('share-plot.csv','w') as sp_file:
    sp_writer = csv.writer(sp_file)
    sp_writer.writerow(sp_header)
    for date, row in buckets.items():
        for i in range(len(row)):
            sp_writer.writerow([date, i, row[i]])
            if row[i] > 0.0 and i > max_months_seen:
                max_months_seen = i
                
print('max age seen: {}'.format(max_months_seen))

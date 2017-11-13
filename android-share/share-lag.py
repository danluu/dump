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

# dict of [date][age] = share
share_buckets = collections.defaultdict(lambda: [0.0] * max_buckets)
cumulative_share_buckets = collections.defaultdict(lambda: [0.0] * max_buckets)
max_months_seen = 0


p_consts = [50.0,75.0,95.0,99.0]
# dict of [percentile][date] = age
percentiles = collections.defaultdict(dict)

# dict of [date][percentile] = age
date_consts = [datetime.datetime.strptime('2010-01-01', '%Y-%m-%d'),
#               datetime.datetime.strptime('2011-01-01', '%Y-%m-%d'),
               datetime.datetime.strptime('2012-01-01', '%Y-%m-%d'),
#               datetime.datetime.strptime('2013-01-01', '%Y-%m-%d'),
               datetime.datetime.strptime('2014-01-01', '%Y-%m-%d'),
#               datetime.datetime.strptime('2015-01-01', '%Y-%m-%d'),
               datetime.datetime.strptime('2016-01-01', '%Y-%m-%d')]
age_by_date = collections.defaultdict(lambda: [0.0] * 100)

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

        if current_share > 0.0:
            bidx = math.floor(age.days / average_month)
            share_buckets[date][bidx] += current_share

            for i in range(bidx, len(cumulative_share_buckets[date])):
                cumulative_share_buckets[date][i] += current_share

# Compute age of various percentiles.
for p in p_consts:
    for date in cumulative_share_buckets:
        current_cumulative = 0.0
        last_cumulative = 0.0
        for i in range(len(cumulative_share_buckets[date])):
            # Consider adding multi-level break
            current_cumulative = cumulative_share_buckets[date][i]
            if current_cumulative > p and last_cumulative <= p:

                # Linear interpolation to find estimated age.
                fraction = (p - last_cumulative) / (current_cumulative - last_cumulative)
                estimated_age = i-1 + fraction
                # print(date, p, i-1, last_cumulative, i, current_cumulative, estimated_age)
                assert(estimated_age >= i-1)
                assert(estimated_age < i)
                percentiles[p][date] = estimated_age

            last_cumulative = current_cumulative

# Compute ages at various dates.
for d in date_consts:
    prev_date = first_date
    for date in cumulative_share_buckets:
        delta = date -d
        if delta < datetime.timedelta(days=30) and delta > datetime.timedelta(0):
            max_upper_bound = 0
            max_age = 0
            prev_share = 0.0
            for age in range(len(cumulative_share_buckets[date])):
                cur_share = cumulative_share_buckets[date][age]
                if (cur_share > prev_share):
                    lower_bound = math.floor(prev_share)
                    upper_bound = math.floor(cur_share)
                    max_upper_bound = upper_bound
                    max_age = age
                    for p in range(lower_bound, upper_bound):
                        age_by_date[d][p] = age

                prev_share = cur_share
            if max_upper_bound < 100:
                for p in range(max_upper_bound, 100):
                    age_by_date[d][p] = max_age

            print(d, max_upper_bound)

        prev_date = date


# Write date, age, share in fully normalized form.
sp_header = ['date','age','percent']
with open('share-plot.csv', 'w') as sp_file:
    sp_writer = csv.writer(sp_file)
    sp_writer.writerow(sp_header)
    for date, row in share_buckets.items():
        for i in range(len(row)):
            sp_writer.writerow([date, i, row[i]])
            if row[i] > 0.0 and i > max_months_seen:
                max_months_seen = i

pp_header = ['percentile','date','age']
with open('percentile-plot.csv', 'w') as pp_file:
    pp_writer = csv.writer(pp_file)
    pp_writer.writerow(pp_header)
    for p, row in percentiles.items():
        for date, age in row.items():
            pp_writer.writerow([p, date, age])

dp_header = ['date','percentile','age']
with open('date-plot.csv', 'w') as dp_file:
    dp_writer = csv.writer(dp_file)
    dp_writer.writerow(dp_header)
    for date, row in age_by_date.items():
        for p in range(len(row)):
            age = row[p]
            dp_writer.writerow([date, p, age])
                
print('max age seen: {}'.format(max_months_seen))
# print(cumulative_share_buckets)
# print(percentiles)
# print(age_by_date)

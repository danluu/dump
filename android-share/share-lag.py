import collections
import csv
import datetime


release_date = {}
share = collections.defaultdict(dict)

with open('version-history.csv') as vh_file:
    vh_reader = csv.reader(vh_file)
    for row in vh_reader:
        date = datetime.datetime.strptime(row[1], "%Y-%m-%d")
        version = row[0]
        release_date[version] = date

print(release_date)

with open('historical-share.csv') as hs_file:
    hs_reader = csv.DictReader(hs_file)
    for row in hs_reader:
        if row['date'] == '':
            continue
        date = datetime.datetime.strptime(row['date'], "%Y-%m-%d")
        for version in row:
            if version != 'date':
                share[date][version] = row[version]


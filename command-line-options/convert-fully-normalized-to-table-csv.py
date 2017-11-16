import collections
import csv

table_prep = collections.defaultdict(dict)
commands = []
versions = ['v7 unix','slackware 3.1','ubuntu 12','ubuntu 17']

with open('popular-cortesi.csv') as f:
    for line in f:
        commands.append(line.strip())

with open('results.combined') as f:
    reader = csv.reader(f)
    header = next(reader)
    assert(header == ['name','options','version'])

    for row in reader:
        command = row[0]
        num_options = row[1]
        version = row[2]

        table_prep[command][version] = num_options

with open('command-table.csv','w') as f:
    writer = csv.writer(f)    
    for command in commands:
        row = [command]
        for version in versions:
            row.append(table_prep[command][version])
        writer.writerow(row)
    

import csv

input_path = 'filesystems.csv'
# input_path = 'small-filesystems.csv'
with open(input_path) as f:
    reader = csv.reader(f)
    header = next(reader)
    body = [line for line in reader]

# TODO: if this script is ever re-used, don't hardcode color config.
color_map = {'':'black',
             'prop':'palegoldenrod',
             'fix':'green',
             'ignore':'crimson'}

print('<style>table {border-collapse:collapse;margin:0px auto;}table,th,td {border: 1px solid black;}td {text-align:center;}</style>')

print('<table>')
print('<tr>')
for hitem in header:
    print('<th>{}</th>'.format(hitem),end='')
print('</tr>')

for row in body:
    print('<tr>')
    for bitem in row:
        if bitem in color_map:
            print('<td bgcolor={}>{}</td>'.format(color_map[bitem],bitem),end='')
        else:
            print('<td>{}</td>'.format(bitem),end='')
    print('</tr>')
print('</table>')

import csv

input_path = '../command-line-options/command-table.csv'
# input_path = 'filesystems.csv'
# input_path = 'small-filesystems.csv'
with open(input_path) as f:
    reader = csv.reader(f)
    header = next(reader)
    body = [line for line in reader]

# TODO: if this script is ever re-used, don't hardcode color config.
# color_map = {
#    '':'gainsboro'}
color_map ={}

print('<style>table {border-collapse:collapse;margin:0px auto;}table,th,td {border: 1px solid black;}td {text-align:center;}</style>')

print('<table>')
# TODO: make this not a hack if this script is ever re-used
# print('<tr><th rowspan="3"></td><th colspan="3">2005</td><th colspan="6">2017</td></tr>')
print('<tr>')
for hitem in header:
    print('<th>{}</th>'.format(hitem),end='')
print('</tr>')
# print('<tr><th colspan="6">file</td><th colspan="3">mmap</td></tr>')

for row in body:
    print('<tr>')
    for bitem in row:
        if bitem in color_map:
            print('<td bgcolor={}>{}</td>'.format(color_map[bitem],bitem),end='')
        else:
            print('<td>{}</td>'.format(bitem),end='')
            # print('<th>{}</th>'.format(bitem),end='')
    print('</tr>')
print('</table>')

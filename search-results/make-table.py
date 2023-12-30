import csv

input_path = 're24-wide.csv'
with open(input_path) as f:
    reader = csv.reader(f)
    header = next(reader)
    body = [line for line in reader]

entry_values = {'Terrible', 'V. Bad', 'Bad', 'Ok', 'Good', 'Great'}

def flip_text_color(color):
    return color == '#67001f' or color == '#053061'

def value_to_color(value):
    lookup = {
        'Terrible': '#053061',
        'V. Bad': '#4393c3',
        'Bad': '#d1e5f0',
        'Ok': '#f7f7f7',
        'Good': '#d6604d',
        'Great': '#67001f',
    }
    # colors = ['#67001f','#b2182b','#d6604d','#f4a582','#fddbc7','#f7f7f7','#d1e5f0','#92c5de','#4393c3','#2166ac','#053061']

    return lookup[value]


print('<style>table {border-collapse:collapse;margin:0px auto;}table,th,td {border: 1px solid black;}td {text-align:center;}</style>')

print('<table>')
# print('<tr><th rowspan="3"></td><th colspan="3">2005</td><th colspan="6">2017</td></tr>')
print('<tr>')
for hitem in header:
    print('<th>{}</th>'.format(hitem),end='')
print('</tr>')
print('<tr><th>bases</th><th colspan="3">outs</th></tr>')
# print('<tr><th colspan="6">file</td><th colspan="3">mmap</td></tr>')

for row in body:
    print('<tr>')
    for bitem in row:
        if bitem in entry_values:
            color = value_to_color(bitem)
            if flip_text_color(color):
                print('<td bgcolor={}><font color=white>{}</font></td>'.format(color, bitem),end='')
            else:
                print('<td bgcolor={}>{}</td>'.format(color, bitem),end='')
        else:
            print('<th>{}</th>'.format(bitem),end='')

    print('</tr>')
print('</table>')

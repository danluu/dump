import csv

input_path = 're24-wide.csv'
with open(input_path) as f:
    reader = csv.reader(f)
    header = next(reader)
    body = [line for line in reader]

entry_values = {'Terrible', 'V. Bad', 'Bad', 'Ok', 'Good', 'Great'}

def flip_text_color(color):
    return color == '#67001f' or color == '#053061' or color == '#2166ac' or color == '#b2182b'

def value_to_color(value):
    lookup = {
        'Great': '#2166ac',
        'Good': '#4393c3',
        'Ok': '#d1e5f0',
        'Bad': '#fddbc7',
        'V. Bad': '#d6604d',
        'Terrible': '#b2182b',
    }
    # colors = ['#67001f','#b2182b','#d6604d','#f4a582','#fddbc7','#f7f7f7','#d1e5f0','#92c5de','#4393c3','#2166ac','#053061']

    return lookup[value]


print('<style>table {border-collapse:collapse;margin:1px 10px;}table,th,td {text-align:center;}</style>')
print('<table style=float:left>')
# print('<tr><th rowspan="3"></td><th colspan="3">2005</td><th colspan="6">2017</td></tr>')
print('<tr>')
for hitem in header:
    print('<th>{}</th>'.format(hitem),end='')
print('</tr>')

for row in body:
    print('<tr>')
    for bitem in row:
        if bitem in entry_values:
            color = value_to_color(bitem)
            if flip_text_color(color):
                print('<td bgcolor={}><font color=white>{}</font></td>'.format(color, bitem),end='')
            else:
                print('<td bgcolor={}><font color=black>{}</font></td>'.format(color, bitem),end='')
        else:
            print('<th>{}</th>'.format(bitem),end='')

    print('</tr>')
print('</table>')

import csv

input_path = 'sac-bunts.csv'
with open(input_path) as f:
    reader = csv.reader(f)
    header = next(reader)
    body = [line for line in reader]

def flip_text_color(color):
    return color == '#800026'

def value_to_color(value):
    colors = ['#ffffcc','#ffeda0','#fed976','#feb24c','#fd8d3c','#fc4e2a','#e31a1c','#bd0026','#800026']

    min_val = 925
    max_val = 1731

    max_idx = len(colors) - 1

    idx = int((max_idx / (max_val - min_val)) * (value - min_val))

    assert(idx >= 0)
    assert(idx <= max_idx)

    return colors[idx]
    

print('<style>table {border-collapse:collapse;margin:0px auto;}table,th,td {border: 1px solid black;}td {text-align:center;}</style>')

print('<div style="overflow-x:auto;">') # For wide table.
print('<table>')
print('<tr>')
for hitem in header:
    print('<th>{}</th>'.format(hitem),end='')
print('</tr>')

for row in body:
    print('<tr>')
    for bitem in row:
        try:
            value = float(bitem)
            color = value_to_color(value)
            if flip_text_color(color):
                print('<td bgcolor={}><font color=white>{}</font></td>'.format(color, bitem),end='')
            else:
                print('<td bgcolor={}>{}</td>'.format(color, bitem),end='')
        except ValueError:
            print('<th>{}</th>'.format(bitem),end='')

    print('</tr>')
print('</table>')
print('</div>') # For wide table.

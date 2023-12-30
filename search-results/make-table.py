import csv

# input_path = 're24.csv'
input_path = 're24-wide.csv'
with open(input_path) as f:
    reader = csv.reader(f)
    header = next(reader)
    body = [line for line in reader]

def flip_text_color(color):
    return color == '#67001f' or color == '#053061'

def value_to_color(value):
    colors = ['#67001f','#b2182b','#d6604d','#f4a582','#fddbc7','#f7f7f7','#d1e5f0','#92c5de','#4393c3','#2166ac','#053061']

    min_val = .117
    mid_val = .555
    max_val = 2.417

    mid_idx = 5
    max_idx = len(colors) - 1

    if value <= mid_val:
        idx = int((mid_idx / (mid_val - min_val)) * (value - min_val))
    else:
        idx = int(((max_idx - mid_idx) / (max_val - mid_val)) * (value - mid_val)) + mid_idx

    assert(idx >= 0)
    assert(idx <= max_idx)

    return colors[idx]


    

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

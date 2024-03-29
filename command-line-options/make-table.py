import csv
import math

input_path = 'command-table.csv'
with open(input_path) as f:
    reader = csv.reader(f)
    header = next(reader)
    body = [line for line in reader]

# TODO: if this script is ever re-used, don't hardcode color config.
# color_map = {
#    '':'gainsboro'}
color_map ={}

blue_colors = ['#f7fbff','#deebf7','#c6dbef','#9ecae1','#6baed6','#4292c6','#2171b5','#08519c','#08306b']
dark_colors = {'black','#800026','#525252','#252525','#2171b5','#08519c','#08306b','#006d2c','#00441b','#6a51a3','#54278f','#3f007d'}

def flip_text_color(color):
    return color in dark_colors

def log_color_scale(raw_value, min_val, max_val, colors):
    # colors = ['white','#f0f0f0','#d9d9d9','#bdbdbd','#969696','#737373','#525252','#252525','black']
    # print(raw_value)
    if raw_value == '0':
        return 'white'
    if raw_value == '':
        return 'silver'
    value = float(raw_value)
    if value > max_val:
        return 'black'

    lmin = math.log2(min_val)
    lmax = math.log2(max_val)
    lval = math.log2(value)

    max_idx = len(colors) - 1
        
    idx = int((max_idx / (lmax - lmin)) * (lval - lmin))
        
    assert(idx >= 0)
    assert(idx <= max_idx)
    
    return colors[idx]


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
    for idx, bitem in enumerate(row):
        if idx != 0:
            color = log_color_scale(bitem,1,85,blue_colors)
            if flip_text_color(color):
                print('<td bgcolor={}><font color=white>{}</font></td>'.format(color, bitem), end='')
            else:
                print('<td bgcolor={}><font color=black>{}</font></td>'.format(color, bitem),end='')
            # print('<td>{}</td>'.format(bitem),end='')
	        # print('<th>{}</th>'.format(bitem),end='')
        else:
            print('<td>{}</td>'.format(bitem), end='')
    print('</tr>')
print('</table>')

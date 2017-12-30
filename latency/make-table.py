import csv
import math
import re

number_matcher = re.compile('(\d*\.?\d*)')
dark_colors = {'black','#800026','#525252','#252525','#2171b5','#08519c','#08306b','#006d2c','#00441b','#6a51a3','#54278f','#3f007d'}

blue_colors = ['#f7fbff','#deebf7','#c6dbef','#9ecae1','#6baed6','#4292c6','#2171b5','#08519c','#08306b']
blue_colors.reverse()

green_colors =  ['#f7fcf5','#e5f5e0','#c7e9c0','#a1d99b','#74c476','#41ab5d','#238b45','#006d2c','#00441b']
green_colors.reverse()

purple_colors = ['#fcfbfd','#efedf5','#dadaeb','#bcbddc','#9e9ac8','#807dba','#6a51a3','#54278f','#3f007d']
purple_colors.reverse()

def flip_text_color(color):
    return color in dark_colors


def latency_to_color(value):
    colors = ['#ffffcc','#ffeda0','#fed976','#feb24c','#fd8d3c','#fc4e2a','#e31a1c','#bd0026','#800026']

    min_val = 30
    max_val = 180

    if value <= max_val:
        max_idx = len(colors) - 1

        idx = int((max_idx / (max_val - min_val)) * (value - min_val))

        assert(idx >= 0)
        assert(idx <= max_idx)

        return colors[idx]
    else:
        return 'black'

def log_color_scale(value, min_val, max_val, colors):
    # colors = ['white','#f0f0f0','#d9d9d9','#bdbdbd','#969696','#737373','#525252','#252525','black']

    if value != float('inf'):
        lmin = math.log2(min_val)
        lmax = math.log2(max_val)
        lval = math.log2(value)

        max_idx = len(colors) - 1
        
        idx = int((max_idx / (lmax - lmin)) * (lval - lmin))
        
        assert(idx >= 0)
        assert(idx <= max_idx)
    
        return colors[idx]
    else:
        return 'silver'

def remove_units(value):
    if value == '':
        return float('inf')

    match = number_matcher.match(value)

    raw_value = float(match.group(1))

    if value.endswith('MHz'):
        return raw_value * 1000000
    elif value.endswith('GHz'):
        return raw_value * 1000000000
    elif value.endswith('k'):
        return raw_value * 1000
    elif value.endswith('M'):
        return raw_value * 1000000
    elif value.endswith('G'):
        return raw_value * 1000000000
    else:
        return raw_value

def gross_main_body(input_path, output_path):
    with open(input_path) as f:
        reader = csv.reader(f)
        header = next(reader)
        body = [line for line in reader]

    with open(output_path, 'w') as outf:
        print('<style>table {border-collapse:collapse;margin:0px auto;}table,th,td {border: 1px solid black;}td {text-align:center;}td.l {text-align:left;}</style>',file=outf)

        print('<table>',file=outf)
        # print('<tr><th rowspan="3"></td><th colspan="3">2005</td><th colspan="6">2017</td></tr>')
        print('<tr>',file=outf)
        for hitem in header:
            print('<th>{}</th>'.format(hitem),end='',file=outf)
        print('</tr>',file=outf)
        # print('<tr><th colspan="6">file</td><th colspan="3">mmap</td></tr>')

        for row in body:
            print('<tr>',file=outf)
            reference = False
            for idx, bitem in enumerate(row):
                if bitem.startswith('http'):
                    continue
                if idx == 0:
                    if bitem == 'packet around the world' or bitem == 'packet':
                        print('<td class="l" bgcolor="silver">{}</td>'.format(bitem),end='',file=outf)
                        reference = True
                    else:
                        # Have a link in mobile table.
                        if len(row) >= 4 and row[3].startswith('http'):
                            item_text = '<a href="{}">{}</a>'.format(row[3], bitem)
                        elif len(row) >= 6 and row[5].startswith('http'):
                            item_text = '<a href="{}">{}</a>'.format(row[5], bitem)
                        else:
                            item_text = bitem
                        print('<td class="l">{}</td>'.format(item_text),end='',file=outf)
                elif idx == 1:
                    value = float(bitem)
                    color = latency_to_color(value)
                    if reference:
                        color = 'silver'
                    if flip_text_color(color):
                        print('<td bgcolor={}><font color=white>{}</font></td>'.format(color, bitem),end='',file=outf)
                    else:
                        print('<td bgcolor={}>{}</td>'.format(color, bitem),end='',file=outf)
                elif idx == 2:
                    if bitem == '':
                        color = 'silver'
                    else:
                        value = int(bitem)
                        color = log_color_scale(value,1977,2017,purple_colors)

                    if flip_text_color(color):
                        print('<td bgcolor={}><font color=white>{}</font></td>'.format(color, bitem),end='',file=outf)
                    else:
                        print('<td bgcolor={}>{}</td>'.format(color, bitem),end='',file=outf)
                elif idx == 3:
                    value = remove_units(bitem)
                    color = log_color_scale(value,1000000,4200000000,blue_colors)
                    if flip_text_color(color):
                        print('<td bgcolor={}><font color=white>{}</font></td>'.format(color, bitem),end='',file=outf)
                    else:
                        print('<td bgcolor={}>{}</td>'.format(color, bitem),end='',file=outf)
                elif idx == 4:
                    value = remove_units(bitem)
                    color = log_color_scale(value,3500,2000000000,blue_colors)
                    if flip_text_color(color):
                        print('<td bgcolor={}><font color=white>{}</font></td>'.format(color, bitem),end='',file=outf)
                    else:
                        print('<td bgcolor={}>{}</td>'.format(color, bitem),end='',file=outf)
                else:
                    print('<td>{}</td>'.format(bitem),end='',file=outf)

            print('</tr>',file=outf)
        print('</table>',file=outf)


input_path = 'computers.csv'
output_path = 'computer-latency.html'
gross_main_body(input_path, output_path)
input_path = 'mobile.csv'
output_path = 'mobile-latency.html'
gross_main_body(input_path, output_path)

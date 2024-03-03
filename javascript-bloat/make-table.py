import csv
import math
import pprint
import re


COLOR_RANGE_EXTEND = False
RED_BALANCE = True

number_matcher = re.compile('(\d*\.?\d*)')
# TODO: need to add dark reds, should just make from scratch instead of using whatever's here.
dark_colors = {'black','#800026','#525252','#252525','#2171b5','#08519c','#08306b','#006d2c','#00441b','#6a51a3','#54278f','#3f007d'}

# light green to dark green
green_colors =  ['#f7fcf5','#e5f5e0','#c7e9c0','#a1d99b','#74c476','#41ab5d','#238b45','#006d2c','#00441b']

# light red to dark red
if (RED_BALANCE):
    red_colors = ['#fff5f0','#fee0d2','#fcbba1','#fc9272','#fb6a4a','#ef3b2c','#cb181d','#a50f15','#a50f15', '#a50f15', '#9B0D14', '#900A12', '#860811', '#71030E', '#67000d']
else:
    red_colors = ['#fff5f0','#fee0d2','#fcbba1','#fc9272','#fb6a4a','#ef3b2c','#cb181d','#a50f15','#67000d']    

def hex_to_rgb(value):
   value = value.lstrip('#')
   lv = len(value)
   return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

def rgb_to_hex(rgb):
   return '%02x%02x%02x' % rgb

# This should really use HSL or something instead of RGB.
def mean_color(color1, color2):
   rgb1 = hex_to_rgb(color1)
   rgb2 = hex_to_rgb(color2)

   avg = lambda x, y: round((x+y) / 2)

   new_rgb = ()

   for i in range(len(rgb1)):
      new_rgb += (avg(rgb1[i], rgb2[i]),)
       
   return rgb_to_hex(new_rgb)

def extend_color_range(colors):
    pprint.pprint(colors)
    more_colors = []
    for i in range(len(colors) - 1):
        more_colors.append(colors[i])
        if i < len(colors) - 2:
            more_colors.append(mean_color(colors[i], colors[i + 1]))
    return more_colors

pprint.pprint(red_colors)
if (COLOR_RANGE_EXTEND):
    red_colors = extend_color_range(red_colors)
    red_colors = extend_color_range(red_colors)
    red_colors = extend_color_range(red_colors)
    red_colors = extend_color_range(red_colors)
    red_colors = extend_color_range(red_colors)
    red_colors = extend_color_range(red_colors)
    
    green_colors = extend_color_range(green_colors)
    green_colors = extend_color_range(green_colors)
else:
    red_colors_size = extend_color_range(red_colors)  

    red_colors = extend_color_range(red_colors)
    red_colors = extend_color_range(red_colors)
    red_colors = extend_color_range(red_colors)

if (COLOR_RANGE_EXTEND):
    dark_colors = ['black'] + green_colors[-4:] + red_colors[-24:]
else:
    dark_colors = ['black'] + green_colors[-1:] + red_colors[-16:]

# make green run from dark to light
green_colors.reverse()

# dark red to light red to light green to dark green
red_green_colors = green_colors + red_colors
red_green_colors_size = green_colors + red_colors_size

# pprint.pprint(red_green_colors)

def flip_text_color(color):
    return color in dark_colors


def value_to_color(value, value_limits, colors):
    colors
    min_val = value_limits['min']
    max_val = value_limits['max']

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
    if value == '' or value == 'FAIL':
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
    elif value.endswith('kB'):
        return raw_value * 1024
    elif value.endswith('MB'):
        return raw_value * 1024 * 1024
    elif value.endswith('ms'):
        # Must be before s!!!
        return raw_value / 1000    
    elif value.endswith('s'):
        return raw_value
    else:
        return raw_value

# This table is a legacy format from when each column
# was normalized seperately. There's no reason to have this big table now.
value_limits = [ 
    None, # 0
    {'min': 6 * 1024, 'max': 9.3 * 1024 * 1024}, # 1, wire
    {'min': 18 * 1024, 'max': 21 * 1024 * 1024}, # 2, raw
    {'min': 50 / 1000, 'max': 30}, # 3, M3 LCP
    {'min': 20 / 1000, 'max': 30}, # 4, M3 CPU
    {'min': 50 / 1000, 'max': 30}, # 5, M1 LCP
    {'min': 20 / 1000, 'max': 30}, # 6, M1 CPU
    {'min': 50 / 1000, 'max': 30}, # 7, M3/10 LCP
    {'min': 20 / 1000, 'max': 30}, # 8, M3/10 CPU
    {'min': 50 / 1000, 'max': 30}, # 9, Tecno LCP
    {'min': 20 / 1000, 'max': 30}, # 10, Tecno CPU                        
    {'min': 50 / 1000, 'max': 30}, # 11, Itel LCP
    {'min': 20 / 1000, 'max': 30}, # 12, Itel CPU
]

def gross_main_body(input_path, output_path):
    with open(input_path) as f:
        reader = csv.reader(f)
        header_1 = next(reader)
        header_2 = next(reader)
        body = [line for line in reader]

    with open(output_path, 'w') as outf:
        print('<style>table {border-collapse:collapse;margin:0px auto;}table,th,td {border: 1px solid black;}td {text-align:center;}td.l {text-align:left;}</style>',file=outf)

        print('<table>',file=outf)
        # print('<tr><th rowspan="3"></td><th colspan="3">2005</td><th colspan="6">2017</td></tr>')
        print('<tr>',file=outf)
        for idx, hitem in enumerate(header_1):
            if idx == 0:
                print('<th>{}</th>'.format(hitem),end='',file=outf)
            else:
                if hitem == '':
                    continue
                else:
                    print('<th colspan="2">{}</th>'.format(hitem),end='',file=outf)
        print('</tr>',file=outf)
        # print('<tr><th colspan="6">file</td><th colspan="3">mmap</td></tr>')
        print('<tr>',file=outf)
        for hitem in header_2:
            print('<th>{}</th>'.format(hitem),end='',file=outf)
        print('</tr>',file=outf)        

        for row in body:
            print('<tr>',file=outf)
            # This loop is a very silly, vestigial, thing. We should either compute the min/max in this script or remove this loop entirely.
            for idx, bitem in enumerate(row):
                if bitem.startswith('http'):
                    continue
                if idx == 0:
                    # TODO: what is this class for?
                    print('<td class="l">{}</td>'.format(bitem),end='',file=outf)
                else:
                    value = remove_units(bitem)
                    if (idx <= 2):
                        color = value_to_color(value, value_limits[idx], red_green_colors_size)
                    else:
                        color = value_to_color(value,value_limits[idx], red_green_colors)
                    if flip_text_color(color):
                        print('<td bgcolor={}><font color=white>{}</font></td>'.format(color, bitem),end='',file=outf)
                    else:
                        print('<td bgcolor={}>{}</td>'.format(color, bitem),end='',file=outf)

            print('</tr>',file=outf)
        print('</table>',file=outf)


input_path = 'slow-device.csv'
output_path = 'slow-device.html'
gross_main_body(input_path, output_path)

import csv
import math
import re

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
            for bitem in row:
                print('<td>{}</td>'.format(bitem),end='',file=outf)

            print('</tr>',file=outf)
        print('</table>',file=outf)


input_path = 'datacenter.csv'
output_path = 'datacenter-cost.html'
gross_main_body(input_path, output_path)

import csv

with open('raw-reference/cfoi_rates_2018hb.csv') as ref_file:
    reader = csv.reader(ref_file, delimiter=',', quotechar='"')
    # name of profession is always row 0
    # code row may not exist, but will probabably be row 1 if it does exist.
    # injury rate column varies
    # Before we've seen a header row (which should start with "Characteristic", we'll skip all rows
    name_row = None
    code_row = None
    rate_row = None

    for row in reader:
        if name_row == None:
            if row[0] != ('Characteristic'):
                continue
            else:
                for i, part in enumerate(row):
                    if part == 'Characteristic':
                        name_row = i
                    if part == 'Characteristic code':
                        code_row = i
                    if part == 'Fatal injury rate3':
                        rate_row = i

                assert(name_row != None)
                assert(rate_row != None)
        else:
            if code_row != None:
                code = row[code_row]
                if len(code) == 0 or len(code) == 2 or ',' in code or ' ' in code:
                    continue

            name = row[name_row]
            rate = row[rate_row]

            print(name, rate)



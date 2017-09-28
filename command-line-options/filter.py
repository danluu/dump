

with open('popular-cortesi.csv') as f:
    targets_list = [line.strip() for line in f]
    targets = set(targets_list)

with open('results.all') as f:
    packages = {}
    for line in f:
        name,number = line.strip().split(',')

        # Overwrite if higher.
        if name in packages:
            if packages[name] <= number:
                packages[name] = number
        else:
            packages[name] = number

with open('filtered-cortesi.csv','w') as outf:
    # outf.write('command,num_options\n')
    outf.write('name,num_options\n')
    for name, num_options in packages.items():
        if name in targets:
            # outf.write("{},{}\n".format(name,num_options))
            outf.write("{},{}\n".format(name,num_options))
                
        

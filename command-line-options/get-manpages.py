import re

def get_available_mans():
    names = []
    
    filepattern = re.compile('a href="(.*)\.1\.gz"')

    with open('zesty.1.html') as f:
        for line in f:
            matched = filepattern.search(line)
            if matched != None:
                names.append(matched.group(1))
    return names


names = get_available_mans()
print(names)


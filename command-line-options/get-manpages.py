import re
import subprocess


def get_available_mans():
    names = set()
    
    filepattern = re.compile('a href="(.*)\.1\.gz"')

    with open('zesty.1.html') as f:
        for line in f:
            matched = filepattern.search(line)
            if matched != None:
                names.add(matched.group(1))
    return names


def get_commands():
    commands = []

    with open('popular-cortesi.csv') as f:
        for line in f:
            commands.append(line.strip())

    return commands

def find_man_path(name):
    result = subprocess.check_output(['find', '/usr/share/man/man1', '-name', '{}.*gz'.format(name)])
    return result.decode("utf-8").strip()

    

# names = get_available_mans()
commands = get_commands()

for c in commands:
    path = find_man_path(c)
    if path == "":
        print("FAIL",c)
    else:
        print(path)
    
    


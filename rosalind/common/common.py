

class Fasta:
    def __init__(self, file):
        self.file = file

    def __iter__(self):
        return self

    def __next__(self):
        name, data = self.read_fasta()
        if name == "":
            raise StopIteration
        return name, data


    def reset(self):
        self.file.seek(0)

    def read_fasta(self):
        name = self.file.readline().rstrip()[1:]
        data = ""

        # Loop until we run into the next name or the file is finished. If we
        # ran into the next name, rewind so that the next time we're called we
        # get the start of the name.
        while True:
            ch = self.file.read(1)
            if not ch:
                break
            if ch == '>':
                self.file.seek(self.file.tell()-1)
                break
            data += ch
            data += self.file.readline().rstrip()
        return name, data

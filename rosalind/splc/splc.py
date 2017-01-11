import os
import sys

sys.path.append(os.path.abspath("../common"))
from common import Fasta

# TODO: restructure code so we can use prot from prot.py
translate = {'UUU':'F',
'CUU':'L',
'AUU':'I',
'GUU':'V',
'UUC':'F',
'CUC':'L',
'AUC':'I',
'GUC':'V',
'UUA':'L',
'CUA':'L',
'AUA':'I',
'GUA':'V',
'UUG':'L',
'CUG':'L',
'AUG':'M',
'GUG':'V',
'UCU':'S',
'CCU':'P',
'ACU':'T',
'GCU':'A',
'UCC':'S',
'CCC':'P',
'ACC':'T',
'GCC':'A',
'UCA':'S',
'CCA':'P',
'ACA':'T',
'GCA':'A',
'UCG':'S',
'CCG':'P',
'ACG':'T',
'GCG':'A',
'UAU':'Y',
'CAU':'H',
'AAU':'N',
'GAU':'D',
'UAC':'Y',
'CAC':'H',
'AAC':'N',
'GAC':'D',
'UAA':'Stop',
'CAA':'Q',
'AAA':'K',
'GAA':'E',
'UAG':'Stop',
'CAG':'Q',
'AAG':'K',
'GAG':'E',
'UGU':'C',
'CGU':'R',
'AGU':'S',
'GGU':'G',
'UGC':'C',
'CGC':'R',
'AGC':'S',
'GGC':'G',
'UGA':'Stop',
'CGA':'R',
'AGA':'R',
'GGA':'G',
'UGG':'W',
'CGG':'R',
'AGG':'R',
'GGG':'G',
}

def prot(rna):
    result = ""
    for i in range(len(rna)//3):
        input = rna[i*3:i*3+3]
        local = translate[input]
        if local == 'Stop':
            break
        result += translate[input]
    return result


def splc(f):
    fastas = Fasta(f)
    _, dna = next(fastas)
    for _, intron in fastas:
        dna = dna.replace(intron,'')
    rna = dna.replace('T','U')
    protein = prot(rna)
    print(protein)


with open('/Users/visualstudio/Downloads/rosalind_splc.txt') as f:
    splc(f)

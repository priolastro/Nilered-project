import os
import re

path='/Users/salvatoreprioli/Desktop/sdu/nilered_PROJ/ElectrStr'


def get2pa(path):
    lista=[]
    for dirpath, dirname, filename in os.walk(path):
        if 'elecStruct' in dirpath:
            for file in filename:
                # if re.match(r'\w*.out', file) and re.match(r'^((?!Diff).)*$',file):
                if re.match(r'\w*.out', file) and re.match(r'^((?!Diff).)*$',file):
                    filepath=os.path.join(dirpath, file)
                    lista.append(filepath)
    return sorted(lista)


for file in get2pa(path):
    with open(file, 'r') as tpa:
        tpa_output=tpa.readlines()
        for i, line in enumerate(tpa_output):
            if '  Two-photon absorption summary' in line:
                    x=i+5
                    print(tpa_output[x])

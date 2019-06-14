import os
import re

def getOPTGSdiff_file(path='/Users/salvatoreprioli/Desktop/sdu/nilered_PROJ/ElectrStr/'):
    lista=[]
    for dirpath, dirname, filename in os.walk(path):
        if 'elecStruct' in dirpath and '.trash' not in dirpath and os.path.basename(dirpath)=='elecStruct':
            for file in filename:
                if re.match(r'\w*[1-8].log', file) or re.match(r'NileRedGS_OPT.log', file):
                    if re.match(r'\w*ES631.log', file):
                        continue
                    filepath=os.path.join(dirpath, file)
                    lista.append(filepath)
    return sorted(lista)

def getESdiff_file(path='/Users/salvatoreprioli/Desktop/sdu/nilered_PROJ/ElectrStr/'):
    lista=[]
    for dirpath, dirname, filename in os.walk(path):
        if 'elecStruct' in dirpath and '.trash' not in dirpath and os.path.basename(dirpath)=='elecStruct':
            for file in filename:
                if re.match(r'\w*[1-8]*ES.log', file):
                    filepath=os.path.join(dirpath, file)
                    lista.append(filepath)
    return sorted(lista)

def getOPTESdiff_file(path='/Users/salvatoreprioli/Desktop/sdu/nilered_PROJ/ElectrStr/'):
    lista=[]
    for dirpath, dirname, filename in os.walk(path):
        if 'elecStruct' in dirpath and '.trash' not in dirpath and os.path.basename(dirpath)=='elecStruct':
            for file in filename:
                if re.match(r'\w*[1-8]*ES_OPT.log', file):
                    filepath=os.path.join(dirpath, file)
                    lista.append(filepath)
    return sorted(lista)

def getTPAdiff_file(path='/Users/salvatoreprioli/Desktop/sdu/nilered_PROJ/ElectrStr/'):
    lista = []
    for dirpath, dirname, filename in os.walk(path):
        if 'elecStruct' in dirpath and '.trash' not in dirpath and os.path.basename(dirpath) == 'elecStruct':
            for file in filename:
                if re.match(r'2pa\w*Diff.out', file):
                    filepath = os.path.join(dirpath, file)
                    lista.append(filepath)
    return sorted(lista)


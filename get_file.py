import os
import re

def getOPTGSdiff_file(path):
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

def getESdiff_file(path):
    lista=[]
    for dirpath, dirname, filename in os.walk(path):
        if 'elecStruct' in dirpath and '.trash' not in dirpath and os.path.basename(dirpath)=='elecStruct':
            for file in filename:
                if re.match(r'\w*[1-8]*ES.log', file):
                    filepath=os.path.join(dirpath, file)
                    lista.append(filepath)
    return sorted(lista)

def getOPTESdiff_file(path):
    lista=[]
    for dirpath, dirname, filename in os.walk(path):
        if 'elecStruct' in dirpath and '.trash' not in dirpath and os.path.basename(dirpath)=='elecStruct':
            for file in filename:
                if re.match(r'\w*[1-8]*ES_OPT.log', file):
                    filepath=os.path.join(dirpath, file)
                    lista.append(filepath)
    return sorted(lista)

def getTPAdiff_file(path):
    lista = []
    for dirpath, dirname, filename in os.walk(path):
        if 'elecStruct' in dirpath and '.trash' not in dirpath and os.path.basename(dirpath) == 'elecStruct':
            for file in filename:
                if re.match(r'2pa\w*Diff.out', file):
                    filepath = os.path.join(dirpath, file)
                    lista.append(filepath)
    return sorted(lista)

def getES631_file(path):
    lista=[]
    for dirpath, dirname, filename in os.walk(path):
        if 'elecStruct' in dirpath and '.trash' not in dirpath and os.path.basename(dirpath)=='elecStruct':
            for file in filename:
                if re.match(r'\w*[1-8]*ES631.log', file):
                    filepath=os.path.join(dirpath, file)
                    lista.append(filepath)
    return sorted(lista)

def getTPA631_file(path):
    lista = []
    for dirpath, dirname, filename in os.walk(path):
        if 'elecStruct' in dirpath and '.trash' not in dirpath and os.path.basename(dirpath) == 'elecStruct':
            for file in filename:
                if re.match(r'2pa\w*.out', file) and 'Diff' not in file:
                    filepath = os.path.join(dirpath, file)
                    lista.append(filepath)
                    yield filepath
    return sorted(lista)

def PyframePath(path):
    for dirpath, dirname, filename in os.walk(path):
        if 'pyframe' in dirname:
            cartella=dirpath+'/pyframe'
            yield cartella

def take_single_file(file):
    for dirpath, dirname, filename in os.walk(file):
        if 'single' in dirpath:
            for element in filename:
                if re.match(r'' + re.escape('1PA') + '.*out', element):
                    path=os.path.join(dirpath, element)
                    yield path
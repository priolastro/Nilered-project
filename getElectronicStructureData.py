import get_dati
import get_file
from get_dict import *
from print_latex import *
from tqdm import tqdm
import numpy as np
import scientific_function

import re
import os

path='/Users/salvatoreprioli/Desktop/sdu/nilered_PROJ/ElectrStr/'




for file in get_file.PyframePath(path):
    wavelenght=[]
    oscillator=[]
    for element in get_file.take_single_file(file):
        wav, osc, tdip=get_dati.getData1PADalton(element)
        wavelenght.append(wav)
        oscillator.append(osc)
    print(file.split('/')[-2],',', np.average(wavelenght),',', scientific_function.nm(np.average(wavelenght)),',' , np.average(oscillator))

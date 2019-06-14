from get_dati import *
from get_file import *
from get_dict import *
from print_latex import *

def getdataGSDICT():
    valoriES={}
    for file in getOPTGSdiff_file():
        lista=[]
        name, dipole = getdataGS(file)
        lista.append(dipole)
        valoriES[name]=lista
    return valoriES

def getdataESDICT():
    valoriES={}
    for file in getESdiff_file():
        lista=[]
        name, wavelength, oscillator, energy, orbitals, dipole, transitiondipole = getdataES(file)
        lista.append(wavelength)
        lista.append(oscillator)
        lista.append(energy)
        lista.append(orbitals)
        lista.append(dipole)
        lista.append(transitiondipole)
        valoriES[name]=lista
    return valoriES

def getdataOPTESDICT():
    valoriOPTES={}
    for file in getOPTESdiff_file():
        lista=[]
        name, wavelength, oscillator, energy, orbitals, dipole, transitiondipole = getdataOPTES(file)
        lista.append(wavelength)
        lista.append(oscillator)
        lista.append(energy)
        lista.append(orbitals)
        lista.append(dipole)
        lista.append(transitiondipole)
        valoriOPTES[name]=lista
    return valoriOPTES

def getdataTPADICT():
    valoriTPA={}
    for file in getTPAdiff_file():
        lista=[]
        name, energy, cross = getdataTPA(file)
        lista.append(energy)
        lista.append(cross)
        valoriTPA[name]=lista
    return valoriTPA
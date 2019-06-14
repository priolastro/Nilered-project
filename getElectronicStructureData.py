from get_dati import *
from get_file import *
from get_dict import *
from print_latex import *

path='/Users/salvatoreprioli/Desktop/sdu/nilered_PROJ/ElectrStr/'


gs=getdataGSDICT(path)
es=getdataESDICT(path)
es_opt=getdataOPTESDICT(path)
tpa=getdataTPADICT(path)
PrintDataLaTex(gs, es, es_opt, tpa)
PrintDipolesLatex(es, es_opt, gs)


#################
# prendere file con 631 G**
################

# import os
# import re
# from tqdm import tqdm
# import numpy as np
#
#
# def getESdiff_file(path='/Users/salvatoreprioli/Desktop/sdu/nilered_PROJ/ElectrStr/'):
#     lista=[]
#     for dirpath, dirname, filename in os.walk(path):
#         if 'elecStruct' in dirpath and '.trash' not in dirpath and os.path.basename(dirpath)=='elecStruct':
#             for file in filename:
#                 if re.match(r'\w*[1-8]*ES631.log', file):
#                     filepath=os.path.join(dirpath, file)
#                     lista.append(filepath)
#     return sorted(lista)
#
# def getTPA_file(path='/Users/salvatoreprioli/Desktop/sdu/nilered_PROJ/ElectrStr/'):
#     lista = []
#     for dirpath, dirname, filename in os.walk(path):
#         if 'elecStruct' in dirpath and '.trash' not in dirpath and os.path.basename(dirpath) == 'elecStruct':
#             for file in filename:
#                 if re.match(r'2pa\w*.out', file) and 'Diff' not in file:
#                     filepath = os.path.join(dirpath, file)
#                     lista.append(filepath)
#                     yield filepath
#     return sorted(lista)
#
# def getdataES(file, conversionAU_DEB=2.5415802529):
#     wavelength = []
#     oscillator = []
#     energy = []
#     orbitals= []
#     dipole=[]
#     transitiondipole=[]
#     name = file.split('/')[-3]
#     with open(file, 'r') as log:
#         log_output=list(reversed(log.readlines()))
#         flag = True
#         for i, line in enumerate(log_output):
#             if 'Excited State   1' in line and flag:
#                 flag = False
#                 osc = float(line.split()[8].replace('f=', ''))
#                 wave = float(line.split()[6])
#                 energ = float(line.split()[4])
#                 orb = str(log_output[i - 1][5:15].strip())
#                 orb_ene = float(log_output[i - 1].split()[-1])
#                 wavelength.append(wave)
#                 oscillator.append(osc)
#                 energy.append(energ)
#                 orbitals.append(orb)
#                 orbitals.append(orb_ene)
#         flag = True
#         for i, line in enumerate(log_output):
#             if 'Dipole moment (field-independent basis, Debye):' in line and flag:
#                 flag = False
#                 dip = float(log_output[i - 1].split()[-1])
#                 dipole.append(dip)
#         flag = True
#         for i, line in enumerate(log_output):
#             if 'transition electric dipole moments ' in line and flag:
#                 flag = False
#                 transdip = np.linalg.norm(np.array(log_output[i - 2].split()[1:4]))
#                 transitiondipole.append(transdip)
#     return name, wavelength, oscillator, energy, orbitals, dipole, transitiondipole
#
# def getdataESDICT():
#     valoriES={}
#     for file in getESdiff_file():
#         lista=[]
#         name, wavelength, oscillator, energy, orbitals, dipole, transitiondipole=getdataES(file)
#         lista.append(wavelength)
#         lista.append(oscillator)
#         lista.append(energy)
#         lista.append(orbitals)
#         lista.append(dipole)
#         lista.append(transitiondipole)
#         valoriES[name]=lista
#     return valoriES
#
# def getdataTPA(file, conversion=1.896788*10**(-50)):
#     energy = []
#     cross_section = []
#     name = file.split('/')[-3]
#     with open(file, 'r') as out:
#         out_output = out.readlines()
#         for i, line in enumerate(out_output):
#             if 'Two-photon absorption summary ' in line:
#                 for l in range(i, i+30):
#                     if '1   1' in out_output[l] and 'Linear' in out_output[l]:
#                         energ=float(out_output[l].split()[2])
#                         cross=float(out_output[l].split()[7])
#                         energy.append(energ)
#                         cross_section.append(cross)
#     return name, energy, cross_section
#
# def PrintDataLaTex(Excitation):
#     print('&\multicolumn{4}{c}{\multirow{2}{*}{Absorption}} && \multicolumn{3}{c}{\multirow{2}{*}{Emission}} &Stokes	&\\\\')
#     print('&&&&&&&&&Shift&$\Delta\mu$\\\\')
#     print('\cline{2-5}\cline{7-9}\\\\')
#     print('Probe& $\Delta$E & \\textit{f} & \\textbf{$|$TM$|$}&$\sigma^{TPA}$ & & $\Delta$E & \\textit{f} & \\textbf{$|$TM$|$}& &\\\\')
#     print('\hline')
#     for nome, dati in Excitation.items():
#         print('{nome} & {energiaEx:0.2f} ({wavelengthEx:.0f}) & {oscEx:.2f} & {tmEx:.2f}\\\\'.format(nome=nome, energiaEx=dati[2][0], wavelengthEx=dati[0][0], oscEx=dati[1][0], tmEx=dati[5][0]))
#
#
# for file in getTPA_file():
#     print(file)
#     name, energy, cross=getdataTPA(file)
#     print(name, energy, cross)

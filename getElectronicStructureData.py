from get_dati import *
from get_file import *

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
#
# # ################################
# # #per stampare i dati formattati
# # ################################
#
def PrintDataLaTex(ground, Excitation, Emission, tpa):
    print('&\multicolumn{4}{c}{\multirow{2}{*}{Absorption}} && \multicolumn{3}{c}{\multirow{2}{*}{Emission}} &Stokes	&\\\\')
    print('&&&&&&&&&Shift&$\Delta\mu$\\\\')
    print('\cline{2-5}\cline{7-9}\\\\')
    print('Probe& $\Delta$E & \\textit{f} & \\textbf{$|$TM$|$}&$\sigma^{TPA}$ & & $\Delta$E & \\textit{f} & \\textbf{$|$TM$|$}& &\\\\')
    print('\hline')
    for nome, dati in Excitation.items():
        print('{nome} & {energiaEx:0.2f} ({wavelengthEx:.0f}) & {oscEx:.2f} & {tmEx:.2f}& {cross:.2f} && {energiaEm:.2f} ({wavelengthEm:.0f}) & {oscEm:.2f}& {tmEm:.2f} & {stokesener:.2f} ({stokeswave:.0f}) & {deltaDipol:.2f} \\\\'.format(nome=nome, energiaEx=dati[2][0], wavelengthEx=dati[0][0], oscEx=dati[1][0], tmEx=dati[5][0], cross=tpa[nome][1][0],energiaEm=Emission[nome][2][0], wavelengthEm=Emission[nome][0][0], oscEm=Emission[nome][1][0], tmEm=Emission[nome][5][0], stokesener=Emission[nome][2][0] - dati[2][0], stokeswave=Emission[nome][0][0] - dati[0][0], deltaDipol=float(Excitation[nome][4][0])-float(ground[nome][0][0])))

def PrintDipolesLatex(Excitation, Emission, gs):
    print('Probe    &   $\mu_{GS}$  &   $\mu_{ES}$  &   $\mu_{ES_{opt}}$    &   $\Delta\mu_{ES-GS}$ &   $\Delta\mu_{ES_{opt}-GS}$\\\\')
    for nome, dati in Excitation.items():
        print('{nome}&{gsdipole:0.2f}&{esdipole:0.2f}&{esoptdipole:0.2f}&{diffFC:0.2f}&{diffES:0.2f}\\\\'.format(nome=nome, gsdipole=gs[nome][0][0], esdipole=Excitation[nome][4][0], esoptdipole=Emission[nome][4][0], diffFC=float(Excitation[nome][4][0])-float(gs[nome][0][0]), diffES=float(Emission[nome][4][0])-float(gs[nome][0][0])))




gs=getdataGSDICT()
es=getdataESDICT()
es_opt=getdataOPTESDICT()
tpa=getdataTPADICT()
PrintDataLaTex(gs, es, es_opt, tpa)
PrintDipolesLatex(es, es_opt, gs)
#
#
#
# ################################
# ################################
# # Benchmarking Proj
# ################################
# # ################################
# import os
# import re
# from tqdm import tqdm
#
# def getOPTGS_file(path='/Users/salvatoreprioli/Desktop/sdu/JBprobes/'):
#     lista=[]
#     for dirpath, dirname, filename in tqdm(os.walk(path)):
#         if os.path.basename(dirpath)=='1PA':
#             for file in filename:
#                 if re.match(r'\w*.log', file) and 'ES' not in file:
#                     filepath=os.path.join(dirpath, file)
#                     lista.append(filepath)
#     return sorted(lista)
#
# def getES_file(path='/Users/salvatoreprioli/Desktop/sdu/JBprobes/'):
#     lista=[]
#     for dirpath, dirname, filename in tqdm(os.walk(path)):
#         if os.path.basename(dirpath) == '1PA':
#             for file in filename:
#                 if re.match(r'\w*ES.log', file):
#                     filepath = os.path.join(dirpath, file)
#                     lista.append(filepath)
#     return sorted(lista)
#
# def getOPTES_file(path='/Users/salvatoreprioli/Desktop/sdu/JBprobes/'):
#     lista=[]
#     for dirpath, dirname, filename in tqdm(os.walk(path)):
#         if os.path.basename(dirpath) == '1PA':
#             for file in filename:
#                 if re.match(r'\w*ES_OPT.log', file):
#                     filepath = os.path.join(dirpath, file)
#                     lista.append(filepath)
#     return sorted(lista)
#
# def getTPA_file(path='/Users/salvatoreprioli/Desktop/sdu/JBprobes/'):
#     lista=[]
#     for dirpath, dirname, filename in tqdm(os.walk(path)):
#         if os.path.basename(dirpath) == '2PA':
#             for file in filename:
#                 if re.match(r'2pa_\w*.out', file):
#                     filepath = os.path.join(dirpath, file)
#                     lista.append(filepath)
#     return sorted(lista)
#
# def getdataGS(file): #solo il dipolo
#     dipole = []
#     name = file.split('/')[-3]
#     with open(file, 'r') as log:
#         log_output = log.readlines()
#     dipole_last_line = max(i for i, line in enumerate(log_output) if 'Dipole moment (field-independent basis, Debye):' in line)
#     dip = float(log_output[dipole_last_line + 1].split()[-1])
#     dipole.append(dip)
#     return name, dipole
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
#                 transdip = np.linalg.norm(np.array(log_output[i - 2].split()[1:4]))*conversionAU_DEB
#                 transdip = abs(sum(float(i) for i in log_output[i - 2].split()[1:4]))*conversionAU_DEB
#                 transitiondipole.append(transdip)
#     return name, wavelength, oscillator, energy, orbitals, dipole, transitiondipole
#
# def getdataOPTES(file,  conversionAU_DEB=2.5415802529):
#     wavelength = []
#     oscillator = []
#     energy = []
#     orbitals= []
#     dipole=[]
#     transitiondipole=[]
#     name = file.split('/')[-3]
#     with open(file, 'r') as log:
#         log_output=list(reversed(log.readlines()))
#         flag=True
#         for i, line in enumerate(log_output):
#             if 'Excited State   1' in line and flag:
#                 flag=False
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
#                 flag=False
#                 dip = float(log_output[i - 1].split()[-1])
#                 dipole.append(dip)
#         flag = True
#         for i, line in enumerate(log_output):
#             if 'transition electric dipole moments ' in line and flag:
#                 flag=False
#                 transdip = np.linalg.norm(np.array(log_output[i - 2].split()[1:4]))*conversionAU_DEB
#                 # transdip = abs(sum(float(i) for i in log_output[i - 2].split()[1:4]))*conversionAU_DEB
#                 transitiondipole.append(transdip)
#     return name, wavelength, oscillator, energy, orbitals, dipole, transitiondipole
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
# #
# # ################################
# # #per fare i dizionari
# # ################################
# #
# def getdataGSDICT():
#     valoriES={}
#     for file in getOPTGS_file():
#         lista=[]
#         name, dipole =getdataGS(file)
#         lista.append(dipole)
#         valoriES[name]=lista
#     return valoriES
#
# def getdataESDICT():
#     valoriES={}
#     for file in getES_file():
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
# def getdataOPTESDICT():
#     valoriOPTES={}
#     for file in getOPTES_file():
#         lista=[]
#         name, wavelength, oscillator, energy, orbitals, dipole, transitiondipole =getdataOPTES(file)
#         lista.append(wavelength)
#         lista.append(oscillator)
#         lista.append(energy)
#         lista.append(orbitals)
#         lista.append(dipole)
#         lista.append(transitiondipole)
#         valoriOPTES[name]=lista
#     return valoriOPTES
#
# def getdataTPADICT():
#     valoriTPA={}
#     for file in getTPA_file():
#         lista=[]
#         name, energy, cross = getdataTPA(file)
#         lista.append(energy)
#         lista.append(cross)
#         valoriTPA[name]=lista
#     return valoriTPA
#
# ################################
# #per stampare i dati formattati
# ################################
#
# def PrintDataLaTex(ground, Excitation, Emission, tpa):
#     print('&\multicolumn{4}{c}{\multirow{2}{*}{Absorption}} && \multicolumn{3}{c}{\multirow{2}{*}{Emission}} &Stokes	&\\\\')
#     print('&&&&&&&&&Shift&$\Delta\mu$\\\\')
#     print('\cline{2-5}\cline{7-9}\\\\')
#     print('Probe& $\Delta$E & \\textit{f} & \\textbf{$|$TM$|$}&$\sigma^{TPA}$ & & $\Delta$E & \\textit{f} & \\textbf{$|$TM$|$}& &\\\\')
#     print('\hline')
#     for nome, dati in Excitation.items():
#         print('{nome} & {energiaEx:0.2f} ({wavelengthEx:.0f}) & {oscEx:.2f} & {tmEx:.2f}& {cross:.2f} && {energiaEm:.2f} ({wavelengthEm:.0f}) & {oscEm:.2f}& {tmEm:.2f} & {stokesener:.2f} ({stokeswave:.0f}) & {deltaDipol:.2f} \\\\'.format(nome=nome, energiaEx=dati[2][0], wavelengthEx=dati[0][0], oscEx=dati[1][0], tmEx=dati[5][0], cross=tpa[nome][1][0],energiaEm=Emission[nome][2][0], wavelengthEm=Emission[nome][0][0], oscEm=Emission[nome][1][0], tmEm=Emission[nome][5][0], stokesener=Emission[nome][2][0] - dati[2][0], stokeswave=Emission[nome][0][0] - dati[0][0], deltaDipol=float(Excitation[nome][4][0])-float(ground[nome][0][0])))
#
# def PrintDipolesLatex(Excitation, Emission, gs):
#     print('Probe    &   $\mu_{GS}$  &   $\mu_{ES}$  &   $\mu_{ES_{opt}}$    &   $\Delta\mu_{ES-GS}$ &   $\Delta\mu_{ES_{opt}-GS}$\\\\')
#     for nome, dati in Excitation.items():
#         print('{nome}&{gsdipole:0.2f}&{esdipole:0.2f}&{esoptdipole:0.2f}&{diffFC:0.2f}&{diffES:0.2f}\\\\'.format(nome=nome, gsdipole=gs[nome][0][0], esdipole=Excitation[nome][4][0], esoptdipole=Emission[nome][4][0], diffFC=float(Excitation[nome][4][0])-float(gs[nome][0][0]), diffES=float(Emission[nome][4][0])-float(gs[nome][0][0])))
#
# gs=getdataGSDICT()
# es=getdataESDICT()
# es_opt=getdataOPTESDICT()
# tpa=getdataTPADICT()
# PrintDataLaTex(gs, es, es_opt, tpa)
# PrintDipolesLatex(es, es_opt, gs)



##################
#prendere file con 631 G**
#################

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

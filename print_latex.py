def PrintDataLaTex(ground, Excitation, Emission, tpa):
    for nome, dati in Excitation.items():
        print('{nome} & {energiaEx:0.2f} ({wavelengthEx:.0f}) & {oscEx:.2f} & {tmEx:.2f}& {cross:.2f} && {energiaEm:.2f} ({wavelengthEm:.0f}) & {oscEm:.2f}& {tmEm:.2f} & {stokesener:.2f} ({stokeswave:.0f}) & {deltaDipol:.2f} \\\\'.format(nome=nome, energiaEx=dati[2][0], wavelengthEx=dati[0][0], oscEx=dati[1][0], tmEx=dati[5][0], cross=tpa[nome][1][0],energiaEm=Emission[nome][2][0], wavelengthEm=Emission[nome][0][0], oscEm=Emission[nome][1][0], tmEm=Emission[nome][5][0], stokesener=Emission[nome][2][0] - dati[2][0], stokeswave=Emission[nome][0][0] - dati[0][0], deltaDipol=float(Excitation[nome][4][0])-float(ground[nome][0][0])))

def PrintDipolesLatex(Excitation, Emission, gs):
    for nome, dati in Excitation.items():
        print('{nome}&{gsdipole:0.2f}&{esdipole:0.2f}&{esoptdipole:0.2f}&{diffFC:0.2f}&{diffES:0.2f}\\\\'.format(nome=nome, gsdipole=gs[nome][0][0], esdipole=Excitation[nome][4][0], esoptdipole=Emission[nome][4][0], diffFC=float(Excitation[nome][4][0])-float(gs[nome][0][0]), diffES=float(Emission[nome][4][0])-float(gs[nome][0][0])))



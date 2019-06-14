class get_dati:
    def getdataGS(file): #solo il dipolo
        dipole = []
        name = file.split('/')[-3]
        with open(file, 'r') as log:
            log_output = log.readlines()
        dipole_last_line = max(i for i, line in enumerate(log_output) if 'Dipole moment (field-independent basis, Debye):' in line)
        dip = float(log_output[dipole_last_line + 1].split()[-1])
        dipole.append(dip)
        return name, dipole

    def getdataES(file, conversionAU_DEB=2.5415802529):
        wavelength = []
        oscillator = []
        energy = []
        orbitals= []
        dipole=[]
        transitiondipole=[]
        name = file.split('/')[-3]
        with open(file, 'r') as log:
            log_output=list(reversed(log.readlines()))
            flag = True
            for i, line in enumerate(log_output):
                if 'Excited State   1' in line and flag:
                    flag = False
                    osc = float(line.split()[8].replace('f=', ''))
                    wave = float(line.split()[6])
                    energ = float(line.split()[4])
                    orb = str(log_output[i - 1][5:15].strip())
                    orb_ene = float(log_output[i - 1].split()[-1])
                    wavelength.append(wave)
                    oscillator.append(osc)
                    energy.append(energ)
                    orbitals.append(orb)
                    orbitals.append(orb_ene)
            flag = True
            for i, line in enumerate(log_output):
                if 'Dipole moment (field-independent basis, Debye):' in line and flag:
                    flag = False
                    dip = float(log_output[i - 1].split()[-1])
                    dipole.append(dip)
            flag = True
            for i, line in enumerate(log_output):
                if 'transition electric dipole moments ' in line and flag:
                    flag = False
                    transdip=np.linalg.norm(np.array(log_output[i - 2].split()[1:4]))*conversionAU_DEB
                    transitiondipole.append(transdip)
        return name, wavelength, oscillator, energy, orbitals, dipole, transitiondipole

    def getdataOPTES(file, conversionAU_DEB=2.5415802529):
        name = file.split('/')[-3]
        wavelength = []
        oscillator = []
        energy = []
        orbitals= []
        dipole=[]
        transitiondipole=[]
        with open(file, 'r') as log:
            log_output=list(reversed(log.readlines()))
            flag=True
            for i, line in enumerate(log_output):
                if 'Excited State   1' in line and flag:
                    flag=False
                    osc = float(line.split()[8].replace('f=', ''))
                    wave = float(line.split()[6])
                    energ = float(line.split()[4])
                    orb = str(log_output[i - 1][5:15].strip())
                    orb_ene = float(log_output[i - 1].split()[-1])
                    wavelength.append(wave)
                    oscillator.append(osc)
                    energy.append(energ)
                    orbitals.append(orb)
                    orbitals.append(orb_ene)
            flag = True
            for i, line in enumerate(log_output):
                if 'Dipole moment (field-independent basis, Debye):' in line and flag:
                    flag=False
                    dip = float(log_output[i - 1].split()[-1])
                    dipole.append(dip)
            flag = True
            for i, line in enumerate(log_output):
                if 'transition electric dipole moments ' in line and flag:
                    flag=False
                    transdip=np.linalg.norm(np.array(log_output[i - 2].split()[1:4]))*conversionAU_DEB
                    transitiondipole.append(transdip)
        return name, wavelength, oscillator, energy, orbitals, dipole, transitiondipole

    def getdataTPA(file, conversion=1.896788*10**(-50)):
        energy = []
        cross_section = []
        name = file.split('/')[-3]
        with open(file, 'r') as out:
            out_output = out.readlines()
            for i, line in enumerate(out_output):
                if 'Two-photon absorption summary ' in line:
                    for l in range(i, i+30):
                        if '1   1' in out_output[l] and 'Linear' in out_output[l]:
                            energ=float(out_output[l].split()[2])
                            cross=float(out_output[l].split()[7])
                            energy.append(energ)
                            cross_section.append(cross)
        return name, energy, cross_section

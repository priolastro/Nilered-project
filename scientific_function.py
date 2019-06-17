import numpy as np
import scipy.constants as sc
import matplotlib.pyplot as plt
from scipy.constants import h, c, e, N_A, electron_mass
esu_Cfactor=2997924579.9996

def spectra(EXC, OS, x=np.linspace(100, 1000, 10000), sigma=0.4, prefattore=((np.sqrt(sc.pi)*(e*esu_Cfactor)**2*N_A)/(1000*np.log(10)*(c*100)**2*electron_mass))/1000):
    e1 = 0
    for i in range(len(EXC)):
        e1 += prefattore*(OS[i]/(10**7/nm(sigma)))*np.exp(-(((1/x)-(1/EXC[i]))/(1/nm(sigma)))**2)
    return e1, x

def eV(wavelength, a=((h*c)/e)*10**9):
    return a/(wavelength)

def nm(wavelength, a=((h*c)/e)*10**9):
    return a/(wavelength)

def plotta_gaussiane(valori,width=10, aspect=0.5, nome_x='Wavelength (nm)',lim_x=[200, 700], nome_y='Intensity [L mol-1 cm-1]',lim_y=[0, 5000]):
    height = width * aspect
    plt.figure(figsize=(width, height))
    for nome, dati in valori.items():
        plt.xlabel(nome_x)
        plt.ylabel(nome_y)
        axes = plt.gca()
        axes.set_ylim(lim_y)
        axes.set_xlim(lim_x)
        spectro, lnspc = spectra(dati[0], dati[1], x=np.linspace(100, 1000, 10000))
        plt.plot(lnspc, spectro, label=nome)
        plt.legend(prop={'size': 8})
    plt.show()
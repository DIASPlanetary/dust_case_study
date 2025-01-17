# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 11:20:15 2025

@author: march
"""

import math_tools as math_tools

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from scipy.optimize import curve_fit
from scipy import stats    

datasetE = np.loadtxt('Europa_data.csv', delimiter=',').T
datasetI = np.loadtxt('Io_data.csv', delimiter=',').T
datasetC = np.loadtxt('Callisto_data.csv', delimiter=',').T
datasetIP = np.loadtxt('Io_pele_data.csv', delimiter=',').T
datasetES = np.loadtxt('Europa_second_data.csv', delimiter=',').T

massE = datasetE[0]
densityE = datasetE[1]
ndensityE = datasetE[2]
RE = []
CSAE = []
MFPE = []

massI = datasetI[0]
densityI = datasetI[1]
ndensityI = datasetI[2]
RI = []
CSAI = []
MFPI = []

massIP = datasetIP[0]
densityIP = datasetIP[1]
ndensityIP = datasetIP[2]
RIP = []
CSAIP = []
MFPIP = []

massC = datasetC[0]
densityC = datasetC[1]
ndensityC = datasetC[2]
RC = []
CSAC = []
MFPC = []

RES = datasetES[0]
ndensityES = datasetES[1]
CSAES = []
MFPES = []

for i in range(0, len(ndensityES)):
    for j in range(0, len(RES)):
        csa =4*3.14*(RES[j]**2)
        CSAES.append(csa)
        mfp = 1/(ndensityES[i]*csa)
        MFPES.append(mfp)

RES = np.array(RES)
CSAES = np.array(CSAES)
MFPES = np.array(MFPES)
ndensityES = np.array(ndensityES)

print('Europa second data')
print('Cross Section area of dust:', CSAES)
print('Mean Free Path', MFPES)


for i in range(0, len(ndensityE)):
    for j in range(0, len(massE)):
        for k in range(0, len(densityE)):
            r = ((3*massE[j])/(4*3.14*densityE[k]))**(1/3)
            RE.append(r)
            csa = 4*3.14*(r**2)
            CSAE.append(csa)
            mfp = 1/(ndensityE[i]*csa)
            MFPE.append(mfp)

RE = np.array(RE)
CSAE = np.array(CSAE)
MFPE = np.array(MFPE)
ndensityE = np.array(ndensityE)

print('Europa data')
print('Cross Section area of dust:', CSAE)
print('Mean Free Path', MFPE)


for i in range(0, len(ndensityI)):
    for j in range(0, len(massI)):
        for k in range(0, len(densityI)):
            r = ((3*massI[j])/(4*3.14*densityI[k]))**(1/3)
            RI.append(r)
            csa = 4*3.14*(r**2)
            CSAI.append(csa)
            mfp = 1/(ndensityI[i]*csa)
            MFPI.append(mfp)

RI = np.array(RI)
CSAI = np.array(CSAI)
MFPI = np.array(MFPI)
ndensityI = np.array(ndensityI)

print('Io data')
print('Cross Section area of dust:', CSAI)
print('Mean Free Path', MFPI)

for i in range(0, len(ndensityIP)):
    for j in range(0, len(massIP)):
        for k in range(0, len(densityIP)):
            r = ((3*massIP[j])/(4*3.14*densityIP[k]))**(1/3)
            RIP.append(r)
            csa = 4*3.14*(r**2)
            CSAIP.append(csa)
            mfp = 1/(ndensityIP[i]*csa)
            MFPIP.append(mfp)

RIP = np.array(RIP)
CSAIP = np.array(CSAIP)
MFPIP = np.array(MFPIP)
ndensityIP = np.array(ndensityIP)

print('Io pele data')
print('Cross Section area of dust:', CSAIP)
print('Mean Free Path', MFPIP)

for i in range(0, len(ndensityC)):
    for j in range(0, len(massC)):
        for k in range(0, len(densityC)):
            r = ((3*massC[j])/(4*3.14*densityC[k]))**(1/3)
            RC.append(r)
            csa = 4*3.14*(r**2)
            CSAC.append(csa)
            mfp = 1/(ndensityC[i]*csa)
            MFPC.append(mfp)

RC = np.array(RC)
CSAC = np.array(CSAC)
MFPC = np.array(MFPC)
ndensityC = np.array(ndensityC)

print('Callisto data')
print('Radius', RC)
print('Cross Section area of dust:', CSAC)
print('Mean Free Path', MFPC)

X_E = CSAE
X_ES = CSAES
X_I = CSAI
X_IP = CSAIP
X_C = CSAC
Y_E = []
Y_ES = []
Y_I = []
Y_IP = []
Y_C = []

for m in range(0, 9):
    Y_E.append(ndensityE[0])
for m in range(9, 18):
    Y_E.append(ndensityE[1])
for m in range(18, 27):
    Y_E.append(ndensityE[2])

for m in range(0, 12):
    Y_ES.append(ndensityES[0])
for m in range(12, 24):
    Y_ES.append(ndensityES[1])
for m in range(24, 36):
    Y_ES.append(ndensityES[2])
for m in range(36, 48):
    Y_ES.append(ndensityES[3])
for m in range(48, 60):
    Y_ES.append(ndensityES[4])
for m in range(60, 72):
    Y_ES.append(ndensityES[5])
for m in range(72, 84):
    Y_ES.append(ndensityES[6])
for m in range(84, 96):
    Y_ES.append(ndensityES[7])
for m in range(96, 108):
    Y_ES.append(ndensityES[8])
for m in range(108, 120):
    Y_ES.append(ndensityES[9])
for m in range(120, 132):
    Y_ES.append(ndensityES[10])
for m in range(132, 144):
    Y_ES.append(ndensityES[11])

for m in range(0, 4):
    Y_I.append(ndensityI[0])
for m in range(4, 8):
    Y_I.append(ndensityI[1])

for m in range(0, 49):
    Y_IP.append(ndensityIP[0])
for m in range(49, 98):
    Y_IP.append(ndensityIP[1])
for m in range(98, 147):
    Y_IP.append(ndensityIP[2])
for m in range(147, 196):
    Y_IP.append(ndensityIP[3])
for m in range(196, 243):
    Y_IP.append(ndensityIP[4])
for m in range(243, 292):
    Y_IP.append(ndensityIP[5])
for m in range(292, 343):
    Y_IP.append(ndensityIP[6])


for m in range(0, 9):
    Y_C.append(ndensityC[0])
for m in range(9, 18):
    Y_C.append(ndensityC[1])
for m in range(18, 27):
    Y_C.append(ndensityC[2])
    

fig, ax = plt.subplots()
ax.scatter(X_E, Y_E, label='Europa Kruger et al., 2003', marker='.', color='b')
ax.scatter(X_I, Y_I, label='Io Kruger et al., 2003', marker='.', color='y')
ax.scatter(X_C, Y_C, label='Callisto Kruger et al., 2003', marker='.', color='r')
ax.scatter(X_IP, Y_IP, label='Io McDoniel et al., 2015', marker='s', color='y')
ax.scatter(X_ES, Y_ES, label='Europa Southworth et al., 2015', marker='^', color='b')

ax.set_xlim(1e-12, 1e-10)
#ax.set_ylim(1e-9, 0.0012)

plt.xlabel("Cross-section area (cm^2)")    
plt.ylabel("Number density (m^-3")   


plt.legend()

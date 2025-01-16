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

massC = datasetC[0]
densityC = datasetC[1]
ndensityC = datasetC[2]
RC = []
CSAC = []
MFPC = []

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
            mfp = 1/(ndensityE[i]*csa)
            MFPI.append(mfp)

RI = np.array(RI)
CSAI = np.array(CSAI)
MFPI = np.array(MFPI)
ndensityI = np.array(ndensityI)

print('Io data')
print('Cross Section area of dust:', CSAI)
print('Mean Free Path', MFPI)

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
X_I = CSAI
X_C = CSAC
Y_E = []
Y_I = []
Y_C = []

for m in range(0, 9):
    Y_E.append(ndensityE[0])
for m in range(9, 18):
    Y_E.append(ndensityE[1])
for m in range(18, 27):
    Y_E.append(ndensityE[2])

for m in range(0, 4):
    Y_I.append(ndensityI[0])
for m in range(4, 8):
    Y_I.append(ndensityI[1])

for m in range(0, 9):
    Y_C.append(ndensityC[0])
for m in range(9, 18):
    Y_C.append(ndensityC[1])
for m in range(18, 27):
    Y_C.append(ndensityC[2])
    

fig, ax = plt.subplots()
ax.scatter(X_E, Y_E, label='Europa data', marker='s', color='b')
ax.scatter(X_I, Y_I, label='Io data', marker='.', color='y')
ax.scatter(X_C, Y_C, label='Callisto data', marker='^', color='r')

ax.set_xlim(1e-12, 1e-10)
ax.set_ylim(1e-9, 0.0012)

plt.xlabel("Cross-section area (cm^2)")    
plt.ylabel("Number density (m^-3")   


plt.legend()

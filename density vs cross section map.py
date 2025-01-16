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

dataset=np.loadtxt('Europa_data.csv', delimiter=',').T

mass = dataset[0]
density = dataset[1]
ndensity = dataset[2]
R = []
CSA = []
MFP = []

for i in range(0, len(ndensity)):
    for j in range(0, len(mass)):
        for k in range(0, len(density)):
            r = ((3*mass[j])/(4*3.14*density[k]))**(1/3)
            R.append(r)
            csa = 4*3.14*(r**2)
            CSA.append(csa)
            mfp = 1/(ndensity[i]*csa)
            MFP.append(mfp)

R = np.array(R)
CSA = np.array(CSA)
MFP = np.array(MFP)
ndensity = np.array(ndensity)
print(R)
print(CSA)
print(MFP)

X_E = CSA   
Y_E = []

for m in range(0, 9):
    Y_E.append(ndensity[0])
print(Y_E)
for m in range(9, 18):
    Y_E.append(ndensity[1])
for m in range(18, 27):
    Y_E.append(ndensity[2])




plt.figure()            
plt.xlabel("Cross-section area (cm^2)")    
plt.ylabel("Number density (m^-3")   

fig, ax = plt.subplots()
ax.scatter(X_E, Y_E, label='Europa data', marker='s', color='b')

ax.set_xlim(1e-11, 1e-10)
ax.set_ylim(1e-9, 0.0012)


plt.ylabel('Number density (m^-3)')
plt.xlabel(' Cross section (cm^2)')

plt.legend()

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

dataset=np.loadtxt('data for plotting.csv', delimiter=',').T

X_E=dataset[0]   
Y_E=dataset[1]
X_I=dataset[2]
Y_I=dataset[3]

plt.figure()            
plt.xlabel("Cross-section area (cm^2)")    
plt.ylabel("Number density (m^-3")   

fig, ax = plt.subplots()
ax.scatter(X_E, Y_E, label='Europa data', marker='s', color='b')
ax.scatter(X_I, Y_I, label='Io data', marker='.', color='y')

ax.set_xlim(1e-8, 1e-6)
ax.set_ylim(1e-9, 0.0015)

plt.ylabel('Number density (m^-3)')
plt.xlabel(' Cross section (cm^2)')

plt.legend()
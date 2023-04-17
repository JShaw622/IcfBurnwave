# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 18:37:23 2023

@author: Jack Shaw
"""

import ENDF6
import matplotlib.pyplot as plt
import numpy as np

# Dictonary for masses in atomic units (u)
u = 1.66053906660e-27
masses = {"D": 2.014, "T":3.016, "3He":3.016,"p":1.007276466620409}

#Defines xaxis for energy in a log scale from 0 to 1000 KeV
Energy_x_axis=np.logspace(0, 3, 100)

PATH="data/endfFiles/"

file = open("data/endfFiles/D_T_a_n.txt")
lines = file.readlines()
sec = ENDF6.find_section(lines, MF=3, MT=3)  # total cross-section
x, y = ENDF6.read_table(sec)

plt.figure()
plt.plot(x, y)
plt.xlabel('Photon energy [eV]')
plt.ylabel('Cross-section [barn]')
plt.show()
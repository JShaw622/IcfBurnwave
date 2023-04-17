# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 20:07:02 2023

@author: Jack Shaw
"""

import numpy as np
import matplotlib.pyplot as plt

import matplotlib as mpl
import matplotlib.font_manager as font_manager

mpl.rcParams['font.family']='serif'
cmfont = font_manager.FontProperties(fname=mpl.get_data_path() + '/fonts/ttf/cmr10.ttf')
mpl.rcParams['font.serif']=cmfont.get_name()
mpl.rcParams['mathtext.fontset']='cm'
mpl.rcParams['axes.unicode_minus']=False

gamma = 5/3

p1 =1
v1 =1

p2=15
v2=0

v2=v1*((gamma+1)*p1+(gamma-1)*p2)/((gamma+1)*p2+(gamma-1)*p1)

pressure = np.arange(0.1,30,0.1)
pressure = pressure/p1

hugoniotV=[]
poissonV=[]
for p2 in pressure:
    #calculates hugoniot adiabat
    v2=v1*((gamma+1)*p1+(gamma-1)*p2)/((gamma+1)*p2+(gamma-1)*p1)
    hugoniotV.append(v2/v1)
    
    #calculates poisson adiabat
    v2=((p1*v1**gamma)/p2)**(1/gamma)
    poissonV.append(v2/v1)
    
    
def calculate_secant(x1,x2,y1,y2):
    m=y2-y1/(x2-x1)
    
    c=y1-m*x1
    
    xline = np.arange(x1,x2,0.01)
    
    yline=[]
    for i in xline:
        yline.append(m*i+c)
        
    return xline, yline

    
    
fig=plt.figure(dpi=300)
plt.plot(hugoniotV,pressure, label="Hugoniot adiabat")
plt.plot(poissonV,pressure, label="Poisson adiabat", linestyle="dashed")
plt.vlines(x=0.25, ymin=0, ymax=max(pressure), linestyle="dotted")


sectantx,sectanty = calculate_secant(0.32, 1, 20, 1)

plt.plot(sectantx,sectanty,linestyle="dotted")
plt.text(0.65, 11, "$-j^2$")


plt.text(0.32,20,"$(V_2,P_2)$")
plt.scatter(0.296,20,c="red")

plt.text(1.02,1.65,"$(V_1,P_1)$")
plt.scatter(1,1,c="red")

plt.axis([0, 1.25, 0, 30])
plt.xticks(ticks=[0,0.25,0.5,0.75,1,1.25],labels=[0,0.25,0.5,0.75,1,1.25])

plt.xlabel("$V_2/V_1$")
plt.ylabel("$P_2/P_1$")

plt.legend()

plt.savefig('HugoniotAdiabat.png',bbox_inches="tight")
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 20:07:02 2023

@author: Jack Shaw
"""

import numpy as np
import matplotlib.pyplot as plt

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


x1=[-1,0,0,1]
y1=[1.5,1.5,0.5,0.5]

plt.plot(x1,y1)

plt.vlines(x=0, ymin=0, ymax=1.5,linestyles="dotted",)

plt.text(-0.75,1.3,"$P_2,\\rho_2,u_2$")

plt.text(0.25,0.3,"$P_1,\\rho_1,u_1$")

plt.text(0.23,0.1,"$v_1=u_1-u_s$")
plt.text(-0.7,0.1,"$v_2=u_2-u_2$")
plt.arrow(0.21,0.1,-0.2,0,length_includes_head=True,width=0.015)
plt.arrow(-0.05,0.1,-0.2,0,length_includes_head=True,width=0.015)

plt.text(0.23,1,"$u_s$")
plt.arrow(0,1,0.2,0,length_includes_head=True,width=0.015)

plt.axis([-1, 1, 0, 2])
plt.xticks(ticks=[-1,0,1],labels=["","",""])

plt.yticks(ticks=[0,1,2],labels=["","",""])

plt.xlabel("$x$")
plt.ylabel("")

plt.savefig('shockEx.png',bbox_inches="tight")
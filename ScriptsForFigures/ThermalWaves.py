# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 20:07:02 2023

@author: Jack Shaw
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.path as mpath
import matplotlib.patches as mpatches
import matplotlib as mpl

xmax=10

x1=np.arange(0,2,0.1)

T1=[]
c=0
for i in x1:
    c +=1
    T1.append((1/(i-xmax))+3)  
    
x3=np.arange(2,9.8,0.1)

T2=[]
for i in x3:
    c +=1
    T2.append((1/(i-xmax))+3)  
    
def curly_arrow(start, end, arr_size = 1, n = 5, col='gray', linew=1., width = 0.1):
    xmin, ymin = start
    xmax, ymax = end
    dist = np.sqrt((xmin - xmax)**2 + (ymin - ymax)**2)
    n0 = dist / (2 * np.pi)
    
    x = np.linspace(0, dist, 151) + xmin
    y = width * np.sin(n * x / n0) + ymin
    line = plt.Line2D(x,y, color=col, lw=linew)
    
    del_x = xmax - xmin
    del_y = ymax - ymin
    ang = np.arctan2(del_y, del_x)
    
    line.set_transform(mpl.transforms.Affine2D().rotate_around(xmin, ymin, ang) + ax.transData)
    ax.add_line(line)

    verts = np.array([[0,1],[0,-1],[2,0],[0,1]]).astype(float) * arr_size
    verts[:,1] += ymax
    verts[:,0] += xmax
    path = mpath.Path(verts)
    patch = mpatches.PathPatch(path, fc=col, ec=col)

    patch.set_transform(mpl.transforms.Affine2D().rotate_around(xmax, ymax, ang) + ax.transData)
    return patch

x2=np.arange(2,9.8,0.1)

y2=[]
c=0
for i in x2:
    c+=1
    y2.append(np.exp((i**1)-9)+0.005*c)
    
    
mpl.rcParams.update({'font.size': 16})

fig, ax =plt.subplots(dpi=300)#

#ax.plot(x1,T1,linestyle="dashed",label="T",c="red")
ax.plot(x3,T2,linestyle="dashed",label="T",c="red")
ax.plot([9.8,13,13,20],[2.4,2.4,1.75,1.75],label="$\\rho$",c="#1f77b4")
ax.plot(x2,y2)

#ax.plot([2,2,20],[0,2,2],label="$\\rho$",c="#1f77b4")

#ax.fill_between(x3,T2,alpha=0.3,fc="grey")

ax.add_patch(curly_arrow((1, 1), (9, 1), n=6.3, arr_size=0.1,col="orange"))

#ax.hlines(1,xmin=3.5,xmax=9,linestyle="dashed")
#ax.arrow(8.5,1,0.5,0,width=0.05,length_includes_head=True,head_length=0.5)
#plt.text(6,1.1,"$q_{dif}$")


plt.text(0.5,0.95,"$q_s$")      

plt.axis([0, xmax+5, 0, 3])

plt.xticks(ticks=[],labels=[])
plt.yticks(ticks=[],labels=[])

plt.xlabel("x")
plt.ylabel("")

plt.legend()

plt.savefig('ThermalWaves2.png',bbox_inches="tight")
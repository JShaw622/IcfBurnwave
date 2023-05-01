# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 22:39:39 2022

@author: Jack
"""
import netCDF4
from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

PATH = "data/TAnalysis/C/"
hyades_file = PATH+'test_T_10_5_19.cdf'#"originalinput.cdf"
f      = Dataset(hyades_file,mode='r') #open the file "hyades_file" in read mode

#Finding the number of zones in the problem and the number of time steps in the problem
numZones = len(f.dimensions["NumZones"])
numTimes = len(f.dimensions["NumTimes"])
print("Time steps: ", numTimes)

#Array of dump times i.e. times at which data is put into the ppf/cdf file
dumpTime = f.variables["DumpTimes"][:]

#Position of a zones center of mass at a given time is given by the variable "Rcm" and in cm 
position = f.variables["Rcm"][:] #Position array dimenstions: ("numTimes", "numZonesPlusTwo")

#Mesh velocitiesin cm/s
#flow = f.variables["U"][:]

#Zone mass density is stored in variable "Rho" units: 'gm/cm^3'
zoneDensity=f.variables["Rho"][:] #Dimenstions ("NumTimes", "NumZones")

#zone ion temperature in keV
zoneTi = f.variables["Ti"][:]

#total thermonuclear energy production in zone in erg
productionTN = f.variables["Bpeprd"][:]

#Calculate RhoR
RhoR = []
for t in range(numTimes):
    RhoR.append(zoneDensity[t,:-1]*position[t,:-1][1:-1])

#-----------------------------------------------------------------------------#

#:length of x axis
startPosition =0
endPosition = 0.1

#Time between frames ms
frameInterval = 100

#specify start and end frames
endFrame = numTimes
startFrame = 0

figDen = plt.figure()
axDen= plt.axes(xlim=(startPosition, endPosition), ylim=(0, 600))
axDen.set_title("Density (blue) and temperature (red) against position")
axDen.set_xlabel("Position (cm)")
axDen.set_ylabel("Density ($gcm^{-3}$)")
lineDen, =axDen.plot([], [])
DenFrame = axDen.text(0,520, "")

#plot temperature on same graph
axT=axDen.twinx()
axT.set_ylim(0, 30)
axT.set_ylabel("Ion Temperature (keV)",color="red")
lineT, = axT.plot([],[],color="red")

def init():
    lineDen.set_data([], [])
    lineT.set_data([],[])
    DenFrame.set_text("frame: 0 / 0"
                      + "\nTime: 0.00000e+00 sec")
    return lineDen, DenFrame

def animateDen(i):
    i = i+ startFrame
    xDen = position[i][1:-1]
    yDen = zoneDensity[i]
    yT = zoneTi[i]
    lineDen.set_data(xDen, yDen)
    lineT.set_data(xDen,yT)
    DenFrame.set_text("frame: " + str(i) + " / " + str(endFrame)
                      + "\nTime: " + str.format('{0:.6}', dumpTime[i]) + " sec")    
    return lineDen, lineT, DenFrame

animDen = FuncAnimation(figDen, animateDen, init_func=init,
                                frames=endFrame-startFrame, interval=frameInterval, blit=True)
animDen.save(PATH+'density.gif', writer='imagemagick')
print("Density finished")

# figFlow = plt.figure()
# axFlow= plt.axes(xlim=(startPosition, endPosition), ylim=(-4*10**7, 10*10**7))
# axDen.set_title("Flow against position")
# axFlow.set_xlabel("Position (cm)")
# axFlow.set_ylabel("Flow (cm/s)")
# lineFlow, =axFlow.plot([], [])
# FlowFrame = axFlow.text(0,4*0.83333*10**7, "")

# def initFlow():
#     lineFlow.set_data([], [])
#     FlowFrame.set_text("frame: 0 / 0"
#                       + "\nTime: 0.00000e+00 sec")
#     return lineFlow, FlowFrame
# def animateFlow(i):
#     i = i+ startFrame
#     x = position[i][1:-1]
#     y = flow[i][:-1]
#     lineFlow.set_data(x, y)
#     FlowFrame.set_text("frame: " + str(i) + " / " + str(endFrame)
#                       + "\nTime: " + str.format('{0:.6}', dumpTime[i]) + " sec")
#     return lineFlow, FlowFrame

# animFlow = FuncAnimation(figFlow, animateFlow, init_func=initFlow,
#                                 frames=endFrame-startFrame, interval=frameInterval, blit=True)
# animFlow.save('Flow.gif', writer='imagemagick')
# print ("Flow Finished")

figTN = plt.figure()
axTN= plt.axes(xlim=(startPosition, endPosition), ylim=(-1*10, 7*10**11))
axTN.set_xlabel("Position (cm)")
axTN.set_ylabel("TN Production (erg)")
lineTN, =axTN.plot([], [])
TNFrame = axTN.text(0, 7*0.91666*10**11, "")

def initTN():
    lineTN.set_data([], [])
    TNFrame.set_text("frame: 0 / 0"
                      + "\nTime: 0.00000e+00 sec")
    return lineTN, TNFrame
def animateTN(i):
    i = i+ startFrame
    x = position[i][1:-1]
    if i!=0:
        y = productionTN[i]#-productionTN[i-1]
    else:
        y = productionTN[0]
    lineTN.set_data(x, y)
    TNFrame.set_text("frame: " + str(i) + " / " + str(endFrame)
                      + "\nTime: " + str.format('{0:.6}', dumpTime[i]) + " sec")
    return lineTN, TNFrame

#animTN = FuncAnimation(figTN, animateTN, init_func=initTN,
#                                frames=endFrame-startFrame, interval=frameInterval, blit=True)
#animTN.save(PATH+'TN.gif', writer='imagemagick')
print("Energy Producion finished")

print("Saving to:" +PATH)

fig2 = plt.figure()
plt.scatter(position[-1][1:-1],zoneTi[-1])
plt.show()

print("End Time: ",dumpTime[endFrame-1])
totalTNproduced = sum(productionTN[endFrame-1])
print("Total TN production (erg): ",totalTNproduced)

print("Production rate: ", totalTNproduced/dumpTime[endFrame-1])

#reads inf file to find HS radius and density    
def get_HS_rhoR(filename):
    #convert filename from .cdf to .inf
    filename = filename[0:-4]+".inf"
    #open file convert to array of lines in file and close the file to save memory
    file = open(filename, "r")
    f = file.readlines()
    file.close()
    
    ##### FIND HOT SPOT RADIUS #####
    #read the radius of the hotspot from file
    Hs_Rad = float((f[6])[-7:-2])
    
    ##### FIND HOT SPOT DENSITY #####
    text = "DEFINE HsDensity "
    HS_rho = float(f[9].replace(text, ""))
    
    ###### Calculate and return the rhoR of the hotspot #####
    rhoR = round(Hs_Rad*HS_rho,5)
    return (rhoR)

print(get_HS_rhoR(hyades_file))

# figInit = plt.figure(dpi=300)

# axDeninit= plt.axes(xlim=(startPosition, 0.05), ylim=(0, 300))
# plt.xticks([0,0.0093,0.05],["0","$r_{hs}$",""])
# #axDeninit.set_title("Density (blue) and temperature (red) against position")
# axDeninit.set_xlabel("Position (cm)")
# axDeninit.set_ylabel("Density (gcm$^{-3}$)")
# #lineDen, =axDen.plot([], [])
# #DenFrame = axDen.text(0,520, "")
# denln=axDeninit.plot(position[0][1:-1],zoneDensity[0],label="Density (gcm$^{-3}$)")
# print(position[0][1:-1])
# #plot temperature on same graph
# axTinit=axDeninit.twinx()
# axTinit.set_ylim(0, 20)
# axTinit.set_ylabel("Ion Temperature (keV)",color="red")

# tline=axTinit.plot(position[0][1:-1],zoneTi[0],c="red",label="Temperature (KeV)")
# plt.plot([0.0093,0.013],[10,10],c="grey")
# plt.fill_between([0.0093,0.013],[10,10],alpha=0.3,fc="grey")

# plt.text(0.01,11.5,"$r_{bar}$")
# plt.plot([0.0093,0.013],[10.5,10.5],c="black",linestyle="dashed")
# plt.plot([0.0093,0.0093],[10.3,10.7],c="black")
# plt.plot([0.013,0.013],[10.3,10.7],c="black")

# lns = denln+tline
# labs = [l.get_label() for l in lns]
# plt.legend(lns, labs, loc=0)


# plt.savefig('initCond.png',bbox_inches="tight")

print(zoneTi[55])

f.close()

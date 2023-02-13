# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 14:48:02 2023

@author: Jack Shaw
"""

import sys
from netCDF4 import Dataset
import matplotlib.pyplot as plt

def main(inputFileName):
    #takes system input and reads the given file which should contain the cdf files to be processed
    inputfiles = open(inputFileName, "r").readlines()
    print("Processing files; ")
    for f in inputfiles:
        print(f[0:-1])
    
    f = inputfiles[0]
    rhoR=[]
    Hs_Tion=[]
    TNproduced=[]
    for f in inputfiles:
        #removing newline character
        f=f[0:-1]
        rhoR.append(get_Hs_rhoR(f))
        Hs_Tion.append(get_Hs_Tion(f))
        TNproduced.append(get_energy_produced(f))
    
    gen_rhoR_T_graph(rhoR, Hs_Tion, TNproduced)
   
#generates a graph in rhoR, T space of the energy produced
def gen_rhoR_T_graph(x, y, z):
    fig =plt.figure()
    plt.scatter(x,y, linewidths=1, alpha=.7,edgecolor='k',s=200,c=z)
    plt.show
   
#sums the produced TN energy in each zone at the final post prcessor dump time and returns the value
def get_energy_produced(filename):
    print("Getting energy produced from: " + filename)
    f = Dataset(filename,mode='r')
    
    #Array of dump times i.e. times at which data is put into the ppf/cdf file
    dumpTime = f.variables["DumpTimes"][:]
    
    #total thermonuclear energy production in zone in erg
    productionTN = f.variables["Bpeprd"][:]

    totalTNproduced = sum(productionTN[len(dumpTime)-1])
    return totalTNproduced

#Reads a file finds the hotspot density and radius and calculates the rhoR value.
#The density is assumed to be constant initially
#returns hotspot rhoR
def get_Hs_rhoR(filename):
    print("Getting Hotspot temperature from: " + filename)
    f = Dataset(filename,mode='r')
    
    HsEndZone = 0
    
    #Hotspot radius is determined by finding at which zone the temperature changes 
    zoneTi = f.variables["Ti"][0]

    for i in range(len(zoneTi)):
        if i+1 < len(zoneTi):
            if zoneTi[i]>zoneTi[i+1]:
                HsEndZone = i
                break
        
    density = f.variables["Rho"][0][HsEndZone]
    radius = f.variables["R"][0][HsEndZone+1] #Radius of the end of the hotspot i.e. mesh position at hs end
    
    rhoR = density*radius
    f.close()
    return rhoR


#Reads a file and returns the temperature of the 1st zone at the begining of the problem
def get_Hs_Tion(filename):
    print("Getting Hotspot temperature from: " + filename)
    f = Dataset(filename,mode='r')
    
    #zone ion temperature in keV
    Temp = f.variables["Ti"][0][0]
    
    f.close()
    return Temp
    
#if __name__ == "__main__":
#    a = sys.argv[1]
main("inputFiles.txt")
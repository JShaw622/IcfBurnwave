# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 19:29:51 2023

@author: Jack Shaw
"""
from netCDF4 import Dataset
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.odr import *
from matplotlib import rc

rc('font', **{'family': 'serif', 'serif': ['Computer Modern']})
rc('text', usetex=True)

def main(path1, path2, inputFileName):
    #takes system input and reads the given file which should contain the cdf files to be processed
    inputfile1 = open(path1+inputFileName, "r").readlines()
    inputfile2 = open(path2+inputFileName, "r").readlines()
    
    
    HsRhoR_1, HsT_1, TNRate_1 = getData(inputfile1)
    HsRhoR_2, HsT_2, TNRate_2 = getData(inputfile2)
    
    #print(HsRhoR_1)
    
    atRhoR= 0.78
    Tslice_1 = getRhoRSlice(atRhoR, HsRhoR_1, HsT_1)
    EprodSlice_1 =getRhoRSlice(atRhoR, HsRhoR_1,TNRate_1)
    
    Tslice_2 = getRhoRSlice(atRhoR, HsRhoR_2, HsT_2)
    EprodSlice_2 =getRhoRSlice(atRhoR, HsRhoR_2,TNRate_2)
    
    Tslices = [Tslice_1,Tslice_2]
    EprodSlices= [EprodSlice_1,EprodSlice_2]
    
    produceGraph(Tslices,EprodSlices,1.5,atRhoR)
    
    
def getData(inputfiles):
    print("Processing files; ")
    for i in inputfiles:
        print(i[0:-1])
    
    Hs_rhoR=[]
    Hs_Tion=[]
    TNproduceRate=[]
    i=0
    for f in inputfiles:
        i+=1
        #removing newline character
        f=f[0:-1]
        Hs_rhoR.append(get_HS_rhoR(f))
        Hs_Tion.append(get_Hs_Tion(f))
        TNproduceRate.append(get_energy_prodRate(f))
        
        #if TNproduceRate[i-1] !=0:
            #print(f,Hs_rhoR[i-1], Hs_Tion[i-1], TNproduceRate[i-1])
    return Hs_rhoR, Hs_Tion, TNproduceRate

def getRhoRSlice(value, valueArray, variableArray):
    i=0
    sliceArray=[]
    for x in valueArray:
        if x == value:
          sliceArray.append(variableArray[i])
        i+=1
    
    return sliceArray
    
def produceGraph(xs,ys,Xerror, hsValue):
    ###### Ensure x and y are numpy arrays
    x1 = np.array(xs[0])
    y1= np.array(ys[0])
    
    x2=np.array(xs[1])
    y2= np.array(ys[1])
    
    fig = plt.figure(dpi=300)
    ax =fig.add_subplot()
    
    ax.scatter(x1,np.log(y2),marker="^",c="Green",linewidth=1,label="No barrier")
    ax.errorbar(x1,np.log(y2),xerr=Xerror, linestyle="None",capsize=2,c="green",linewidth=1)
    
    ax.scatter(x1,np.log(y1),marker="x",c="black",linewidth=1,label="Fe barrier ($\\rho r_{bar}=1\\times10^{-8}$ kgm$^{-2}$)")
    ax.errorbar(x1,np.log(y1),xerr=Xerror, linestyle="None",capsize=2,c="black",linewidth=1)

    ax.plot([],[],' ',label="Hot spot: \n$\\rho r_{hs}=("+str(round(round(hsValue,2)*10,1))+"\\pm 0.7)\\times 10^{-8}$ kgm$^{-2}$")
 
    ax.tick_params(axis="both",which="both",direction="in",top=True, right=True)
    plt.minorticks_on()
    ax.set_xlabel("$T$ (KeV)")
    ax.set_ylabel("$\\ln(P_{Tn})$")
    ax.set_ylim([40, 65])
    plt.legend(handlelength=1,fontsize=12)
    plt.savefig("T_logE_"+str(int(100*round(hsValue,2)))+".png",bbox_inches="tight")
    plt.show()
    
#reads inf file to find barrier radius and density    
def get_Bar_rhoR(filename):
    #convert filename from .cdf to .inf
    filename = filename[0:-4]+".inf"
    #open file convert to array of lines in file and close the file to save memory
    file = open(filename, "r")
    f = file.readlines()
    file.close()
    
    ##### FIND BARRIER THICKNESS #####
    #read the radius of the hotspot from file
    Hs_Rad = float((f[6])[-7:-1])
    
    #read the radius of the end of the barrier from file
    BarEnd_Rad= float((f[13])[-7:-1])
    
    Bar_rad = round(BarEnd_Rad-Hs_Rad,5)
    
    
    ##### FIND BARRIER DENSITY #####
    text = "DEFINE BDensity "
    Bar_rho = float(f[16].replace(text, ""))
    
    ###### Calculate and return the rhoR of the barrier #####
    rhoR = round(Bar_rad*Bar_rho,5)
    
    return (rhoR)
    
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
      
#sums the produced TN energy in each zone at the final post prcessor dump time and returns the value
def get_energy_prodRate(filename):
    try:
        #print("Getting energy produced from: " + filename)
        f = Dataset(filename,mode='r')
    except:
        print("\n*****\n Error reading: " +filename+"\n******\n")
        return 0
    
    #Array of dump times i.e. times at which data is put into the ppf/cdf file
    dumpTime = f.variables["DumpTimes"][:]
    
    #total thermonuclear energy production in zone in erg
    productionTN = f.variables["Bpeprd"][:]
    totalTNproduced = sum(productionTN[len(dumpTime)-1])
    
    ##### Find average energy production per second #####
    productionRate = totalTNproduced/dumpTime[-1]
    return productionRate


#Reads a file and returns the temperature of the 1st zone at the begining of the problem
def get_Hs_Tion(filename):
    #convert filename from .cdf to .inf
    filename = filename[0:-4]+".inf"
    #open file convert to array of lines in file and close the file to save memory
    file = open(filename, "r")
    f = file.readlines()
    file.close()
    
    ##### FIND HS temp #####
    text = "DEFINE HsT "
    Temp = float((f[8].replace(text, "")))
    
    return Temp
    
#if __name__ == "__main__":
#    a = sys.argv[1]

PathFe = "data/TAnalysis/Fe/"
PathNoBar="data/TAnalysis/NoBar/"
main(PathFe,PathNoBar,"inputFiles.txt")

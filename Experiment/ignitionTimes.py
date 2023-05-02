# -*- coding: utf-8 -*-
"""
Created on Mon May  1 22:39:40 2023

@author: SprongusThree
"""
import sys
from netCDF4 import Dataset
import pandas as pd
import seaborn as sns
from pylab import *
import matplotlib.pyplot as plt
from scipy.odr import *
from matplotlib import rc

hyades_file = 'data/TAnalysis/noBar/test_T_10_19_19.cdf'#"originalinput.cdf"
hyades_file="IgnitionCDFFiles.csv"

def getEproduced(file):
    try:
        f      = Dataset(file,mode='r') #open the file "hyades_file" in read mode
    except:
        print("Error reading:",file)
        return [0,0],[0,0,0]

    #total thermonuclear energy production in zone in erg
    productionTN = f.variables["Bpeprd"][:]

    #Array of dump times i.e. times at which data is put into the ppf/cdf file
    dumpTime = f.variables["DumpTimes"][:]

    numTimes = len(f.dimensions["NumTimes"])
    #print(file)
    
    hotspotTemp=f.variables["Ti"][0][0]
    
    #total thermonuclear energy production in zone in erg
    productionTN = f.variables["Bpeprd"][:]
    totalTNproduced = sum(productionTN[len(dumpTime)-1])
    #print(totalTNproduced)
    f.close()
    
    TNArray=[]
    for i in range(1,numTimes):
        currentTNproduced = sum(productionTN[i])
        TNArray.append(currentTNproduced)
        
    return np.array(TNArray), dumpTime, hotspotTemp

def findIgnitionTime(data, times):
    for i in range(len(data)):
        value =data[i]
        if value>100:
            print("ignition at:", times[i])
            return times[i]

def getIgnTimes(path, inputFileName, ignFile):
    inputfiles = open(path+inputFileName, "r").readlines()
    #print("Processing files; ")
    #for i in inputfiles:
    #    print(i[0:-1])
        
    ignData = df=pd.read_csv(ignFile)
    ignIndex=ignData["ignIndex"]
    #print(inputfiles[380])
    #fig = plt.figure(dpi=300)
    #ax = fig.add_subplot()    
    ignitionTimes=[]
    temps=[]
    for i in ignIndex:
        i=int(i)
        #f=inputfiles[int(i)][:-1]

        #print(i)
        try:
            f=inputfiles[int(i-1)][:-1]
            TN1, time, hs1=getEproduced(f) 
            f=inputfiles[int(i)][:-1]
            TN2, time, THs=getEproduced(f)
            increase = TN2/TN1
            #ax.scatter(time[:-1],np.log(increase), label="Ign")
            ignitionTimes.append(findIgnitionTime(increase,time))
            temps.append(THs)
        except:
            print("Error @: ", i)
            
    return ignitionTimes, temps
    

PATH="data/TAnalysis/noBar/"
inputfile="inputfiles.txt"
ignDatafile=PATH+"noBar.csv"
noBarIgnTimes,noBarTemps=getIgnTimes(PATH,inputfile,ignDatafile)

PATH="data/TAnalysis/Fe/"
inputfile="inputfiles.txt"
ignDatafile=PATH+"Fe.csv"
FeIgnTimes,FeTemps=getIgnTimes(PATH,inputfile,ignDatafile)


fig = plt.figure(dpi=300)
ax = fig.add_subplot()  

ax.errorbar(noBarTemps,noBarIgnTimes,xerr=1.5,yerr=0,linestyle="none",capsize=2,marker="^",c="g")
ax.errorbar(FeTemps,FeIgnTimes,xerr=1.5,yerr=0,linestyle="none",capsize=2,marker="x",c="black")
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 12:49:02 2023

@author: Jack Shaw

This will produce graphs of parameter sweeps so long as the input files and cdf files are included
"""
import sys
from netCDF4 import Dataset
import pandas as pd
import seaborn as sns
from pylab import *
import matplotlib.pyplot as plt


def main(inputFileName):
    #takes system input and reads the given file which should contain the cdf files to be processed
    inputfiles = open(inputFileName, "r").readlines()
    print("Processing files; ")
    for i in inputfiles:
        print(i[0:-1])
    
    Hs_rhoR=[]
    Hs_Tion=[]
    Bar_rhoR=[]
    TNproduceRate=[]
    i=0
    for f in inputfiles:
        i+=1
        #removing newline character
        f=f[0:-1]
        Hs_rhoR.append(get_HS_rhoR(f))
        Bar_rhoR.append(get_Bar_rhoR(f))
        TNproduceRate.append(get_energy_prodRate(f))
        
        if TNproduceRate[i-1] !=0:
            print(f,Hs_rhoR[i-1], Bar_rhoR[i-1], TNproduceRate[i-1])
    
    calc_TNchange(TNproduceRate)
    
    gen_heatmap(Hs_rhoR, Bar_rhoR, TNproduceRate, xLabel="Hot spot \u03C1r ($gcm^{-2}$)", yLabel="Barrier \u03C1r ($gcm^{-2}$)")

def calc_TNchange(TNArray):
    diffArray=[]
    for i in range(len(TNArray)-1):
        diff = TNArray[i+1]-TNArray[i]
        #print(diff)
        
        diffArray.append(diff)
    
    TNFig = plt.figure()
    plt.scatter(range(len(diffArray)),diffArray)
    #plt.plot(TNArray)
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


#generates a graph in rhoR, T space of the energy produced
def gen_heatmap(x, y, z, xLabel="X", yLabel="Y", zLabel="TN energy production rate ($erg/s$)"):
    #makes a dictonary out of the labels to be set as dataframe index column and value names
    columnDict = [xLabel,yLabel,zLabel]
    
    #Puts data into a pandas dataframe for seaborn plotting as a heatmap
    df = pd.DataFrame.from_dict(np.array([x,y,z]).T)
    df.columns = columnDict
    pivotted= df.pivot(index=yLabel,columns=xLabel,values=zLabel)
    #print(pivotted)
    pivotted = pivotted.sort_values(yLabel,ascending=False)    
    
    ax = sns.heatmap(pivotted,cmap='magma', vmin=0,cbar_kws={'label':zLabel})
    #ax.set_xticks(range(0,10),np.around((df['X_value'].tolist()[0:10]),3))
    
    #plt.scatter(x[0:500],y[0:500], linewidths=1, alpha=.7,edgecolor='k',s=20,c=z[0:500])
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
   #plt.title("FLXLRM 1.00")
    plt.show()
   
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
    #print("Getting Hotspot temperature from: " + filename)
    f = Dataset(filename,mode='r')
    
    #zone ion temperature in keV
    Temp = f.variables["Ti"][0][0]
    
    f.close()
    return Temp
    
#if __name__ == "__main__":
#    a = sys.argv[1]
Path = "data/SmallRuns2/Ag/"
main(Path+"inputFiles.txt")

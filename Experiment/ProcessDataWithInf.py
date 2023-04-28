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
from scipy.odr import *
from matplotlib import rc

rc('font', **{'family': 'serif', 'serif': ['Computer Modern']})
rc('text', usetex=True)

def func (x, a, b, c, d):
    x=np.array(x)
    return a*np.exp(-b*(x-d))+c

def straightFit(p,x):
    m,c=p
    x=np.array(x)
    return m*x+c

def main(path, inputFileName, outputFilename):
    #takes system input and reads the given file which should contain the cdf files to be processed
    inputfiles = open(path+inputFileName, "r").readlines()
    print("Processing files; ")
    for i in inputfiles:
        print(i[0:-1])
    
    Hs_rhoR=[]
    Hs_Tion=[]
    Bar_rhoR=[]
    TNproduceRate=[]
    Temp=[]
    i=0
    for f in inputfiles:
        i+=1
        #removing newline character
        f=f[0:-1]
        Hs_rhoR.append(get_HS_rhoR(f))
        #Bar_rhoR.append(get_Bar_rhoR(f))
        Temp.append(get_Hs_Tion(f))
        TNproduceRate.append(get_energy_prodRate(f)/(10**7))
        
        if TNproduceRate[i-1] !=0:
            print(f,Hs_rhoR[i-1], Temp[i-1], TNproduceRate[i-1])
    
    #outputs the critical RhoR for ignition into a csv file:
    ignitionIndexArray=calc_TNchange(TNproduceRate)
    xerrorValue = (Hs_rhoR[1]-Hs_rhoR[0])/2
    IgnitionBoundryX, IgnitionBoundryY, xerror, yerror=print_criticalRhoR(ignitionIndexArray,inputfiles,xerrorValue, path+outputFilename)        
    
    gen_heatmap(Hs_rhoR, Temp, TNproduceRate,IgnitionBoundryX,IgnitionBoundryY,xerror,yerror, xLabel="Hot spot $\\rho r (\\times 10^{-7}$kgm$^{-2})$", yLabel="Initial $T_{hs}$ (KeV)")

def print_criticalRhoR(index,files,error,outputFilename="OUTPUTFILE.csv"):
    #Consider only the files with input index
    print("\nIgnition in files:")
    Hs_rhoR=[]
    Bar_rhoR=[]
    xerr=[]
    yerr=[]
    i=0
    for x in index:
        f=files[x]
        xerr.append(error)
        yerr.append(1.5)
        #removes newline character
        f=f[0:-1]
        Hs_rhoR.append(get_HS_rhoR(f))
        Bar_rhoR.append(get_Hs_Tion(f))
        print(f+" $\\rho r_{hs}$: "+str(Hs_rhoR[i])+" $\\rho r_{bar}$: "+str(Bar_rhoR[i]))
        i+=1
        
    df=pd.DataFrame(np.array([Hs_rhoR,xerr,Bar_rhoR,yerr]).T)
    df.columns=["$\\rho r_{hs}$","$\\delta \\rho r_{hs}$","$T_{hs}$","\\delta T_{hs}"]
    print(df)
    
    df.to_csv(outputFilename)
    
    return Hs_rhoR, Bar_rhoR, xerr, yerr

def calc_TNchange(TNArray):
    #Array stores index of first instance of ignition.
    ignitionIndexArr=[]
    
    newline=True
    diffArray=[]
    for i in range(len(TNArray)-1):
        if TNArray[i]==0:
            print("Error in TNArray: ", i+1)
            diff=0
        else:
            diff = TNArray[i+1]-TNArray[i]
            #print(diff)
        
        diffArray.append(diff)
        try:
            #print(diff/TNArray[i])
            if diffArray[i]>0:
                if diff/TNArray[i] >=100:
                    if newline:
                        print("Ignition at: "+str(i+1))
                        ignitionIndexArr.append(i+1)
                        newline=False
            else:
                newline=True
        except:
            print("No change ")
            
    TNFig = plt.figure()
    plt.scatter(range(len(diffArray)),diffArray)
    #plt.plot(TNArray)
    plt.show()
    return ignitionIndexArr
    

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
def gen_heatmap(x, y, z,ignX,ignY,xErr,yErr, xLabel="X", yLabel="Y", zLabel="Fusion energy production rate (J s$^{-1}$)"):
    #makes a dictonary out of the labels to be set as dataframe index column and value names
    columnDict = [xLabel,yLabel,zLabel]
    
    #Puts data into a pandas dataframe for seaborn plotting as a heatmap
    df = pd.DataFrame.from_dict(np.array([x,y,z]).T)
    df.columns = columnDict
    #print(df)
    pivotted= df.pivot(index=yLabel,columns=xLabel,values=zLabel)
    #print(pivotted)
    pivotted = pivotted.sort_values(yLabel,ascending=False)    
    
    fig1 = plt.figure(dpi=300)
    ax = sns.heatmap(pivotted,cmap='magma', vmin=0, vmax=2*10**20,cbar_kws={'label':zLabel})
    #ax.set_xticks(range(0,10),np.around((df['X_value'].tolist()[0:10]),3))
    
    #plt.scatter(x[0:500],y[0:500], linewidths=1, alpha=.7,edgecolor='k',s=20,c=z[0:500])
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
   #plt.title("FLXLRM 1.00")
    plt.savefig('heatmapTRhoR_NoBar.png',bbox_inches="tight") 
    plt.show()
    
    
    
    #### log log plot stuff
    ignX=np.array(ignX)
    ignY=np.array(ignY)
    xErr=np.array(xErr)
    yErr=np.array(yErr)
    
    ###### sort the arrays into decreasing numerical order
    arr1inds = np.array(ignX).argsort()
    ignX=ignX[arr1inds[::-1]]
    xErr=xErr[arr1inds[::-1]]
    ignY=ignY[arr1inds[::-1]]
    yErr=yErr[arr1inds[::-1]]
    print(ignX)
    
    fig = plt.figure(dpi=300)
    ax =fig.add_subplot()
    
    ax.scatter(np.log(ignX),np.log(ignY),marker="x",c="black",linewidth=1)
    
    logXerror = np.array(xErr)/np.array(ignX)
    logYerror = np.array(yErr)/np.array(ignY)
    ax.errorbar(np.log(ignX),np.log(ignY),xerr=logXerror,yerr=logYerror, linestyle="None",capsize=2,c="black",linewidth=1)

    linearModel = Model(straightFit)    

    Data=RealData(np.log(ignX),np.log(ignY),sx=logXerror,sy=logYerror)
    odr=ODR(Data,linearModel,beta0=[-3,4])
    
    modelOutput=odr.run()
    
    fitY=straightFit(modelOutput.beta, np.log(ignX))
    
    upperBeta = modelOutput.beta+modelOutput.sd_beta
    lowerBeta= modelOutput.beta-modelOutput.sd_beta
    
    upperFitY=straightFit(upperBeta,np.log(ignX))
    lowerFitY=straightFit(lowerBeta,np.log(ignX))

    modelOutput.pprint()
    
    line1=r"Fit: $y=mx+c$" + "\n"
    eqnStart=r"\begin{eqnarray*}"
    line2 =r"y&=&mx+c"+"\\\\"
    line3 =r"m&=&"+str(round(modelOutput.beta[0],1))+"\pm "+str(round(modelOutput.sd_beta[0],1))+"\\\\"
    line4=r"c&=&"+str(round(modelOutput.beta[1],2))+"\pm"+str(round(modelOutput.sd_beta[1],2))+"\\\\"
    eqnEnd= r"\end{eqnarray*}"
    
    fitlabel=line1+eqnStart+line3+line4+eqnEnd
    
    ax.plot(np.log(ignX),fitY, c="r", linestyle="dashed",label=fitlabel)
    ax.plot(np.log(ignX),upperFitY, c="g", linestyle="dotted")
    ax.plot(np.log(ignX),lowerFitY, c="g", linestyle="dotted")
    ax.fill_between(np.log(ignX), upperFitY, lowerFitY, facecolor="gray", alpha=0.5)
    
    #ax.axhline(np.log(5), linestyle="dashed", c="orange")
    
    ax.tick_params(axis="both",which="both",direction="in",top=True, right=True)
    plt.minorticks_on()
    ax.set_xlabel("$\\ln(\\rho r_{hs})$")
    ax.set_ylabel("$\\ln(T_{0,hs})$")
    plt.legend(handlelength=1)
    ax.set_ylim([-0.5, 4.1])
    plt.savefig('loglogTRhoR_Fe.png',bbox_inches="tight")
    plt.show()
    
    
    #popt, pcov = curve_fit(straightFit,np.log(ignX),np.log(ignY))
    #ax.plot(np.log(ignX),straightFit(np.log(ignX),*popt))
    #print(popt)
    #testx=np.arange(0.5, 1.8,0.1)
    #testy=1/(testx**(1.5))
    #ax.plot(np.log(testx),np.log(testy)+2.5)
    #ax.plot(ignX,func(ignX,1,5,4.2,2))
    #ax.set_ylim([0, 60])

    
   
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
Path = "data/TAnalysis/Fe/"
outputName = "Fe.csv"
main(Path,"inputFiles.txt",outputName)

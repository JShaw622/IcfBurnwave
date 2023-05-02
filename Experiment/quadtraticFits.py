# -*- coding: utf-8 -*-
"""
Created on Mon May  1 21:11:06 2023

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
from matplotlib.legend_handler import HandlerTuple
import matplotlib.lines as mlines

rc('font', **{'family': 'serif', 'serif': ['Computer Modern']})
rc('text', usetex=True)

def quadfit(p,x):
    m,c = p
    x=np.array(x)
    return m*1/((x)**(2.06555679))+c

def getDataPoints(f):
    df=pd.read_csv(f)
    return df

def getFitPrams(x,y,xerr,yerr, beta):
    realData=RealData(x,y,sx=xerr,sy=yerr)
    odr=ODR(realData,mod,beta0=beta)
    output=odr.run()
    output.pprint()
    
    return output.beta, output.sd_beta

file1="data/TAnalysis/NoBar/NoBar.csv"
file2="data/TAnalysis/Fe/Fe.csv"
#file3="data/TAnalysis/C/C.csv"

noBarData= getDataPoints(file1)[::-1]
FeData= getDataPoints(file2)[::-1]
#CData= getDataPoints(file3)[::-1]

Terror=1.5
rError=0.07

feYerr= Terror/FeData["$T_{hs}$"]
feXerr= rError/FeData["$\\rho r_{hs}$"]

noBarYerr= Terror/noBarData["$T_{hs}$"]
noBarXerr= rError/noBarData["$\\rho r_{hs}$"]

#CYerr= Terror/CData["$T_{hs}$"]
#CXerr= rError/CData["$\\rho r_{hs}$"]

mod = Model(quadfit)

noBarGuess = [np.exp(2.45397654),2]
FeGuess = [np.exp(3.26611662),2]
CGuess = [np.exp(4.93336567),2]
noBarBeta, noBarErr = getFitPrams(noBarData["$\\rho r_{hs}$"],noBarData["$T_{hs}$"], noBarXerr, noBarYerr,noBarGuess)
FeBeta, FeErr = getFitPrams(FeData["$\\rho r_{hs}$"],FeData["$T_{hs}$"], feXerr, feYerr, FeGuess)
#CBeta, CErr = getFitPrams(CData["$\\rho r_{hs}$"],CData["$T_{hs}$"], CXerr, CYerr)


fig = plt.figure(dpi=300)
ax = fig.add_subplot()
ax.set_ylim(0, 60)

x=np.arange(0.4,3,0.01)

ax.errorbar(noBarData["$\\rho r_{hs}$"],noBarData["$T_{hs}$"],xerr=rError,yerr=Terror,linestyle="none",marker="^",capsize=2,c="g")
ax.errorbar(FeData["$\\rho r_{hs}$"],FeData["$T_{hs}$"],xerr=rError,yerr=Terror,linestyle="none",marker="x",capsize=2,c="black")

ax.plot(x,quadfit(noBarBeta, x),c="green")
ax.plot(x,quadfit(FeBeta,x),c="black")



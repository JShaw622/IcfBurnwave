# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 21:11:21 2023

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

class HandlerTupleVertical(HandlerTuple):
    def __init__(self, **kwargs):
        HandlerTuple.__init__(self, **kwargs)

    def create_artists(self, legend, orig_handle,
                       xdescent, ydescent, width, height, fontsize, trans):
        # How many lines are there.
        numlines = len(orig_handle)
        handler_map = legend.get_legend_handler_map()

        # divide the vertical space where the lines will go
        # into equal parts based on the number of lines
        height_y = (height / numlines)

        leglines = []
        for i, handle in enumerate(orig_handle):
            handler = legend.get_legend_handler(handler_map, handle)

            legline = handler.create_artists(legend, handle,
                                             xdescent,
                                             (2*i + 4)*height_y,
                                             width,
                                             2*height,
                                             fontsize, trans)
            leglines.extend(legline)

        return leglines


def straightFit(p,x,err):
    m, c =p
    m=m+err[0]
    c=c+err[1]
    x=np.array(x)
    return m*x+c

def straightFitMod(p,x):
    m, c =p
    x=np.array(x)
    return m*x+c


def getDataPoints(f):
    df=pd.read_csv(f)
    return df

file1="data/TAnalysis/NoBar/NoBar.csv"
file2="data/TAnalysis/Fe/Fe.csv"
file3="data/TAnalysis/C/C.csv"

noBarData= getDataPoints(file1)[::-1]
FeData= getDataPoints(file2)[::-1]
CData= getDataPoints(file3)[::-1]

print(FeData)

Terror=1.5
rError=0.07

feYerr= Terror/FeData["$T_{hs}$"]
feXerr= rError/FeData["$\\rho r_{hs}$"]
#print(FeData["$\\rho r_{hs}$"],feXerr)

#print(0.15/FeData["$\\rho r_{hs}$"][0])
#for i in range(len(FeData["$\\rho r_{hs}$"])):
#    print(feXerr[i],rError/FeData["$\\rho r_{hs}$"][i])

noBarYerr= Terror/noBarData["$T_{hs}$"]
noBarXerr= rError/noBarData["$\\rho r_{hs}$"]

CYerr= Terror/CData["$T_{hs}$"]
CXerr= rError/CData["$\\rho r_{hs}$"]

linearModel = Model(straightFitMod)    

print("No Barrier Data")
# noBarPoints = dict(zip(
#     noBarData["$\\rho r_{hs}$"],noBarData["$T_{hs}$"]
# ))
NoBarXpoints, NoBarYpoints=noBarData["$\\rho r_{hs}$"],noBarData["$T_{hs}$"]

# Output keys (equivalent of new_list1)
#print(list(noBarPoints.keys()))
# Output values (equivalent of new_list2)
#print(list(noBarPoints.values()))
#NoBarXpoints=np.array(list(noBarPoints.keys()))
#NoBarYpoints=np.array(list(noBarPoints.values()))

DataforNo=RealData(np.log(NoBarXpoints),np.log(NoBarYpoints),sx=noBarXerr,sy=noBarYerr)
odrforNo=ODR(DataforNo,linearModel,beta0=[-2,2])
modelOutputNo=odrforNo.run()
modelOutputNo.pprint()
noBarBeta=modelOutputNo.beta
noBarErr=modelOutputNo.sd_beta

print("~~~~~~~~\nFe Data")
# fePoints = dict(zip(
#     FeData["$\\rho r_{hs}$"],FeData["$T_{hs}$"]
# ))
feXpoints= FeData["$\\rho r_{hs}$"]
feYpoints = FeData["$T_{hs}$"]

# Output keys (equivalent of new_list1)
#print(list(fePoints.keys()))
# Output values (equivalent of new_list2)
#print(list(fePoints.values()))
#feXpoints=np.array(list(fePoints.keys()))
#feYpoints=np.array(list(fePoints.values()))   
DataforIron=RealData(np.log(feXpoints),np.log(feYpoints),sx=feXerr,sy=feXerr)
odrforIron=ODR(DataforIron,linearModel,beta0=[-2,3])
modelOutputIron=odrforIron.run()
modelOutputIron.pprint()
feBeta=modelOutputIron.beta
feErr=modelOutputIron.sd_beta

print("~~~~~~~~\nC Data")
# fePoints = dict(zip(
#     FeData["$\\rho r_{hs}$"],FeData["$T_{hs}$"]
# ))
CXpoints= CData["$\\rho r_{hs}$"]
CYpoints = CData["$T_{hs}$"]

# Output keys (equivalent of new_list1)
#print(list(fePoints.keys()))
# Output values (equivalent of new_list2)
#print(list(fePoints.values()))
#feXpoints=np.array(list(fePoints.keys()))
#feYpoints=np.array(list(fePoints.values()))   
DataforC=RealData(np.log(CXpoints),np.log(CYpoints),sx=CXerr,sy=CXerr)
odrforC=ODR(DataforC,linearModel,beta0=[-2,3])
modelOutputC=odrforC.run()
modelOutputC.pprint()
CBeta=modelOutputC.beta
CErr=modelOutputC.sd_beta

x=np.arange(0.49,2.85,0.01)
#FefitY=straightFit(modelOutputIron.beta, np.log(x), [0,0])
#NoBarfitY=straightFit(modelOutputNo.beta, np.log(x), [0,0])


fig = plt.figure(dpi=300)
ax = fig.add_subplot()

#ax.plot(np.log(x),FefitY)
#ax.plot(np.log(x),NoBarfitY)

#noBarPoints = ax.scatter(np.log(noBarData["$\\rho r_{hs}$"]),np.log(noBarData["$T_{hs}$"]),c="green",marker="^")
#fePoints = ax.scatter(np.log(FeData["$\\rho r_{hs}$"]),np.log(FeData["$T_{hs}$"]),c="black",marker="x",label="Fe")

#ax.errorbar(np.log(noBarData["$\\rho r_{hs}$"]),np.log(noBarData["$T_{hs}$"]),xerr=0.07/noBarData["$\\rho r_{hs}$"],yerr=1.5/noBarData["$T_{hs}$"],linestyle="none",c="green",marker="^",capsize=2)
#ax.errorbar(np.log(FeData["$\\rho r_{hs}$"]),np.log(FeData["$T_{hs}$"]),xerr=0.07/FeData["$\\rho r_{hs}$"],yerr=1.5/FeData["$T_{hs}$"],linestyle="none",c="black",marker="x",capsize=2,label="Fe")

line1=r"Fit: $y=mx+c$" + "\n"
eqnStart=r"\begin{eqnarray*}"
line2 =r"y&=&mx+c"+"\\\\"
line3 =r"m&=&"+str(feBeta[0])+"\pm "+str(feErr[0])+"\\\\"
line4=r"c&=&"+str(feBeta[1])+"\pm"+str(feBeta[1])+"\\\\"
eqnEnd= r"\end{eqnarray*}"

fitlabel=line1+eqnStart+line3+line4+eqnEnd

upperFe=straightFit(feBeta,np.log(x),feErr)
lowerFe=straightFit(feBeta,np.log(x),feErr*-1)

upperNoBar=straightFit(noBarBeta,np.log(x),noBarErr)
lowerNoBar=straightFit(noBarBeta,np.log(x),noBarErr*-1)

upperC=straightFit(CBeta,np.log(x),CErr)
lowerC=straightFit(CBeta,np.log(x),CErr*-1)

ax.plot(np.log(x),straightFit(feBeta,np.log(x),[0,0]), c="r", linestyle="dashed")
ax.plot(np.log(x),upperFe, c="r", linestyle="dotted",alpha=0.5)
ax.plot(np.log(x),lowerFe,c="r", linestyle="dotted",alpha=0.5)
ax.fill_between(np.log(x),upperFe,lowerFe,facecolor="gray", alpha=0.5)

ax.plot(np.log(x),straightFit(noBarBeta,np.log(x),[0,0]),c="b",linestyle="dashed")
ax.plot(np.log(x),upperNoBar, c="b", linestyle="dotted",alpha=0.5)
ax.plot(np.log(x),lowerNoBar,c="b", linestyle="dotted",alpha=0.5)
ax.fill_between(np.log(x),upperNoBar,lowerNoBar,facecolor="gray", alpha=0.5)

ax.plot(np.log(x),straightFit(CBeta,np.log(x),[0,0]),c="m",linestyle="dashed")
ax.plot(np.log(x),upperC, c="m", linestyle="dotted",alpha=0.5)
ax.plot(np.log(x),lowerC,c="m", linestyle="dotted",alpha=0.5)
ax.fill_between(np.log(x),upperC,lowerC,facecolor="gray", alpha=0.5)

fePoints=          ax.scatter(np.log(feXpoints),np.log(feYpoints),c="black",marker="x")
noBarPoints =      ax.scatter(np.log(NoBarXpoints),np.log(NoBarYpoints),c="green",marker="^")
CPoints =          ax.scatter(np.log(CXpoints),np.log(CYpoints),c="c",marker="*")

noBarErrorPoints = ax.errorbar(np.log(NoBarXpoints),np.log(NoBarYpoints),xerr=noBarXerr,yerr=noBarYerr,linestyle="none",c="green",marker="^",capsize=2)
feErrorPoints=     ax.errorbar(np.log(feXpoints),np.log(feYpoints), xerr=feXerr,yerr=feYerr,linestyle="none",c="black",marker="x",capsize=2)
feErrorPoints=     ax.errorbar(np.log(CXpoints),np.log(CYpoints), xerr=CXerr,yerr=CYerr,linestyle="none",c="c",marker="*",capsize=2)

#ax.plot(np.log(ignX),upperFitY, c="g", linestyle="dotted")
#ax.plot(np.log(ignX),lowerFitY, c="g", linestyle="dotted")
#ax.fill_between(np.log(ignX), upperFitY, lowerFitY, facecolor="gray", alpha=0.5)

#ax.axhline(np.log(5), linestyle="dashed", c="orange")

ax.tick_params(axis="both",which="both",direction="in",top=True, right=True)
plt.minorticks_on()
ax.set_xlabel("$\\ln(\\rho r_{hs})$")
ax.set_ylabel("$\\ln(T_{0,hs})$")
ax.set_ylim([0.2,4.1])

feFit = mlines.Line2D([],[], c="r", linestyle="dashed")
noBarFit = mlines.Line2D([],[], c="b", linestyle="dashed")

###################### Legend labels ####################
l1="Fe Barrier:\n $\\rho r_{barrier}=1\\times10^{-8}$ kgm$^{-2}$\n$m="
l2=str(round(feBeta[0],1))+"\\pm"+str(round(feErr[0],1))+"$\n"
l3="$c\\;\\,="+str(round(feBeta[1],1))+"\\pm"+str(round(feErr[1],1))+"$"
IronLabel = l1+l2+l3

l1="No Barrier\n$m="
l2=str(round(noBarBeta[0],1))+"\\pm"+str(round(noBarErr[0],1))+"$\n"
l3="$c\\;\\,="+str(round(noBarBeta[1],2))+"\\pm"+str(round(noBarErr[1],2))+"$"
NoBarLabel = l1+l2+l3


l =ax.legend(handles=[(feFit,fePoints),(noBarFit,noBarPoints)],labels=[IronLabel,NoBarLabel],handler_map={tuple: HandlerTupleVertical(ndivide=None)})

plt.savefig('loglogTRhoR_NoBar_BOTH.png',bbox_inches="tight")
plt.show()
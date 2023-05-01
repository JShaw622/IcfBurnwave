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

noBarData= getDataPoints(file1)
FeData= getDataPoints(file2)

feXpoints=[2.85, 1.67, 1.23, 1.23, 1.08, 1.08, 1.08, 1.08, 0.93, 0.93, 0.93, 0.93, 0.93, 0.93, 0.93, 0.93, 0.93, 0.93, 0.93, 0.99, 0.99, 0.99, 0.91, 0.91, 0.91, 0.91, 0.91, 0.91, 0.91, 0.91, 0.91, 0.84, 0.84,
 0.84, 0.84, 0.84, 0.84, 0.84, 0.84, 0.84, 0.84]
feYpoints=[ 4.,  6.,  9., 11., 14., 16., 19., 22., 24., 50., 47., 29., 32., 35., 37., 40., 42., 45.,
 27.,21., 24., 25., 35., 26., 27., 29., 31., 32., 34., 36., 37., 49., 39., 40., 41., 42., 44.,
 45, 46, 47, 50]
feBeta=[-3.1,  3.28]
feErr=np.array([0.3,0.08])
noBarXpoints=[1.67, 1.23, 1.08, 0.93, 0.78, 0.78, 0.64, 0.64, 0.64, 0.64, 0.64, 0.64, 0.64, 0.64, 0.49, 0.49, 0.49, 0.49]
noBarBeta=[-1.9,  2.45]
noBarErr=np.array([0.2,0.07])

feXpoints=feXpoints[::-1]
feYpoints=feYpoints[::-1]


fePoints = dict(zip(
    feXpoints,feYpoints
))

# Output dictionary
print(fePoints)

# Output keys (equivalent of new_list1)
print(list(fePoints.keys()))

# Output values (equivalent of new_list2)
print(list(fePoints.values()))


feXpoints=np.array(list(fePoints.keys()))
feYpoints=np.array(list(fePoints.values()))

linearModel = Model(straightFitMod)    

Data=RealData(np.log(feXpoints),np.log(feYpoints),sx=0.07/feXpoints,sy=1.5/feYpoints)
odr=ODR(Data,linearModel,beta0=[-3,4])

modelOutput=odr.run()
modelOutput.pprint()

x=np.arange(0.49,2.85,0.01)
fitY=straightFit(modelOutput.beta, np.log(x), [0,0])



fig = plt.figure(dpi=300)
ax = fig.add_subplot()

ax.plot(np.log(x),fitY)

ax.scatter(np.log(feXpoints),np.log(feYpoints))

# noBarPoints = ax.scatter(np.log(noBarData["$\\rho r_{hs}$"]),np.log(noBarData["$T_{hs}$"]),c="green",marker="^")
# fePoints = ax.scatter(np.log(FeData["$\\rho r_{hs}$"]),np.log(FeData["$T_{hs}$"]),c="black",marker="x",label="Fe")

# ax.errorbar(np.log(noBarData["$\\rho r_{hs}$"]),np.log(noBarData["$T_{hs}$"]),xerr=0.07/noBarData["$\\rho r_{hs}$"],yerr=1.5/noBarData["$T_{hs}$"],linestyle="none",c="green",marker="^",capsize=2)
# ax.errorbar(np.log(FeData["$\\rho r_{hs}$"]),np.log(FeData["$T_{hs}$"]),xerr=0.07/FeData["$\\rho r_{hs}$"],yerr=1.5/FeData["$T_{hs}$"],linestyle="none",c="black",marker="x",capsize=2,label="Fe")

# line1=r"Fit: $y=mx+c$" + "\n"
# eqnStart=r"\begin{eqnarray*}"
# line2 =r"y&=&mx+c"+"\\\\"
# line3 =r"m&=&"+str(feBeta[0])+"\pm "+str(feErr[0])+"\\\\"
# line4=r"c&=&"+str(feBeta[1])+"\pm"+str(feBeta[1])+"\\\\"
# eqnEnd= r"\end{eqnarray*}"

# fitlabel=line1+eqnStart+line3+line4+eqnEnd

upperFe=straightFit(feBeta,np.log(x),feErr)
lowerFe=straightFit(feBeta,np.log(x),feErr*-1)

upperNoBar=straightFit(noBarBeta,np.log(x),noBarErr)
lowerNoBar=straightFit(noBarBeta,np.log(x),noBarErr*-1)

ax.plot(np.log(x),straightFit(feBeta,np.log(x),[0,0]), c="r", linestyle="dashed")
ax.plot(np.log(x),upperFe, c="g", linestyle="dotted")
ax.plot(np.log(x),lowerFe,c="g", linestyle="dotted")
ax.fill_between(np.log(x),upperFe,lowerFe,facecolor="gray", alpha=0.5)

ax.plot(np.log(x),straightFit(noBarBeta,np.log(x),[0,0]),c="b",linestyle="dashed")
ax.plot(np.log(x),upperNoBar, c="g", linestyle="dotted")
ax.plot(np.log(x),lowerNoBar,c="g", linestyle="dotted")
ax.fill_between(np.log(x),upperNoBar,lowerNoBar,facecolor="gray", alpha=0.5)

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


#l =ax.legend(handles=[(feFit,fePoints),(noBarFit,noBarPoints)],labels=["Fe barrier\n$m=-3.1\\pm0.3$","No Barrier\n$m=-1.9\\pm0.2$"],handler_map={tuple: HandlerTupleVertical(ndivide=None)})

plt.savefig('loglogTRhoR_NoBar_BOTH.png',bbox_inches="tight")
plt.show()
# j2j0_calc.py
# 
# Module for calculating the j2/j0 distribution.
# 
# Yuanpeng Zhang @ June-20-2018
# Spallation Neutron Source
# Oak Ridge National Laboratory
# 

import numpy as np
import sys
sys.path.insert(0,"./")
from phys_constants import *
from dist_calc import dist_calc

def j2j0_calc(j2j0Min,j2j0Max,j2j0binNum,EFermi,metric,atomList,j2j0WinAnalysis,j2j0WinMin,j2j0WinMax,rbinsNum):

	kFermi = np.sqrt(2*electrMass*EFermi*electrCharge)/hbar/1E10

	j2j0 = []
	distList = []

	rMax = 0.0
	rMin = 100.0

	for index1 in range(len(atomList)-1):
		for index2 in range(index1+1,len(atomList)):
			atom1 = atomList[index1]
			atom2 = atomList[index2]
			if atom1[1]=="Fe" and atom2[1]=="Fe":
				distTemp = dist_calc(metric,atom1,atom2)
				if distTemp>rMax:
					rMax = distTemp
				if distTemp<rMin:
					rMin = distTemp
				j2j0Temp = (kFermi*distTemp)**(-3)*\
						   (np.cos(2*kFermi*distTemp) - np.sin(2*kFermi*distTemp)/(2*kFermi*distTemp))
				j2j0.append(j2j0Temp)
				if j2j0WinAnalysis=="T":
					if j2j0Temp>j2j0WinMin and j2j0Temp<j2j0WinMax:
						distList.append(distTemp)

	print "rMin, rMax = ", rMin, rMax
	print "len(j2j0) = ", len(j2j0), "\n"

	bins = np.linspace(j2j0Min,j2j0Max,j2j0binNum+1)
	j2j0Hist = np.histogram(j2j0,bins)[0]

	j2j0binsOut = []
	for i in range(j2j0binNum):
		j2j0binsOut.append([(bins[i]+bins[i+1])/2.0,j2j0Hist[i]])

	if j2j0WinAnalysis=="T":
		rbinsMin = min(distList)
		rbinsMax = max(distList)
		bins4Dist = np.linspace(rbinsMin,rbinsMax,rbinsNum+1)
		distHist = np.histogram(distList,bins4Dist)[0]

		distBinsOut = []
		for i in range(rbinsNum):
			distBinsOut.append([(bins4Dist[i]+bins4Dist[i+1])/2.0,distHist[i]])

	print "j/j0 distribution successfully calculated."

	if j2j0WinAnalysis=="F":
		return j2j0binsOut
	else:
		return j2j0binsOut,distBinsOut

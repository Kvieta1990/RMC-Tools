# mag_cluster_average.py

import numpy as np

def mag_cluster_average(magAtmList,magAtmNeigh,mag_mom):

    overallMagP = 0
    magPDistib = []

    for i in range(len(magAtmList)):
        magPTemp = 0
        magPNum = 0
        for j in range(len(magAtmNeigh[i])-1):
            for k in range(j+1,len(magAtmNeigh[i])):
                magPTemp += np.dot(mag_mom[j],mag_mom[k])
                magPNum += 1
        overallMagP += magPTemp/magPNum
        magPDistib.append(magPTemp/magPNum)

    averageMagP = overallMagP/len(magAtmList)

    print "Magnetic cluster analysis successfully finished."

    return (magPDistib,averageMagP)
# read_rmc6f.py
#
# Module for reading in the rmc6f configuration file.
#
# Yuanpeng Zhang @ Feb-25-2018
# Spallation Neutron Source
# Oak Ridge National Laboratory
#

import numpy as np

def read_rmc6f(config_name):
    
    file = open(config_name,"r")

    line = file.readline()
    while line:
        line = file.readline()
        if "Lattice vectors" in line:
            break

    vectors = []
    for i in range(3):
        line = file.readline()
        vectors.append(line.split())

    vectors = [[float(y) for y in x] for x in vectors]
   
    metric = np.zeros((3,3))
    for j in range(3):
        for i in range(3):
            metric[i][j] = 0
            for k in range(3):
                metric[i][j] += vectors[i][k]*vectors[j][k]

    line = file.readline()

    atomList = []
    while line:
        line = file.readline()
        if line:
            atomList.append([int(line.split()[0]),line.split()[1],[float(x) for x in line.split()[3:6]]])

    file.close()

    magAtmList = []
    for item in atomList:
        if (item[1]=="Fe"):
            magAtmList.append(item)

    print "The magnetic atoms list successfully read in."

    return (metric,magAtmList)
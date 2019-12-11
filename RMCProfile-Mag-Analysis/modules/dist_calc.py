# dist_calc.py
# 
# Module containing the function defined for calculating the atomic distances.
# 
# Yuanpeng Zhang @ June-20-2018
# Spallation Neutron Source
# Oak Ridge National Laboratory
# 

import numpy as np

def dist_calc(metric,coor1,coor2):

    m12 = metric[1][0]
    m13 = metric[2][0]
    m23 = metric[2][1]

    xa = coor1[2][0] + 3.0
    ya = coor1[2][1] + 3.0
    za = coor1[2][2] + 3.0
    x = xa - coor2[2][0]
    y = ya - coor2[2][1]
    z = za - coor2[2][2]
    x = x - 2.0*int(x*0.5) - 1.0
    y = y - 2.0*int(y*0.5) - 1.0
    z = z - 2.0*int(z*0.5) - 1.0

    dist = np.sqrt(metric[0][0]*x*x+metric[1][1]*y*y+metric[2][2]*z*z+m12*x*y+m13*x*z+m23*y*z)

    return dist
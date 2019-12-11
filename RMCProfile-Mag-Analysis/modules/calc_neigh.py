# calc_neigh.py

from dist_calc import dist_calc

def calc_neigh(metric,magAtmList,mclusterR):

    magAtmNeigh = []
    index = 0

    for item in magAtmList:
        magAtmNeigh.append([])
        indexTemp = 0
        for item1 in magAtmList:
            distTemp = dist_calc(metric,item,item1)
            if (distTemp <= mclusterR):
                magAtmNeigh[index].append(indexTemp)
            indexTemp += 1
        index += 1

    print "The neighbour list for magnetic atoms successfully calculated."

    return magAtmNeigh
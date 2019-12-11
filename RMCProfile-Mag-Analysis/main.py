#
# This is the main program for running through the whole flowchart, i.e. read in
# main control file -> initial fit to extract the energy transfer coefficient ->
# calculate the energy transfer rate based on the fitted coefficient -> output
# result to file.
#
# Yuanpeng Zhang @ Feb-25-2018
# Spallation Neutron Source
# Oak Ridge National Laboratory
#

import sys
sys.path.insert(0,"./modules")
from read_control import read_control
from read_rmc6f import read_rmc6f
from calc_neigh import calc_neigh
from read_mag_cfg import read_mag_cfg
from mag_cluster_average import mag_cluster_average

try:
    contr_file = sys.argv[1]
except:
    print "Usage: python mc_main.py CONTROL_FILE_NAME"
    sys.exit(0)

print "------------------------------------------------------------------------>"
print "First, we read in the main control file.\n"
nuc_config_name,mag_config_name,magAtmType,\
        mclusterR,outFile = read_control(contr_file)
print "<------------------------------------------------------------------------\n"

print "------------------------------------------------------------------------>"
print "Next, we proceed to read in the magnetic atoms list.\n"
metric,magAtmList = read_rmc6f(nuc_config_name)
print "<------------------------------------------------------------------------\n"

print "------------------------------------------------------------------------>"
print "Next, we move on to calculate the neighbour list.\n"
magAtmNeigh = calc_neigh(metric,magAtmList,mclusterR)
print "<------------------------------------------------------------------------\n"

print "------------------------------------------------------------------------>"
print "Next, we move on to read in the magnetic moments.\n"
mag_mom = read_mag_cfg(mag_config_name)
if (len(magAtmNeigh) != len(mag_mom)):
    sys.exit("The number of magnetic moments does not equal the number of \
              magnetic atoms.\nHence we have to stop...")
print "<------------------------------------------------------------------------\n"

print "------------------------------------------------------------------------>"
print "Next, we move on to calculate the overall average cluster magnetic moment.\n"
magPDistib,averageMagP = mag_cluster_average(magAtmList,magAtmNeigh,mag_mom)
print "<------------------------------------------------------------------------\n"

magCAnalysisOut = open(outFile,"w")
magCAnalysisOut.write("# Magnetic local cluster polarization analysis for the following files:\n")
magCAnalysisOut.write("# Nucleus configuration: " + nuc_config_name + \
        ", Magnetic configuration: " + mag_config_name + "\n")
magCAnalysisOut.write("# Average polarization with local cluster radius of {0:5.2F} \
        angstrom is: {1:10.5F}\n".format(mclusterR,averageMagP))
for i in range(len(magPDistib)):
    magCAnalysisOut.write("{0:5d}{1:10.5F}\n".format(i+1,magPDistib[i]))

print "================================"
print "-----------Job done!------------"
print "================================"
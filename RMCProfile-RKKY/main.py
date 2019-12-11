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
from j2j0_calc import j2j0_calc

try:
    contr_file = sys.argv[1]
except:
    print "Usage: python mc_main.py CONTROL_FILE_NAME"
    sys.exit(0)

print "------------------------------------------------------------------------>"
print "First, we read in the main control file.\n"
config_name,j2j0Min,j2j0Max,j2j0binNum,EFermi,out_file,j2j0WinAnalysis,j2j0WinMin,\
	j2j0WinMax,rbinsNum,distHistOutFile = read_control(contr_file)
print "<------------------------------------------------------------------------\n"

print "------------------------------------------------------------------------>"
print "Next, we proceed to read in the structure configuration.\n"
metric,atomList = read_rmc6f(config_name)
print "<------------------------------------------------------------------------\n"

print "------------------------------------------------------------------------>"
print "Next, we move to the main body of the J/J0 statistics calculation.\n"
if j2j0WinAnalysis=="T":
	print "J/J0 window analysis will be carried out.\n"
	j2j0Out,rbinsOut = j2j0_calc(j2j0Min,j2j0Max,j2j0binNum,EFermi,metric,\
		atomList,j2j0WinAnalysis,j2j0WinMin,j2j0WinMax,rbinsNum)
else:
	j2j0Out = j2j0_calc(j2j0Min,j2j0Max,j2j0binNum,EFermi,metric,atomList,\
		j2j0WinAnalysis,j2j0WinMin,j2j0WinMax,rbinsNum)
print "<------------------------------------------------------------------------\n"

outFile = open(out_file,"w")

outFile.write("# J2/J0 distribution statistics for " + config_name + ".\n")
for item in j2j0Out:
	outFile.write("{0:10.3E}{1:10d}\n".format(item[0],item[1]))

outFile.close()

if j2j0WinAnalysis=="T":
	outFile = open(distHistOutFile,"w")
	outFile.write("# Distribution of the atomic distances corresponding to the following J/J0 window:\n")
	outFile.write("# {0:15.3E}{1:15.3E}\n".format(j2j0WinMin,j2j0WinMax))
	for item in rbinsOut:
		outFile.write("{0:10.2F}{1:10d}\n".format(item[0],item[1]))

print "================================"
print "-----------Job done!------------"
print "================================"

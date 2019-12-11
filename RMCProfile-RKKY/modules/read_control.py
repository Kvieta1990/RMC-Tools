# read_control.py
#
# Module for reading in the main control file.
#
# Yuanpeng Zhang @ Feb-25-2018
# Spallation Neutron Source
# Oak Ridge National Laboratory
#

import sys

def read_control(contr_file):

    j2j0WinLineFound = False

    file = open(contr_file,"r")

    line = file.readline()

    while line:
        if ("RMC6F_FILE" in line):
            config_name = line.split("::")[1].split("%%")[0].strip()
        elif ("FERMI_ENERGY" in line):
            global EFermi
            EFermi = float(line.split("::")[1].split("%%")[0])
        elif ("J_TO_J0_PARAMETERS" in line):
            j2j0Min = float(line.split("::")[1].split("%%")[0].split()[0])
            j2j0Max = float(line.split("::")[1].split("%%")[0].split()[1])
            j2j0binNum = int(line.split("::")[1].split("%%")[0].split()[2])
        elif ("J_TO_J0_WINDOW" in line):
            j2j0WinAnalysis = line.split("::")[1].split("%%")[0].split()[0].strip()
            if j2j0WinAnalysis=="T":
                j2j0WinMin = float(line.split("::")[1].split("%%")[0].split()[1])
                j2j0WinMax = float(line.split("::")[1].split("%%")[0].split()[2])
                rbinsNum = int(line.split("::")[1].split("%%")[0].split()[3])
                distHistOutFile = line.split("::")[1].split("%%")[0].split()[4].strip()
            elif j2j0WinAnalysis=="F":
                j2j0WinMin = 0.0
                j2j0WinMax = 0.0
                rbinsNum = 0
                distHistOutFile = "dummy"
            else:
                sys.exit("Input format for J_TO_J0_WINDOW incorrect! Hence we have to stop.")
        elif ("OUT_FILE" in line):
            out_file = line.split("::")[1].split("%%")[0].strip()
        else:
            sys.exit("Input not recognized in the control file! Hence we have to stop...")

        line = file.readline()

    print "Main control file successfully read in."

    return (config_name,j2j0Min,j2j0Max,j2j0binNum,EFermi,out_file,j2j0WinAnalysis,j2j0WinMin,\
            j2j0WinMax,rbinsNum,distHistOutFile)
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

    file = open(contr_file,"r")

    line = file.readline()

    while line:
        if ("NUC_CONFIG_FILE" in line):
            nuc_config_name = line.split("::")[1].split("%%")[0].strip()
        elif ("MAG_CONFIG_FILE" in line):
            mag_config_name = line.split("::")[1].split("%%")[0].strip()
        elif ("MAG_ATOM_TYPE" in line):
            magAtmType = line.split("::")[1].split("%%")[0].strip()
        elif ("MAG_CLUSTER_RADIUS" in line):
            mclusterR = float(line.split("::")[1].split("%%")[0])
        elif ("OUTPUT_FILE" in line):
            outFile = line.split("::")[1].split("%%")[0].strip()
        else:
            sys.exit("Input not recognized in the control file! Hence we have to stop...")

        line = file.readline()

    print "Main control file successfully read in."

    return (nuc_config_name,mag_config_name,magAtmType,mclusterR,outFile)
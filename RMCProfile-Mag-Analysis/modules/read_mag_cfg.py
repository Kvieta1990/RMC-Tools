# read_mag_cfg.py

def read_mag_cfg(mag_config_name):

    magcfgFile = open(mag_config_name,"r")

    line = magcfgFile.readline()
    magAtmNum = int(line.split()[1])

    line = magcfgFile.readline()

    mag_mom = []
    for i in range(magAtmNum):
        line = magcfgFile.readline()
        mag_mom.append([float(x) for x in line.split()])

    print "The magnetic moments successfully read in."

    return mag_mom
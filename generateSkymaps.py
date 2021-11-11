import ctools
import os
import argparse


parser = argparse.ArgumentParser(description='Create skymaps.')
parser.add_argument('--backsub', type=str, required=True, choices=["IRF", "NONE"], help='Type of background subtraction.')
parser.add_argument('--num_sources', type=int, required=True, help='Number of point source.')
args = parser.parse_args()

BACK_SUB = args.backsub
SOURCES_NUMBER = args.num_sources
EVENTS = "ev" + BACK_SUB + str(SOURCES_NUMBER) + ".fits"
SELECTED_EVENTS = "sel" + BACK_SUB + str(SOURCES_NUMBER) + ".fits"

start = 0
for filename in os.listdir("data/skymaps/" + BACK_SUB + "/" + str(SOURCES_NUMBER)):
    if "skymap" in filename:
        num = int(((filename.split("_"))[2])[:-5])
        if num > start:
            start = num
            
for i in range(len(os.listdir("data/xml_files/"+str(SOURCES_NUMBER)))-1):
    if start == 0 or i > start:
        sim = ctools.ctobssim()
        sim["inmodel"] = "data/xml_files/"+str(SOURCES_NUMBER)+"/sigma_" + str(i) + ".xml"
        sim["outevents"] = EVENTS
        sim["caldb"] = "prod2"
        sim["irf"] = "South_0.5h"
        sim["ra"] = 221
        sim["dec"] = 46
        sim["rad"] = 5.0
        sim["tmin"] = 0.0
        sim["tmax"] = 900.0
        sim["emin"] = 0.1
        sim["emax"] = 100.0
        sim.execute()
    
        sim = ctools.ctselect()
        sim["inobs"] = EVENTS
        sim["rad"] = 3.0
        sim["emin"] = 0.1
        sim["emax"] = 100.0
        sim["tmin"] = "NONE"
        sim["tmax"] = "NONE"
        sim["outobs"] = SELECTED_EVENTS
        sim.execute()
    
        sim = ctools.ctskymap()
        sim["inobs"] = SELECTED_EVENTS
        sim["outmap"] = "data/skymaps/" + str(BACK_SUB) + "/" + str(SOURCES_NUMBER) +"/skymap_" + BACK_SUB + "_" + str(i) + ".fits"
        sim["nxpix"] = 250
        sim["nypix"] = 250
        sim["binsz"] = 0.02
        sim["coordsys"] = "CEL"
        sim["proj"] = "CAR"
        sim["xref"] = 221
        sim["yref"] = 46
        sim["emin"] = 0.1
        sim["emax"] = 100.0
        sim["bkgsubtract"] = BACK_SUB
        if BACK_SUB == "IRF":
    	    sim["irf"] = "South_0.5h"
    	    sim["caldb"] = "prod2"
        sim.execute()

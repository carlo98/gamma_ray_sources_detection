from xml.dom import minidom 
import os
import numpy as np
import random as rnd
from csv import writer
import argparse


parser = argparse.ArgumentParser(description='Create xml files.')
parser.add_argument('--num_files', type=int, required=True, help='Number of xml files.')
parser.add_argument('--num_sources', type=int, required=True, help='Number of point source.')
parser.add_argument('--min_dist', type=float, default=0.17, help='Minimum change in ra and dec.')
args = parser.parse_args()

MIN_DIST = args.min_dist
N_SOURCES = args.num_sources

start = 0
for filename in os.listdir("data/xml_files/" + str(N_SOURCES)):
    if "sigma" in filename:
        num = int(((filename.split("_"))[1])[:-5])
        if num > start:
            start = num
  
for num in range(args.num_files):
	if num > start or start == 0:
		root = minidom.Document() 
		  
		xml = root.createElement('source_library')
		xml.setAttribute('title', 'source library')
		root.appendChild(xml) 
		  
		value_ra = []
		value_dec = []
		source1Child = []
		spectrumChild = []
		parameter1Child = []
		parameter5Child = []
		parameter2Child = []
		parameter3Child = []
		spatialModelChild_1 = []
		parameter4Child = []
		for i in range(N_SOURCES):
			source1Child.append(root.createElement('source')) 
			source1Child[-1].setAttribute('name', 'Crab'+str(i))
			source1Child[-1].setAttribute('type', 'PointSource')
			xml.appendChild(source1Child[-1])

			spectrumChild.append(root.createElement('spectrum'))
			spectrumChild[-1].setAttribute('type', 'PowerLaw')
			source1Child[-1].appendChild(spectrumChild[-1])

			parameter1Child.append(root.createElement('parameter'))
			parameter1Child[-1].setAttribute('name', 'Prefactor')
			parameter1Child[-1].setAttribute('scale', '1e-17')
			value_pre = rnd.random()
			parameter1Child[-1].setAttribute('value', str(2-value_pre))
			parameter1Child[-1].setAttribute('min', '1e-07')
			parameter1Child[-1].setAttribute('max', '1000.0')
			parameter1Child[-1].setAttribute('free', '1')
			spectrumChild[-1].appendChild(parameter1Child[-1])

			parameter5Child.append(root.createElement('parameter'))
			parameter5Child[-1].setAttribute('name', 'Index')
			parameter5Child[-1].setAttribute('scale', '-1')
			parameter5Child[-1].setAttribute('value', '2.48')
			parameter5Child[-1].setAttribute('min', '0.0')
			parameter5Child[-1].setAttribute('max', '+5.0')
			parameter5Child[-1].setAttribute('free', '1')
			spectrumChild[-1].appendChild(parameter5Child[-1])

			parameter2Child.append(root.createElement('parameter'))
			parameter2Child[-1].setAttribute('name', 'PivotEnergy')
			parameter2Child[-1].setAttribute('scale', '1e6')
			parameter2Child[-1].setAttribute('value', '0.3')
			parameter2Child[-1].setAttribute('min', '0.01')
			parameter2Child[-1].setAttribute('max', '1000.0')
			parameter2Child[-1].setAttribute('free', '0')
			spectrumChild[-1].appendChild(parameter2Child[-1])
			spatialModelChild_1.append(root.createElement('spatialModel'))
			spatialModelChild_1[-1].setAttribute('type', 'PointSource')
			source1Child[-1].appendChild(spatialModelChild_1[-1])

			parameter3Child.append(root.createElement('parameter'))
			parameter3Child[-1].setAttribute('name', 'RA')
			parameter3Child[-1].setAttribute('scale', '1.0')
			value_ra.append(rnd.random() * ((-1) ** (rnd.random()>=0.5)))
			flag = True
			while flag:
				flag = False
				for j in range(len(value_ra)-1):
					if np.abs(value_ra[-1] - value_ra[j]) <= MIN_DIST:
						flag = True
						break
				value_ra[-1] = rnd.random() * ((-1) ** (rnd.random()>=0.5))
			parameter3Child[-1].setAttribute('value', str(221 + value_ra[-1]))
			parameter3Child[-1].setAttribute('min', '-360')
			parameter3Child[-1].setAttribute('max', '360')
			parameter3Child[-1].setAttribute('free', '0')
			spatialModelChild_1[-1].appendChild(parameter3Child[-1])

			parameter4Child.append(root.createElement('parameter'))
			parameter4Child[-1].setAttribute('name', 'DEC')
			parameter4Child[-1].setAttribute('scale', '1.0')
			value_dec.append(rnd.random() * ((-1) ** (rnd.random()>=0.5)))
			flag = True
			while flag:
				flag = False
				for j in range(len(value_dec)-1):
					if np.abs(value_dec[-1] - value_dec[j]) <= MIN_DIST:
						flag = True
						break
				value_dec[-1] = rnd.random() * ((-1) ** (rnd.random()>=0.5))
			parameter4Child[-1].setAttribute('value', str(46 + value_dec[-1]))
			parameter4Child[-1].setAttribute('min', '-90')
			parameter4Child[-1].setAttribute('max', '90')
			parameter4Child[-1].setAttribute('free', '0')
			spatialModelChild_1[-1].appendChild(parameter4Child[-1])
			
		source2Child = root.createElement('source') 
		source2Child.setAttribute('name', 'CTABackgroundModel')
		source2Child.setAttribute('type', 'CTAIrfBackground')
		source2Child.setAttribute('instrument', 'CTA')
		xml.appendChild(source2Child)

		spectrum2Child = root.createElement('spectrum')
		spectrum2Child.setAttribute('type', 'PowerLaw')
		source2Child.appendChild(spectrum2Child)

		parameter6Child = root.createElement('parameter')
		parameter6Child.setAttribute('name', 'Prefactor')
		parameter6Child.setAttribute('scale', '1.0')
		parameter6Child.setAttribute('value', '1.0')
		parameter6Child.setAttribute('min', '1e-3')
		parameter6Child.setAttribute('max', '1e+3')
		parameter6Child.setAttribute('free', '1')
		spectrum2Child.appendChild(parameter6Child)

		parameter7Child = root.createElement('parameter')
		parameter7Child.setAttribute('name', 'Index')
		parameter7Child.setAttribute('scale', '1.0')
		parameter7Child.setAttribute('value', '0.0')
		parameter7Child.setAttribute('min', '-5.0')
		parameter7Child.setAttribute('max', '+5.0')
		parameter7Child.setAttribute('free', '1')
		spectrum2Child.appendChild(parameter7Child)

		parameter8Child = root.createElement('parameter')
		parameter8Child.setAttribute('name', 'PivotEnergy')
		parameter8Child.setAttribute('scale', '1e6')
		parameter8Child.setAttribute('value', '1.0')
		parameter8Child.setAttribute('min', '0.01')
		parameter8Child.setAttribute('max', '1000.0')
		parameter8Child.setAttribute('free', '0')
		spectrum2Child.appendChild(parameter8Child)
		  
		xml_str = root.toprettyxml(indent ="\t")  
		  
		save_path_file = "sigma_" + str(num) + ".xml"
		  
		with open("data/xml_files/"+str(N_SOURCES)+"/"+save_path_file, "w") as f: 
			f.write(xml_str)
		with open("data/xml_files/"+str(N_SOURCES)+"/blobs.csv", "a+", newline='') as write_obj:
			csv_writer = writer(write_obj)
			# Add contents of list as last row in the csv file
			to_be_saved = [num]
			for i in range(N_SOURCES):
			    to_be_saved.append(221+value_ra[i])
			    to_be_saved.append(46+value_dec[i])
			csv_writer.writerow(to_be_saved)
			

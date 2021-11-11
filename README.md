# Gamma Ray Sources Detection
Project developed for the course of Image Processing & Computer Vision of University of Bologna.
A detailed project description and result analysis is provided in the pdf file, please look there.

## Installation
- (Install Anaconda)[https://www.anaconda.com/products/individual]
- Create a new environment with `conda create --name <myenv> --file spec-file.txt`

### Folders
Create the following structure:
\- Data
\- \- xml_files
\- \- \- num_sources_0
\- \- \-  ...
\- \- skymaps
\- \- \- IRF
\- \- \- \- num_sources_0
\- \- \- \- ...
\- \- \- NONE
\- \- \- \- num_sources_0
\- \- \- \- ...
\- \- dataset_irf
\- \- dataset_none

## Usage
To create a new xml file use the script generateXml.py:
`python3 generateXml.py --num_files <num_files> --num_sources <num_sources>`

To create the skymaps associated to the xml files create before, run:
`python3 generateSkymaps.py --backsub <IRF/NONE> --num_sources <num_sources>`

Use the notebooks "irf.ipynb" and "none.ipynb" to perform source detection.

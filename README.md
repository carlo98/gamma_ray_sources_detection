# Gamma Ray Sources Detection
Project developed for the course of Image Processing & Computer Vision of University of Bologna.

A detailed project description and result analysis are provided in the pdf file, please look there.

## Installation
- [Install Anaconda](https://www.anaconda.com/products/individual)
- Create a new environment with `conda create --name <myenv> --file spec-file.txt`

### Folders
Create a folder named "data" and in it the following structure:
```
data
├── dataset_irf
├── dataset_none
├── skymaps
│   ├── IRF
│   │   └── 1
│   └── NONE
│       └── 2
└── xml_files
    ├── 1
    └── 2
```


## Usage
To create a new xml file use the script generateXml.py:
`python3 generateXml.py --num_files <num_files> --num_sources <num_sources>`

To create the skymaps associated to the xml files create before, run:
`python3 generateSkymaps.py --backsub <IRF/NONE> --num_sources <num_sources>`

Use the notebooks "irf.ipynb" and "none.ipynb" to perform source detection.

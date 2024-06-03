# Summer School tutorial

## Introduction
This notebok is an illustrative example of how to analyse force curves acquired from nanoscope to fit an appropriate contact model (hertz) and meausure the nano-mechanics.

what does this notebook do:

- Loads a folder of Nanoscope files

- user defined parameters for fitting hertz model

- running the fitting routine for one curve

- plotting the Hertz fit results

- Loop cell - A simple loop to run over all the curves in the given folder  

  



## Setting up the computer
- Open a terminal window at the tutorial files folder.
- Create & activate an environment with python 3.9 (important)
```
conda create -n yourenvname python=3.9 
conda activate yourenvname
```
- Install git package for downstream installations
```
conda install git
```

- Install the PYFMreader and PyFMRheo from DyNaMo's repositary 
```

pip install -e git+https://github.com/DyNaMo-INSERM/PyFMReader_DyNaMo@master#egg=pyfmreader_dynamo    

pip install -e git+https://github.com/DyNaMo-INSERM/PyFMRheo_DyNaMo@main#egg=pyfmrheo_dynamo
```

## Download tutorial
git clone https://github.com/DyNaMo-INSERM/Tutorial_AFM_mecabio.git

## Change folder
cd Tutorial_AFM_mecabio

## Open the notebook
jupyter lab PYFM_rheo_summerschool-1.ipynb

- Install other dependencies from requirements.txt
```
pip install -r requirements.txt
```
- Open a jupyter notebook 
```
jupyter lab 
```

# Summer School tutorial

## Introduction
This notebok is an illustrative example of how to analyse force curves acquired from nanoscope to fit an appropriate contact model (hertz) and meausure the nano-mechanics.

what does this notebook do:
- Loads a folder of Nanoscope files
- user defined parameters for fitting hertz model
- running the fitting routine for one curve
- plotting the Hertz fit results
- Looping the code to run over all the curves in the folder  

  



## Setting up the computer
- Open a terminal window at the tutorial files folder.
- Create an environment with python 3.9 (important)
```
conda create -n yourenvname python=3.9 
conda activate yourenvname
```

- Install the dependencies from requirements.txt
```
pip install -r requirements.txt
```
- Opening a jupyter notebook 
```
jupyter lab 
```

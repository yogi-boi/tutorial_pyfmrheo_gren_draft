#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 28 13:31:54 2024

@author: yogehs
"""

from pyfmreader import loadfile
from pyfmrheo.utils.force_curves import get_poc_RoV_method, get_poc_regulaFalsi_method, correct_tilt, correct_offset

from pyfmrheo.routines import doHertzFit
import matplotlib.pyplot as plt
import numpy as np
import os 
from pathlib import Path
def raw_plt_curve(force_curve,error=None):
    curve_id_= force_curve.curve_index
    segs = force_curve.get_segments()
    ext_data = segs[0][1]
    retract_data = segs[1][1]
    temp_fig_title = f"Error_{error}_curve_id_{curve_id_}"
    fig = plt.figure(temp_fig_title);plt.clf();
    plt.title(temp_fig_title);

    for _, segment in force_curve.get_segments():
        segment_data = segment
        plt.scatter(segment_data.zheight,segment_data.vdeflection,label = segment_data.segment_type)
        plt.xlabel("Z height ")
        plt.ylabel("deflection signal ")


    plt.legend()#;plt.show()
    return(fig)
# Define path of file to process
folder_path = '/Users/yogehs/Documents/ATIP_PhD/tutorial_pyfmrheo_gren/test_files/'
file_paths_in_folder = sorted([folder_path+f for f in os.listdir(folder_path) if Path(f).suffix[1:].isnumeric()])
file_paths_in_folder
file_path = file_paths_in_folder[2]


# Load File
file = loadfile(file_path)
filemetadata = file.filemetadata
print(filemetadata['file_type'])


filemetadata['peakforce'] = False
filemetadata['PFC_freq'] = 0
filemetadata['PFC_amp'] = 0
filemetadata['QNM_sync_dist'] = 0

filemetadata['PFC_nb_samppoints'] = 0
# Define parameters to perform the HertzFit

# Get some of the file metadata
closed_loop = filemetadata['z_closed_loop']
file_deflection_sensitivity = filemetadata['defl_sens_nmbyV'] #nm/V
file_spring_constant = filemetadata['spring_const_Nbym'] #N/m
height_channel = filemetadata['height_channel_key']

deflection_sensitivity = file_deflection_sensitivity / 1e9 #m/V
spring_constant = file_spring_constant

print(f"Closed loop: {closed_loop}")
print(f"Height channel: {height_channel}")
print(f"Deflection Sens.: {deflection_sensitivity} m/V")
print(f"Spring Constant: {spring_constant} N/m")
maxnoncontact = 1e-6 #um

param_dict = {
    'height_channel': height_channel,   # Channel where to find the height data
    'def_sens': deflection_sensitivity, # Deflection sensitivity in m/V
    'k': spring_constant,               # Spring constant in N/m
    'contact_model': 'paraboloid',      # Geometry of the indenter: paraboloidal, conical, pyramidal
    'tip_param': 5e-06,                 # Tip raidus in meters or tip angle in degrees
    'curve_seg': 'extend',              # Segement to perform the fit: extend or retract
    'correct_tilt': True,              # Perform tilt correction
    'tilt_min_offset': 1e-08,           # Maximum range where to perform the tilt correction in meters
    'tilt_max_offset': 1e-06,           # Minimum range where to perform the tilt correction in meters
    'poisson': 0.5,                     # Poisson's ratio
    'poc_method': 'RoV',                # Method to find the contact point: RoV or RegulaFalsi
    'poc_win': 2e-07,                   # Window size for the RoV method
    'max_ind': 0.0,                     # Maximum indentation range for fit in meters
    'min_ind': 500e-09,                     # Minimum indentation range for fit in meters
    'max_force': 0.0,                   # Maximum force range for fit in Newtons
    'min_force': 0.0,                   # Minimum force range for fit in Newtons
    'fit_range_type': 'full',           # Fit data range: full, indentation or force
    'd0': 0.0,                          # Initial point of contact
    'slope': 0.0,                       # Initial slope
    'auto_init_E0': True,               # Estimate automatically the initial value of the Young's Modulus
    'E0': 500,                         # Initial Young's Modulus value
    'f0': 0.0,                          # Initial F0 value
    'contact_offset': maxnoncontact,    # Baseline offset for the Hertz Fit
    'fit_line': False,                  # Fit line to the baseline
    'downsample_flag': False,            # Downsample the signal for Hertz Fit
    'pts_downsample': 0,   # Number of points to downsample
    'offset_type':'percentage',         # How to correct for baseline offset: percentage or value
    'max_offset':.3,                    # Max percentage to compute offset
    'min_offset':0.1                      # Min percentage to compute offset
}


# Select curve by index
curve_idx = 0
force_curve = file.getcurve(curve_idx)
# Preprocess curve
force_curve.preprocess_force_curve(param_dict['def_sens'], param_dict['height_channel'])
# JPK files require the height signal to be shifted
if filemetadata['file_type'] in ('jpk-force', 'jpk-force-map', 'jpk-qi-data'):
    force_curve.shift_height()
    
raw_plt_curve(force_curve,'hehh')
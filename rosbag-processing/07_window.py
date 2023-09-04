#!/usr/bin/env python
import argparse
import numpy as np
import pandas as pd
from scipy.spatial.transform import Rotation as Rot
import os
from tqdm import tqdm
import re

import sys
curr_dir = os.path.dirname(os.path.abspath(__file__))
libs_path = f'{curr_dir}/../python-imports'
sys.path.insert(1, libs_path)

import myhelpers as H

# parse
parser = argparse.ArgumentParser()
parser.add_argument('infile', type=str, help='path to rel merged csv file')
parser.add_argument('outfile', type=str, help='path to rel merged csv file')
parser.add_argument('config', type=str, help='path to python antenna config')
parser.add_argument('window_dur', type=float, help='window duration in seconds')
parser.add_argument('window_step', type=float, help='window step size in seconds')
args = parser.parse_args()



# load args
INFILE = args.infile
OUTFILE = args.outfile
CONFIG = args.config
WINDOW_DUR = args.window_dur
WINDOW_STEP = args.window_step



# load config.py
assert CONFIG[-3:] == '.py'
CONFIG_DIR = os.path.dirname(CONFIG)
CONFIG_BASE = os.path.basename(os.path.splitext(CONFIG)[0])

sys.path.insert(1,CONFIG_DIR)
exec(f'from {CONFIG_BASE} import *')



# constants
COLS_POSE = ['x','y','z','roll','pitch','yaw']
COLS_A_POSE = [f'A_{i}' for i in COLS_POSE]
COLS_B_POSE = [f'B_{i}' for i in COLS_POSE]
COLS_EST_POSE = [f'est_{i}' for i in COLS_POSE]
COLS_RES_POSE = [f'res_{i}' for i in COLS_POSE]
COLS_MEAS = [f'{i+1}_{j+1}' for i in range(BASE_ANTENNA_COUNT) for j in range(TARGET_ANTENNA_COUNT)]
COLS_MEAS_TRUE = [f'{i}_t' for i in COLS_MEAS]
COLS_MEAS_ERR = [f'{i}_err' for i in COLS_MEAS]
COLS_SPHERICAL = ['rho', 'az', 'el']
COLS_RES_SPHERICAL = [f'res_{i}' for i in COLS_SPHERICAL]
COLS_SPHERICAL_ERR = [f'{i}_err' for i in COLS_SPHERICAL]



# windowing
df = pd.read_csv(INFILE)
T_MAX = np.max(df['t'])
COLS_ANGLE = [col for col in df.columns if any([key in col for key in ['roll','pitch','yaw','az','el']])]

windows = []

i = 0
while i*WINDOW_STEP+WINDOW_DUR < T_MAX:
    t_start = i*WINDOW_STEP
    t_finish = i*WINDOW_STEP + WINDOW_DUR
    
    curr = df[(df['t'] >= t_start) & (df['t'] < t_finish)]
    
    mean = curr.mean()
    
    # fix angle means
    for col in COLS_ANGLE:
        mean[col] = H.deg_mean(curr[col])
        
    # set time to beginning of time window
    mean['t'] = t_start
        
    # calculate std for range measurements
    std = curr[COLS_MEAS].std()
    std = std.add_suffix('_std')
    
    window = pd.concat([mean,std])
    windows.append(window)
    
    i += 1
    


# write DataFrame
df_window = pd.DataFrame(windows)
df_window.to_csv(OUTFILE,index=False)

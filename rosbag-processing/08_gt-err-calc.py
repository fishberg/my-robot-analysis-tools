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
import mypose
from mypose import Pose

# parse
parser = argparse.ArgumentParser()
parser.add_argument('infile', type=str, help='path to rel merged csv file')
parser.add_argument('outfile', type=str, help='path to rel merged csv file')
parser.add_argument('config', type=str, help='path to python antenna config')
args = parser.parse_args()



# load args
INFILE = args.infile
OUTFILE = args.outfile
CONFIG = args.config



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



# gt err calculation
df = pd.read_csv(INFILE)

dist_true_lst = []
dist_err_lst = []

for idx in tqdm(range(len(df))):
    curr = df.iloc[idx]
    A_T = Pose.from_xyzrpy(*curr[COLS_A_POSE])
    B_T = Pose.from_xyzrpy(*curr[COLS_B_POSE])
    base_ants = mypose.transform_pts(A_T,BASE_CONFIG)
    target_ants = mypose.transform_pts(B_T,TARGET_CONFIG)
    dist_true = mypose.all_pairs_euclid_numpy(base_ants.T, target_ants.T)
        
    dist_true_lst.append(dist_true.flatten())
    
    dist = np.array(curr[COLS_MEAS]).reshape((BASE_ANTENNA_COUNT,TARGET_ANTENNA_COUNT))
    dist_err = dist - dist_true
    dist_err_lst.append(dist_err.flatten())
    
df[COLS_MEAS_TRUE] = dist_true_lst
df[COLS_MEAS_ERR] = dist_err_lst



# r calc
r = df[COLS_MEAS].mean(axis=1)
r_t = df[COLS_MEAS_TRUE].mean(axis=1)
r_err = r - r_t

COLS_RS = ['r','r_t','r_err']
df[COLS_RS] = pd.DataFrame([r,r_t,r_err]).T



# write file
df.to_csv(OUTFILE,index=False)

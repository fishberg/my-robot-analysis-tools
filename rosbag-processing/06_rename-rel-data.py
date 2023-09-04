#!/usr/bin/env python
import argparse
import numpy as np
import pandas as pd
from scipy.spatial.transform import Rotation as Rot
import os
from tqdm import tqdm
import re

# parse
parser = argparse.ArgumentParser()
parser.add_argument('infile', type=str, help='path to rel merged csv file')
parser.add_argument('outfile', type=str, help='path to rel merged csv file')
parser.add_argument('unit_a', type=str, help='prefix for UNIT_A')
parser.add_argument('unit_b', type=str, help='prefix for UNIT_B')
parser.add_argument('rel', type=str, help='prefix for relative')
parser.add_argument('--unit_a_ant', '-a', type=int, action='append', help='ordered node IDs for UNIT_A')
parser.add_argument('--unit_b_ant', '-b', type=int, action='append', help='ordered node IDs for UNIT_B')
args = parser.parse_args()

# arguments
INFILE = args.infile
OUTFILE = args.outfile
UNIT_A = args.unit_a
UNIT_B = args.unit_b
REL = args.rel
UNIT_A_ANTENNA = args.unit_a_ant
UNIT_B_ANTENNA = args.unit_b_ant

# constants
POSE = ['x','y','z','roll','pitch','yaw']

# load CSV
df = pd.read_csv(INFILE)

# from columns
FROM_T = ['t']
FROM_POSE_A = [f'{UNIT_A}_{i}' for i in POSE]
FROM_POSE_B = [f'{UNIT_B}_{i}' for i in POSE]
FROM_POSE_REL = [f'{REL}_{i}' for i in POSE]
FROM_ANTENNA = [f'n{i}_n{j}' for i in UNIT_A_ANTENNA for j in UNIT_B_ANTENNA]
FROM = FROM_T + FROM_POSE_REL + FROM_POSE_A + FROM_POSE_B + FROM_ANTENNA

# drop other columns
df = df[FROM]

# to columns
TO_T = ['t']
TO_POSE_A = [f'A_{i}' for i in POSE]
TO_POSE_B = [f'B_{i}' for i in POSE]
TO_POSE_REL = [f'{i}' for i in POSE]
TO_ANTENNA = [f'{i+1}_{j+1}' for i in range(len(UNIT_A_ANTENNA)) for j in range(len(UNIT_B_ANTENNA))]
TO = TO_T + TO_POSE_REL + TO_POSE_A + TO_POSE_B + TO_ANTENNA

# rename
D = dict(zip(FROM,TO))
df = df.rename(columns=D)

# write outfile
df.to_csv(OUTFILE,index=False)

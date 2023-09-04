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

from mypose import Pose
from numpy.linalg import inv

parser = argparse.ArgumentParser()
parser.add_argument('infile', type=str, help='path to merged csv file')
parser.add_argument('outfile', type=str, help='out filename')
parser.add_argument('base_prefix', type=str, help='relative pose origin (x,y,z,r,p,y)')
parser.add_argument('target_prefix', type=str, help='relative pose target (x,y,z,r,p,y)')
parser.add_argument('rel_prefix', type=str, help='new relative pose column (x,y,z,r,p,y)')

args = parser.parse_args()
out_filename = args.outfile

df = pd.read_csv(args.infile)

base_pose = [f'{args.base_prefix}_{i}' for i in ['x','y','z','roll','pitch','yaw']]
target_pose = [f'{args.target_prefix}_{i}' for i in ['x','y','z','roll','pitch','yaw']]
rel_pose = [f'{args.rel_prefix}_{i}' for i in ['x','y','z','roll','pitch','yaw']]
rel_x, rel_y, rel_z, rel_roll, rel_pitch, rel_yaw = rel_pose

rels = []
for row in tqdm(df.iloc,total=len(df)):
    A = Pose.from_xyzrpy(*row[base_pose])
    B = Pose.from_xyzrpy(*row[target_pose])
    x,y,z,roll,pitch,yaw = Pose.to_xyzrpy(inv(A) @ B)
    D = {rel_x: x, rel_y: y, rel_z: z, rel_roll: roll, rel_pitch: pitch, rel_yaw: yaw}
    rels.append(D)

df_rel = pd.DataFrame(rels)

df_merge = pd.concat([df,df_rel],axis=1)
df_merge.to_csv(out_filename,index=False)

#!/usr/bin/env python
import argparse
import numpy as np
import pandas as pd
from scipy.spatial.transform import Rotation as Rot
import os
from tqdm import tqdm
import re

# TODO prefix as part of mocap and uwb (so order doesn't matter)
# expects mocap first, then uwb
parser = argparse.ArgumentParser()
parser.add_argument('--outfile', '-o', type=str, help='out filename')
parser.add_argument('--step', '-s', type=float, help='time step')
parser.add_argument('--file', '-f', type=str, action='append', help='path to mocap or uwb csv file')
parser.add_argument('--prefix', '-p', type=str, action='append',  help='prefix for mocap or uwb csv columns')
args = parser.parse_args()

assert len(args.file) == len(args.prefix)

out_filename = args.outfile

csv = [pd.read_csv(f) for f in args.file]
prefix = [f'{pre}_' for pre in args.prefix]

t_min = int(np.min([np.min(df['t']) for df in csv])) + 1
t_max = int(np.min([np.max(df['t']) for df in csv]))
t_step = args.step
t_range = np.arange(t_min, t_max, t_step)

df_merge = pd.DataFrame()
df_merge['t'] = t_range - t_min
df_merge['merge_t'] = t_range

csv = [df.add_prefix(pre) for df,pre in zip(csv,prefix)]

for df,pre in zip(csv,prefix):
   df_merge = pd.merge_asof(df_merge, df, left_on='merge_t', right_on=f'{pre}t', direction='nearest')

df_merge.to_csv(out_filename,index=False)

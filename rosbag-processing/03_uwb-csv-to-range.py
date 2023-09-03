#!/usr/bin/env python
import argparse
import numpy as np
import pandas as pd
from scipy.spatial.transform import Rotation as Rot
import os
from tqdm import tqdm
import re

def parse_nodes(s):
    finds = re.findall('id: \d+\ndis: \d+.\d+', s)
    d = []
    
    for f in finds:
        ids,dis = f.split('\n')
        ids = int(ids[4:])
        dis = float(dis[5:])
        d.append( (ids,dis) )
    
    return dict(d)

def dict_to_cols(d_series):
    keys = sorted(list(set([key for d in d_series for key in d])))
    cols = {}
    for key in keys:
        cols[key] = []
    
    for d in d_series:
        for key in d:
            cols[key].append(d[key])
        remain = set(keys) - set(d)
        for r in remain:
            cols[r].append(np.nan)
        
    return cols

def mk_uwb_df(filename):
    df = pd.read_csv(filename)
    d_series = df['nodes'].map(parse_nodes)
    cols = dict_to_cols(d_series)
    
    df['t'] = df['Time']

    for key in cols:
        df['n' + str(key)] = cols[key]
    
    SELECT = ['t'] + ['n' + str(key) for key in cols]
    df = df[SELECT]
    
    return df

def mk_out_filename(filename):
    base,ext = os.path.splitext(filename)
    out_filename = f'{base}_uwb{ext}'
    return out_filename

parser = argparse.ArgumentParser()
parser.add_argument('csv_filename', type=str, help='path to uwb csv file')
args = parser.parse_args()

filename = args.csv_filename
out_filename = mk_out_filename(filename)

df = mk_uwb_df(filename)
df.to_csv(out_filename,index=False)

#!/usr/bin/env python
import argparse
import numpy as np
import pandas as pd
from scipy.spatial.transform import Rotation as Rot
import os
from tqdm import tqdm

def compute_rpy(df):
    roll = []
    pitch = []
    yaw = []

    for i in tqdm(range(len(df))):
        curr = df.iloc[i]

        qx = curr['pose.orientation.x']
        qy = curr['pose.orientation.y']
        qz = curr['pose.orientation.z']
        qw = curr['pose.orientation.w']

        rot = Rot.from_quat([qx, qy, qz, qw])
        rx,ry,rz = np.rad2deg(rot.as_euler('xyz'))

        roll.append(rx)
        pitch.append(ry)
        yaw.append(rz)

    return roll,pitch,yaw

def mk_mocap_df(filename):
    df = pd.read_csv(filename)

    roll,pitch,yaw = compute_rpy(df)

    df['t'] = df['Time']
    df['x'] = df['pose.position.x']
    df['y'] = df['pose.position.y']
    df['z'] = df['pose.position.z']
    df['roll'] = roll
    df['pitch'] = pitch
    df['yaw'] = yaw

    SELECT = ['t','x','y','z','roll','pitch','yaw']
    df = df[SELECT]

    return df

def mk_out_filename(filename):
    base,ext = os.path.splitext(filename)
    out_filename = f'{base}_xyzrpy{ext}'
    return out_filename

parser = argparse.ArgumentParser()
parser.add_argument('csv_filename', type=str, help='path to mocap csv file')
args = parser.parse_args()

filename = args.csv_filename
out_filename = mk_out_filename(filename)

df = mk_mocap_df(filename)
df.to_csv(out_filename,index=False)

#!/usr/bin/env python
import argparse
import bagpy
from tqdm import tqdm

parser = argparse.ArgumentParser()
parser.add_argument('bag_filename', type=str, help='path to bag file')
args = parser.parse_args()

filename = args.bag_filename

b = bagpy.bagreader(filename,verbose=True)
csv_files = [b.message_by_topic(t) for t in tqdm(b.topics)]
print(f'{filename} -> {csv_files}')

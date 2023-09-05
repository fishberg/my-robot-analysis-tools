# Quick Start:
# import os, sys
# PATH_TO_LIB = os.path.expanduser('~/dirs/my-robot-analysis-tools/python-imports')
# if PATH_TO_LIB not in sys.path:
#     sys.path.insert(1, PATH_TO_LIB)
# from myimports import *

import os
import sys
import time

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from numpy import arange, deg2rad, rad2deg, cos, sin, arccos, arcsin, arctan2

from numpy import array as ARR
from numpy import pi as PI
from numpy.linalg import norm as NORM
from numpy.linalg import inv as INV
from scipy.spatial.transform import Rotation as ROT
from importlib import reload
from glob import glob as glob

from tqdm.auto import tqdm, trange

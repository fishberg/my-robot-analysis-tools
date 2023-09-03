from myimports import *
import sigfig
import pickle

# Reload with:
'''
import myhelpers
RELOAD(myhelpers)
from myhelpers import *
'''

# ======================================
# radians
# ======================================

def pmpi(rads):
    '''
    clamps all rads to [-π,π)
    '''
    return ((rads - PI) % (2*PI)) - PI

# --------------------------------------

def rad_dist_signed(to,fr):
    '''
    signed angular distance from `fr` to `to`
    '''
    diff = to - fr
    dist_signed = arctan2(sin(diff),cos(diff))
    return dist_signed

# --------------------------------------

def rad_dist_unsigned(to,fr):
    '''
    unsigned angular distance from `fr` to `to`
    '''
    dist_signed = rad_dist_signed(to,fr)
    dist_unsigned = np.abs(dist_signed)
    return dist_unsigned

# --------------------------------------

def rad_err_signed(true,pred):
    '''
    error signal between true and prediction
    z = z_t + err
    err = z - z_t
    '''
    err_signed = rad_dist_signed(pred,true) #true,pred)
    return err_signed

# --------------------------------------

def rad_err_unsigned(true,pred):
    '''
    absolute error signal between true and pred
    z = z_t + err
    err = abs(z - z_t)
    '''
    err_unsigned = rad_dist_unsigned(true,pred)
    return err_unsigned

# --------------------------------------

def rad_vel(rads,same_len=True):
    '''
    signed angular rate of change.
    default behavior is similar to to df.diff for easier plotting
    (i.e. returned list is same length with first element as np.nan)
    same_len=False makes it behave similar to np
    (i.e. returned list is N-1 length)
    '''
    arg = np.nan if same_len else np._NoValue
    vel_signed = pmpi(np.diff(rads,prepend=arg))
    return vel_signed

# --------------------------------------

def rad_speed(rads,same_len=True):
    '''
    unsigned angular rate of change.
    default behavior is similar to to df.diff for easier plotting
    (i.e. returned list is same length with first element as np.nan)
    same_len=False makes it behave similar to np
    (i.e. returned list is N-1 length)
    '''
    vel_signed = rad_vel(rads,same_len=same_len)
    vel_unsigned = np.abs(vel_signed)
    return vel_unsigned

# ======================================
# degrees
# ======================================

def pm180(degs):
    '''
    clamps all degs to [-180,180)
    '''
    return ((degs - 180) % 360) - 180

# --------------------------------------

def deg_dist_signed(to,fr):
    '''
    signed angular distance from `fr` to `to`
    '''
    rad_args = deg2rad([to,fr])
    rad_res = rad_dist_signed(*rad_args)
    deg_res = rad2deg(rad_res)
    return deg_res

# --------------------------------------

def deg_dist_unsigned(to,fr):
    '''
    unsigned angular distance from `fr` to `to`
    '''
    rad_args = deg2rad([to,fr])
    rad_res = rad_dist_unsigned(*rad_args)
    deg_res = rad2deg(rad_res)
    return deg_res

# --------------------------------------

def deg_err_signed(true,pred):
    '''
    error signal between true and pred
    z = z_t + err
    err = z - z_t
    '''
    rad_args = deg2rad([true,pred])
    rad_res = rad_err_signed(*rad_args)
    deg_res = rad2deg(rad_res)
    return deg_res

# --------------------------------------

def deg_err_unsigned(true,pred):
    '''
    absolute error signal between true and pred
    z = z_t + err
    err = abs(z - z_t)
    '''
    rad_args = deg2rad([true,pred])
    rad_res = rad_err_unsigned(*rad_args)
    deg_res = rad2deg(rad_res)
    return deg_res

# --------------------------------------

def deg_vel(rads,same_len=True):
    '''
    signed angular rate of change.
    default behavior is similar to to df.diff for easier plotting
    (i.e. returned list is same length with first element as np.nan)
    same_len=False makes it behave similar to np
    (i.e. returned list is N-1 length)
    '''
    rad_args = deg2rad([rads])
    rad_res = rad_vel(*rad_args,same_len=same_len)
    deg_res = rad2deg(rad_res)
    return deg_res

# --------------------------------------

def deg_speed(rads,same_len=True):
    '''
    unsigned angular rate of change.
    default behavior is similar to to df.diff for easier plotting
    (i.e. returned list is same length with first element as np.nan)
    same_len=False makes it behave similar to np
    (i.e. returned list is N-1 length)
    '''
    rad_args = deg2rad([rads])
    rad_res = rad_vel(*rad_args,same_len=same_len)
    deg_res = rad2deg(rad_res)
    return deg_res

# ======================================
# pos
# ======================================

def pos_err_abs_arr(a,b):
    '''

    '''
    assert a.shape[0] in [2,3]
    assert b.shape[0] in [2,3]
    assert a.shape[1] == b.shape[1]
    raise NotImplementedError

# --------------------------------------

def pos_dist(df,cols1,cols2):
    '''
    position distance between agents at df[cols1] and df[cols2]
    respectively
    (i.e. cols1=['x','y','z'],cols2=['res_x','res_y','res_z'])
    '''
    assert len(cols1) == len(cols2)
    sq_diff = [(df[i] - df[j])**2 for i,j in zip(cols1,cols2)]
    dists = np.sqrt(np.sum(sq_diff,axis=0))
    return dists

# --------------------------------------

def pos_err_abs(df,cols_true,cols_pred):
    '''
    abs position error where agents are at df[cols_true] and df[cols_pred]
    respectively
    (i.e. cols_true=['x','y','z'],cols_pred=['res_x','res_y','res_z'])
    '''
    return pos_dist(df,cols_true,cols_pred)

# ======================================
# pose
# ======================================


# ======================================
# misc
# ======================================

def QR(arr,dp=2):
    '''
    Quick Round, where `dp` is `decimal places`
    '''
    return np.round(arr,c)

# --------------------------------------

def QSR(arr,sf):
    '''
    Quick SigFig Round, where `sf` is significant figures (sigfigs)
    '''
    func = np.vectorize(lambda x: sigfig.round(x,sf))
    return func(arr)

# ======================================
# todo
# ======================================

# def mean_angle(lst):
#     x = 0
#     y = 0
#     for rad in np.deg2rad(lst):
#         x += np.cos(rad)
#         y += np.sin(rad)    
#     return np.rad2deg(np.arctan2(y,x))
# 
# def calc_spherical(x,y,z):
#     x = np.array(x)
#     y = np.array(y)
#     z = np.array(z)
#     #assert len(x) == len(y)
#     #assert len(y) == len(z)
#     rho = np.linalg.norm([x,y,z],axis=0)
#     #assert len(x) == len(rho)
#     az = np.rad2deg(np.arctan2(y,x))
#     #assert len(x) == len(az)
#     el = np.rad2deg(np.arcsin(z / rho))
#     return rho,az,el

def str_read(filename):
    with open(filename,'r') as READ:
        data = READ.read()
    return data

def str_write(filename,s):
    with open(filename,'w') as WRITE:
        WRITE.write(s)

def str_writeln(filename,s):
    with open(filename,'w') as WRITE:
        WRITE.write(s + '\n')

def str_append(filename,s):
    with open(filename,'a') as WRITE:
        APPEND.write(s)

def str_appendln(filename,s):
    with open(filename,'a') as APPEND:
        APPEND.write(s + '\n')

def str_remove_multispace(s):
    while '  ' in s:
        s = s.replace('  ', ' ')
    return s



# ======================================
# pickle
# ======================================

def pickle_write(filename,obj):
    with open(filename,'wb') as WRITE:
        pickle.dump(obj, WRITE)

def pickle_read(filename):
    with open(filename,'rb') as READ:
        obj = pickle.load(READ)
    return obj



# ======================================
# matplotlib
# ======================================
    
# matplotlib default config
def set_matplotlib_defaults():
    # settings might not stick until after the first plot is made
    plt.plot()
    plt.close('all')

    SMALL_SIZE = 15
    MEDIUM_SIZE = 20
    BIGGER_SIZE = 20

    plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
    plt.rc('axes', titlesize=BIGGER_SIZE)    # fontsize of the axes title
    plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
    plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
    plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
    plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
    plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title

    plt.rcParams["figure.figsize"] = [10,10]

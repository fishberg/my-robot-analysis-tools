from scipy.spatial.transform import Rotation as Rot
import numpy as np

class Pose:
    
    @staticmethod
    def from_xyzrpy(x,y,z,roll,pitch,yaw):
        rot = Rot.from_euler('zyx',[yaw,pitch,roll],degrees=True)
        T = np.zeros((4,4))
        T[0:3,0:3] = rot.as_matrix()
        T[0:3,3] = np.array([x,y,z])
        T[3,3] = 1
        return T
    
    @staticmethod
    def from_xyzy(x,y,z,yaw):
        return Pose.from_xyzrpy(x,y,z,0,0,yaw)
    
    @staticmethod
    def from_xyy(x,y,yaw):
        return Pose.from_xyzrpy(x,y,0,0,0,yaw)
    
    @staticmethod
    def from_xyzrot(x,y,z,rot):
        T = np.zeros((4,4))
        assert rot.shape == (3,3)
        T[0:3,0:3] = rot[:,:]
        T[0:3,3] = np.array([x,y,z])
        T[3,3] = 1
        return T
    
    @staticmethod
    def to_xyzrpy(T):
        x,y,z = T[0:3,3]
        rot = Rot.from_matrix(T[0:3,0:3])
        yaw,pitch,roll = rot.as_euler('zyx', degrees=True)
        return (x,y,z,roll,pitch,yaw)
    
    @staticmethod
    def to_xyzy(T):
        x,y,z,roll,pitch,yaw = Pose.to_xyzrpy(T)
        return (x,y,z,yaw)
    
    @staticmethod
    def to_xyy(T):
        x,y,z,roll,pitch,yaw = Pose.to_xyzrpy(T)
        return (x,y,yaw)
    
    @staticmethod
    def to_xyzrot(T):
        x,y,z = T[0:3,3]
        rot = T[0:3,0:3]
        return (x,y,z,rot)
    
    @staticmethod
    def to_T(self):
        return T

########################################

# pts: 3xN
def to_homogeneous_pts(pts):
    assert len(pts.shape) == 2
    assert pts.shape[0] == 3
    hpts = np.ones((4,pts.shape[1]))
    hpts[0:3,:] = pts[:,:]
    return hpts

# hpts: 4xN
def un_homogeneous_pts(hpts):
    assert len(hpts.shape) == 2
    assert hpts.shape[0] == 4
    pts = hpts[0:3,:]
    return pts

# T: 4x4
# pts: 3xN
def transform_pts(T,pts):
    hpts = to_homogeneous_pts(pts)
    res = un_homogeneous_pts(T @ hpts)
    return res

########################################

# treats each row as a vector
# both must have same number of cols
# A.shape = (n,m)
# B.shape = (l,m)
# output = (n,l)

# https://nenadmarkus.com/p/all-pairs-euclidean/
def all_pairs_euclid_numpy(A, B):
	#
	sqrA = np.broadcast_to(np.sum(np.power(A, 2), 1).reshape(A.shape[0], 1), (A.shape[0], B.shape[0]))
	sqrB = np.broadcast_to(np.sum(np.power(B, 2), 1).reshape(B.shape[0], 1), (B.shape[0], A.shape[0])).transpose()
	#
	return np.sqrt(
		sqrA - 2*np.matmul(A, B.transpose()) + sqrB
	)

# base: Nx3
# other: Mx3
# T: 4x4
#def get_pairwise(base_pts,other_points,x,y,z,rx,ry,rz):
def get_pairwise(base,other,T):
    assert len(base.shape) == 2
    assert base.shape[1] == 3

    assert len(other.shape) == 2
    assert other.shape[1] == 3

    other_h = to_homogeneous_pts(other.T)
    other_T = un_homogeneous_pts(T @ other_h).T

    return all_pairs_euclid_numpy(base, other_T)

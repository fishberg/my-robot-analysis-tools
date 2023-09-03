# Run all tests by running `pytest` within this folder
# https://docs.pytest.org/en/7.1.x/getting-started.html

from myimports import *
from myhelpers import *

from numpy import isclose as EQ
from numpy import any as ANY
from numpy import all as ALL

# ======================================
# radians
# ======================================

def test_pmpi():
    assert EQ( pmpi(PI)   , -PI )
    assert EQ( pmpi(2*PI) , 0   )
    assert EQ( pmpi(PI)   , -PI )
    assert EQ( pmpi(3*PI) , -PI )

def test_rad_dist_signed():
    x1 = -1
    x2 = 1
    assert EQ( rad_dist_signed(x2,x1) , 2 )
    assert EQ( rad_dist_signed(x1,x2) , -2 )

    x1 = PI - .1
    x2 = -PI + .1
    assert EQ( rad_dist_signed(x2,x1) ,  .2)
    assert EQ( rad_dist_signed(x1,x2) , -.2)

def test_rad_dist_unsigned():
    x1 = -1
    x2 = 1
    assert EQ( rad_dist_unsigned(x2,x1) , 2 )
    assert EQ( rad_dist_unsigned(x1,x2) , 2 )

    x1 = PI - .1
    x2 = -PI + .1
    assert EQ( rad_dist_unsigned(x2,x1) , .2)
    assert EQ( rad_dist_unsigned(x1,x2) , .2)

def test_rad_vel():
    x = rad_vel(arange(10))
    y = np.ones(10)
    y[0] = np.nan
    assert ALL(EQ( x, y, equal_nan=True ))

    x = rad_vel(pmpi(arange(10)))
    y = np.ones(10)
    y[0] = np.nan
    assert ALL(EQ( x, y, equal_nan=True ))

    x = rad_vel(arange(10),same_len=False)
    y = np.ones(9)
    assert ALL(EQ( x, y, equal_nan=True ))

    '''
    a = reversed(arange(10))
    x = rad_vel(a)
    y = -1 * np.ones(10)
    y[0] = np.nan
    assert ALL(EQ( x, y, equal_nan=True ))
    '''

# ======================================
# degrees
# ======================================

def test_deg_err_signed():
    # z = z_t + z_err
    # z_err = z - z_t

    true = [10,20,30]
    pred = [-10,-10,-10]
    res = deg_err_signed(true,pred)
    assert ALL(EQ( res, [-20,-30,-40]))

    true = [-10,-10,-10]
    pred = [10,20,30]
    res = deg_err_signed(true,pred)
    assert ALL(EQ( res, [20,30,40] ))

# ======================================
# pos
# ======================================



# ======================================
# pose
# ======================================


# ======================================
# misc
# ======================================

def test_QSR():
    assert QSR(12345,3) == 12300
    assert QSR(123.45,3) == 123
    assert QSR(12.345,3) == 12.3
    assert QSR(-12345,3) == -12300
    assert QSR(-123.45,3) == -123

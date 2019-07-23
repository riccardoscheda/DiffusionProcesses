########## file for the functions for the integration of the system ###########


import numpy as np

def phi(q,p,omega = 0.1):
    """
    The vectorial field which generates the evolution in the pase space
    ---------------------------------
    Parameters:
    q : the generalized coordinate, float
    p : the generalized momenta, float
    omega : frequency, float

    Return the derivative of the potential with respect to q and p.
    Since the potential depends only on the coordinate q, the derivative for the momenta is always zero
    """
    return omega**2*q, 0.


def euler(q,p,dt = 0.1,eps= 0.1,beta = 0.1):
    """
    Euler method to obtain the evolution of the system
    ------------------------------------------
    Parameters:
    q : the generalized coordinate, float
    dt : the evolution time step, float
    eps : constant which scale the intensity of the white noise csi
    beta : dumping constant (?)

    Returns the evolution of the coordinates q and p

    """
    # white noise
    csi = np.random.normal(0, 1)
    #evolution of the coordinate q
    evoq = p
    evop = -beta * p + phi(q,p)[0]*dt + eps*np.sqrt(dt)*csi
    return evoq, evop

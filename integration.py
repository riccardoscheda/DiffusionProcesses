########## file for the functions for the integration of the system ###########


import numpy as np

def phi(q,p,omega = 2):
    """
    The vectorial field which generates the evolution in the pase space
    ---------------------------------
    Parameters:
    q : the generalized coordinate, float
    p : the generalized momenta, float
    omega : frequency, float

    Return the derivative of the potential with respect to q.
    """
    return p, - omega**2*q


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
    #evolution of the coordinates q and p
    evoq = q + phi(q,p)[0]*dt
    evop = -beta*p + phi(q,p)[1]*dt + eps*np.sqrt(dt)*csi
    return evoq, evop


def simplettic(q,p,dt = 0.1,eps= 0.1,beta = 0.1):
    """
    Simplettic integration method to obtain the evolution of the system
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
    #evolution of the coordinates q and p
    evoq = q + phi(q,p + dt*phi(q, p)[1])[0]*dt
    evop = -beta*p + phi(q,p)[1]*dt + eps*np.sqrt(dt)*csi
    return evoq, evop

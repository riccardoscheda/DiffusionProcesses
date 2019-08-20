########## file for the functions for the integration of the system ###########


import numpy as np

def mod(v):
    """
    Computes the module of a vector
    """
    return np.sqrt(sum(v*v,axis=0))

def phi(q,p,omega = 0.5):
    """
    The vectorial field which generates the evolution in the pase space
    Parameters:
    ---------------------------------
    q : the generalized coordinate, float
    p : the generalized momenta, float
    omega : frequency, float

    Return the derivative of the potential with respect to q.
    """
    #mass of the particle
    m = 1.2e-21
    #return p, - omega**2*q
    return p/m, 0.



def simplettic(q,p,dt,eps,gamma):
    """
    Simplettic integration method to obtain the evolution of the system
    Parameters:
    ------------------------------------------
    q : the generalized coordinate, float
    dt : the evolution time step, float
    eps : constant which scale the intensity of the white noise csi
    gamma : dumping constant (?)

    Returns the evolution of the coordinates q and p

    """
    # white noise
    csi = np.random.normal(0, 1)

    #evolution of the coordinates q and p
    evoq = q + phi(q,p + dt*phi(q, p)[1])[0]*dt
    evop = p -gamma*p - phi(q,p)[1]*dt + eps*np.sqrt(dt)*csi
    return evoq, evop


#####################################################################
#####################################################################

def euler(q,p,dt ,eps,gamma):
    """
    Euler method to obtain the evolution of the system
    Parameters:
    ------------------------------------------
    q : the generalized coordinate, float
    dt : the evolution time step, float
    eps : constant which scale the intensity of the white noise csi
    gamma : dumping constant (?)

    Returns the evolution of the coordinates q and p

    """
    # white noise
    csi = np.random.normal(0, 1)
    #evolution of the coordinates q and p
    evoq = q + phi(q,p)[0]*dt
    evop = -gamma*p + phi(q,p)[1]*dt + eps*np.sqrt(dt)*csi
    return evoq, evop

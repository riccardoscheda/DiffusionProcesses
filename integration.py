########## file for the functions for the integration of the system ###########

import numpy as np


def mod(v):
    """
    Computes the module of a vector
    """
    return np.sqrt(sum(v*v,axis=0))

def phi(q,p,omega = 1.5):
    """
    The vectorial field which generates the evolution in the pase space
    Parameters:
    ---------------------------------
    q : the generalized coordinate, float
    p : the generalized momenta, float
    omega : frequency, float

    Return the derivative of the potential with respect to q.
    """
    
##################HARMONIC OSCILLATOR
#    return p , -(q-2)*omega**2  
################# DOUBLE WELL POTENTIAL
    a = 1.7
    b = 1.7
    return p, -(4*q**3 +3*b*q**2 - 3*a*q**2 - 2*a*b*q)
###################


def entropy(rho,bins):
    """
    Computes the entropy of the system.
    Parameters:
    ---------------------------------------
    rho: the probability distribution of the system
    bins: the bins of the distribution

    Returns the entropy as a float
    """

    return np.sum(rho*np.log(rho)*np.diff(bins))


def Shannon_entropy(N,qx,qy,qz,px,py,pz):


  space = np.array(qx)

  space = np.vstack((space,qy))
  space = np.vstack((space,qz))
  space = np.vstack((space,px))
  space = np.vstack((space,py))
  space = np.vstack((space,pz))


  
  hist_space, bins = np.histogramdd(np.array(space.T), density = 1,bins = (2,2,2,2,2,2))#,range = (interval,interval,interval,interval,interval,interval))

  hist_space += 1e-35


  return hist_space, bins

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
    evop = p -gamma*p*dt + phi(q,p)[1]*dt + eps*np.sqrt(dt)*csi
    return evoq, evop


def simplettic(q,p,dt,eps,gamma):
    """
    Simplettic integration method to obtain the evolution of the system
    Parameters:
    ------------------------------------------
    q : the generalized coordinate, float
    dt : the evolution time step, float
    eps : constant which scale the intensity of the white noise csi
    gamma : damping constant (?)

    Returns the evolution of the coordinates q and p

    """
    # white noise
    csi = np.random.normal(0, 1.)

    #evolution of the coordinates q and p
    evoq = q + phi(q,p + dt*phi(q, p)[1])[0]*dt
    evop = p -gamma*p*dt + phi(q,p)[1]*dt + eps*np.sqrt(dt)*csi
    return evoq, evop

########Main file for the evolution of the system########


import pylab as plt
import numpy as np
#########################
import integration as int



#number of iterations
it = 100
#time step
dt = .1
#arrays for the coordinates which will contain the evolution of the system
q_eu, p_eu = np.empty(it), np.empty(it)
# initial conditions
q_eu[0], p_eu[0] = 3, .0
#evolution
for t in range(it-1):


    plt.clf()

    #euler method
#    q_eu[t+1], p_eu[t+1] = int.euler(q_eu[t], p_eu[t],dt,eps = 0.0 ,beta = 0)
    #simplettic method
    q_eu[t+1], p_eu[t+1] = int.simplettic(q_eu[t], p_eu[t],dt,eps = 0. ,beta = -0.9)

    #phase space
    # plt.xlim(-3,3)
    # plt.ylim(-3,3)
    # plt.plot(q_eu[:t+1],p_eu[:t+1])


    plt.ylim(-10,10)
    plt.xlim(0,100)
    plt.plot(q_eu[:t+1])
    plt.plot(p_eu[:t+1])

    plt.pause(0.05)

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
q_eu[0], p_eu[0] = .5, 0
#evolution
for t in range(it-1):
  plt.clf()
  q_eu[t+1], p_eu[t+1] = int.euler(q_eu[t], p_eu[t], dt)
  plt.xlim(0,100)
  plt.plot(q_eu[:t+1])
  plt.plot(p_eu[:t+1])
  plt.pause(0.01)

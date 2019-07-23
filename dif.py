import pylab as plt
import numpy as np
#########################
import integration as int

it = 100
dt = .1
q_eu, p_eu = np.empty(it), np.empty(it)
q_eu[0], p_eu[0] = .5, 0 # initial conditions
for t in range(it-1):
  plt.clf()
  q_eu[t+1], p_eu[t+1] = int.euler(q_eu[t], p_eu[t], dt)
  plt.xlim(0,100)
  plt.plot(q_eu[:t+1])
  plt.plot(p_eu[:t+1])
  plt.pause(0.01)

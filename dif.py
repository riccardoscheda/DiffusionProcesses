########Main file for the evolution of the system########


import pylab as plt
import numpy as np
import matplotlib.animation as animation
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

fig = plt.figure()
ax1 = fig.add_subplot(3,1,1)
ax2 = fig.add_subplot(3,1,2)
ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
ax2 = fig.add_axes([0.6, 0.6, 0.30, 0.30])

def animate(t):

    q_eu[t+1], p_eu[t+1] = int.simplettic(q_eu[t], p_eu[t],dt,eps = 0. ,beta = -1)

    ax1.clear()
    ax1.set_xlim(0,100)
    ax1.set_ylim(-10,10)
    ax1.plot(q_eu[:t+1])
    ax1.plot(p_eu[:t+1])
    ax2.clear()
    ax2.set_xlim(-4,4)
    ax2.set_ylim(-4,4)
    ax2.plot(q_eu[:t+1],p_eu[:t+1])



while True:
    ani = animation.FuncAnimation(fig, animate, interval=80)
    plt.show()

########Main file for the evolution of the system########


import pylab as plt
import numpy as np
import matplotlib.animation as animation
#########################
import integration as int



#number of iterations
it = 200
#number of realizations
N = 10
#time step
dt = .1
#arrays for the coordinates which will contain the evolution of the system
q_eu, p_eu = np.empty((it,N)), np.empty((it,N))
# initial conditions
q_eu[0], p_eu[0] = 0.5, .0

fig = plt.figure()
ax1 = fig.add_subplot(3,1,1)
ax2 = fig.add_subplot(3,1,2)
ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
ax2 = fig.add_axes([0.6, 0.6, 0.30, 0.30])

# def animate(t):
#     for i in range(N):
#         q_eu[t+1][i], p_eu[t+1][i] = int.simplettic(q_eu[t][i], p_eu[t][i],dt,eps = 30 ,beta = +0.9)
#
#     ax1.clear()
#     ax1.set_xlim(0,100)
#     ax1.set_ylim(-30,30)
#     ax1.plot(q_eu[:t+1])
#     #ax1.plot(p_eu[:t+1])
#     # ax2.clear()
#     # ax2.set_xlim(-2,2)
#     # ax2.set_ylim(-2,2)
#     # ax2.plot(q_eu[:t+1],p_eu[:t+1])
#
#
#
# while True:
#     ani = animation.FuncAnimation(fig, animate, interval=80)
#     plt.show()

for t in range(it-1):
    for i in range(N):
        q_eu[t+1][i], p_eu[t+1][i] = int.simplettic(q_eu[t][i], p_eu[t][i],t,dt,eps = 10 ,beta = +0.9)

ax1.set_xlim(0,200)
ax1.set_ylim(-30,30)
ax1.plot(q_eu[:t+1])
plt.show()

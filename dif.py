########Main file for the evolution of the system########


import pylab as plt
import numpy as np
import matplotlib.animation as animation
#########################
import integration as int

############PARAMETERS###################
Kb = 1
T = 500
m = 1
gamma = 0.4
eps = np.sqrt(2*m*Kb*T*abs(gamma))


#dimensions of the space
d = 2
#number of realizations
N = 1
#number of iterations
it = 200
#time step
dt = .1
#arrays for the coordinates which will contain the evolution of the system
qx, px = np.empty((it,N)), np.empty((it,N))
qy, py = np.empty((it,N)), np.empty((it,N))
# initial conditions
qx[0], px[0] = .1, 0.1
qy[0], py[0] = .1, 0

fig = plt.figure()
ax1 = fig.add_subplot(3,1,1)
ax2 = fig.add_subplot(3,1,2)
ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
ax2 = fig.add_axes([0.6, 0.6, 0.30, 0.30])

def animate(t):
    for i in range(N):
        qx[t+1][i], px[t+1][i] = int.simplettic(qx[t][i], px[t][i],dt,eps  ,gamma)
        qy[t+1][i], py[t+1][i] = int.simplettic(qy[t][i], py[t][i],dt,eps  ,gamma)

    ax1.clear()
    ax1.set_xlim(-15,15)
    ax1.set_ylim(-15,15)
    ax1.plot(qx[:t+1],qy[:t+1])
    ax1.scatter(qx[t],qy[t],color="red")
    #ax1.plot(px[:t+1])
    # ax2.clear()
    # ax2.set_xlim(-2,2)
    # ax2.set_ylim(-2,2)
    # ax2.plot(qx[:t+1],px[:t+1])



while True:
    ani = animation.FuncAnimation(fig, animate, interval=80)
    plt.show()

# for t in range(it-1):
#         for k in range(N):
#             qx[t+1][k], px[t+1][k] = int.simplettic(qx[t][k], px[t][k],dt,eps ,gamma)
#
# rhox = np.histogram(qx[-1][0],bins = 50)
# rhop = np.histogram(px[-1], bins = 50)
# #ax1.set_xlim(-200,200)
# #ax1.plot(rhox[1][:-1],rhox[0])
# ax1.hist(qx[-1],bins = 50)
# #ax1.hist(qx[0],bins = 30,alpha = 0.5,label = "initial state")
# #ax1.hist(qx[90],bins = 30, alpha = 0.5,label = "final state")
# #ax1.legend()

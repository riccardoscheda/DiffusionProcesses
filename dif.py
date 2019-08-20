
########Main file for the evolution of the system########


import pylab as plt
import numpy as np
import matplotlib.animation as animation
import scipy.stats as stats
#########################
import integration as int

############PARAMETERS###################
Kb = 1.380648e-23
T = 500
m = 1e-21
gamma = 0.5
a = np.sqrt(2*Kb*T/m*gamma)
#eps = np.sqrt(2*Kb*T*m*abs(gamma))
eps = a**2

maxwell = stats.maxwell
data = maxwell.rvs(loc=0, scale=1, size=10000)

#params = maxwell.fit(data, floc=0)
params = (0, a)

########################################

#dimensions of the space
d = 2
#number of realizations
N = 5000
#number of iterations
it = 50
#time step
dt = .1
#arrays for the coordinates which will contain the evolution of the system
qx, px = np.empty((it,N)), np.empty((it,N))
qy, py = np.empty((it,N)), np.empty((it,N))
vel = []
# initial conditions
qx[0], px[0] = 3, 100
qy[0], py[0] = 3, 100

fig = plt.figure(dpi = 200)
ax1 = fig.add_subplot(3,1,1)
ax2 = fig.add_subplot(3,1,2)
ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
ax2 = fig.add_axes([0.6, 0.6, 0.30, 0.30])

#def animate(t):
for t in range(it-1):
    plt.ion()
    # ax2.clear()
    # ax2.set_xlim(-15,15)
    # ax2.set_ylim(-15,15)
    # ax2.plot(qx[:t+1][0],qy[:t+1][0])
    # ax2.scatter(qx[t][0],qy[t][0],color="red")

    for i in range(N):
        qx[t+1][i], px[t+1][i] = int.simplettic(qx[t][i], px[t][i],dt,eps  ,gamma)
        qy[t+1][i], py[t+1][i] = int.simplettic(qy[t][i], py[t][i],dt,eps  ,gamma)

    vel = np.sqrt(px[t]**2 + py[t]**2)
    hist = np.histogram(vel,density = True,bins = 25)

    entropy = int.entropy(hist)
    ax1.clear()
    #ax1.set_xlim(0,40)
    #ax1.set_ylim(0,0.5)

    ax1.plot(hist[1][:-1],hist[0])

####fitting#####
    x = np.linspace(0, 25, 100)
    ax1.plot(x, maxwell.pdf(x, *params), lw=1)
    plt.pause(0.05)
    plt.show()

#while True:
#    ani = animation.FuncAnimation(fig, animate, interval=50)
#    plt.show()

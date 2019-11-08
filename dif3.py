
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

import matplotlib.animation as animation # animation plot
import pandas as pd

import integration as inte


#############PARAMETERS######################################
#Kb = 1.380648e-23
Kb = 0.01
T = 100

m = 1e-21
m = 1
gamma = 1.
eps = np.sqrt(2*Kb*T*m*gamma)

#eps = np.sqrt(2*Kb*T/m*gamma)

################## HARMONIC OSCILLATOR ######################
#eps = 0.
#gamma = .0
############################################################


#iterations
frames = 100
#particles
N = 5000
#time step
dt = 0.1

##############################################################
qx, px = np.ones(N)*10, -np.ones(N)*m*2

rhox, binx = np.histogram(qx,density = 1, bins = 50)
rhop, binp = np.histogram(px,density = 1,bins = 50)

varx = rhox.var()
varp = rhop.var()

var = varx*varp
########################################################
fig, ax = plt.subplots(2,2)

particle, = ax[0,0].step([],[], label = "rho_x")
trajectory, = ax[0,0].step([],[], label = "rho_p")
maxwelldist, = ax[1,0].step([],[],label = 'distribution')
maxwellfit, = ax[1,0].plot([],[],label = "fit")
ax[0,0].legend()
ax[1,0].legend()
phasespace, = ax[0,1].plot([],[])
entr, = ax[1,1].plot([],[], label = "S")
shan, = ax[1,1].plot([],[], linestyle = "--", label = "S_infty")
ax[1,1].legend()


tx = []
tp = []
entropy = []
shannon = []



def init():

  ax[0,0].set_xlim(-100,100)
  ax[0,0].set_ylim(0,1)
  #ax[0,0].set_title("space")
  ax[0,0].set_xlabel("x")
  ax[0,0].set_ylabel("y")

  ax[0,1].set_xlim(-10,10)
  ax[0,1].set_ylim(-0.1,1)
  ax[0,1].set_xlabel("x")
  ax[0,1].set_ylabel("p")
  ax[0,1].set_title(" Phase space")

  ax[1,0].set_xlim(-0.1, 10)
  ax[1,0].set_ylim(-0.001, 0.01)
  ax[1,0].set_xlabel("v")
  ax[1,0].set_ylabel("rho(v)")
  ax[1,0].set_title("velocity Distribution")

  ax[1,1].set_xlim(0, 800)
  ax[1,1].set_ylim(-10, 10)
  ax[1,1].set_xlabel("time")
  ax[1,1].set_ylabel("entropy")
  ax[1,1].set_title("Entropy")

  return particle,

def evo(frames):
    for i in range(N):
      qx[i], px[i] = inte.simplettic(qx[i], px[i],dt,eps  ,gamma)

    vel = np.sqrt(px**2)/m

    bins = np.arange(np.floor(qx.min()),np.ceil(qx.max()))
    n = 100
    
    rhox, binx = np.histogram(qx,density = 1, bins = 50)
    rhop, binp = np.histogram(px,density = 1,bins = 50)
    
    bins = np.arange(np.floor(vel.min()),np.ceil(vel.max()))
    hist = np.histogram(vel,density = 1, bins=100)


    #tx.append(qx[0])
    #tp.append(px[0]/m)

    rhox += 1e-35
    rhop += 1e-35
    #entropy.append(-np.sum(rhox*rhop*np.log(rhox*rhop)*np.diff(binx)*np.diff(binp)))
    
    particle.set_data(np.linspace(-100,100, num = len(rhox)), rhox)
    trajectory.set_data(np.linspace(-100,100, num = len(rhop)), rhop)
    
    ####################################################
    space = np.array(qx)
    space = np.vstack((space,px))
    
    hist_space, bins = np.histogramdd(np.array(space.T),density = 1)#,range = (interval,interval,interval,interval,interval,interval))
    hist_space += 1e-35
  
    entropy.append(-np.sum(hist_space*np.log(hist_space)*np.diff(bins[0])*np.diff(bins[1])))
    

    ###########################################################
    #fit
    x = np.linspace(0, 10, num = 1000)
    maxwellpdf = 2*np.sqrt(m/(2*np.pi*Kb*T))*np.exp(-x**2*m/(2*Kb*T))/100

    maxwelldist.set_data(hist[1][:-1],hist[0]/100)
    maxwellfit.set_data(x, maxwellpdf)
    entr.set_data(np.arange(0,len(entropy)),entropy)
    
    
    x = np.linspace(0, 1000, num = 1000)
    y = np.ones(1000)*(np.log(Kb*T) + 0.5*np.log(var))
    shan.set_data(x,y)

    return particle, trajectory, maxwelldist, maxwellfit, entr, shan


ani = FuncAnimation(fig, evo, frames = np.arange(0,100), interval = 25,init_func = init, blit = True)
plt.show()

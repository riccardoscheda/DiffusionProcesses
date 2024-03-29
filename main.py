
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

import matplotlib.animation as animation # animation plot
import pandas as pd
import networkx as nx
from matplotlib.animation import FuncAnimation, PillowWriter
import integration as inte

plt.rc('text', usetex=True)
plt.rc('font', family='serif')
plt.rcParams.update({'font.size': 10})
############PARAMETERS######################################
gamma = 1.
eps = 0.6
KT = eps**2/(2*gamma)
m = 1
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
qx, px = np.ones(N)*0, -np.ones(N)*m*0

rhox, binx = np.histogram(qx,density = 1,bins=50)
rhop, binp = np.histogram(px,density = 1,bins=50)

varx = rhox.var()
varp = rhop.var()

var = varx + varp
########################################################
fig, ax = plt.subplots(2,2)

particle, = ax[0,0].step([],[], label = r'$\rho_p$')
trajectory, = ax[0,0].step([],[], label = "fit")
maxwelldist, = ax[1,0].step([],[],label = 'distribution')
maxwellfit, = ax[1,0].plot([],[],label = "fit")
ax[0,0].legend()
ax[1,0].legend()
phasespace, = ax[0,1].step([],[])
entr, = ax[1,1].plot([],[], label = "S")
shan, = ax[1,1].plot([],[], linestyle = "--", label = r"$S_{\infty}$")
ax[1,1].legend()


tx = []
tp = []
entropy = []
shannon = []



def init():

  ax[0,0].set_xlim(-2,2)
  ax[0,0].set_ylim(0,0.05)
  ax[0,0].set_title(r"$p$")
  #ax[0,0].set_xlabel("p",loc="top")
  ax[0,0].set_ylabel(r'$\rho_p$')

  ax[0,1].set_xlim(-5,5)
  ax[0,1].set_ylim(0,0.1)
  #ax[0,1].set_xlabel("x",loc="top")
  ax[0,1].set_ylabel(r'$\rho_x$')
  ax[0,1].set_title(r"$x$")

  ax[1,0].set_xlim(-0.1, 5)
  ax[1,0].set_ylim(-0.001, 0.1)
  ax[1,0].set_xlabel(r"$v$")
  ax[1,0].set_ylabel(r'$\rho(v)$')
  #ax[1,0].set_title("velocity Distribution")

  ax[1,1].set_xlim(0, 300)
  ax[1,1].set_ylim(-5, 5)
  ax[1,1].set_xlabel(r'$time$')
  ax[1,1].set_ylabel(r'entropy')
  #ax[1,1].set_title(r'Entropy')

  return particle,

def evo(frames):
    for i in range(N):
      qx[i], px[i] = inte.simplettic(qx[i], px[i],dt,eps  ,gamma)

    vel = np.sqrt(px**2)/m

    bins = np.arange(np.floor(qx.min()),np.ceil(qx.max()))
    n = 100
    
    rhox, binx = np.histogram(qx,density = 1, bins = 100)
    rhop, binp = np.histogram(px,density = 1,bins = 50)
    

    hist = np.histogram(vel,density = 1, bins=50)


    
    #tx.append(qx[0])
    #tp.append(px[0]/m)

    rhox += 1e-35
    rhop += 1e-35
    #entropy.append(-np.sum(rhox*rhop*np.log(rhox*rhop)*np.diff(binx)*np.diff(binp)))
    
    x = np.linspace(-10, 10, num = 1000)
    maxwellpdf = np.sqrt(m/(2*np.pi*KT))*np.exp(-x**2*m/(2*KT))/50
    trajectory.set_data(x, maxwellpdf)
    particle.set_data(binp[1:], rhop/50)
    phasespace.set_data(binx[1:],rhox/50)
  
    ####################################################
    space = np.array(qx)
    space = np.vstack((space,px))
    
    hist_space, bins = np.histogramdd(np.array(space.T),bins =50,density = 1)#,range = (interval,interval,interval,interval,interval,interval))
    hist_space += 1e-35
  
    entropy.append(-np.sum(hist_space*np.log(hist_space)*np.diff(bins[0])*np.diff(bins[1])))
    


    ###########################################################
    #fit
    x = np.linspace(0, 10, num = 1000)
    maxwellpdf = 2*np.sqrt(m/(2*np.pi*KT))*np.exp(-x**2*m/(2*KT))/50

    maxwelldist.set_data(hist[1][1:],hist[0]/50)
    
    maxwellfit.set_data(x, maxwellpdf)
    entr.set_data(np.arange(0,len(entropy)),entropy)
    
    
    
    x = np.linspace(0, 1000, num = 1000)
    y = np.ones(1000)*(np.log(KT) + 0.5*np.log(var)) 
    shan.set_data(x,y)

    return particle, trajectory, phasespace, maxwelldist, maxwellfit, entr, shan


ani = FuncAnimation(fig, evo, frames = np.arange(0,100), interval = 50,init_func = init, blit = True)
plt.tight_layout(rect=[0, 0.02, 1, 0.95])
#plt.show()

# if you want to save a gif
ani.save('Doublewell.gif', dpi=200, writer='pillow')
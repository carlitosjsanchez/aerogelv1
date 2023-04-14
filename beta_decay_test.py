# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 17:07:49 2023

@author: FAYOGA
"""

import matplotlib.pyplot as plt


''' 

We will simulate & graph (Beta +) Decay of K-40 from Banana!

The 70 kg man emits typically 160-180 positrons per hour.


'''

# Set the functions for the particles decay (they'll release positrons)

prob = .1072 # Number of Beta + Decay in K-40
time_step = 1 # The time-step of the decay (per one second)

# Make a Python Loop

particles  = 3333 # Number of K-40 atoms that 70KG man emits per second. 
time = 0 # Start time (in seconds)

particle_list = [] # store the value of particles with relationship to time
time_list = [] # amount of time that passes for K-40 particles to decay

while time <= 60: # must last 60
    particle_list.append(particles)
    time_list.append(time)
    print(time, particles)
    particles += -particles * prob * time_step
    time += time_step

# now for plotting graph

plt.plot(time_list, particle_list, 'r')
plt.xlabel("time (sec)")
plt.ylabel("particles")
plt.savefig('decay.png', dpi = 300)
plt.show()

# LETS SEE IF IT WORKED.











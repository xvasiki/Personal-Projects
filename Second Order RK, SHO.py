#Vasiki Konneh
#Code using RK2 for Simple Harmonic Oscillator; examines 4 diff. casses of oscillation damping
    # β = 0
    # β = ω0/20
    # β = 5ω0
    # β = ω0
#produces pos v. time & vel vs. time graphs,
# t_max = 10 s & frequency set to 2


import matplotlib.pyplot as plt
import numpy as np
import math
import pandas as pd
omega0 = 2
betaNo = 0
betaUnder = .1
betaOver = 10
betaCrit = omega0
# acceleration as a function of beta, position, and velocity
def vdot(beta, pos, vel):
 return -2*beta*vel - omega0**2*pos
# initial values and dt
t = [0]
dt = 0.1
posInit = 5
vInit = -1
xNo = [posInit]
xUnder = [posInit]
xOver = [posInit]
xCrit = [posInit]
vNo = [vInit]
vUnder = [vInit]
vOver = [vInit]
vCrit = [vInit]
step = 0

while t[step] < 10:
    # RK2 for undamped
    xNoHalf = xNo[step] + vNo[step] * dt / 2
    vNoHalf = vNo[step] + vdot(betaNo, xNo[step], vNo[step]) * dt / 2

    xNo.append(xNo[step] + vNoHalf * dt)
    vNo.append(vNo[step] + vdot(betaNo, xNoHalf, vNoHalf) * dt)

    # RK2 for underdamped
    xUnderHalf = xUnder[step] + vUnder[step] * dt / 2
    vUnderHalf = vUnder[step] + vdot(betaUnder, xUnder[step],
                                     vUnder[step]) * dt / 2

    xUnder.append(xUnder[step] + vUnderHalf * dt)
    vUnder.append(vUnder[step] + vdot(betaUnder, xUnderHalf, vUnderHalf) * dt)

    # RK2 for overdamped
    xOverHalf = xOver[step] + vOver[step] * dt / 2
    vOverHalf = vOver[step] + vdot(betaOver, xOver[step], vOver[step]) * dt / 2

    xOver.append(xOver[step] + vOverHalf * dt)
    vOver.append(vOver[step] + vdot(betaOver, xOverHalf, vOverHalf) * dt)

    # RK2 for critically damped
    xCritHalf = xCrit[step] + vCrit[step] * dt / 2
    vCritHalf = vCrit[step] + vdot(betaCrit, xCrit[step], vCrit[step])*dt/2

    xCrit.append(xCrit[step] + vCritHalf*dt)
    vCrit.append(vCrit[step] + vdot(betaCrit, xCritHalf,vCritHalf)*dt)

    # append new time to t array and take one step forward (step is to keep track of where we are in the array)
    t.append(t[step] + dt)
    step = step + 1
# plot
plt.figure()
plt.subplot(211)
plt.plot(t, xNo, t, xUnder, t, xOver, t, xCrit)
plt.xlabel('Time (s)')
plt.ylabel('Position (m)')
plt.legend(['no damping', 'under', 'over', 'critical'])
plt.subplot(212)
plt.plot(t, vNo, t, vUnder, t, vOver, t, vCrit)
plt.legend(['no damping', 'under', 'over', 'critical'])
plt.xlabel('Time (s)')
plt.ylabel('Velocity (m/s)')
plt.show()
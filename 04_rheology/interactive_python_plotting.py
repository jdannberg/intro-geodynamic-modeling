import matplotlib.pyplot as plt
from scipy import special
import numpy as np

plt.ion()

density = 3300
gravity = 10
diffusivity = 1e-6
time = 3.2e15
strainrate = 3e-16
A = 3.7e-15
grainsize = 1e-3
E = 335000
V = 4e-6
gasconstant = 8.314

z = np.arange(0.0, 1e5, 1e3)
pressure = density*gravity*z
fig, (ax1, ax2, ax3) = plt.subplots(3, 1)
ax1.plot(z, pressure)
ax1.set_ylabel('Pressure in Pa')

temperature=273+(1600-273)*special.erf(z/np.sqrt(diffusivity*time))
ax2.plot(z, temperature)
ax2.set_ylabel('Temperature in K')

stress=strainrate/A*grainsize**3*np.exp((E+pressure*V)/(gasconstant*temperature)) 
ax3.set_yscale('log')
ax3.set_ylim(1, 1e30)
ax3.plot(z, stress)
ax3.set_ylabel('Stress in Pa')
ax3.set_xlabel('Depth in m')

phi=20./180.*3.1416
cohesion = 2e6
yield_stress=pressure*np.sin(phi)+cohesion*np.cos(phi)
ax3.plot(z, yield_stress)

ax3.set_yscale('linear')
ax3.set_ylim(0, 6e8)

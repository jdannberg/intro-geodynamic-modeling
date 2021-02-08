import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Load the columns of the csv file
x = np.genfromtxt('onset-convection-data.csv', dtype=float, delimiter=' ', usecols = (0))
y = np.genfromtxt('onset-convection-data.csv', dtype=float, delimiter=' ', usecols = (1))
z1 = np.genfromtxt('onset-convection-data.csv', dtype=float, delimiter=' ', usecols = (2))
z2 = np.genfromtxt('onset-convection-data.csv', dtype=float, delimiter=' ', usecols = (3))

z=z2/z1

# make the plot
fig, ax = plt.subplots()
cax = ax.scatter(x,y, c=z, s=1000, cmap='viridis', vmin=0.97, vmax=1.03)

# use logarithmic scales for the axes
ax.set_xscale('log')
ax.set_yscale('log')

# add labels and units
fig.colorbar(cax).set_label("Relative velocity change", labelpad=20, rotation=270) 
plt.xlabel("Viscosity (Pa s)")
plt.ylabel("Temperature variation across the mantle (K)")

plt.show()

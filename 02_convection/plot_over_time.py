import matplotlib.pyplot as plt
import numpy as np

# Load the columns of the csv file
x = np.genfromtxt('output/statistics', dtype=float, usecols = (1))
y = np.genfromtxt('output/statistics', dtype=float, usecols = (10))

# make the plot
fig, ax = plt.subplots()
cax = ax.plot(x, y, 'o-')

# add labels and units
plt.xlabel("Time (yr)")
plt.ylabel("Velocity (m/yr)")

plt.show()

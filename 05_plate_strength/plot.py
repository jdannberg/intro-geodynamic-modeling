import matplotlib.pyplot as plt
import numpy as np

output_directory = "output-plate"
ouput_file = output_directory + "/statistics"

# Load the columns of the csv file
x = np.genfromtxt(ouput_file, dtype=float, usecols = (1))
vmax = np.genfromtxt(ouput_file, dtype=float, usecols = (34))
vmin = np.genfromtxt(ouput_file, dtype=float, usecols = (35))

# make the plot
fig, ax = plt.subplots()
cax = ax.plot(x, vmax-vmin, 'bo-')

# add labels and units
plt.xlabel("Time (yr)")
plt.ylabel("Velocity (m/yr)")

plt.show()

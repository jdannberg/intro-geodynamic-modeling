import sys
import csv
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

# Read CSV
csvFileName = sys.argv[1]
csvData = []
with open(csvFileName, 'r') as csvFile:
    csvReader = csv.reader((line for line in csvFile if not line.startswith('#') and not line.isspace()), delimiter=' ')
    for csvRow in csvReader:
        csvData.append(csvRow)

# Get X, Y, Z
csvData = np.array(csvData)
X, Y, Z = csvData[:,1].astype(np.float), csvData[:,2].astype(np.float), csvData[:,9].astype(np.float)

# Plot X,Y,Z
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_trisurf(X, Y, Z, edgecolors='none', alpha=1.0, cmap="magma")

# Labels and color bar
ax.set_xlabel('Longitude (degrees)')
ax.set_ylabel('Latitude (degrees)')

color_bar = fig.colorbar(surf, shrink=0.5, aspect=5)
color_bar.ax.set_ylabel('Gravity anomaly (m/s^2)')

# Annotate maximum gravity
gravitymax = round(max(Z),4)
label = 'Maximum: ' + str(gravitymax) + ' m/s^2'
ax.text2D(0.05, 0.95, label, transform=ax.transAxes)

plt.show()

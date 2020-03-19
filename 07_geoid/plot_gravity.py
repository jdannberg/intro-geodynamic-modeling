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
ax.plot_trisurf(X, Y, Z, edgecolors='none', alpha=1.0, cmap="magma")
# ax.scatter(X, Y, Z, c='red')
plt.show()

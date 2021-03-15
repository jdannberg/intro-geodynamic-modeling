import numpy as np
import pandas

# Longitude and latitude of the starting point (in degrees)
longitude = -72
latitude = -18.4

# Convert from latitude and longitude to the coordinates in the data file
if longitude < 0.0: longitude += 180.0
theta = (90.0 - latitude) * np.pi/180.0
phi = longitude * np.pi/180.0
phi2 = phi + 1.0 / np.sin(theta) * 2200.0 / 6371.0

# Read in the data file as a pandas dataframe, and select data in the light lat/lon range
table = pandas.read_csv("LAB_CAM2016.txt", delimiter='\t', comment='#', names=['Longitude', 'Latitude', 'Depth'])
selection = table[(table['Longitude']>phi) & (table['Longitude']<phi2) & (table['Latitude']<theta)]
last_value = selection.iloc[-1].at['Latitude']

selection2 = selection[table['Latitude']==last_value]
selection2.reset_index(drop=True, inplace=True)

# Create a new data frame for the composition
column_names = ['x', 'y', 'C1', 'C2', 'C3', 'C4']
composition = pandas.DataFrame(0, index=np.arange(len(selection2)), columns=column_names)

x0 = selection2.iloc[0].at['Longitude']
theta = selection2.iloc[0].at['Latitude']
composition['x'] = (selection2['Longitude'] - x0) * np.sin(theta) * 6371000.0 - 500000.0
composition['y'] = 250000.0 - selection2['Depth']

# Write data to an output file
file_name = "lithosphere.txt"
f = open(file_name, "w")
f.write('# Initial composition\n')
f.write('# Only next line is parsed in format: [nx] [ny] because of keyword "POINTS:"\n')
f.write('# POINTS: ' + str(len(composition)) + '\n')
f.write('# x     y       composition\n')
f.close()

print('Writing "lithosphere.txt"\n')
composition.to_csv(file_name, header=False, sep=' ', index=False, mode='a')

# Create a new data frame for the temperature
column_names = ['x', 'y', 'temperature']
T = pandas.DataFrame(1600, index=np.arange(len(selection2)), columns=column_names)
T['x'] = composition['x']
T['y'] = composition['y']

# Write data to an output file
file_name = "lithosphere_T.txt"
f = open(file_name, "w")
f.write('# Initial temperature\n')
f.write('# Only next line is parsed in format: [nx] [ny] because of keyword "POINTS:"\n')
f.write('# POINTS: ' + str(len(composition)) + '\n')
f.write('# x     y       temperature\n')
f.close()

print('Writing "lithosphere_T.txt"')
T.to_csv(file_name, header=False, sep=' ', index=False, mode='a')

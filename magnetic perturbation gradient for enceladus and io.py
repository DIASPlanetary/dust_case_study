# -*- coding: utf-8 -*-
"""
Created on Mon Mar 10 13:57:39 2025

@author: march
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from scipy.interpolate import interp1d
from scipy.spatial import ConvexHull


def clean_array(arr):
    # Removes infinite, NaN, and zero values from a NumPy array
    arr = np.array(arr)  # Ensure input is a NumPy array
    mask = ~np.isinf(arr) & ~np.isnan(arr) & (arr != 0)
    return arr[mask]


def data_processing(radius, density, velocity, radius_m):
    CSA = []
    MFP = []
    SB = []
    for i in range(0, len(density)):
        for j in range(0, len(radius)):
            csa = 4*np.pi*(radius[j]**2)
            CSA.append(csa)
            mfp = 1/(density[i]*csa)
            MFP.append(mfp)
            sb = (mu0*radius_m*density[i]*150*elec*velocity)/2
            SB.append(sb)
    return CSA, MFP, SB


# Load the datasets from the respective CSV files
datasetEnM = np.loadtxt('Enceladus_meier_extremes.csv', delimiter=',').T
datasetIA = np.loadtxt('Io_adeloye_extremes.csv', delimiter=',').T
datasetEuS = np.loadtxt('Europa_south_extremes.csv', delimiter=',').T
datasetEnMo = np.loadtxt('Enceladus_morooka_data.csv', delimiter=',').T
datasetEnY = np.loadtxt('Enceladus_yaroshenko_data.csv', delimiter=',').T
datasetEnS = np.loadtxt('Enceladus_shafiq_data.csv', delimiter=',').T
datasetEnE = np.loadtxt('Enceladus_ershova_data.csv', delimiter=',').T
datasetEnK = np.loadtxt('Enceladus_kempf_data.csv', delimiter=',').T
datasetEnW = np.loadtxt('Enceladus_waite_data.csv', delimiter=',').T

mu0 = 4*np.pi*(10**-7)
elec = 1.6*(10**-19)


# Assign the first column as Radius of the particle
REnM = datasetEnM[0]
# Assign the second column as number density of particles
ndensityEnM = datasetEnM[1]
CSAEnM = []
MFPEnM = []
SBEnM = []

RIA = datasetIA[0]
ndensityIA = datasetIA[1]
CSAIA = []
MFPIA = []
SBIA = []

REuS = datasetEuS[0]
ndensityEuS = datasetEuS[1]
CSAEuS = []
MFPEuS = []
SBEuS = []

REnMo = datasetEnMo[0]
ndensityEnMo = datasetEnMo[1]
CSAEnMo = []
MFPEnMo = []
SBEnMo = []

REnY = datasetEnY[0]
ndensityEnY = datasetEnY[1]
CSAEnY = []
MFPEnY = []
SBEnY = []

REnS = datasetEnS[0]
ndensityEnS = datasetEnS[1]
CSAEnS = []
MFPEnS = []
SBEnS = []

REnE = datasetEnE[0]
ndensityEnE = datasetEnE[1]
CSAEnE = []
MFPEnE = []
SBEnE = []

REnK = datasetEnK[0]
ndensityEnK = datasetEnK[1]
CSAEnK = []
MFPEnK = []
SBEnK = []

REnW = datasetEnW[0]
ndensityEnW = datasetEnW[1]
CSAEnW = []
MFPEnW = []
SBEnW = []

CSAEnM, MFPEnM, SBEnM = data_processing(REnM, ndensityEnM, 252e3, 1200)
CSAEnMo, MFPEnMo, SBEnMo = data_processing(REnMo, ndensityEnMo, 252e3, 500)
CSAEuS, MFPEuS, SBEuS = data_processing(REuS, ndensityEuS, 1560e3, 700)
CSAIA, MFPIA, SBIA = data_processing(RIA, ndensityIA, 1821e3, 895)
CSAEnY, MFPEnY, SBEnY = data_processing(REnY, ndensityEnY, 252e3, 500)
CSAEnS, MFPEnS, SBEnS = data_processing(REnS, ndensityEnS, 252e3, 1000)
CSAEnE, MFPEnE, SBEnE = data_processing(REnE, ndensityEnE, 252e3, 800)
CSAEnK, MFPEnK, SBEnK = data_processing(REnK, ndensityEnK, 252e3, 500)
CSAEnW, MFPEnW, SBEnW = data_processing(REnW, ndensityEnW, 252e3, 400)


# Transform the above lists  in arrays
REnM = np.array(REnM)
CSAEnM = np.array(CSAEnM)
MFPEnM = np.array(MFPEnM)
ndensityEnM = np.array(ndensityEnM)
SBEnM = np.array(SBEnM)

RIA = np.array(RIA)
CSAIA = np.array(CSAIA)
MFPIA = np.array(MFPIA)
ndensityIA = np.array(ndensityIA)
SBIA = np.array(SBIA)

REuS = np.array(REuS)
CSAEuS = np.array(CSAEuS)
MFPEuS = np.array(MFPEuS)
ndensityEuS = np.array(ndensityEuS)
SBEuS = np.array(SBEuS)

REnMo = np.array(REnMo)
CSAEnMo = np.array(CSAEnMo)
MFPEnMo = np.array(MFPEnMo)
ndensityEnMo = np.array(ndensityEnMo)
SBEnMo = np.array(SBEnMo)

REnY = np.array(REnY)
CSAEnY = np.array(CSAEnY)
MFPEnY = np.array(MFPEnY)
ndensityEnY = np.array(ndensityEnY)
SBEnY = np.array(SBEnY)

REnS = np.array(REnS)
CSAEnS = np.array(CSAEnS)
MFPEnS = np.array(MFPEnS)
ndensityEnS = np.array(ndensityEnS)
SBEnS = np.array(SBEnS)

REnE = np.array(REnE)
CSAEnE = np.array(CSAEnE)
MFPEnE = np.array(MFPEnE)
ndensityEnE = np.array(ndensityEnE)
SBEnE = np.array(SBEnE)

REnK = np.array(REnK)
CSAEnK = np.array(CSAEnK)
MFPEnK = np.array(MFPEnK)
ndensityEnK = np.array(ndensityEnK)
SBEnK = np.array(SBEnK)

REnW = np.array(REnW)
CSAEnW = np.array(CSAEnW)
MFPEnW = np.array(MFPEnW)
ndensityEnW = np.array(ndensityEnW)
SBEnW = np.array(SBEnW)

# Assign X and Y values for plotting
X_EnM = clean_array(CSAEnM)
X_IA = clean_array(CSAIA)
X_EuS = clean_array(CSAEuS)
X_EnMo = clean_array(CSAEnMo)
X_EnY = clean_array(CSAEnY)
X_EnS = clean_array(CSAEnS)
X_EnE = clean_array(CSAEnE)
X_EnK = clean_array(CSAEnK)
X_EnW = clean_array(CSAEnW)
Y_EnM = []
Y_IA = []
Y_EuS = []
Y_EnMo = []
Y_EnY = []
Y_EnS = []
Y_EnE = []
Y_EnK = []
Y_EnW = []

# For each dataset, repeat the number density value,
# to match the number of x values in each set
for m in range(0, 1):
    Y_EnM.append(ndensityEnM[0])
for m in range(1, 2):
    Y_EnM.append(ndensityEnM[1])

for m in range(0, 2):
    Y_IA.append(ndensityIA[0])
for m in range(2, 4):
    Y_IA.append(ndensityIA[1])

for m in range(0, 2):
    Y_EuS.append(ndensityEuS[0])
for m in range(2, 4):
    Y_EuS.append(ndensityEuS[1])

for m in range(0, 2):
    Y_EnMo.append(ndensityEnMo[0])
for m in range(2, 4):
    Y_EnMo.append(ndensityEnMo[1])

for m in range(0, 2):
    Y_EnY.append(ndensityEnY[0])
for m in range(2, 4):
    Y_EnY.append(ndensityEnY[1])

for m in range(0, 1):
    Y_EnS.append(ndensityEnS[0])
for m in range(1, 2):
    Y_EnS.append(ndensityEnS[1])

for m in range(0, 2):
    Y_EnE.append(ndensityEnE[0])
for m in range(2, 4):
    Y_EnE.append(ndensityEnE[1])

for m in range(0, 2):
    Y_EnK.append(ndensityEnK[0])
for m in range(2, 4):
    Y_EnK.append(ndensityEnK[1])

for m in range(0, 1):
    Y_EnW.append(ndensityEnW[0])
for m in range(1, 2):
    Y_EnW.append(ndensityEnW[1])


# Create lists to contain all the combined data
all_CSA = []
all_ndensity = []
all_SB = []

# Process each dataset, ensuring alignment of CSA, ndensity, and MFP
for CSA, ndensity, SB in [
    (CSAEnM, ndensityEnM, SBEnM),
    (CSAIA, ndensityIA, SBIA),
    (CSAEuS, ndensityEuS, SBEuS),
    (CSAEnMo, ndensityEnMo, SBEnMo),
    (CSAEnY, ndensityEnY, SBEnY),
    (CSAEnS, ndensityEnS, SBEnS),
    (CSAEnE, ndensityEnE, SBEnE),
    (CSAEnK, ndensityEnK, SBEnK),
    (CSAEnW, ndensityEnW, SBEnW)
]:
    # Repeat ndensity to match CSA and MFP sizes
    repeated_ndensity = np.repeat(ndensity, len(CSA) // len(ndensity))

    # Append to the combined lists
    all_CSA.extend(CSA)
    all_ndensity.extend(repeated_ndensity)
    all_SB.extend(SB)

# Convert lists to numpy arrays
all_CSA = np.array(all_CSA)
all_ndensity = np.array(all_ndensity)
all_SB = np.array(all_SB)

# Define a grid for the background
x = np.log10(all_CSA)  # Log scale for cross-sectional area
y = np.log10(all_ndensity)  # Log scale for number density
z = np.log10(all_SB*10**9)

# Mask out invalid values (nan or infinity)
mask = ~(np.isinf(x) | np.isnan(x) | (x == 0) |
         np.isinf(y) | np.isnan(y) | (y == 0) |
         np.isinf(z) | np.isnan(z) | (z == 0))

x = x[mask]
y = y[mask]
z = z[mask]


# Define a grid for plotting with expanded edges
x_margin = 0.1  # Margin as a fraction of the range
y_margin = 0.1
z_margin = 0.1
x_range = x.max() - x.min()
y_range = y.max() - y.min()
z_range = z.max() - z.min()

x_grid = np.linspace(x.min() - x_margin * x_range,
                     x.max() + x_margin * x_range, 200)
y_grid = np.linspace(y.min() - y_margin * y_range,
                     y.max() + y_margin * y_range, 200)
z_grid = np.linspace(z.min() - z_margin * z_range,
                     z.max() + z_margin * z_range, 200)

X_grid, Y_grid = np.meshgrid(x_grid, y_grid)


interp_func = interp1d(y_grid, z_grid, kind='linear', fill_value="extrapolate")
Z_grid = interp_func(Y_grid)


# Plot the heatmap with pcolormesh
fig, ax = plt.subplots(figsize=(12, 10))
heatmap = ax.pcolormesh(
    10**X_grid, 10**Y_grid,
    10**Z_grid,  # Convert back from log scale for axes and color
    cmap='plasma',
    norm=LogNorm(vmin=10**z.min(),
                 vmax=10**z.max()),  # Logarithmic color scaling
    shading='auto'  # Avoid grid artifacts
)
specific_lines = [10, 17.3, 190]
sp_log_lines = np.log10(specific_lines)
lista_colori = ['blue', 'green', 'yellow']

# Add contour lines
contours = ax.contour(
    10**X_grid, 10**Y_grid, Z_grid,
    levels=sp_log_lines, colors=lista_colori, linewidths=1
)
# ax.clabel(contours, inline=True, fontsize=10, fmt="%.1f nT")


# Add a colorbar
cbar = fig.colorbar(heatmap, ax=ax, pad=0.02)
cbar.set_label("Magnetic perturbation (nT)", fontsize=14)

# Add scatterplot points with larger markers
marker_size = 165  # Adjust marker size for better visibility
ax.scatter(X_EnM, Y_EnM, label='Enceladus Meier et al., 2015 (Plume)',
           marker='D', s=marker_size, color='green', edgecolor='white')
ax.scatter(X_IA, Y_IA, label='Io Adeloye et al., 2025 (Modelled Plume)',
           marker='X', s=marker_size, color='yellow', edgecolor='black')
ax.scatter(X_EuS, Y_EuS, label='Europa Southworth et al., 2015',
           marker='^', s=marker_size, color='blue', edgecolor='white')
ax.scatter(X_EnMo, Y_EnMo, label='Enceladus Morooka et al., 2011 (Plume)',
           marker='^', s=marker_size, color='green', edgecolor='white')
ax.scatter(X_EnY, Y_EnY, label='Enceladus Yaroshenko et al., 2009 (E-Ring)',
           marker='o', s=marker_size, color='green', edgecolor='white')
ax.scatter(X_EnS, Y_EnS, label='Enceladus Shafiq et al., 2010 (Plume)',
           marker='p', s=marker_size, color='green', edgecolor='white'),
ax.scatter(X_EnE, Y_EnE, label='Enceladus Ershova et al., 2024 (Plume)',
           marker='H', s=marker_size, color='green', edgecolor='white')
ax.scatter(X_EnK, Y_EnK, label='Enceladus Kempf et al., 2010 (Plume)',
           marker='.', s=marker_size, color='green', edgecolor='white'),
ax.scatter(X_EnW, Y_EnW, label='Enceladus Waite et al., 2006 (Plume)',
           marker='<', s=marker_size, color='green', edgecolor='white')

plt.plot(X_EnM, Y_EnM, 'black')
plt.plot(X_EnS, Y_EnS, 'black')

pxEnMo = [1.256e-17, 1.256e-13]
pyEnMo = [9.5e7, 9.5e7]
plt.plot(pxEnMo, pyEnMo, 'black')


# Function to add a shadow around a dataset
def add_shadow_region(x_data, y_data, color, alpha=0.4):
    # Draws a shadow around a dataset using Convex Hull if possible.
    x_data, y_data = np.array(x_data), np.array(y_data)

    # Convert to log scale, handling zeros
    x_data = np.where(x_data > 0, np.log10(x_data), np.nan)
    y_data = np.where(y_data > 0, np.log10(y_data), np.nan)

    # Ensure unique points for ConvexHull
    unique_points = np.column_stack((x_data, y_data))
    unique_points = np.unique(unique_points, axis=0)

    # ConvexHull requires at least 3 unique points
    if unique_points.shape[0] >= 3:
        try:
            hull = ConvexHull(unique_points)
            hull_x = 10**unique_points[hull.vertices, 0]
            # Convert back from log scale
            hull_y = 10**unique_points[hull.vertices, 1]
            ax.fill(hull_x, hull_y, color=color, alpha=alpha, linewidth=0)
        except Exception as e:
            print(f"ConvexHull error: {e}")  # Debugging
    else:
        print("o")


# Apply shadowed regions to each dataset
add_shadow_region(X_EnM, Y_EnM, 'black')
add_shadow_region(X_IA, Y_IA, 'black')
add_shadow_region(X_EuS, Y_EuS, 'black')
add_shadow_region(X_EnMo, Y_EnMo, 'black')
add_shadow_region(X_EnY, Y_EnY, 'black')
add_shadow_region(X_EnS, Y_EnS, 'black')
add_shadow_region(X_EnE, Y_EnE, 'black')
add_shadow_region(X_EnK, Y_EnK, 'black')


# Set plot labels, scales, and title
ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlabel("Cross-Section Area (m²)", fontsize=14)
ax.set_ylabel("Number Density (m⁻³)", fontsize=14)
ax.set_title("Dust case study Magnetic perturbation colormap", fontsize=18)


# Extract existing legend handles and labels
handles, labels = ax.get_legend_handles_labels()

# Add contour lines to legend
contour_handles, contour_labels = contours.legend_elements()
contour_labels = [
    "Europa minimum perturbation (10 nT)",
    "Enceladus minimum perturbation (17.3 nT)",
    "Io minimum perturbation (190 nT)"]

# Update legend with both scatter and contour handles
ax.legend(handles + contour_handles, labels + contour_labels,
          loc='upper right', fontsize=9.8, edgecolor='black')

plt.tight_layout()
plt.show()


# Save the values from all_CSA, all_MFP and
# all magn perturbation valuesinto a text file
with open("CSA_MFP_SB_2_data.txt", "w") as file:
    file.write("# Cross-Section Area and Mean Free Path Data\n")
    file.write("# Format: Origin | CSA (m²) | MFP (m) "
               "| Magnetic perturbation (T)\n\n")

    datasets = [
        ("Io Adeloye", CSAIA, MFPIA, SBIA),
        ("Enceladus Meier", CSAEnM, MFPEnM, SBEnM),
        ("Enceladus Morooka", CSAEnMo, MFPEnMo, SBEnMo),
        ("Enceladus Yaroshenko", CSAEnY, MFPEnY, SBEnY),
        ("Enceladus Shafiq", CSAEnS, MFPEnS, SBEnS),
        ("Enceladus Ershova", CSAEnE, MFPEnE, SBEnE),
        ("Enceladus Kempf", CSAEnK, MFPEnK, SBEnK),
        ("Enceladus Waite", CSAEnW, MFPEnW, SBEnW)]

    for name, CSA_values, MFP_values, SB_values in datasets:
        file.write(f"# {name} Data\n")
        for csa, mfp, sb in zip(CSA_values, MFP_values, SB_values):
            file.write(f"{name} | {csa:.6e} | {mfp:.6e} | {sb:.6e}\n")
        file.write("\n")

print("Data successfully saved to CSA_MFP_SB_2_data.txt")

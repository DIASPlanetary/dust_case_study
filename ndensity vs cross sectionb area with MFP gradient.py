# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 13:58:24 2025

@author: march
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from scipy.spatial import ConvexHull

elec = 1.6*(10**-19) # Electron charge in Coulombs
mu0 = 4*np.pi*(10**-7) # Permeability of free space, in N*A^-2


def clean_array(arr):
    # Removes infinite, NaN, and zero values from a NumPy array.
    arr = np.array(arr)  # Ensure input is a NumPy array
    mask = ~np.isinf(arr) & ~np.isnan(arr) & (arr != 0)
    return arr[mask]


def data_processing(radius, density, velocity, radius_m):
    # function to process the datasets
    CSA = []
    MFP = []
    SB = []
    for i in range(0, len(density)):
        for j in range(0, len(radius)):
            csa = 4*np.pi*(radius[j]**2)  # calculate MFP
            CSA.append(csa)
            mfp = 1/(density[i]*csa)  # calculate CSA
            MFP.append(mfp)
            sb = (mu0*radius_m*density[i]*150*elec*velocity)/2  # calculate SB
            SB.append(sb)
    return CSA, MFP, SB


# Load the datasets from the respective CSV files
datasetEuK = np.loadtxt('Europa_kruger_extremes.csv', delimiter=',').T
datasetIK = np.loadtxt('Io_kruger_extremes.csv', delimiter=',').T
datasetCK = np.loadtxt('Callisto_kruger_extremes.csv', delimiter=',').T
datasetIM = np.loadtxt('Io_mcdoniel_extremes.csv', delimiter=',').T
datasetEuS = np.loadtxt('Europa_south_extremes.csv', delimiter=',').T
datasetEnM = np.loadtxt('Enceladus_meier_extremes.csv', delimiter=',').T
datasetEnMo = np.loadtxt('Enceladus_morooka_data.csv', delimiter=',').T
datasetIA = np.loadtxt('Io_adeloye_extremes.csv', delimiter=',').T

# Assign the first column as Radius of the particle
REuK = datasetEuK[0]
# Assign the second column as number density of particles
ndensityEuK = datasetEuK[1]
CSAEuK = []
MFPEuK = []
SBEuK = []

RIK = datasetIK[0]
ndensityIK = datasetIK[1]
CSAIK = []
MFPIK = []
SBIK = []

RCK = datasetCK[0]
ndensityCK = datasetCK[1]
CSACK = []
MFPCK = []
SBCK = []

RIM = datasetIM[0]
ndensityIM = datasetIM[1]
CSAIM = []
MFPIM = []
SBIM = []

REuS = datasetEuS[0]
ndensityEuS = datasetEuS[1]
CSAEuS = []
MFPEuS = []
SBEuS = []

REnM = datasetEnM[0]
ndensityEnM = datasetEnM[1]
CSAEnM = []
MFPEnM = []
SBEnM = []

REnMo = datasetEnMo[0]
ndensityEnMo = datasetEnMo[1]
CSAEnMo = []
MFPEnMo = []
SBEnMo = []

RIA = datasetIA[0]
ndensityIA = datasetIA[1]
CSAIA = []
MFPIA = []
SBIA = []


CSAEuK, MFPEuK, SBEuK = data_processing(REuK, ndensityEuK, 1560e3, 5500)
CSAIK, MFPIK, SBIK = data_processing(RIK, ndensityIK, 1821e3, 10300)
CSACK, MFPCK, SBCK = data_processing(RCK, ndensityCK, 2410e3, 6300)
CSAIM, MFPIM, SBIM = data_processing(RIM, ndensityIM, 1821e3, 800)
CSAEuS, MFPEuS, SBEuS = data_processing(REuS, ndensityEuS, 1560e3, 700)
CSAEnM, MFPEnM, SBEnM = data_processing(REnM, ndensityEnM, 252e3, 1200)
CSAEnMo, MFPEnMo, SBEnMo = data_processing(REnMo, ndensityEnMo, 252e3, 500)
CSAIA, MFPIA, SBIA = data_processing(RIA, ndensityIA, 1821e3, 895)

# Transform the above lists  in arrays
REuK = np.array(REuK)
CSAEuK = np.array(CSAEuK)
MFPEuK = np.array(MFPEuK)
ndensityEuK = np.array(ndensityEuK)
SBEuK = np.array(SBEuK)

RIK = np.array(RIK)
CSAIK = np.array(CSAIK)
MFPIK = np.array(MFPIK)
ndensityIK = np.array(ndensityIK)
SBIK = np.array(SBIK)

RCK = np.array(RCK)
CSACK = np.array(CSACK)
MFPCK = np.array(MFPCK)
ndensityCK = np.array(ndensityCK)
SBCK = np.array(SBCK)

RIM = np.array(RIM)
CSAIM = np.array(CSAIM)
MFPIM = np.array(MFPIM)
ndensityIM = np.array(ndensityIM)
SBIM = np.array(SBIM)

REuS = np.array(REuS)
CSAEuS = np.array(CSAEuS)
MFPEuS = np.array(MFPEuS)
ndensityEuS = np.array(ndensityEuS)
SBEuS = np.array(SBEuS)

REnM = np.array(REnM)
CSAEnM = np.array(CSAEnM)
MFPEnM = np.array(MFPEnM)
ndensityEnM = np.array(ndensityEnM)
SBEnM = np.array(SBEnM)

REnMo = np.array(REnMo)
CSAEnMo = np.array(CSAEnMo)
MFPEnMo = np.array(MFPEnMo)
ndensityEnMo = np.array(ndensityEnMo)
SBEnMo = np.array(SBEnMo)

RIA = np.array(RIA)
CSAIA = np.array(CSAIA)
MFPIA = np.array(MFPIA)
ndensityIA = np.array(ndensityIA)
SBIA = np.array(SBIA)

# Assign X and Y values for plotting
X_EuK = clean_array(CSAEuK)
X_IK = clean_array(CSAIK)
X_CK = clean_array(CSACK)
X_IM = clean_array(CSAIM)
X_EuS = clean_array(CSAEuS)
X_EnM = clean_array(CSAEnM)
X_EnMo = clean_array(CSAEnMo)
X_IA = clean_array(CSAIA)
Y_EuK = []
Y_IK = []
Y_CK = []
Y_IM = []
Y_EuS = []
Y_EnM = []
Y_EnMo = []
Y_IA = []

# For each dataset, repeat the number density value,
# to match the number of x values in each set
for m in range(0, 2):
    Y_EuK.append(ndensityEuK[0])
for m in range(2, 4):
    Y_EuK.append(ndensityEuK[1])

for m in range(0, 1):
    Y_IK.append(ndensityIK[0])
for m in range(1, 2):
    Y_IK.append(ndensityIK[1])

for m in range(0, 2):
    Y_CK.append(ndensityCK[0])
for m in range(2, 4):
    Y_CK.append(ndensityCK[1])

for m in range(0, 2):
    Y_IM.append(ndensityIM[0])
for m in range(2, 4):
    Y_IM.append(ndensityIM[1])

for m in range(0, 2):
    Y_EuS.append(ndensityEuS[0])
for m in range(2, 4):
    Y_EuS.append(ndensityEuS[1])

for m in range(0, 1):
    Y_EnM.append(ndensityEnM[0])
for m in range(1, 2):
    Y_EnM.append(ndensityEnM[1])

for m in range(0, 2):
    Y_EnMo.append(ndensityEnMo[0])
for m in range(2, 4):
    Y_EnMo.append(ndensityEnMo[1])

for m in range(0, 2):
    Y_IA.append(ndensityIA[0])
for m in range(2, 4):
    Y_IA.append(ndensityIA[1])

# Create lists to contain all the combined data
all_CSA = []
all_ndensity = []
all_MFP = []

# Process each dataset, ensuring alignment of CSA, ndensity, and MFP
for CSA, ndensity, MFP in [
    (CSAEuK, ndensityEuK, MFPEuK),
    (CSAIK, ndensityIK, MFPIK),
    (CSACK, ndensityCK, MFPCK),
    (CSAIM, ndensityIM, MFPIM),
    (CSAEuS, ndensityEuS, MFPEuS),
    (CSAEnM, ndensityEnM, MFPEnM),
    (CSAEnMo, ndensityEnMo, MFPEnMo),
    (CSAIA, ndensityIA, MFPIA),
]:
    # Repeat ndensity to match CSA and MFP sizes
    repeated_ndensity = np.repeat(ndensity, len(CSA) // len(ndensity))

    # Append to the combined lists
    all_CSA.extend(CSA)
    all_ndensity.extend(repeated_ndensity)
    all_MFP.extend(MFP)

# Convert lists to numpy arrays
all_CSA = np.array(all_CSA)
all_ndensity = np.array(all_ndensity)
all_MFP = np.array(all_MFP)

# Define a grid for the background
x = np.log10(all_CSA)  # Log scale for cross-sectional area
y = np.log10(all_ndensity)  # Log scale for number density
z = np.log10(1/(all_CSA*all_ndensity))  # Log scale for mean free path

# Mask out invalid values (nan or infinity)
mask = ~(np.isinf(x) |
         np.isnan(x) |
         np.isinf(y) |
         np.isnan(y) |
         np.isinf(z) |
         np.isnan(z))

x = x[mask]
y = y[mask]
z = z[mask]


# Define a grid for plotting with expanded edges
x_margin = 0.1  # Margin as a fraction of the range
y_margin = 0.1
x_range = x.max() - x.min()
y_range = y.max() - y.min()

x_grid = np.linspace(x.min() - x_margin * x_range,
                     x.max() + x_margin * x_range, 200)
y_grid = np.linspace(y.min() - y_margin * y_range,
                     y.max() + y_margin * y_range, 200)
X_grid, Y_grid = np.meshgrid(x_grid, y_grid)

Z_grid = np.log10(1 / (10**X_grid * 10**Y_grid))

# Plot the heatmap with pcolormesh
fig, ax = plt.subplots(figsize=(12, 10))
heatmap = ax.pcolormesh(
    10**x_grid, 10**y_grid,
    10**Z_grid,  # Convert back from log scale for axes and color
    cmap='plasma',
    norm=LogNorm(vmin=10**z.min(),
                 vmax=10**z.max()),  # Logarithmic color scaling
    shading='auto'  # Avoid grid artifacts
)

values = [201e3, 300e3, 415e3, 750e3, 892e3, 1.78e10, 9.46e15]
valueslog = np.log10(values)
lista_colori = ['pink', 'green', 'cyan', 'yellow', 'white', 'orange', 'black']

# Add contour lines
contour_levels = np.logspace(np.floor(z.min()), np.ceil(z.max()), num=10)
contours = ax.contour(
    10**X_grid, 10**Y_grid, Z_grid,
    levels=valueslog, colors=lista_colori, linewidths=1
)

# Add a colorbar
cbar = fig.colorbar(heatmap, ax=ax, pad=0.02)
cbar.set_label("Magnetic perturbation (nT)", fontsize=14)

# ax.clabel(contours, inline=True, fontsize=10, fmt="%.1f m")


# Add scatterplot points with larger markers
marker_size = 150  # Adjust marker size for better visibility
ax.scatter(X_EuK, Y_EuK, label='Europa Kruger et al., 2003',
           marker='.', s=marker_size, color='blue', edgecolor='white')
ax.scatter(X_IK, Y_IK, label='Io Kruger et al., 2003',
           marker='.', s=marker_size, color='orange', edgecolor='white')
ax.scatter(X_CK, Y_CK, label='Callisto Kruger et al., 2003',
           marker='.', s=marker_size, color='red', edgecolor='white')
ax.scatter(X_IM, Y_IM, label='Io McDoniel et al., 2015',
           marker='s', s=marker_size, color='orange', edgecolor='white')
ax.scatter(X_EuS, Y_EuS, label='Europa Southworth et al., 2015',
           marker='^', s=marker_size, color='blue', edgecolor='white')
ax.scatter(X_EnM, Y_EnM, label='Enceladus Meier et al., 2015',
           marker='D', s=marker_size, color='green', edgecolor='white')
ax.scatter(X_EnMo, Y_EnMo, label='Enceladus Morooka et al., 2011',
           marker='^', s=marker_size, color='green', edgecolor='white')
ax.scatter(X_IA, Y_IA, label='Io Adeloye et al., 2025',
           marker='X', s=marker_size, color='orange', edgecolor='white')

plt.plot(X_EnM, Y_EnM, 'black')
pxEnMo = [1.256e-17, 1.256e-13]
pyEnMo = [9.5e7, 9.5e7]
plt.plot(pxEnMo, pyEnMo, 'black')


# Function to add a shadow around a dataset
def add_shadow_region(x_data, y_data, color, alpha=0.5):
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
add_shadow_region(X_EuK, Y_EuK, 'black')
add_shadow_region(X_IK, Y_IK, 'black')
add_shadow_region(X_CK, Y_CK, 'black')
add_shadow_region(X_IM, Y_IM, 'black')
add_shadow_region(X_EuS, Y_EuS, 'black')
add_shadow_region(X_EnM, Y_EnM, 'black')
add_shadow_region(X_IA, Y_IA, 'black')


# Function to add labeled shadowed boxes
def add_label_box(x_data, y_data, label, color):
    """Places a label box near the dataset."""
    x_pos = np.median(x_data)  # Use median to find a position for the label
    y_pos = np.median(y_data)

    ax.text(x_pos, y_pos, label, fontsize=10, color=color,
            ha='center', va='center',
            bbox=dict(facecolor='white',
                      edgecolor=color, boxstyle='round,pad=0.3', alpha=1))


# Add boxes for each dataset
add_label_box(X_EuK, Y_EuK, 'Europa Kruger', 'black')
add_label_box(X_IK, Y_IK, 'Io Kruger', 'black')
add_label_box(X_CK, Y_CK, 'Callisto Kruger', 'black')
add_label_box(X_IM, Y_IM, 'Io McDoniel', 'black')
add_label_box(X_EuS, Y_EuS, 'Europa Southworth', 'black')
add_label_box(X_EnM, Y_EnM, 'Enceladus Meier', 'black')
add_label_box(X_IA, Y_IA, 'Io Adeloye', 'black')


# Set plot labels, scales, and title
ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlabel("Cross-Section Area (m²)", fontsize=14)
ax.set_ylabel("Number Density (m⁻³)", fontsize=14)
ax.set_title("Mean Free Path Variation Across Moons colormap", fontsize=18)
ax.set_ylim(0, 10e8)

# Extract existing legend handles and labels
handles, labels = ax.get_legend_handles_labels()

# Add contour lines to legend
contour_handles, contour_labels = contours.legend_elements()
contour_labels = [
    "Europa Kruger closest approach (201 km)",
    "Io Adeloye Tvashtar plume (300 km)",
    "Callisto Kruger closest approach (415 km)",
    "Enceladus Morooka Plume (750 km)",
    "Io Kruger closest approach (892 km)",
    "Solar System Radius (1.78e10 km)",
    "1 Light Year (9.46e15 km)"]

# Update legend with both scatter and contour handles
ax.legend(handles + contour_handles, labels + contour_labels,
          loc='upper right', fontsize=9.8, edgecolor='black')

plt.tight_layout()
plt.show()

# Save the values from all_CSA and all_MFP into a text file
with open("CSA_MFP_SB_addition_data.txt", "w") as file:
    file.write("# Cross-Section Area and Mean Free Path Data\n")
    file.write("# Format: Origin | CSA (m²) | MFP (m) "
               "| Magnetic perturbation (T)\n\n")

    datasets = [
        ("Europa Kruger", CSAEuK, MFPEuK, SBEuK),
        ("Callisto Kruger", CSACK, MFPCK, SBCK),
        ("Io Kruger", CSAIK, MFPIK, SBIK),
        ("Io McDoniel", CSAIM, MFPIM, SBIM),
        ("Europa Southworth", CSAEuS, MFPEuS, SBEuS),
        ("Enceladus Meier", CSAEnM, MFPEnM, SBEnM),
        ("Enceladus Morooka", CSAEnMo, MFPEnMo, SBEnMo),
        ("Io Adeloye", CSAIA, MFPIA, SBIA)
    ]

    for name, CSA_values, MFP_values, SB_values in datasets:
        file.write(f"# {name} Data\n")
        for csa, mfp, sb in zip(CSA_values, MFP_values, SB_values):
            file.write(f"{name} | {csa:.6e} | {mfp:.6e} | {sb:.6e}\n")
        file.write("\n")

print("Data successfully saved to CSA_MFP_SB_addition_data.txt")

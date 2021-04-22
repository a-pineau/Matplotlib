import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)

# loading data from text files
data_Iv2D = np.loadtxt('data/Ang_CA2D_Iv2D.txt')
data_Iv3D = np.loadtxt('data/Ang_CA2D_Iv3D.txt')
data_Iv3D_50 = np.loadtxt('data/Ang_Iv3D_a50.txt')

# extracting data (column-column)
x_2D = data_Iv2D[:, 0]
y_2D = data_Iv2D[:, 1]

x_3D = data_Iv3D[:, 0]
y_3D = data_Iv3D[:, 1]

x_3D_50 = data_Iv3D_50[:, 0]
y_3D_50 = data_Iv3D_50[:, 1]

fig, ax = plt.subplots()

# plots
ax.plot(x_2D, y_2D, 'x', color='darkblue', label='CA2D_Iv2D')
ax.plot(x_3D, y_3D, 'o', color='red', mfc='none', label='CA2D_Iv3D')
ax.plot(x_3D_50, y_3D_50, '+', color='green', label='CA2D_Iv3D_a50')

# adding legend
# bbox_to_anchor is used to place the legend outside of the axes
# handletextpad sets the distance between the label and the marker
# columnspacing sets the distance between the labels (or columns)
ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.1), ncol=3, handletextpad=0, columnspacing=0.1)

# setting xlabel and ylabel
ax.set_xlabel('Cell size, $l_{CA}$ [µm]')
ax.set_ylabel(r'GB Angle, $\theta$ [°]')

# using a log scale for the x-axis only
ax.semilogx()

# setting the ticks
ax.tick_params(direction='in', which='both')
ax.yaxis.set_major_locator(MultipleLocator(5))
ax.yaxis.set_minor_locator(MultipleLocator(1))

# setting lower and upper limits of the y-axis
ax.set_ylim(5, 25)

# horizontal lines
ax.axhline(8, color='black', linestyle='--', linewidth=1)
ax.axhline(19, color='black', linestyle='--', linewidth=1)
ax.axhline(20.5, color='black', linestyle='--', linewidth=1)

# vertical lines
ax.axvline(33.6, color='royalblue', linestyle='--', linewidth=1)
ax.axvline(72.1, color='royalblue', linestyle='--', linewidth=1)
ax.axvline(56.6, color='springgreen', linestyle='--', linewidth=1)
ax.axvline(115.8, color='springgreen', linestyle='--', linewidth=1)

# adding some annotations
plt.text(1.5, 8.5, r'FOG, $\theta$ = 8°', ha='center', va='center')
plt.annotate(r'$\delta{l^{(33°, 8°)}_{Iv3D}}$', color='royalblue',
 xy=(33.6, 23), xycoords='data',
 xytext=(-70, 0), textcoords='offset points', va='center',
 arrowprops=dict(arrowstyle="->", color='royalblue'))

# saving fig
plt.savefig('figs/multiple_plot_same_axes.pdf', bbox_inches='tight', pad_inches=0.025)

# displaying fig
plt.show()

import matplotlib.pyplot as plt
from matplotlib import rc
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
import numpy as np

# rc('font', **{'family': 'serif', 'serif': ['Computer Modern']})
# rc('text', usetex=True)

data_Iv2D = np.loadtxt('Ang_CA2D_Iv2D.txt')
data_Iv3D = np.loadtxt('Ang_CA2D_Iv3D.txt')
data_Iv3D_50 = np.loadtxt('Ang_Iv3D_a50.txt')

x_2D = data_Iv2D[:, 0]
y_2D = data_Iv2D[:, 1]

x_3D = data_Iv3D[:, 0]
y_3D = data_Iv3D[:, 1]

x_3D_50 = data_Iv3D_50[:, 0]
y_3D_50 = data_Iv3D_50[:, 1]

fig, ax = plt.subplots()

ax.plot(x_2D, y_2D, 'x', color='darkblue')
ax.plot(x_3D, y_3D, 'o', color='red', mfc='none')
ax.plot(x_3D_50, y_3D_50, '+', color='green')

ax.set_xlabel('Cell size, $l_{CA}$ [µm]')
ax.set_ylabel(r'GB Angle, $\theta$ [°]')
ax.semilogx()
ax.tick_params(direction='in', which='both')
ax.yaxis.set_major_locator(MultipleLocator(5))
ax.yaxis.set_minor_locator(MultipleLocator(1))
ax.set_ylim(5, 25)

ax.axhline(8, color='black', linestyle='--', linewidth=1)
ax.axhline(19, color='black', linestyle='--', linewidth=1)
ax.axhline(20.5, color='black', linestyle='--', linewidth=1)

ax.axvline(33.6, color='royalblue', linestyle='--', linewidth=1)
ax.axvline(72.1, color='royalblue', linestyle='--', linewidth=1)
ax.axvline(56.6, color='springgreen', linestyle='--', linewidth=1)
ax.axvline(115.8, color='springgreen', linestyle='--', linewidth=1)

plt.text(1.5, 8.5, r'FOG, $\theta$ = 8°', ha='center', va='center')
plt.annotate(r'$\delta{l^{(33°, 8°)}_{Iv3D}}$', color='royalblue',
 xy=(33.6, 23), xycoords='data',
 xytext=(-70, 0), textcoords='offset points', va='center',
 arrowprops=dict(arrowstyle="->", color='royalblue'))


plt.savefig('PhD_P3.pdf', bbox_inches='tight', pad_inches=0.025)
plt.show()

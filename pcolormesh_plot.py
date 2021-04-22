import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import random

from numpy import random
from matplotlib import ticker

x = np.arange(start=-45, stop=46, step=1)
y = np.arange(start=-45, stop=46, step=1)
Z = np.random.rand(90, 90)

fig, ax = plt.subplots()

# define a mesh to keep track of it when using colorbar
mesh = ax.pcolormesh(x, y, Z, cmap='hsv')
ax.tick_params(labelsize=13)
ax.set_xlabel(xlabel=r'$\alpha_1$', fontsize=16)
ax.set_ylabel(ylabel=r'$\alpha_2$', fontsize=16)
plt.title(r'$\theta$ = f($\alpha_1$, $\alpha_2$)', fontsize=16)

cb = plt.colorbar(mesh)
tick_locator = ticker.MaxNLocator(nbins=10)
cb.locator = tick_locator
cb.update_ticks()
# cb.set_label(r'$\theta$ [°]')
cb.ax.set_title(r'$\theta$ [°]', fontsize=16)

#save fig
plt.savefig('figs/pcolormesh_plot.pdf',bbox_inches='tight', pad_inches=0.025)

# display
plt.show()

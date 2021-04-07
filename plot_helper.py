import random
import numpy as np
import matplotlib.pyplot as plt

from matplotlib import rc
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)

def single_plot(X, Y, x_label=None, y_label=None, x_fontsize=12, y_fontsize=12,
                t_fontsize=12, my_color='blue', width=2, my_alpha=1, my_title=None, grid=False,
                save=False, file_name=None):
    """
    A helper function to make a simple plot
    Parameters:
    -----------
    X: array/list           Y: array/list
    X axis data             Y axis data

    color: string (default='blue')           marker: string
    Curve color            Marker's type

    label: string (default=None)          xlabel: string          ylabel: string          title: string
    Plot's label name       x label name            y label name            Plot's title

    grid: boolean (default=None)
    Enable/disable grid

    for marker's type, see: https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html

    Returns
    -------
    None: plots the data
    """
    fig, ax = plt.subplots(constrained_layout=True)

    ax.plot(X, Y, color=my_color, linewidth=width, alpha=my_alpha)
    ax.set_xlabel(x_label, fontsize=x_fontsize)
    ax.set_ylabel(y_label, fontsize=y_fontsize)
    ax.set_title(my_title, fontsize=t_fontsize)

    if grid: ax.grid()
    if save: plt.savefig(file_name, bbox_inches='tight', pad_inches=0.025)
    plt.show()



if __name__ == '__main__':
    x = sorted([random.randint(0, x) for x in range(0, 100)])
    y = sorted([random.randint(0, x) for x in range(0, 100)])
    single_plot(x, y, 'x [m]', 'y [s]', my_title='$x = f(y)$', t_fontsize=20, grid=True,
                x_fontsize=20, y_fontsize=20, my_color='green', width=4, my_alpha=0.5,
                save=True, file_name='test.pdf')


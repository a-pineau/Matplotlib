import matplotlib.pyplot as plt
import numpy as np
import random

def my_plotter(data1, data2, 
    color, marker,
    label, xlabel, ylabel, title, 
    grid):
    """
    A helper function to make a graph

    Parameters
    ----------
    data1: array            data2: array
    The x data              The y data
        
    color: string           marker: string
    Data's color            Marker's type
        
    label: string           xlabel: string          ylabel: string          title: string      
    Plot's label name       x label name            y label name            Plot's title
        
    grid: boolean
    True: grid on
    False: grid off
    
    for marker's type, see: https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html

    Returns
    -------
    None:
        Simply plots the data
    """

    plt.plot()
    plt.plot(data_1, data_2, color=color, label=label)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    
    # grid on/off
    if grid: plt.grid()
    # add legend
    plt.legend()
    # show plot
    plt.show()
    

data_1 = sorted([random.randint(0, x) for x in range(0, 100)])
data_2 = sorted([random.randint(0, x) for x in range(0, 100)])

my_plotter(data_1, data_2, 'green', 'o', x_fontsize=20, y_fontsize=20,
           'A label', 'x_label [m]', 'y_label [s]', 'A title',
           True)

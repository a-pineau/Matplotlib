import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib import rc

# rc('font',**{'family':'serif','serif':['Times']})

id_grains = ['A', 'B', 'C', 'D']
label_colors = {'t1': 'blue', 't2': 'red', 't3': 'green', 't4': 'orange'}

# data set
data = np.array([[20.9, 41.3, 54.3, 39.8],
                 [57.5, 33.4, 31.6, 38.1], 
                 [21.6, 22.4, 13.9, 18.9],
                 [0, 2.9, 0, 3.2] 
                ]) 

len_data=len(data)
x = np.arange(len_data)
width = 0.2 # bar width
y_offset_text = 2 # data value (on top of bars) text offset

fig = plt.figure(figsize=(8, 8), dpi=100, constrained_layout=True) # the displayed figure
spec = gridspec.GridSpec(ncols=1, nrows=3, figure=fig) # using gridpsec to display multiple barplots

fig_ax1 = fig.add_subplot(spec[0, 0])
fig_ax2 = fig.add_subplot(spec[1, 0])
fig_ax3 = fig.add_subplot(spec[2, 0])

# top
for i, key in enumerate(label_colors):
    # two plots are needed to have black border and alpha facescolor, otherwise edgecolor depends on alpha value too
    fig_ax1.bar(x + i * width, data[:,i], width, color=label_colors[key], label=key, alpha=0.5, zorder=10)
    fig_ax1.bar(x + i * width, data[:,i], width, color='None', edgecolor='black', zorder=10)
    for k in range(len(data[:, i])):
        fig_ax1.text(x[k] + i * width, data[:, i][k] + y_offset_text, str(data[:, i][k]), ha='center')

fig_ax1.set_xlabel('ID grains')
fig_ax1.set_ylabel('Fraction surfacique (%)')
fig_ax1.set_ylim(0, 70)
fig_ax1.set_xticks(x + width + width/2)
fig_ax1.set_xticklabels(id_grains)
fig_ax1.legend(fancybox=False, framealpha=1, edgecolor='black')
fig_ax1.set_title('f(t) = g(x)')

# middle 
for i, key in enumerate(label_colors):
    fig_ax2.bar(x + i * width, data[:,i], width, color=label_colors[key], label=key, alpha=0.5)
    fig_ax2.bar(x + i * width, data[:,i], width, color='None', edgecolor='black')

fig_ax2.set_xlabel('ID grains')
fig_ax2.set_ylabel('Fraction surfacique (%)')
fig_ax2.set_xticks(x + width + width/2)
fig_ax2.set_xticklabels(id_grains)
fig_ax2.legend(frameon=False)
fig_ax2.set_title('f(t) = g(x)')

# bottom
y_offset_text = 4 
for i, key in enumerate(label_colors):
    fig_ax3.bar(x + i * width, data[:,i], width, color=label_colors[key], label=key, alpha=0.5, zorder=10)
    fig_ax3.bar(x + i * width, data[:,i], width, color='None', edgecolor='black', zorder=10)
    for k in range(len(data[:, i])):
        fig_ax3.text(x[k] + i * width, data[:, i][k] + y_offset_text, str(data[:, i][k]), 
                     ha='center', rotation=+90)

fig_ax3.set_xlabel('ID grains')
fig_ax3.set_ylabel('Fraction surfacique (%)')
fig_ax3.set_ylim(0, 80)
fig_ax3.set_xticks(x + width + width/2)
fig_ax3.set_xticklabels(id_grains)
fig_ax3.legend(fancybox=False, framealpha=1, edgecolor='black')
fig_ax1.set_title('f(t) = g(x)')


# save
fig.savefig('figs/multiple_barplots.pdf', bbox_inches='tight', pad_inches=0.025)
plt.show()

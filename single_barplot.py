import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec


fig1 = plt.figure(figsize=(5, 5), dpi=100, constrained_layout=True)
spec1 = gridspec.GridSpec(ncols=1, nrows=2, figure=fig1)

X = np.arange(4)
ID_grains = ['A', 'B', 'C', 'D']
FRAC_data = np.array([[20.9, 57.5, 21.6, 0],
             [41.3, 33.4, 22.4, 2.9],
             [54.3, 31.6, 13.9, 3.2],
             [39.8, 38.1, 18.9, 3.2]
            ])

ax1 = fig1.add_subplot(spec1[0, 0])
ax2 = fig1.add_subplot(spec1[1, 0])
print(FRAC_data[:, 0])
print(FRAC_data[:, 1])
print(FRAC_data[:, 2])
print(FRAC_data[:, 3])
width = 0.25
ax1.bar(X + 0 * width, FRAC_data[:, 0], color = 'b')
ax1.bar(X + 1 * width, FRAC_data[:, 1], color = 'r')
ax1.bar(X + 2 * width, FRAC_data[:, 2], color = 'g')
ax1.bar(X + 3 * width, FRAC_data[:, 3], color = 'orange')

plt.show()





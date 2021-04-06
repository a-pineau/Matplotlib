# -----------------------------------------------------------------------------
# Copyright (c) 2015, Nicolas P. Rougier. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.
# -----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C,S = np.cos(X), np.sin(X)


plt.figure(figsize=(8, 5), dpi=100, frameon=True)
plt.plot(X, C, color='green', linewidth=3, alpha=0.5, label='Cosine')
plt.plot(X, S, color='red', linewidth=3, label='Sine')
plt.legend(loc='upper left', frameon=True)
plt.xlabel('X')
plt.ylabel('Y')

plt.xlim(-np.pi, np.pi)
plt.ylim(-2, 2)
plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
   [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])

t = 2*np.pi/3

# red
plt.plot([t,t],[0,np.sin(t)], color ='red', linewidth=1.5, linestyle="--")
plt.scatter(t, np.sin(t), 50, color ='red')
plt.annotate(r'$\sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$',
 xy=(t, np.sin(t)), xycoords='data',
 xytext=(0, +50), textcoords='offset points', fontsize=16, ha='center',
 arrowprops=dict(arrowstyle="->"))

# blue
plt.plot([t,t],[0,np.cos(t)], color ='green', linewidth=1.5, linestyle="--", alpha=0.5)
plt.scatter(t, np.cos(t), 400, color ='green', alpha=0.5)
plt.annotate(r'Salut ça va wesh bien',
             xy=(t, np.cos(t)), xycoords='data',
             xytext=(0, -50), textcoords='offset points', fontsize=16, ha='center',
             arrowprops=dict(arrowstyle="->"))

'''
ax = plt.gca()
ax.spines['right'].set_color('orange')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
'''

plt.grid()
plt.savefig('test2.pdf', bbox_inches='tight')
plt.show()

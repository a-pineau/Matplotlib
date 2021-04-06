import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import random

X = sorted([random.randint(0, x) for x in range(100)])
Y = sorted([random.randint(0, x) for x in range(100)])

fig1 = plt.figure(figsize=(5, 5), dpi=100, constrained_layout=True)
spec1 = gridspec.GridSpec(ncols=2, nrows=2, figure=fig1)

fig1_ax1 = fig1.add_subplot(spec1[0, 0])
fig1_ax2 = fig1.add_subplot(spec1[0, 1])
fig1_ax3 = fig1.add_subplot(spec1[1, 0])
fig1_ax4 = fig1.add_subplot(spec1[1, 1])

fig1_ax1.plot(X, Y, color='green', linewidth=3, alpha=0.5, label='Cosine')
fig1_ax1.set_xlabel('X1')
fig1_ax1.set_ylabel('Y1')
fig1_ax1.set_title('X1 = f(Y1)')
fig1_ax1.axis('square')

fig1_ax2.plot(X, Y, color='darkblue', linewidth=3, alpha=0.5, label='Cosine')
fig1_ax2.set_xlabel('X2')
fig1_ax2.set_ylabel('Y2')
fig1_ax2.set_title('X2 = f(Y2)')
fig1_ax2.axis('square')

fig1_ax3.plot(X, Y, color='red', linewidth=3, alpha=0.5, label='Cosine')
fig1_ax3.set_ylabel('X3')
fig1_ax3.set_ylabel('Y3')
fig1_ax3.set_title('X3 = f(Y3)')
fig1_ax3.axis('square')

fig1_ax4.plot(X, Y, color='darkorchid', linewidth=3, alpha=0.5, label='Cosine')
fig1_ax4.set_ylabel('X4')
fig1_ax4.set_ylabel('Y4')
fig1_ax4.set_title('X4 = f(Y4)')
fig1_ax4.axis('square')

fig1.savefig('test.pdf', bbox_inches='tight')
plt.show()



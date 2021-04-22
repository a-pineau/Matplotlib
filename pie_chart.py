import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec


# Pie chart
data = [15, 30, 45, 10]
labels = ['Frogs', 'Hogs', 'Dogs', 'Logs']

fig, ax = plt.subplots(1, 3, figsize=(10,10))

ax[0].pie(data, explode=(0, 0, 0.075, 0), labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
ax[0].set(title='With explode and shadow')

ax[1].pie(data, labels=labels, autopct='%1.1f%%', shadow=False, startangle=90)
ax[1].set(title='No explode, no shadow')

ax[2].pie(data, labels=labels, autopct='%1.1f%%', shadow=False, wedgeprops={'width':0.65})
ax[2].set(title='Donut, startangle=0°')

fig.savefig('figs/pie_chart.pdf', bbox_inches='tight')
# display 
plt.show()

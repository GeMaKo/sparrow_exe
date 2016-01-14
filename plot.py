import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
import numpy as np
import assignment as asm

__author__ = 'Gerrit'

colors = ["#1f77b4", "#d62728", "#2ca02c", "#414451"]
plt.style.use("C:/Users/Gerrit/PycharmProjects/dis_style.mplstyle")

#ind = np.arange(len(total_data["total"]))+0.5

fig, ax = plt.subplots(nrows=1, ncols=1, sharex=True)
fig.set_figheight(12)
fig.set_figwidth(14)
profile_fn = "C:\Users\Gerrit\PycharmProjects\sparrow_res\example\T0515-D1.out"
ret = asm.assign(profile_fn)
x = range(1, 101, 1)
len(x)
len(ret.probability[0:100, 0])
#acc = plt.plot(x, ret.accuracy)
#print ret.probability[:,0]
he = ax.plot(x, ret.probability[0:100, 0], color=colors[0], linewidth=2, label="Helix")
st = ax.plot(x, ret.probability[0:100, 1], color=colors[1], linewidth=2, label="Strand")
co = ax.plot(x, ret.probability[0:100, 2], color=colors[2], linewidth=2, label="Coil")

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc="lower right", numpoints=1)

#ax[0].set_xlim(0, ind[-1]+.5)
ax.set_xlim(1, x[-1])
start, end = ax.get_xlim()
major_xticks = np.arange(0, end+1, 10)
minor_xticks = np.arange(0, end+1, 5)
ax.set_xticks(major_xticks)
ax.set_xticks(minor_xticks, minor=True)
ax.set_ylim(0, 1.0001)
start, end = ax.get_ylim()
major_yticks = np.arange(start, end, .2)
minor_yticks = np.arange(start, end, .1)
minorLocator = AutoMinorLocator(2)
ax.yaxis.set_minor_locator(minorLocator)
ax.set_yticks(major_yticks)
ax.set_yticks(minor_yticks, minor=True)
ax.set_ylabel('Probability measure')
ax.set_xlabel('Residue Index')

ax.tick_params(which='major', length=9, width=2)
ax.tick_params(which='minor', length=5, width=2)

plt.savefig("plot.png",format="png",bbox_inches='tight')
plt.show()





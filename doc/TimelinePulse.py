# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 23:08:49 2021

@author: r.hif
"""

from matplotlib import pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch

def eventArrow(ax, text, time, height, depth):
    ax.annotate("", xy=(time, depth), xytext=(time, height),  arrowprops=dict(arrowstyle="->"))
    ax.text(time-0.2, 0.01+height, text, rotation=0, size=5)

    return True;

# ax = plt.axes()

f, ax = plt.subplots(1,1)
f.set_dpi(300)


pulse2 = 1
eventArrow(ax, "master_pulse, Audio-Beat", pulse2, 2.25, 0)

eventArrow(ax, "slave0_pulse",6  ,   1, 0.5)
rect0 = patches.Rectangle((6.1, .7), 8.8 , .2, linewidth=1, edgecolor='k', facecolor='lightyellow')
# ax.add_patch(rect0)

p_fancy = FancyBboxPatch((6.1, .7), 8.8 , .2,
                             boxstyle="round,pad=0.02",
                             fc="lightyellow",
                             ec=(0.5, 0.5, 0.5))

ax.add_patch(p_fancy)

ax.text(9, 0.75, "waitTime0", rotation=0, size=5)
rect0 = patches.Rectangle((1.1, .7), 4.8 , .2, linewidth=1, edgecolor='grey', facecolor='none')
ax.add_patch(rect0)
ax.text(3, 0.75, "Latency0", rotation=0, size=5)

eventArrow(ax, "slave1_pulse", 1.5 , 0.5, 0  )
rect1 = patches.Rectangle((1.6, .2), 13.3 , .2, linewidth=1, edgecolor='grey', facecolor='none')
ax.add_patch(rect1)
ax.text(6.5, 0.25, "waitTime1", rotation=0, size=5)
rect1 = patches.Rectangle((1.1, .2), .3 , .2, linewidth=1, edgecolor='grey', facecolor='none')
ax.add_patch(rect1)
ax.text(1, 0.25, "L1", rotation=0, size=4)


strobesOn = pulse2+14

eventArrow(ax, "slave2_pulse", strobesOn , 1.5, 0  )
rect1 = patches.Rectangle((1.1, 1.2), 13.8 , .2, linewidth=1, edgecolor='grey', facecolor='none')
ax.add_patch(rect1)
ax.text(7, 1.25, "Latency2", rotation=0, size=5)


eventArrow(ax, "slaveN_pulse", 10, 2, 1.5  )
rectN = patches.Rectangle((10.1, 1.7), 4.8, .2, linewidth=1, edgecolor='grey', facecolor='none')
ax.add_patch(rectN)
ax.text(11, 1.75, "waitTimeN", rotation=0, size=5)
rectN = patches.Rectangle((1.1, 1.7), 8.8, .2, linewidth=1, edgecolor='grey', facecolor='none')
ax.add_patch(rectN)
ax.text(5, 1.75, "LatencyN", rotation=0, size=5)



eventArrow(ax, "Strobes On", strobesOn, 2.25, 0)
onTime = 11

rectO0 = patches.Rectangle((strobesOn+.1, .7), onTime , .2, linewidth=1, edgecolor='grey', facecolor='none')
ax.add_patch(rectO0)
ax.text(strobesOn+5, 0.75, "onTime", rotation=0, size=5)

rectO1 = patches.Rectangle((strobesOn+.1, .2), onTime , .2, linewidth=1, edgecolor='grey', facecolor='none')
ax.add_patch(rectO1)
ax.text(strobesOn+5, 0.25, "onTime", rotation=0, size=5)

rectO2 = patches.Rectangle((strobesOn+.1, 1.2), onTime , .2, linewidth=1, edgecolor='grey', facecolor='none')
ax.add_patch(rectO2)
ax.text(strobesOn+5, 1.25, "onTime", rotation=0, size=5)

rectON = patches.Rectangle((strobesOn+.1, 1.7), onTime, .2, linewidth=1, edgecolor='grey', facecolor='none')
ax.add_patch(rectON)
ax.text(strobesOn+5, 1.75, "onTime", rotation=0, size=5)


eventArrow(ax, "Strobes Off", strobesOn+onTime+.2, 2.25, 0)



# plt.annotate(r"$\}$",fontsize=32,            xy=(0.27, 0.05), xycoords='figure fraction', rotation=-90)
# plt.annotate(r"$\}$",fontsize=32,xy=(0.27, 0.05), xycoords='figure fraction', rotation=-90)


ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.set_aspect(5)
ax.annotate("", xy=(0, 2.5), xytext=(0, -.015),  arrowprops=dict(arrowstyle="->"))
ax.annotate("", xy=(30, 0), xytext=( -.015, 0),  arrowprops=dict(arrowstyle="->"))
plt.xlim(0,30)
plt.ylim(0,2.5)
plt.ylabel("Nodes")
plt.xlabel("Time")
plt.yticks([])
plt.xticks([])

# f.set_dpi(600)
f.tight_layout()
plt.savefig("TimelinePulse.pdf")
plt.savefig("TimelinePulse.png")
# plt.show()
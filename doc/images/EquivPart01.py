# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 23:08:49 2021

@author: r.hif
"""

from matplotlib import pyplot as plt
import matplotlib.patches as patches
# from matplotlib.patches import FancyBboxPatch

def eventArrow(ax, text, time, height, depth):
    ax.annotate("", xy=(time, depth), xytext=(time, height),  arrowprops=dict(arrowstyle="->"))
    ax.text(time-0.2, 0.01+height, text, rotation=0, size=5)

    return True;

# ax = plt.axes()

f, ax = plt.subplots(1,1)
f.set_dpi(300)

# print(f.get_size_inches())
# -> [6.4 4.8]
f.set_size_inches(6.4, 1.25)

eventArrow(ax, "lower Border", 1  ,   0.5, 0)
rect0 = patches.Rectangle((6.1, .7), 8.8 , .2, linewidth=1, edgecolor='k', facecolor='lightyellow')
# ax.add_patch(rect0)

eventArrow(ax, "higher Border", 20, .5, 0)

rectValid = patches.Rectangle((1+.1, .2), 18.8 , .2, linewidth=1, edgecolor='grey', facecolor='none')
ax.add_patch(rectValid)
ax.text(9.5, .25, "valid Partition", rotation=0, size=5)

rectInValid = patches.Rectangle((20+.1, .2), 2.8 , .2, linewidth=1, edgecolor='grey', facecolor='none')
ax.add_patch(rectInValid)
ax.text(20.4, .25, "invalid Partition", rotation=0, size=5)

rectInValid = patches.Rectangle((-2+.1, .2), 2.8 , .2, linewidth=1, edgecolor='grey', facecolor='none')
ax.add_patch(rectInValid)
ax.text(-1.7, .25, "invalid Partition", rotation=0, size=5)


ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
# ax.spines['bottom'].set_visible(False)
ax.set_aspect(3)

reng = range(-2,24,1)
plt.xticks(reng)
plt.yticks([])

# f.set_dpi(600)
f.tight_layout()
plt.savefig("EquivPart01.pdf")
# plt.savefig("EquivPart01.png")
# plt.show()
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

def tcArrow(ax, text, time, height, depth):
    ax.annotate("", xy=(time, depth), xytext=(time, height),  arrowprops=dict(arrowstyle="->"))
    ax.text(time+0.15, 0.01+height, text, rotation=0, size=5)
    return True;

# ax = plt.axes()

f, ax = plt.subplots(1,1)
f.set_dpi(300)

# print(f.get_size_inches())
# -> [6.4 4.8]
# f.set_size_inches(6.4, 1.25)
f.set_size_inches(6.4, 2)

lowBorder = -10.0
hiBorder = 10.0

tcArrow(ax, "TC9", -10.01, 0.25, 0)
tcArrow(ax, "TC3", -10,  	0.40, 0)
tcArrow(ax, "TC7", -9.99,	0.55, 0)
tcArrow(ax, "TC4", -0.01, 	0.25, 0)
tcArrow(ax, "TC1", 0,  	 	0.40, 0)
tcArrow(ax, "TC5", 0.01,  	0.55, 0)
tcArrow(ax, "TC6", 9.99,  0.25, 0)
tcArrow(ax, "TC2", 10,   	0.40, 0)
tcArrow(ax, "TC8", 10.01,  0.55, 0)

# eventArrow(ax, "lower Border", lowBorder  ,   0.5, 0)
# rect0 = patches.Rectangle((6.1, .7), 8.8 , .2, linewidth=1, edgecolor='k', facecolor='lightyellow')
# ax.add_patch(rect0)

# eventArrow(ax, "higher Border", hiBorder, .5, 0)

rectHeight = 0.75

rectValid = patches.Rectangle((lowBorder+.1, rectHeight), (hiBorder-lowBorder)-.2 , .2, linewidth=1, edgecolor='grey', facecolor='none')
ax.add_patch(rectValid)
ax.text(0 - 1, rectHeight + .05, "valid Partition", rotation=0, size=5)

rectInValidRight = patches.Rectangle((hiBorder+.1, rectHeight), 3.85 , .2, linewidth=1, edgecolor='grey', facecolor='none')
ax.add_patch(rectInValidRight)
ax.text(hiBorder +0.75, rectHeight + .05, "invalid Partition", rotation=0, size=5)

rectInValidLeft = patches.Rectangle((lowBorder-4+.05, rectHeight), 3.85 , .2, linewidth=1, edgecolor='grey', facecolor='none')
ax.add_patch(rectInValidLeft)
ax.text(lowBorder -3.25 , rectHeight + .05, "invalid Partition", rotation=0, size=5)


ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
# ax.spines['bottom'].set_visible(False)
ax.set_aspect(3)

reng = range(-14,16,2)
plt.xticks(reng)
plt.yticks([])

# f.set_dpi(600)
f.tight_layout()
plt.savefig("EquivPart02.pdf")
# plt.savefig("EquivPart02.png")
# plt.show()
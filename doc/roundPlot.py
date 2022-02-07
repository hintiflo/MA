import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# make up some example data
np.random.seed(0)
df = pd.DataFrame(np.random.uniform(0,20, size=(4,4)))
df = df.div(df.sum(1), axis=0)
# plot a stacked horizontal bar chart


fig, ax = plt.subplots()
ax = df.plot.barh(stacked=True, width=0.98, legend=False)
ax.figure.set_size_inches(6,6)

from matplotlib.patches import FancyBboxPatch
ax = df.plot.barh(stacked=True, width=1, legend=False)
ax.figure.set_size_inches(6,6)
new_patches = []
for patch in reversed(ax.patches):
    bb = patch.get_bbox()
    color=patch.get_facecolor()
    p_bbox = FancyBboxPatch((bb.xmin, bb.ymin),
                        abs(bb.width), abs(bb.height),
                        boxstyle="round,pad=-0.0040,rounding_size=0.015",
                        ec="none", fc=color,
                        mutation_aspect=4
                        )
    patch.remove()
    new_patches.append(p_bbox)
for patch in new_patches:
    ax.add_patch(patch)
plt.show()
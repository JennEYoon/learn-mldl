# Scatter Plots
# graph-scatter.py

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
plt.style.use('seaborn-whitegrid')

x = np.linspace(0, 10, 30)
y=np.sin(x)
plt.plot(x, y, 'o', color='black')
plt.show()

plt.scatter(x, y, marker='o')
plt.show()

rng = np.random.RandomState(5)
x = rng.randn(100)
y = rng.randn(100)
colors = rng.rand(100)
sizes = 1000 * rng.rand(100)

plt.scatter(x, y, c=colors, s=sizes, alpha=0.3, cmap='viridis')
plt.colorbar()
plt.suptitle('Fig - Scatter w. colors, sizes')
plt.savefig("fig-scatter-cs.png")
plt.show()



import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,100)
y = x*2

# Functional Method
fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])
ax.plot(x, y)
ax.set_title('title')
ax.set_xlabel('X')
ax.set_ylabel('Y')
plt.show()

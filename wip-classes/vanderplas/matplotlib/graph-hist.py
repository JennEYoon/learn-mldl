# graph-hist.py

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
plt.style.use('seaborn-whitegrid')


data = np.random.randn(1000)
plt.hist(data)
plt.title("fig-histogram 1")
plt.savefig("fig-hist1.png")
plt.show()

#  3-histograms.
x1 = np.random.normal(0, 0.8, 100)  # (loc=mean, scale=std, size=samples drawn)
x2 = np.random.normal(-2, 1, 100)
x3 = np.random.normal(3, 2, 100)

kwargs = dict(histtype='stepfilled', alpha=0.3, normed=True, bins=40)
plt.hist(x1, **kwargs)
plt.hist(x2, **kwargs)
plt.hist(x3, **kwargs)
plt.title("Fig - hist12")
plt.savefig("fig-hist2.png")
plt.show()


############ normal distribution histogram ########
mu, sigma = 0, 0.3
s = np.random.normal(mu, sigma, 1000)
count, bins, ignored = plt.hist(s, 30, density=True)
plt.suptitle("Fig - normal distribution")

plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
                np.exp( - (bins - mu)**2 / (2 * sigma**2) ),
    linewidth=2, color='r')
plt.savefig("fig-hist2.png")    
plt.show()


#### 2D histogram binnings ##########
mean = [0, 0]
cov = [[1, 1], [1, 2]]
x, y = np.random.multivariate_normal(mean, cov, 1000000).T
plt.hist2d(x, y, bins=30, cmap='Blues')
cb = plt.colorbar()
cb.set_label('counts in bin')
plt.savefig("fig-2dhist1.png")
plt.show()

# Not sure what this is doing.
plt.hexbin(x, y, gridsize=30, cmap="Reds")
cb = plt.colorbar(label='count in bin')
plt.savefig("fig-2dhist.png")
plt.show()

####### sns histogram grid ##########
import seaborn as sns

tips = sns.load_dataset("tips")
tips.head()

tips['tip_pct'] = 100 * tips['tip'] / tips['total_bill']

grid = sns.FacetGrid(tips, row='sex', col='time', margin_titles=True)
grid.map(plt.hist, 'tip_pct', bins=np.linspace(0, 40, 15))
plt.suptitle("Figure histogram-grid tips")
plt.subplots_adjust(top = 0.85, bottom=0.1, right=0.9, hspace=0.2, wspace=0.2)
plt.savefig("fig-hist-tips.png")
plt.show()

# graph1.py
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
plt.style.use('seaborn-white')

# sine & cosine wave
x = np.linspace(0, 10, 100)  
# linear from 0 to 10, 100 equal step sizes.

plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x))
plt.show()

# plt.plot() is MATLAB-style interface
# ax.plot() is Object-Oriented interface

########## MATLAB- style, plt.plot() ###################
# "plt" is a global state that manages current instances of fig, axes.

x3 = np.linspace(0, 25, 25)  
plt.figure(1)  # create a figure object.

# create the first of two panels
plt.subplot(211)  # rows, columns, panel 1st.
plt.plot(x3, np.sin(x3-1))
plt.title("Sine Wave")

plt.subplot(212)  # rows, columns, panel 2nd.
plt.plot(x3, np.cos(x3), '-r')
plt.title("Cosine Wave")

# Must to at the bottom, just before show().
plt.suptitle('Suptitle Plotting', fontsize=14, fontweight="bold")  
plt.subplots_adjust(top = 0.85, bottom=0.05, hspace=0.3, wspace=0.3)
plt.savefig("fig1.png")
plt.show()

#### suptitle(), MATPLOTLIB style, plt ###############
names = ['group_a', 'group_b', 'group_c']
values = [1, 10, 100]

plt.figure(num=10, figsize=[9.5, 4.0], edgecolor='black')

plt.subplot(131)  # 1st panel, bar graph.
plt.bar(names, values)
plt.title("bar graph")

plt.subplot(132)  # 2nd panel, scatter graph.
plt.scatter(names, values)
plt.title("scatter graph")

plt.subplot(133)  # 3rd panel, line graph.
plt.plot(names, values)
plt.title("line graph")

plt.suptitle('Fig 10 - Categorical', fontsize=14, fontweight='bold')
plt.subplots_adjust(top = 0.85, bottom=0.1, wspace=0.35)
plt.savefig("fig10.png")
plt.show()


########### Object-Oriented style, ax.plot() ############

x = np.linspace(0, 10, 100)  

# First create a grid of plots.
# ax will be an array of two Axes objects.
fig, ax = plt.subplots(2)

# Call plot() on ax objects
ax[0].plot(x, np.sin(x))
ax[1].plot(x, np.cos(x))

# Create fig5, ax separately.
fig5 = plt.figure(num=5, figsize=(9.5, 6.0))

ax = fig5.add_subplot(211)  # panel 1
ax.plot(x, np.sin(x))
ax.set_title('1st axes title')
ax.set_xlabel('xlabel 1')
ax.set_ylabel('ylabel 1')

ax = fig5.add_subplot(212)  # panel 2
ax.plot(x, np.cos(x-1), 'or')
ax.set_title('2nd axes title')
ax.set_xlabel('xlabel 2')
ax.set_ylabel('ylabel 2')

fig5.subplots_adjust(top = 0.88, bottom=0.08, hspace=.4, wspace=0.35)
fig5.suptitle('Figure 5 suptitle', fontsize=14, fontweight='bold')
plt.savefig("fig5.png")
plt.show()

####### Object Oriented, 2 columns ##############
# First create a grid of plots.
# ax will be an array of two Axes objects.
# fig, ax = plt.subplots(2)  # 2 rows, 1 column.
# ax[0].plot(x, np.sin(x))
# ax[1].plot(x, x*x)
# plt.show()

# Create 1 row, 2 columns figure.
fig, ax = plt.subplots(1, 2, figsize=(9.5, 4.5)) 
ax[0].plot(x, np.cos(x), 'or')
ax[1].plot(x, x*x, '--g')

ax[0].set_title('Axes title')
ax[1].set_title('Axes title 2')
ax[0].set_xlabel('xlabel')
ax[0].set_ylabel('ylabel')
ax[1].set_xlabel('xlabel 2')
ax[1].set_ylabel('ylabel 2')
plt.suptitle('Figure 2-columns-b', fontsize=14, fontweight='bold')
plt.subplots_adjust(top = 0.85, bottom=0.1, wspace=0.25)
plt.savefig("figb-2columns.png")
plt.show()


# Or plat 2 lines in 1 graph.
fig, ax = plt.subplots(1)
ax.plot(x, x, '-b')
ax.plot(x, x*x, 'or')
ax.set_title('Axes title')
ax.set_xlabel('xlabel')
ax.set_ylabel('ylabel')
plt.suptitle('Figure suptitle', fontsize=14, fontweight='bold')
plt.savefig("fig6.png")
plt.show()

######## Object Oriented, Numbered Figure, 2 columns #####

fig7 = plt.figure(num=7, figsize=[9.5, 4.5], edgecolor="b")

ax = fig7.add_subplot(121)
ax.plot(x, np.sin(x))
ax.set_title('1st axes title')
ax.set_xlabel('xlabel 1')
ax.set_ylabel('ylabel 1')

ax = fig7.add_subplot(122)
ax.plot(x, x*x, 'or')
ax.set_title('2nd axes title')
ax.set_xlabel('xlabel 2')
ax.set_ylabel('ylabel 2')

fig7.subplots_adjust(top = 0.85, bottom=0.1, wspace=0.35)
fig7.suptitle('Figure 2-columns', fontsize=14, fontweight='bold')
plt.savefig("fig-2columns.png")
plt.show()


## legend ##
plt.style.use('seaborn-whitegrid')
plt.plot(x, np.sin(x), '-g', label='sin(x)')
plt.plot(x, np.cos(x), ':b', label='cons(x)')
plt.axis('equal')
plt.title("Fig legend")
plt.legend()
plt.savefig("fig-legend.png")
plt.show()

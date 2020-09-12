from mpl_toolkits import mplot3d
import mpl_toolkits.mplot3d.art3d as art3d

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Circle

import numpy as np
import random

from objects.cell import Cell
from objects.environment import SingleEnv

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.set_xticks(np.arange(0, 1050, step=100))
ax.set_yticks(np.arange(0, 1050, step=100))
ax.set_zticks(np.arange(0, 50, step=10))
cell = Cell()

defaultDelayFrame = 200                         # 200 millisecond

# Create environment with a cell, 10 users and 5 UAVs
environment = SingleEnv(cell,
                        10,                         # number of users
                        5,                          # number of UAVs
                        2000,                       # number of steps
                        defaultDelayFrame / 1000)   # time Step in second

listPoints4Scatter = environment.generateUserPoints()
listPoints4ScatterUAV = environment.generateUAVPoints()

scats = []


def drawCell(ax, cell):
    c_circle = Circle(
        (cell.centerPoint.x, cell.centerPoint.y), cell.r, fill=False)
    ax.add_patch(c_circle)
    art3d.pathpatch_2d_to_3d(c_circle, z=0, zdir="z")

    # draw basestation
    ax.plot([cell.centerPoint.x, cell.centerPoint.x], [
            cell.centerPoint.y, cell.centerPoint.y], [0, 20], 'gray')

    # scale viewbox
    ax.plot([1000, 500], [500, 500], [0, 20], 'gray', alpha=0)
    ax.plot([500, 500], [1000, 500], [0, 20], 'gray', alpha=0)
    ax.plot([0, 500], [500, 500], [0, 20], 'gray', alpha=0)
    ax.plot([500, 500], [0, 500], [0, 20], 'gray', alpha=0)


def animate(num, dataUser, dataUAV):
    global scats
    # remove old scatters of users
    for scat in scats:
        scat.remove()
    scats = []

    print(num)
    datum = dataUser[num]
    datumUAV = dataUAV[num]
    scats.append(ax.scatter(datum.x, datum.y, datum.z, color='r', s=20))
    scats.append(ax.scatter(datumUAV.x, datumUAV.y,
                            datumUAV.z, color='blue', s=20))


# Draw the ground circle of Cell
drawCell(ax, cell)

# draw Users & UAVs
anim = animation.FuncAnimation(fig,                 # figure
                               animate,             # callable
                               1500,                # iterable
                               fargs=(
                                   [listPoints4Scatter,
                                    listPoints4ScatterUAV]),    # additional arguments
                               interval=defaultDelayFrame,      # delay between frames in milliseconds
                               blit=False)

# export to video
# writer = animation.FFMpegWriter(fps=15, codec="h264", extra_args=[
#     "-preset", "veryslow", "-crf", "0"])

# Show 3D model
plt.show()

# リアルタイムプロットは下記ページを参照
# https://qiita.com/hausen6/items/b1b54f7325745ae43e47

import math
import func
import plot3D
import time
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import sys

def testfn():
    fig = plt.figure()
    axis = fig.add_subplot(111, projection="3d", xlabel="x", ylabel="y", zlabel="z")
    point, = axis.plot([], [], [], "o", color = "C3")

    axis.set_xlim(-1,1)
    axis.set_ylim(-1,1)
    axis.set_zlim(-1,1)

    plot3D.init(axis)

    t = 0
    while True:
        cos = np.cos(t)
        sin = np.sin(t)

        ax = 0
        ay = 0
        az = -1

        mx = 1
        my = 0
        mz = 0

        vec_acc = np.mat([ax,ay,az]).T
        vec_mag = np.mat([mx,my,mz]).T

        Rmat = func.euler_rotate(t, math.pi/4, 0)
        vec_acc = Rmat * vec_acc
        vec_mag = Rmat * vec_mag


        attitude = func.get_attitude(vec_acc, vec_mag)


        roll = attitude[0]
        pitch = attitude[1]
        yaw = attitude[2]

        basis_x = np.mat([1, 0, 0]).T
        direction = func.euler_rotate(roll, pitch, yaw) * basis_x

        plot3D.plot_vector(direction, point)
        t += 0.05
        plt.pause(.05)

        print(roll, pitch, yaw)

if __name__ == "__main__":
    try:
        testfn()
    except:
        print("Program ended by user.\n")
        sys.exit()
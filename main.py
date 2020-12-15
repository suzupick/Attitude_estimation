# リアルタイムプロットは下記ページを参照
# https://qiita.com/hausen6/items/b1b54f7325745ae43e47

import math
import func
import plot3D
import time
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

fig = plt.figure()
axis = fig.add_subplot(111, projection="3d")
point, = axis.plot([], [], [], "o", color = "C3")

t = 0
while True:
    cos = math.cos(t)
    sin = math.sin(t)

    ax = cos
    ay = sin
    az = cos*sin

    mx = sin
    my = cos*cos
    mz = cos

    vec_a_car = np.mat([ax,ay,az]).T
    vec_m_car = np.mat([mx,my,mz]).T

    try:
        vec_attitude = func.get_attitude(vec_a_car, vec_m_car)
    except:
        continue

    roll = vec_attitude[0]
    pitch = vec_attitude[1]
    yaw = vec_attitude[2]
    basis_x = np.mat([1, 0, 0]).T
    vec_car_position = func.Rz(yaw) * func.Ry(pitch) * func.Rx(roll) * basis_x

    plot3D.plot_vector(vec_car_position, point)
    t += 0.05
    plt.pause(.05)
import calc_attitude
import sys
import client
import numpy as np
import math
import plot3D
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.pyplot import axes
import matplotlib.pyplot as plt

def main_fn():
    axis, point = plot3D.init()

    RPi_3Dcmps = client.socket_comm("192.168.0.6", 50007)
    RPi_3Dcmps.connect()
    while True:
        attitude = RPi_3Dcmps.request_attitude()
        roll = attitude[0]
        pitch = attitude[1]
        yaw = attitude[2]

        basis_x = np.mat([1, 0, 0]).T
        direction_x = calc_attitude.euler_rotate(-roll, -pitch, -yaw).T * basis_x

        plot3D.plot_vector(direction_x, point)
        plt.pause(.01)

        print(roll, pitch, yaw)
    

if __name__ == "__main__":
    try:
        main_fn()
    except KeyboardInterrupt:
        print("Program ended by user.\n")
        sys.exit()
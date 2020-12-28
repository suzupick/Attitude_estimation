from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

def init():
    fig = plt.figure()
    axis = fig.add_subplot(111, projection="3d", xlabel="x", ylabel="y", zlabel="z")
    point, = axis.plot([], [], [], "o", color = "C3")

    axis.set_xlim(-1,1)
    axis.set_ylim(-1,1)
    axis.set_zlim(-1,1)

    _phi = np.linspace(0, 2*np.pi, 30)
    _theta = np.linspace(0, np.pi, 15)
    phi, theta = np.meshgrid(_phi, _theta)

    r = 1
    x = r*np.cos(phi)*np.sin(theta)
    y = r*np.sin(phi)*np.sin(theta)
    z = r*np.cos(theta)

    axis.plot_wireframe(x, y, z, color="k", alpha=0.2)

    return axis, point

def plot_vector(vec, point):
    point.set_data((vec[0,0], vec[1,0]))
    point.set_3d_properties(vec[2,0])
    
if __name__ == "__main__":
    fig = plt.figure()
    axis = fig.add_subplot(111, projection="3d")
    point, = axis.plot([], [], [], "o", color = "C3")
    # init(axis)
    plot_vector(np.mat([1,1,1]).T, point)
    plt.show()
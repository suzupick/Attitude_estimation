from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

def init(ax):
    _phi = np.linspace(0, 2*np.pi, 30)
    _theta = np.linspace(0, np.pi, 15)
    phi, theta = np.meshgrid(_phi, _theta)

    r = 1
    x = r*np.cos(phi)*np.sin(theta)
    y = r*np.sin(phi)*np.sin(theta)
    z = r*np.cos(theta)

    ax.plot_wireframe(x, y, z, color="k")

def plot_vector(vec, point):
    point.set_data((vec[0], vec[1]))
    point.set_3d_properties(vec[2])
    
if __name__ == "__main__":
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    init(ax)
    plot_vector(1, 1, 1, ax)
    plt.show()
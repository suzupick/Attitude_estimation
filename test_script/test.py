import math
import matplotlib.pyplot as plt
from numpy.core.function_base import linspace
import func
import numpy as np

x = linspace(-2*math.pi, 2*math.pi, 300)
y = []

for i in x:
    Rmat = func.euler_rotate(1,i,0)
    vec_acc = Rmat * np.mat([0,0,-1]).T
    vec_mag = Rmat * np.mat([1,0,0]).T
    tmp = func.get_attitude(vec_acc, vec_mag)[1]
    y.append(tmp)

fig = plt.figure()
axis = fig.add_subplot(1,1,1)
axis.plot(x,y)
plt.show()
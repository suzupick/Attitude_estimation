import math
import matplotlib.pyplot as plt
from numpy.core.function_base import linspace
import func
import numpy as np

x = linspace(-2*math.pi, 2*math.pi)
y = []
for i in x:
    vec_acc = np.mat([0,0,-1]).T
    vec_acc = func.euler_rotate(i, 1, 1) * vec_acc
    tmp = func.accel2roll(vec_acc)
    y.append(tmp)

fig = plt.figure()
axis = fig.add_subplot(1,1,1)
axis.plot(x,y)
plt.show()
import math
import matplotlib.pyplot as plt
from numpy.core.function_base import linspace
import func
import numpy as np

x = linspace(-5*math.pi, 5*math.pi, 500)
y = []

for i in x:
    tmp = i
    tmp = func.map_to_anguler_domain(tmp)
    y.append(tmp)

fig = plt.figure()
axis = fig.add_subplot(1,1,1)
axis.plot(x,y)
plt.show()


print(x % math.pi - math.pi)
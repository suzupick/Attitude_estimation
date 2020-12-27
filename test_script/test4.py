import math
import matplotlib.pyplot as plt
from numpy.core.function_base import linspace
import func
import numpy as np


vec_acc_0 = np.mat([0,0,-1]).T
vec_mag_0 = np.mat([1,0,0]).T
Rmat = func.euler_rotate(2, 2, 3)

vec_acc_1 = Rmat * vec_acc_0
vec_mag_1 = Rmat * vec_mag_0

att = func.get_attitude(vec_acc_1, vec_mag_1)
# vec_acc_2 = func.euler_rotate(att[0], att[1], att[2]) * vec_acc_0

# print(vec_acc_1)
# print(vec_acc_2)


print(att)
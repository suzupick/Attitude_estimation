import numpy as np
import math

mat1 = np.mat(
    [[1,2],
    [3,4]]
)

mat2 = np.mat(
    [[1,-1],
    [-1,1]]
)

vec1 = np.mat([1,2]).T

print(mat1 * mat2)
print(mat1 * vec1)
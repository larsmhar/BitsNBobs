# @ is shorthand for matrix multiplication,
# which is cool I guess
import numpy as np

m = np.matrix([[1, 3], [3, 1]])
a = np.matrix([[2, 2], [2, 1]])

print(m @ a) # [[8, 5], [8, 7]]

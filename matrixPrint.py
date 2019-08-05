def print_matrix(matrix, sep="\n"):
    print(*matrix, sep)

matrix = [
    ["This", "is", "some", "text"],
    [2, 1, 4, 1, 5],
    ["a", 2, "b", 2]
]

print_matrix(matrix)

# Also works with numpy
import numpy as np


new_matrix =  np.asarray(matrix)

print_matrix(new_matrix)

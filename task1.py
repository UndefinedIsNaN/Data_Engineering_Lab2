import numpy as np

def normalize_2d(matrix):
    norm = np.linalg.norm(matrix)
    matrix = matrix/norm  # normalized matrix
    return matrix

matrix = np.load('C:/Users/Mitya/Downloads/2_2/first_task.npy')
rev_matrix = matrix[:, ::-1]
matrix_sum = np.sum(matrix)
matrix_mean = np.mean(matrix)
diagonal_sum = np.trace(matrix)
diag_mean = np.mean(np.diagonal(matrix))
rev_diagonal_sum = np.trace(matrix[:, ::-1])
rev_diag_mean = np.mean(np.diagonal(rev_matrix))

import json

# a Python object (dict):
x = {
  "sum": int(matrix_sum),
  "avr": int(matrix_mean),
  "sumMD": int(diagonal_sum),
  "avrMD": int(diag_mean),
  "sumSD": int(rev_diagonal_sum),
  "avrSD": int(rev_diag_mean),
  "max": int(np.max(matrix)),
  "min": int(np.min(matrix)),
}


# convert into JSON:
y = json.dumps(x)
print(y)
matrix = normalize_2d(matrix)
print(matrix)
np.save('C:/Users/Mitya/Downloads/2_2/matrix.npy',matrix)

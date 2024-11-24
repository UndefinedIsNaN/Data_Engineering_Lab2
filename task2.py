import numpy as np
import os

matrix = np.load('C:/Users/Mitya/Downloads/2_2/second_task.npy')
x = []
y = []
z = []
for i in range(np.shape(matrix)[0]):

    for j in range(np.shape(matrix)[1]):

        if matrix[i][j] > 502:
            x.append(i)
            y.append(j)
            z.append(matrix[i][j])

np.savez("second_task.npz", x=x, y=y, z=z)
np.savez_compressed("second_task_comp.npz", x=x, y=y, z=z)
s = os.path.getsize("second_task.npz")
s_comp = os.path.getsize("second_task_comp.npz")
print(f"savez = {s}")
print(f"savez_comp = {s_comp}")
print(f"diff = {s - s_comp}")
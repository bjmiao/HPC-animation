import numpy as np
import matplotlib.pyplot as plt
from plot_stencil import plot_stencil

plt.figure()
data = np.zeros((30, 30))
data[0, :] = 1
data[:, 0] = 1
data[29, :] = -1
data[:, 29] = -1
data[0,29] = 0
data[29,0] = 0

data2 = data.copy()
for i in range(1,29):
    for j in range(1, 29):
        data2[i,j] = (i+j) / 60 * (-2) + 1


iter_per_frame = 10
# plt.pause(5)
fig, ((ax1, ax2)) = plt.subplots(nrows=1, ncols=2)
plot_stencil(data, ax1, "Boundary Condition")
plot_stencil(data, ax2, "Boundary Condition")
plt.pause(4)

plot_stencil(data, ax1, "Trivial Initial Value")
plot_stencil(data2, ax2, "Guessed Initial Value")
plt.pause(2)

for frame in range(50):
    data_old = data.copy()
    data2_old = data2.copy()
    for _ in range(iter_per_frame):
        for i in range(1, 29):
            for j in range(1, 29):
                data[i,j] = 0.125*(data[i-1,j] + data[i+1,j] + data[i,j-1] + data[i,j+1]) + 0.5 * data[i,j]
                data2[i,j] = 0.125*(data2[i-1,j] + data2[i+1,j] + data2[i,j-1] + data2[i,j+1]) + 0.5 * data2[i,j]
    residual = np.abs(np.subtract(data_old, data)).max().max()
    residual2 = np.abs(np.subtract(data2_old, data2)).max().max()
    title1 = "#Iteration : %d \n residual %f" %(frame * iter_per_frame, residual)
    title2 = "#Iteration : %d \n residual %f" %(frame * iter_per_frame, residual2)
    plot_stencil(data, ax1, title1)
    plot_stencil(data2, ax2, title2)
    plt.pause(0.1)

plt.pause(5)
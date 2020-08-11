import numpy as np
import matplotlib.pyplot as plt


def plot_stencil(data, ax=None, title = None):
    norm = plt.Normalize(-1, 1)
    (x, y) = data.shape
    if ax == None:
        ax = plt.gca();
    ax.cla()

    im = ax.imshow(data, cmap='bwr', norm=norm,
                    interpolation='none', vmin=-1, vmax=1, aspect='equal');
    # Major ticks
    ax.set_xticks([]);
    ax.set_yticks([]);

    # Labels for major ticks
    ax.set_xticklabels(np.arange(1, x, 1));
    ax.set_yticklabels(np.arange(1, y, 1));
    # Minor ticks
    ax.set_xticks(np.arange(-.5, x, 1), minor=True);
    ax.set_yticks(np.arange(-.5, y, 1), minor=True);

    # Gridlines based on minor ticks
    ax.grid(which='minor', color='black', linestyle='-', linewidth=0.5)
    ax.set_title(title)

if __name__ == "__main__":
    plt.figure()
    frame = 32
    data = np.zeros((frame, 30, 30))
    norm = plt.Normalize(-1, 1)

    for i in range(frame//4):
        a1 = i*4
        (x,y) = (1, i+1)
        data[a1+1, x, y] = 1
        data[a1+1, x+1, y] = 1
        data[a1+1, x-1, y] = 1
        data[a1+1, x, y+1] = 1
        data[a1+1, x, y-1] = 1
        data[a1+2, x, y] = -1
    im = plt.imshow(data[0,:,:], cmap='bwr', norm=norm,
                    interpolation='none', vmin=-1, vmax=1, aspect='equal');
    # plt.pause(3)

    for i in range(frame):
        plot_stencil(data[i,:,:])
        plt.pause(0.5)
    plt.pause(1)
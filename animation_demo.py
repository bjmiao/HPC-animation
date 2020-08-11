"""
================
pyplot animation
================

Generating an animation by calling `~.pyplot.pause` between plotting commands.

The method shown here is only suitable for simple, low-performance use.  For
more demanding applications, look at the :mod:`.animation` module and the
examples that use it.

Note that calling `time.sleep` instead of `~.pyplot.pause` would *not* work.
"""

def update(i, update_element, data, cache):
    t, n = update_element
    # print(n, cache[i,:])
    if (n in cache[i,:]):
        data[:, t-1, n-1] = -1
    else:
        data[:, t-1, n-1] = 1

import matplotlib.pyplot as plt
import numpy as np

nsize = 16
tsize = 10
frame = 40
cachesize = 8
np.random.seed(19680801)

norm = plt.Normalize(-1, 1)

data1 = np.zeros((frame, tsize, nsize))
data2 = np.zeros((frame, tsize, nsize))
data1[:,:,:] = np.zeros((frame, tsize, nsize))
data2[:,:,:] = np.zeros((frame, tsize, nsize))
cache1 = np.zeros((frame, cachesize), dtype=int)
cache2 = np.zeros((frame, cachesize), dtype=int)
cache_null = np.zeros((1,cachesize))
cache_null[0, :] = np.linspace(-0.3, 0.3, cachesize)
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2)

update_list1 = [(1, 1),(1, 2),(1, 3),(1, 4),(1, 5),(1, 6),(1, 7),(1, 8),(1, 9),(1, 10),(1, 11),(1, 12),(1, 13),(1, 14),(1, 15),(1, 16),
    (2, 1),(2, 2),(2, 3),(2, 4),(2, 5),(2, 6),(2, 7),(2, 8),(2, 9),(2, 10),(2, 11),(2, 12),(2, 13),(2, 14),(2, 15),(2, 16),
    (3, 1),(3, 2),(3, 3),(3, 4),(3, 5),(3, 6),(3, 7),(3, 8)]

update_list2 = [(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(1,7),(2,2),(2,3),(2,4),(2,5),(2,6),(3,3),(3,4),(3,5),(4,4),
    (2,1),(3,1),(3,2),(4,1),(4,2),(4,3),(1,8),(1,9),(1,10),(1,11),(1,12),(1,13),(1,14),(1,15),(1,16),
    (2,10),(2,11),(2,12),(2,13),(2,14),(2,15),(3,11),(3,12),(3,13),]

for i in range(1, frame):
    cache1[i, :] = list(range(1,9))
    cache2[i, :] = list(range(1,9))

for i in [7,9,10,11,12,13,14,15,16,23,25,26,27,28,29,30,31]:
    cache1[i, :] = list(range(9,17))

for i in list(range(25,40)):
    cache2[i, :] = list(range(9,17))


ax3.imshow(cache_null, cmap='bwr', norm=norm)
ax4.imshow(cache_null, cmap='bwr', norm=norm)

plt.pause(3)
for i in range(frame):
    update_element1 = update_list1[i]
    update_element2 = update_list2[i]    
    update( i, update_element1, data1, cache1)
    update( i, update_element2, data2, cache2)
    ax1.cla()
    ax2.cla()
    
    ax1.imshow(data1[i,:,:], cmap='bwr', norm=norm)
    ax2.imshow(data2[i,:,:], cmap='bwr', norm=norm)
    ax1.invert_yaxis()
    ax2.invert_yaxis()
    ax1.set_xlabel("Array")
    ax1.set_ylabel("Time")
    ax1.set_xticks(range(nsize))
    ax1.set_yticks(range(tsize))
    ax2.set_xlabel("Array")
    ax2.set_ylabel("Time")
    ax2.set_xticks(range(nsize))
    ax2.set_yticks(range(tsize))

    ax1.set_title("Baseline: Step {}".format(i))
    ax2.set_title("Optimized: Step {}".format(i))
    
    ax3.cla()
    ax4.cla()
    ax3.imshow(cache_null, cmap='bwr', norm=norm)
    ax4.imshow(cache_null, cmap='bwr', norm=norm)
    ax3.set_xticks([])
    ax3.set_yticks([])
    ax4.set_xticks([])
    ax4.set_yticks([])
    ax3.set_title("Cache for Baseline")
    ax4.set_title("Cache for Optimizaed")

    for c in range(cachesize):
        text = ax3.text(c, 0, str(cache1[i,c]-1), ha='center', va='center', color='b')
        text = ax4.text(c, 0, str(cache2[i,c]-1), ha='center', va='center', color='b')
    # Note that using time.sleep does *not* work here!
    plt.pause(0.1)

# bwr
from matplotlib import container
import numpy as np
from numpy.core.fromnumeric import partition
from numpy.random import default_rng
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from bubbleSort import bubbleSort
from quickSort import quickSort
from insertionSort import insertionSort
from mergeSort import mergeSort

class TrackedArray():
    def __init__(self, arr):
        self.arr = np.copy(arr)
        self.reset()

    def reset(self):
        self.indices = []
        self.values = []
        self.access_type = []
        self.full_copies = []

    def track(self, key, access_type):
        self.indices.append(key)
        self.values.append(self.arr[key])
        self.access_type.append(access_type)
        self.full_copies.append(np.copy(self.arr))

    def GetActivity(self, idx=None):
        if isinstance(idx, type(None)):
            return [(i, op) for (i, op) in zip(self.indices, self.access_type)]
        else:
            return (self.indices[idx], self.access_type[idx])

    def __getitem__(self, key):
        self.track(key, "get")
        return self.arr.__getitem__(key)

    def __setitem__(self, key, value):
        self.arr.__setitem__(key, value)
        self.track(key, "set")

    def __delitem__(self, key):
        self.track(key, "del")
        self.arr.__delitem__(key)

    def __len__(self):
        return self.arr.__len__()

    def __str__(self):
        return self.arr.__str__()

    def __repr__(self):
        return self.arr.__repr__()


N = 20

arr = np.round(np.linspace(1, 1000, N), 0)

np.random.shuffle(arr)
print(arr)
arr = TrackedArray(arr)

print(arr)

fig, ax = plt.subplots(figsize=(16, 8))


bubbleSort(arr)
fig.suptitle(bubbleSort(arr))
#insertionSort(arr)
#fig.suptitle(insertionSort(arr))
#quickSort(arr, 0, len(arr)-1)
#fig.suptitle(quickSort(arr, 0, len(arr)-1))



def update(frame):
    for (rectangle, height) in zip(container.patches, arr.full_copies[frame]):
        rectangle.set_height(height)
        rectangle.set_color('#1f234e')

    return (*container,)


ani = animation.FuncAnimation(fig, update, frames=range(len(arr.full_copies)),
                              blit=True, interval=1/10, repeat=False)

container = ax.bar(np.arange(0, len(arr), 1),
                   align="edge", width=0.8, height=arr)
plt.show()

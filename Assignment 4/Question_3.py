'''
This program makes random array, sorts it and reshapes to 3x4 and 4x3.
'''

import numpy as np

randarr = np.random.randint(1, 101, 12)
sortedarr = np.sort(randarr)

print("Sorted array:", sortedarr)
print("3x4 matrix:\n", sortedarr.reshape(3,4))
print("4x3 matrix:\n", sortedarr.reshape(4,3))

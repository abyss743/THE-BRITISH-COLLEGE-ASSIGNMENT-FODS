'''
This program takes two matrices and does add, subtract and multiply with numpy.
'''

import numpy as np

print("Matrix A rows cols")
r1,c1 = map(int, input().split())
A = np.array([list(map(float,input().split())) for _ in range(r1)])

print("Matrix B rows cols")
r2,c2 = map(int, input().split())
B = np.array([list(map(float,input().split())) for _ in range(r2)])

if A.shape == B.shape:
    print("Add:\n", A+B)
    print("Sub:\n", A-B)
else:
    print("Cannot add/sub - different size")

if A.shape[1] == B.shape[0]:
    print("Multiply:\n", A @ B)
else:
    print("Cannot multiply")

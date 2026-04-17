'''
This program takes one number and shows cube, cube root, natural log, base-2 log and power 6.
'''

import math

x = float(input("Enter a number: "))

print("Cube          :", x**3)
print("Cube root     :", x**(1/3))
print("Natural log   :", math.log(x) if x > 0 else "Undefined")
print("Base-2 log    :", math.log2(x) if x > 0 else "Undefined")
print("Power 6       :", x**6)

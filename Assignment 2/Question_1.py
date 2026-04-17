'''
Function that shows sum, difference, product and quotient of two integers.
'''

def do_calc(x, y):
    print("Sum      :", x + y)
    print("Difference:", x - y)
    print("Product  :", x * y)
    if y != 0:
        print("Quotient :", x / y)
    else:
        print("Quotient : cannot divide by zero")

a = int(input("First integer: "))
b = int(input("Second integer: "))
do_calc(a, b)

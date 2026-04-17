'''
Separate functions for addition, multiplication, division, floor division and exponentiation.
'''

def add(x, y): return x + y
def multiply(x, y): return x * y
def divide(x, y): return x / y if y != 0 else "Cannot divide"
def floor_div(x, y): return x // y if y != 0 else "Cannot divide"
def power(x, y): return x ** y

p = float(input("First number: "))
q = float(input("Second number: "))

print("Addition      :", add(p, q))
print("Multiplication:", multiply(p, q))
print("Division      :", divide(p, q))
print("Floor Division:", floor_div(p, q))
print("Exponent      :", power(p, q))

'''
This program calculates factorial with input validation.
'''

try:
    n = int(input("Enter positive integer: "))
    if n < 0:
        print("Invalid input! Please enter a positive integer.")
    else:
        fact = 1
        for i in range(1, n+1):
            fact = fact * i
        print("Factorial =", fact)
except:
    print("Invalid input! Please enter a positive integer.")

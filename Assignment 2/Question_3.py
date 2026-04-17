'''
Function to check if a number is Armstrong or not.
'''

def check_arm(n):
    order = len(str(n))
    total = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        total += digit ** order
        temp //= 10
    return total == n

num = int(input("Enter number: "))
if check_arm(num):
    print(num, "is Armstrong")
else:
    print(num, "is not Armstrong")

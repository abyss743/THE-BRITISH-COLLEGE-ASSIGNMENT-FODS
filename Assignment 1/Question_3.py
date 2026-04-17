'''
This program checks whether the number is positive even, positive odd, negative even or negative odd.
'''

num = int(input("Enter a number: "))

if num > 0:
    if num % 2 == 0:
        print(num, "is Positive Even")
    else:
        print(num, "is Positive Odd")
elif num < 0:
    if num % 2 == 0:
        print(num, "is Negative Even")
    else:
        print(num, "is Negative Odd")
else:
    print("The number is Zero")

'''
Menu driven program to add positive and negative numbers separately until exit.
'''

pos_sum = 0
neg_sum = 0

while True:
    val = input("Enter a number or 'exit': ")
    if val.lower() == 'exit':
        break
    try:
        num = float(val)
        if num > 0:
            pos_sum += num
        elif num < 0:
            neg_sum += num
    except:
        print("Invalid input")

print("Positive sum:", pos_sum)
print("Negative sum:", neg_sum)

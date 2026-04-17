'''
Program to remove duplicates and sort the list in ascending order.
'''

nums = []
count = int(input("How many numbers: "))
for i in range(count):
    nums.append(int(input(f"Number {i+1}: ")))

clean = sorted(set(nums))
print("Unique sorted:", clean)

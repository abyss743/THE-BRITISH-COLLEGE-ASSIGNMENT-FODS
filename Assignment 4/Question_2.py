'''
This program takes at least 12 numbers, sorts them and does slicing.
'''

inp = input("Enter at least 12 numbers (comma separated): ")
nums = [int(x.strip()) for x in inp.split(",")]

sortednums = sorted(nums)
print("Sorted:", sortednums)

print("3-6 :", sortednums[3:7])
print("6-9 :", sortednums[6:10])
print("4-10:", sortednums[4:11])

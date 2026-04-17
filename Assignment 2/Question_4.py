'''
Function that returns frequency dictionary of numbers in list. Tested with three lists.
'''

def count_freq(lst):
    d = {}
    for item in lst:
        d[item] = d.get(item, 0) + 1
    return d

print("Test1:", count_freq([1,2,2,3,3,3]))
print("Test2:", count_freq([5,5,5,10]))
print("Test3:", count_freq([100,200,100,300]))

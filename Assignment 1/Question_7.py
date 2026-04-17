'''
This program finds numbers divisible by 9 but not by 6. Range can be entered by user.
'''

s = int(input("Enter start (default 1000): ") or 1000)
e = int(input("Enter end (default 2500): ") or 2500)

result = [i for i in range(s, e+1) if i % 9 == 0 and i % 6 != 0]
print("Numbers divisible by 9 but not by 6:", result)

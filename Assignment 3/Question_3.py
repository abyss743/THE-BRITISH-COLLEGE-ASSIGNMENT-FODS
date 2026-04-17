'''
This program takes list of integers, does operations and saves with date time. Shows log on exit.
'''

from datetime import datetime

while True:
    inp = input("Enter numbers (comma sep) or exit: ")
    if inp.lower() == "exit":
        break
    try:
        nums = [int(x) for x in inp.split(",")]
        total = sum(nums)
        diff = nums[0] - nums[1] if len(nums)>1 else 0
        prod = 1
        for n in nums: prod *= n
        div = nums[0]/nums[1] if len(nums)>1 and nums[1]!=0 else "undef"
        
        now = datetime.now().strftime("%Y-%m-%d %H:%M")
        with open("operations_log.txt", "a") as f:
            f.write(f"[{now}] Numbers:{nums} Sum:{total} Diff:{diff} Prod:{prod} Div:{div}\n")
    except:
        print("Invalid input")

print("Log contents:")
with open("operations_log.txt", "r") as f:
    print(f.read())

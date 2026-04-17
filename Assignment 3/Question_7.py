'''
Staff class and program to add multiple staff and save to staff.csv with try/except.
'''

import csv

class Staff:
    def __init__(self):
        self.id = input("Emp ID: ")
        self.name = input("Full Name: ")
        self.addr = input("Address: ")
        self.phone = input("Phone: ")
        self.marital = input("Marital Status: ")
        self.dep = input("Dependents: ")
        self.sal = input("Salary: ")

staffs = []
while True:
    ch = input("Add staff (y/n): ")
    if ch.lower() != "y": break
    s = Staff()
    staffs.append(s)

try:
    with open("staff.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["ID","Name","Address","Phone","Marital","Dependents","Salary"])
        for s in staffs:
            w.writerow([s.id, s.name, s.addr, s.phone, s.marital, s.dep, s.sal])
    print("Data saved to staff.csv")
except:
    print("Error saving file")

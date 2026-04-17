'''
This program takes student details and appends to records.csv.
'''

import csv

name = input("Student Name: ")
roll = input("Roll No: ")
prog = input("Program: ")
yr = input("Year: ")
grp = input("Group: ")

with open("records.csv", "a", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([name, roll, prog, yr, grp])

print("Record added successfully")

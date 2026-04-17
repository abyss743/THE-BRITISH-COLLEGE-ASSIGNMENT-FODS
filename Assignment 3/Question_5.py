'''
Class Learner with roll_no, full_name, address, enrollment_year, program, group.
'''

class Learner:
    def __init__(self):
        self.roll = input("Roll No: ")
        self.name = input("Full Name: ")
        self.addr = input("Address: ")
        self.year = input("Enrollment Year: ")
        self.prog = input("Program: ")
        self.grp = input("Group: ")
    
    def show(self):
        print("Roll No:", self.roll)
        print("Name   :", self.name)
        print("Address:", self.addr)
        print("Year   :", self.year)
        print("Program:", self.prog)
        print("Group  :", self.grp)

stud = Learner()
stud.show()

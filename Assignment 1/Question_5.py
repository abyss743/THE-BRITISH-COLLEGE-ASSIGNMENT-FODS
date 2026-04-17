'''
This program takes 6 subject marks and calculates total, average, percentage and grade.
'''

marks = []
for i in range(6):
    m = float(input(f"Marks of subject {i+1}: "))
    marks.append(m)

total = sum(marks)
avg = total / 6
perc = avg

print("\nTotal      :", total)
print("Average    :", avg)
print("Percentage :", perc, "%")

if perc >= 85:
    print("Grade: Distinction")
elif perc >= 70:
    print("Grade: First Division")
elif perc >= 55:
    print("Grade: Second Division")
elif perc >= 45:
    print("Grade: Third Division")
else:
    print("Grade: Fail")

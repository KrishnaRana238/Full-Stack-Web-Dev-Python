# Task: Store student grades and calculate average grade.

grades = {
    "John": [85, 90, 78],
    "Alice": [92, 88, 95],
    "Bob": [70, 75, 80],
    "Charlie": [88, 82, 84]
}
for i, j in grades.items():
    print("Student:", i, "Grades:", sum(j))
    print("Average Grade for", i, ":", sum(j) / len(j))
          
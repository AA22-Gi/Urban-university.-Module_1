grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

student_grades = {}
students = sorted(list(students))

for i in range(len(grades)):
    student_grades[students[i]] = sum(grades[i]) / len(grades[i])
print("Each student's average score:", student_grades)
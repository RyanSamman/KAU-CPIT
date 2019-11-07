numberStudents = eval(input("Enter the number of students: "))

max_score_1 = max_score_2 = 0
max_score_name_1 = max_score_name_2 = 0

for i in range(0, numberStudents):
    student = input("Enter a student name: ")
    score = eval(input("Enter a student score: "))

    if score > max_score_1:
        max_score_1, max_score_name_2, max_score_2 = score, max_score_name_1, max_score_1
        max_score_name_1 = student

    elif score > max_score_2:
        max_score_2 = score
        max_score_name_2 = student

if numberStudents == 0:
    print("Error,h no students to compare")
elif numberStudents == 1:
    print("Top student")
    print(max_score_name_1, max_score_1)
else:
    print("Top two students: ")
    print(max_score_name_1, max_score_1)
    print(max_score_name_2, max_score_2)

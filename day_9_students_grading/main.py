student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}
for name in student_scores:
    #  print(name)
    if student_scores[name] <= 70:
        student_grades[name] = "Fail"
    elif student_scores[name] > 70 and student_scores[name] <= 80:
        student_grades[name] = "Acceptable"
    elif student_scores[name] > 80 and student_scores[name] <= 90:
        student_grades[name] = "Exceeds Expectations"
    else:
        student_grades[name] = "Outstanding"
# elif 80 >= student_scores[name] > 70:
#     student_grates{name: "Acceptable"}
# elif 90 >= student_scores[name] > 80:
#     student_grades{name: "Exceeds Expectations"}
# else:
#     student_grades{name: "Outstanding"}
# TODO-2: Write your code below to add the grades to student_grades.👇


# 🚨 Don't change the code below 👇
print(student_grades)
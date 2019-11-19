grades = []
more_grades = "jah"
m = 1
while more_grades == "jah":
    grade = input(f"Palun sisesta {m}. hinne:")
    grades.append(int(grade))
    m = m + 1
    if input("Kas sul on veel hindeid? Vasta jah/ei: ").lower() != "jah":
        more_grades = "ei"
print(grades)
sum_of_marks = 0
for numbers in grades:
    sum_of_marks += numbers
grade = sum_of_marks / len(grades)
print(grade)


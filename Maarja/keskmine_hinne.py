hinded = []
more_grades = "jah"
m = 1
while more_grades == "jah":
    grade = input(f"Palun sisesta {m}. hinne:")
    hinded.append(int(grade))
    m = m + 1
    if input("Kas sul on veel hindeid? Vasta jah/ei: ").lower() != "jah":
        more_grades = "ei"
print(hinded)
sum_of_marks = 0
for numbers in hinded:
    sum_of_marks += numbers
grade = sum_of_marks / len(hinded)
print(grade)

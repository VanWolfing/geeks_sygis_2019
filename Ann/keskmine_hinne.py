print("Welcome to grade sheet generator!")

subject_num = input("How many subjects do you want to insert? ")

subject_list = []
for num in range(int(subject_num)):
    subject = input("Insert the name of the subject: ")
    subject_list.append(subject)

subject_dict = {}
grades = []
for subject in subject_list:
    grade_num = input("How many grades do you have in the subject? ")
    for num in range(int(grade_num)):
        grade = input(f"Please add your grades for {subject}: ")
        grades.append(grade)

    subject_dict[subject] = grades


def get_average_grade(grade_list):
    for grade in grade_list:
        print(grade)
        sum += grade

    sum = sum / len(grade_list)
    return sum


print(subject_dict["eng"])

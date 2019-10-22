# TODO kindlasti peaks saama koodi efektiivsemaks teha, vaata üle
# TODO kui jõuad tegele visuaalse poolega ka, siis on tore lastele saata :D


def get_average_grade(subject_dict, subject):
    # TODO lõpeta keskmise hinde arvutamine
    sum = 0
    if subject == "" or subject == "a":
        # TODO a tagastab listi listidest
        grade_list = subject_dict.values()

    print(grade_list)
    for grade in grade_list:
        sum += grade

    sum = sum / len(grade_list)
    return sum


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
    grades = []


subject = input("Which subject do you want to get your average grade for (if you inserted only one grade " +
                "then press enter)? ")

get_average_grade(subject_dict, subject)



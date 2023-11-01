n = int(input("number of students: "))

students = []
for i in range(n):
    name = input("name of student: ")
    students.append(name)


for i in range(n-1, -1, -1):
    student = students[i]
    for x in range(i-1, -1, -1):
        past_student = students[x]
        print(past_student + ":Salam " + student + "!")
    print(student + ": khodahafez bacheha!")
    for x in range(i-1, -1, -1):
        past_student = student[x]
        print(past_student + ":khodahafez" + student + "!")
# def filter_passing_scores(students_scores):
#     return dict(filter(lambda key, value: ))


def filter_passing_scores(student_scores):
    passed_students = dict(filter(lambda item: item[1] > 10, student_scores.items()))
    return passed_students


students_scores = {
    "Ali": 20,
    "Mohammad": 19,
    "Abbas": 4,
    "Alireza": 13,
    "Farhad": 9,
    "Hooman": 15
}
print(filter_passing_scores(students_scores))

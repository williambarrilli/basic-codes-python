#d1 = {'azul': '1E415E','verde':'092E20','amarelo',}

d = {'pedro': '6','joana': '7'}


# d1 = {}
# d1 ['will'] = 6
# d1 ['pedro'] = 7
# for key, val in d1.items():
#     print('{}= {}'.format(key,val))
# print(d1)

student = {'name': 'Jose', 'school': 'Computing', 'grades': (66,77,88)}

student2 = {'name': 'Pedro', 'school': 'Arquitetura', 'grades': (22,33,44)}

student_list = [student, student2]

def average_grade_all_students(student_list):
    total = 0
    count = 0
    for student in student_list:
        total += sum(student.get('grades'))
        print(total)


average_grade_all_students(student_list)


def average_grade_all_students(student_list):
    total = 0
    count = 0
    for student in student_list:
        grades = student.get('grades')
        count += len(grades)
        total += sum(grades)
        return total/count


average_grade_all_students(student_list)

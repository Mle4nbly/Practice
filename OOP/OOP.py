from statistics import mean

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.student_grades = {}        

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.lecturer_grades:
                lecturer.lecturer_grades[course] += [grade]
            else:
                lecturer.lecturer_grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def student_statistic(self):
        self.student_grades_avg = []
        for values in self.student_grades.values():
            for value in values:
                self.student_grades_avg.append(value)
        self.average = mean(self.student_grades_avg)
        student_dict[self.name, self.surname] = [self.average]

        self.courses_ip = str()
        for course in range(len(self.courses_in_progress)):
            self.courses_ip += self.courses_in_progress[course] + ', '

        self.f_courses = str()
        for course in range(len(self.finished_courses)):
            self.f_courses += self.finished_courses[course] + ', '
    
    def __gt__ (self, other: 'Student'):
        return self.average > other.average
    
    def __lt__ (self, other: 'Student'):
        return self.average < other.average 

    def __eq__ (self, other: 'Student'):
        return self.average == other.average

    def __str__(self):           
        return f'Студент \nИмя - {self.name} \nФамилия - {self.surname} \nСредняя оценка за домашнее задание : {self.average} \nКурсы в процессе изучения : {self.courses_ip[:len(self.courses_ip)-2]} \nЗавершенные курсы : {self.f_courses[:len(self.f_courses)-2]}'
        

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        Mentor.__init__(self, name, surname)
        self.lecturer_grades = {}

    def lecturer_statistic(self):
        self.lecturer_grades_avg = []
        for values in self.lecturer_grades.values():
            for value in values:
                self.lecturer_grades_avg.append(value)
        self.average = mean(self.lecturer_grades_avg)
        lecturer_dict[self.name, self.surname] = [self.average]

    def __gt__ (self, other: 'Lecturer'):
        return self.average > other.average
    
    def __lt__ (self, other: 'Lecturer'):
        return self.average < other.average 

    def __eq__ (self, other: 'Lecturer'):
        return self.average == other.average
    
    def __str__(self):
        return f'Лектор \nИмя - {self.name} \nФамилия - {self.surname} \nСредняя оценка за лекции : {self.average}'
        
class Reviewer(Mentor):
    def __init__(self, name, surname):
        Mentor.__init__(self, name, surname)

        
    def rate_homework(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.student_grades:
                student.student_grades[course] += [grade]
            else:
                student.student_grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def __str__(self):
        return f'Эксперт \nИмя - {self.name} \nФамилия - {self.surname}'

student_dict = {}
lecturer_dict = {}

average_list_student = []
average_list_lecturer = []

some_student_1 = Student('Viktor', 'Mercedesov', 'male')
some_student_1.courses_in_progress += ['Python']
some_student_1.courses_in_progress += ['Git']
some_student_1.finished_courses += ['Введение в программирование']
some_student_2 = Student('Pasha', 'Dvabasha', 'male')
some_student_2.courses_in_progress += ['Python']
some_student_2.courses_in_progress += ['Git']
some_student_2.finished_courses += ['Введение в программирование']

some_lecturer_1 = Lecturer('Somebody', 'Oncetoldme')
some_lecturer_1.courses_attached += ['Python']
some_lecturer_2 = Lecturer('Theworldis', 'Gonnarollme')
some_lecturer_2.courses_attached += ['Python']

some_reviewer_1 = Reviewer('Spotlight', 'Uh')
some_reviewer_1.courses_attached += ['Python']
some_reviewer_2 = Reviewer('Moonlight', 'Uh')
some_reviewer_2.courses_attached += ['Python']

some_student_1.rate_lecture(some_lecturer_2, 'Python', 10)
some_student_1.rate_lecture(some_lecturer_1, 'Python', 8)
some_student_2.rate_lecture(some_lecturer_2, 'Python', 9)
some_student_2.rate_lecture(some_lecturer_1, 'Python', 4)

some_reviewer_1.rate_homework(some_student_1, 'Python', 7)
some_reviewer_1.rate_homework(some_student_2, 'Python', 9)
some_reviewer_2.rate_homework(some_student_1, 'Python', 3)
some_reviewer_2.rate_homework(some_student_2, 'Python', 5)

some_student_1.student_statistic()
some_student_2.student_statistic()
some_lecturer_1.lecturer_statistic()
some_lecturer_2.lecturer_statistic()

def comparision_of_student():
    for average in student_dict.values():
        for student in student_dict.keys():
            if student_dict[student] == average and average == max(student_dict.values()):
                print('Наибольший показатель средней оценки у студента за ДЗ:')
                print(*student)
                print('Средняя оценка - ', *average)
                print('')
                break
comparision_of_student()

def comparision_of_lecturer():
    for average in lecturer_dict.values():
        for lecturer in lecturer_dict.keys():
            if lecturer_dict[lecturer] == average and average == max(lecturer_dict.values()):
                print('Наибольший показатель средней оценки у лектора за лекции:')
                print(*lecturer)
                print('Средняя оценка - ', *average)
                print('')
                break
comparision_of_lecturer()

def average_rating_students():
    if some_student_1.courses_in_progress == some_student_2.courses_in_progress:
        average_list_student.append(some_student_1.average)
        average_list_student.append(some_student_2.average)
    print('')
    print('Средняя оценка за ДЗ по всем студентам - ',mean(average_list_student))
average_rating_students()

def average_rating_lecturer():
    if some_lecturer_1.courses_attached == some_lecturer_2.courses_attached:
        average_list_lecturer.append(some_lecturer_1.average)
        average_list_lecturer.append(some_lecturer_2.average)
    print('')
    print('Средняя оценка за лекции по всем лекторам - ',mean(average_list_lecturer))
    print('')
average_rating_lecturer()
    
print(f'{some_student_1}\n'
f'\n'
f'{some_student_2}\n'
f'\n'
f'{some_lecturer_1}\n'
f'\n'
f'{some_lecturer_2}\n'
f'\n'
f'{some_reviewer_1}\n'
f'\n'
f'{some_reviewer_2}\n')







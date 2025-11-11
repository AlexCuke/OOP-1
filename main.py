class Student:
    instances = [] # объявляем атрибут класса для хранения всех экземпляров
    def __init__(self, name, surname, gender): # Описание элементов класса
        instances = []
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        Student.instances.append(self)
    def rate_lecture(self, lecturer, course, grade): # Оценка
        if (
                isinstance(lecturer, Lecturer)
                and course in self.courses_in_progress
                and course in lecturer.courses_attached
        ):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade(self): # Средняя оценка
        all_grades = []
        for grades in self.grades.values():
            all_grades.extend(grades)
        return sum(all_grades) / len(all_grades) if all_grades else 0
    def __str__(self): #  Распечатка
        avg = self.average_grade()
        return f"Имя: {self.name} \nФамилия: {self.surname}\nСредняя оценка за домашние задания: {avg:.1f}\nКурсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы:{self.finished_courses}\n"

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.average_grade() < other.average_grade()
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Student):
            return self.average_grade() <= other.average_grade()
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.average_grade() == other.average_grade()
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, Student):
            return self.average_grade() != other.average_grade()
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Student):
            return self.average_grade() > other.average_grade()
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Student):
            return self.average_grade() >= other.average_grade()
        return NotImplemented

class Mentor:
    def __init__(self, name, surname): # Описание элементов класса
        self.name = name
        self.surname = surname
        self.courses_attached = []
    def rate_hw(self, student, course, grade): # Оценка
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

class Lecturer (Mentor):
    def __init__(self, name, surname): # Описание элементов класса
        super().__init__(name, surname)
        self.grades={}
    def average_grade(self): # Средняя оценка
        all_grades = []
        for grades in self.grades.values():
            all_grades.extend(grades)
        return sum(all_grades) / len(all_grades) if all_grades else 0
    def __str__(self): #  Распечатка
        avg = self.average_grade()
        return f"Имя: {self.name} \nФамилия: {self.surname}\nСредняя оценка за лекции:  {avg:.1f}\n"
    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade() < other.average_grade()
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade() <= other.average_grade()
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade() == other.average_grade()
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade() != other.average_grade()
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade() > other.average_grade()
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade() >= other.average_grade()
        return NotImplemented

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade): # Описание элементов класса
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


    def __str__(self): #  Распечатка
        return f"Имя: {self.name} \nФамилия: {self.surname}\n"


print('Задание 1:')
lecturer = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Пётр', 'Петров')
print(isinstance(lecturer, Mentor)) # True
print(isinstance(reviewer, Mentor)) # True
print(lecturer.courses_attached)    # []
print(reviewer.courses_attached)    # []
print('end 1\n')


print('Задание 2:')
lecturer = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Пётр', 'Петров')
student = Student('Алёхина', 'Ольга', 'Ж')

student.courses_in_progress += ['Python', 'Java']
lecturer.courses_attached += ['Python', 'C++']
reviewer.courses_attached += ['Python', 'C++']

print(student.rate_lecture(lecturer, 'Python', 7))   # None
print(student.rate_lecture(lecturer, 'Java', 8))     # Ошибка
print(student.rate_lecture(lecturer, 'С++', 8))      # Ошибка
print(student.rate_lecture(reviewer, 'Python', 6))   # Ошибка

print(lecturer.grades)  # {'Python': [7]}
print('end 2\n')


print('Задание 3:')

# Задание Проверяющих, Лекторов и студентов
reviewer1 = Reviewer('Пётр', 'Петров')
reviewer1.courses_attached += ['Python', 'C++']
reviewer2 = Reviewer('Андрей', 'Серов')
reviewer2.courses_attached += ['Java']
lecturer1 = Lecturer('Иван', 'Иванов',)
lecturer1.courses_attached += ['Python', 'C++']
lecturer2 = Lecturer('Михаил', 'Груздев',)
lecturer2.courses_attached += ['Java','C++']
student1 = Student('Алёхина', 'Ольга', 'Ж',)
student1.courses_in_progress += ['Python', 'Java']
student1.finished_courses += ['C++']
student2= Student('Семен', 'Слепаков', 'М',)
student2.courses_in_progress += ['C++','Java']
student2.finished_courses += ['Python']

# Процесс оценки друг друга
reviewer1.rate_hw(student1, 'Python', 5)
reviewer1.rate_hw(student2, 'C++', 8)
reviewer2.rate_hw(student1, 'Java', 9)
student1.rate_lecture(lecturer1, 'C++', 7)
student1.rate_lecture(lecturer2, 'Java', 10)
student2.rate_lecture(lecturer1, 'Python', 8)
student2.rate_lecture(lecturer2, 'C++', 8)

#  сравнение
print(student1 > student2)  # Сравнение студентов
print(lecturer1 < lecturer2)  # Сравнение лекторов
print(student1 == student2)  # Сравнение студентов
print(lecturer1 == lecturer2)  # Сравнение лекторов
print('\n')
# Dывод на экран
print('Проверяющие:\n')
print(reviewer1)
print(reviewer2)
print('Лекторы:\n')
print(lecturer1)
print(lecturer2)
print('Студенты:\n')
print(student1)
print(student2)
print('end 3\n')


print('Задание 4:')

# Списки для  экземпляров
students = []
lecturers = []
reviewers = []

# Создание Проверяющих, Лекторов и студентов
students.append(Student('Алёхина', 'Ольга', 'Ж'))
students.append(Student('Семен', 'Слепаков', 'М'))
lecturers.append(Lecturer('Иван', 'Иванов'))
lecturers.append(Lecturer('Михаил', 'Груздев'))
reviewers.append(Reviewer('Пётр', 'Петров'))
reviewers.append(Reviewer('Андрей', 'Серов'))

# Назначение курсов
students[0].courses_in_progress += ['Python', 'Java']
students[0].finished_courses += ['C++']
students[1].courses_in_progress += ['C++', 'Java']
students[1].finished_courses += ['Python']

lecturers[0].courses_attached += ['Python', 'C++']
lecturers[1].courses_attached += ['Java', 'C++']

reviewers[0].courses_attached += ['Python', 'C++']
reviewers[1].courses_attached += ['Java']

# Оценка
reviewers[0].rate_hw(students[0], 'Python', 5)
reviewers[0].rate_hw(students[1], 'C++', 8)
reviewers[1].rate_hw(students[0], 'Java', 9)

students[0].rate_lecture(lecturers[0], 'Python', 7)
students[0].rate_lecture(lecturers[1], 'Java', 10)
students[1].rate_lecture(lecturers[0], 'C++', 8)
students[1].rate_lecture(lecturers[1], 'C++', 8)

# Сравнение
print(students[0] > students[1])
print(lecturers[0] < lecturers[1])
print(students[0] == students[1])
print(lecturers[0] == lecturers[1])

# Вывод на экран
print('Проверяющие:\n')
for some_reviewer in reviewers:
    print(some_reviewer)

print('Лекторы:\n')
for some_lecturer in lecturers:
    print(some_lecturer)

print('Студенты:\n')
for some_student in students:
    print(some_student)

course=['Python', 'Java','C++']
def avg_grade_students(students, course):
    grades = []
    for some_student in students:
        if course in some_student.grades:
            grades.extend(some_student.grades[course])
    return sum(grades) / len(grades) if grades else 0

def avg_grade_lecturers(lecturers, course):
    grades = []
    for some_lecturer in lecturers:
        if course in some_lecturer.grades:
            grades.extend(some_lecturer.grades[course])
    return sum(grades) / len(grades) if grades else 0


for some_course in course:
    print(f'Средняя оценка студентов по курсу {some_course} : {avg_grade_students(students, some_course)}')
for some_course in course:
    print(f'Средняя оценка лекторов по курсу {some_course} : {avg_grade_lecturers(lecturers, some_course)}')
print('end 4\n')



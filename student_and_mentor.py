class Student:
    student_list = []
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        Student.student_list.append(self)

    def get_feedback(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached \
                and course in self.courses_in_progress and 0 < grade <= 10:
            if course not in lecturer.feedback:
                lecturer.feedback[course] = [grade]
            else:
                lecturer.feedback[course].append(grade)
        else:
            print("Некорректная оценка")

    def average_marks(self):
        sum_marks = 0
        count_marks = 0
        for mark in self.grades.values():
            sum_marks += sum(mark)
            count_marks += len(mark)
        if count_marks != 0:
            return sum_marks / count_marks
        else:
            return None

    def __str__(self):
        return f'Имя: {self.name}' \
               f'\nФамилия: {self.surname}' \
               f'\nСредняя оценка за домашнее задание: {self.average_marks()}' \
               f'\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}' \
               f'\nЗавершенные курсы: {", ".join(self.finished_courses)}'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    feedback_list = []

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.feedback = {}
        Lecturer.feedback_list.append(self)

    def average_feedback(self):
        sum_feedback = 0
        count_feedback = 0
        for feedback in self.feedback.values():
            sum_feedback += sum(feedback)
            count_feedback += len(feedback)
        if count_feedback != 0:
            return sum_feedback / count_feedback
        else:
            return None

    def __str__(self):
        return f'Имя: {self.name}' \
               f'\nФамилия: {self.surname}' \
               f'\nСредняя оценка за лекции: {self.average_feedback()}'


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}' \
               f'\nФамилия: {self.surname}'


def avg_studentmarks_course(students: list, cours: str):
    count = 0
    lst_avg = 0
    for student in students:
        if isinstance(student, Student):
            if cours in student.grades:
                sum_lst = sum(student.grades[cours])
                lst_avg += sum_lst / len(student.grades[cours])
                count += 1
    return lst_avg / count


def avg_lecturerfeedback_course(lecturers: list, cours: str):
    count = 0
    lst_avg = 0
    for lecturer in lecturers:
        if isinstance(lecturer, Lecturer):
            if cours in lecturer.feedback:
                sum_lst = sum(lecturer.feedback[cours])
                lst_avg += sum_lst / len(lecturer.feedback[cours])
                count += 1
    return lst_avg / count


student1 = Student("Egor", "Semenov", "Male")
student2 = Student("Elena", "Popova", "Female")
student1.finished_courses.append('Git')
student2.finished_courses.append('Django')
student1.courses_in_progress = ["Python", "SQL", "Django", "Flask"]
student2.courses_in_progress = ["Python", "SQL", "Git", "Flask", "API"]


reviewer1 = Reviewer('Konstantin', 'Meshkov')
reviewer2 = Reviewer('Georgiy', 'Kolosov')
reviewer1.courses_attached = ["Python", "SQL", "Django", "Flask"]
reviewer2.courses_attached = ["Python", "SQL", "Git", "Flask", "API"]
reviewer1.rate_hw(student1, "Python", 5)
reviewer1.rate_hw(student1, "SQL", 4)
reviewer1.rate_hw(student1, "Django", 4)
reviewer1.rate_hw(student1, "Flask", 5)
reviewer2.rate_hw(student2, "Python", 4)
reviewer2.rate_hw(student2, "SQL", 3)
reviewer2.rate_hw(student2, "Git", 5)
reviewer2.rate_hw(student2, "Flask", 5)
reviewer2.rate_hw(student2, "API", 5)


lector1 = Lecturer('Alexander', 'Kuzmin')
lector2 = Lecturer('Aleksei', 'Smirnov')
lector1.courses_attached = ["Python", "SQL", "Django"]
lector2.courses_attached = ["Git", "Flask", "API"]
student1.get_feedback(lector1, "Python", 10)
student1.get_feedback(lector1, "SQL", 6)
student1.get_feedback(lector1, "Django", 8)
student2.get_feedback(lector2, "Git", 9)
student2.get_feedback(lector2, "Flask", 8)
student2.get_feedback(lector2, "API", 10)


print("--------Students--------")
print(student1)
print(student1.grades)
print("----------")
print(student2)
print(student2.grades)
print("--------Reviewers--------")
print(reviewer1)
print("----------")
print(reviewer2)
print("--------Lecturers--------")
print(lector1)
print(lector1.feedback)
print("----------")
print(lector2)
print(lector2.feedback)

print(avg_studentmarks_course(Student.student_list, 'Python'))
print(avg_lecturerfeedback_course(Lecturer.feedback_list, 'Python'))
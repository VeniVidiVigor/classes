class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

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
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за д/з {self.average_marks()} /' \
               f'\nКурсы в процессе изучения {self.courses_in_progress}\nЗавершенные курсы {self.finished_courses}'


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
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за курс: {self.average_feedback()}'


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
        return f'Имя: {self.name}\nФамилия: {self.surname}'


def avg_studentmarks_course(students: list, cours: str):
    count = 0
    lst_avg = 0
    for student in students:
        if isinstance(student, Student):
            if cours in student.grades:
                sum_lst = sum(student.grades[cours])
                lst_avg = sum_lst / len(student.grades[cours])
                count += 1
    return lst_avg / count


def avg_lecturerfeedback_course(lecturers: list, cours: str):
    count = 0
    lst_avg = 0
    for lecturer in lecturers:
        if isinstance(lecturer, Lecturer):
            if cours in lecturer.feedback:
                sum_lst = sum(lecturer.feedback[cours])
                lst_avg = sum_lst / len(lecturer.feedback[cours])
                count += 1
    return lst_avg / count
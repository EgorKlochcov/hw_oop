class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = ["У студента нет завершенных курсов"]
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        if "У студента нет завершенных курсов" in self.finished_courses:
            self.finished_courses.clear()
            self.finished_courses.append(course_name)
        else:
            self.finished_courses.append(course_name)

    def lecturer_grade(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def _average_grade(self, grades):
        if grades:
            amount = 0
            all_sum = 0
            for v in grades.values():
                amount += len(v)
                all_sum += sum(v)
            return all_sum / amount

        else:
            return "У студента не проставлены оценки "

    def __lt__(self, other):
        if not isinstance(other, Student):
            return "Нельзя сравнить"

        if int(self._average_grade(self.grades)) > int(other._average_grade(other.grades)):
            res = f"Средний балл студента {self.name} больше студента {other.name}"
            return res
        else:
            res = f"Средний балл студента {self.name} меньше студента {other.name}"
            return res

    def __str__(self):
        cip = ", ".join(self.courses_in_progress)
        fc = ", ".join(self.finished_courses)
        res = f"Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {float(self._average_grade(self.grades))} \nКурсы в процессе изучения: {cip} \nЗавершенные курсы: {fc}"
        return res


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def _average_grade(self, grades):
        if grades:
            amount = 0
            all_sum = 0
            for v in grades.values():
                amount += len(v)
                all_sum += sum(v)
            return all_sum / amount

        else:
            return "У Лектора пока что нет оценок от студентов"

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return "Нельзя сравнить"

        if int(self._average_grade(self.grades)) > int(other._average_grade(other.grades)):
            res = f"Средний балл лектора {self.name} больше лектора {other.name}"
            return res
        else:
            res = f"Средний балл лектора {self.name} меньше лектора {other.name}"
            return res

    def __str__(self):
        res = f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {float(self._average_grade(self.grades))}"
        return res


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
        res = f"Имя: {self.name}\nФамилия: {self.surname}"
        return res


def average_hw_grade(students, course):
    grade = 0
    for student in students:
        grade += sum(student.grades.get(course)) / len(student.grades.get(course))
    return f"Средний балл студентов на курсе {course} равен {float(grade / len(students))}"


def average_lec_course(lectors, course):
    grade = 0
    for lector in lectors:
        grade += sum(lector.grades.get(course)) / len(lector.grades.get(course))
    return f"Средний балл лекторов на курсе {course} равен {float(grade / len(lectors))}"


# _______________________________________________________________________________________________________________________________
# _______________________________________________________________________________________________________________________________
#                                          Полевые испытания

student_alex = Student("Alex", "Alexeev", "male")
student_alex.courses_in_progress += ["Python"]
student_alex.courses_in_progress += ["Git"]
student_alex.add_courses("Основы пайтон")

student_ivan = Student("Ivan", "Ivanov", "male")
student_ivan.courses_in_progress += ["Python"]
student_ivan.courses_in_progress += ["Основы пайтон"]
student_ivan.courses_in_progress += ["Git"]

rev_anton = Reviewer("Anton", "Antonov")
rev_anton.courses_attached += ["Python"]

rev_dima = Reviewer("Dmitry", "Dmitryiev")
rev_dima.courses_attached += ["Git"]

lec_oleg = Lecturer("Oleg", "Olegov")
lec_oleg.courses_attached += ["Python"]
lec_oleg.courses_attached += ["Git"]

lec_nina = Lecturer("Nina", "Nikolaeva")
lec_nina.courses_attached += ["Python"]
lec_nina.courses_attached += ["Git"]

rev_anton.rate_hw(student_alex, "Python", 9)
rev_anton.rate_hw(student_alex, "Python", 8)
rev_anton.rate_hw(student_alex, "Python", 10)

rev_anton.rate_hw(student_ivan, "Python", 7)
rev_anton.rate_hw(student_ivan, "Python", 9)
rev_anton.rate_hw(student_ivan, "Python", 6)

rev_dima.rate_hw(student_ivan, "Git", 8)
rev_dima.rate_hw(student_ivan, "Git", 7)
rev_dima.rate_hw(student_ivan, "Git", 9)

rev_dima.rate_hw(student_alex, "Git", 10)
rev_dima.rate_hw(student_alex, "Git", 10)
rev_dima.rate_hw(student_alex, "Git", 9)

student_alex.lecturer_grade(lec_oleg, "Git", 9)
student_alex.lecturer_grade(lec_oleg, "Git", 9)

student_alex.lecturer_grade(lec_oleg, "Python", 10)
student_alex.lecturer_grade(lec_oleg, "Python", 10)

student_ivan.lecturer_grade(lec_oleg, "Git", 8)
student_ivan.lecturer_grade(lec_oleg, "Git", 10)

student_ivan.lecturer_grade(lec_oleg, "Python", 10)
student_ivan.lecturer_grade(lec_oleg, "Python", 8)

student_alex.lecturer_grade(lec_nina, "Python", 8)
student_alex.lecturer_grade(lec_nina, "Python", 8)

student_alex.lecturer_grade(lec_nina, "Git", 9)
student_alex.lecturer_grade(lec_nina, "Git", 10)

student_ivan.lecturer_grade(lec_nina, "Python", 7)
student_ivan.lecturer_grade(lec_nina, "Python", 7)

student_ivan.lecturer_grade(lec_nina, "Git", 7)
student_ivan.lecturer_grade(lec_nina, "Git", 8)

students_list = [student_ivan, student_alex]
lectors_list = [lec_nina, lec_oleg]

print(student_alex, student_ivan, rev_anton, rev_dima, lec_oleg, lec_nina, sep="\n\n")
print()
print(lec_oleg > lec_nina)
print()
print(student_alex > student_ivan)
print()
print(average_hw_grade(students_list, "Python"))
print()
print(average_lec_course(lectors_list, "Python"))
print()
print(average_lec_course(lectors_list, "Git"))
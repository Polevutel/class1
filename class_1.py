class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grade(self):
        total = 0
        count = 0
        for grades_list in self.grades.values():
            total += sum(grades_list)
            count += len(grades_list)
        return round(total / count, 1)

    def __str__(self):
        return f"Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.average_grade()}"

    def __lt__(self, other):
        return self.average_grade() < other.average_grade()

    def __le__(self, other):
        return self.average_grade() <= other.average_grade()

    def __eq__(self, other):
        return self.average_grade() == other.average_grade()

    def __ne__(self, other):
        return self.average_grade() != other.average_grade()

    def __gt__(self, other):
        return self.average_grade() > other.average_grade()

    def __ge__(self, other):
        return self.average_grade() >= other.average_grade()

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return f"Имя: {self.name} \nФамилия: {self.surname}"

class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_in_progress = []
        self.completed_courses = []
        self.grades = {}

    def average_grade(self):
        total = 0
        count = 0
        for course_grades in self.grades.values():
            total += sum(course_grades)
            count += len(course_grades)
        return round(total / count, 1)

    def __str__(self):
        return f"Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {self.average_grade()} \nКурсы в процессе изучения: {', '.join(self.courses_in_progress)} \nЗавершенные курсы: {', '.join(self.completed_courses)}"

    def __lt__(self, other):
        return self.average_grade() < other.average_grade()

    def __le__(self, other):
        return self.average_grade() <= other.average_grade()

    def __eq__(self, other):
        return self.average_grade() == other.average_grade()

    def __ne__(self, other):
        return self.average_grade() != other.average_grade()

    def __gt__(self, other):
        return self.average_grade() > other.average_grade()

    def __ge__(self, other):
        return self.average_grade() >= other.average_grade()

# Создание экземпляров классов
lecturer1 = Lecturer("Владимир", "Смирнов")
lecturer2 = Lecturer("Ольга", "Тихонова")
reviewer1 = Reviewer("Андрей", "Журба")
reviewer2 = Reviewer("Екатерина", "Волкова")
student1 = Student("Михаил", "Дощечкин")
student2 = Student("София", "Золотова")

# Добавление оценок
lecturer1.grades = {"Python": [10, 9, 8], "Git": [9, 8, 7]}
lecturer2.grades = {"Python": [9, 9, 9], "Git": [8, 8, 8]}
student1.grades = {"Python": [9, 8, 10], "Git": [7, 7, 9]}
student2.grades = {"Python": [7, 9, 8], "Git": [10, 8, 9]}

# Вывод информации о лекторах
print("Лекторы:")
print(lecturer1)
print(lecturer2)

# Вывод информации о проверяющих
print("Проверяющие:")
print(reviewer1)
print(reviewer2)

# Вывод информации о студентах
print("Студенты:")
print(student1)
print(student2)

# Функция для подсчета средней оценки за домашние задания по всем студентам в рамках конкретного курса
def average_grade_course_students(students, course):
    total = 0
    count = 0
    for student in students:
        if course in student.grades:
            total += sum(student.grades[course])
            count += len(student.grades[course])
    return round(total / count, 1)
python_avg_grade = average_grade_course_students([student1, student2], "Python")
print(f"Средняя оценка за домашние задания по курсу Python: {python_avg_grade}")

# Функция для подсчета средней оценки за лекции всех лекторов в рамках курса
def average_grade_course_lecturers(lecturers, course):
    total = 0
    count = 0
    for lecturer in lecturers:
        if course in lecturer.grades:
            total += sum(lecturer.grades[course])
            count += len(lecturer.grades[course])
    return round(total / count, 1)

# Вызов функции и подсчет средней оценки за лекции всех лекторов в рамках курса "Git"
git_avg_grade = average_grade_course_lecturers([lecturer1, lecturer2], "Git")
print(f"Средняя оценка за лекции по курсу Git: {git_avg_grade}")
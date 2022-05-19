
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    
    def add_courses(self, course_name):
        self.finished_course.append(course_name)  


    def rate_lect(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.course_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка' 

    def average_grade_st(self):
        x = []       
        for _, grades_list in self.grades.items():
            x.extend(grades_list)
        if len(x) != 0:
            avg_grade = sum(x) / len(x)
            return avg_grade
        return 'Оценок нет'

    def __lt__(self, other):
        if (not isinstance(self, Student)) or (not isinstance(other, Student)):
            return
        if other.average_grade_st() < self.average_grade_st():
            print(f"Cредний балл выше у студента: {self.name}")
        else:
            print(f"Cредний балл выше у студента: {other.name}")


    def __str__(self):
        res = f"""Имя: {self.name} \n 
        Фамилия: {self.surname} \n 
        Средняя оценка за домашние задания: {self.average_grade_st()} \n 
        Курсы в процессе изучения: {','.join(self.courses_in_progress)} \n 
        Завершенные курсы: {','.join(self.finished_courses)}"""
        return res

    

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []



class Lecturer(Mentor):
    def __init__(self, name, surname):
       super().__init__(name, surname)
       self.course_attached = []
       self.grades = {}

    def average_grade_lect(self):
        y = []
        for _, grades_list in self.grades.items():
            y.extend(grades_list)
        if len(y) != 0:
            avg_grade = sum(y) / len(y)
            return avg_grade
        return 'Оценок нет'

    def __lt__(self, other):
        if (not isinstance(self, Lecturer)) or (not isinstance(other, Lecturer)):
            return 'Ошибка'
        if other.average_grade_lect() < self.average_grade_lect():
            print(f"Cредний балл выше у лектора: {self.name}")
        else:
            print(f"Cредний балл выше у лектора: {other.name}")

    def __str__(self):
        res = f"""
        Имя: {self.name} \n 
        Фамилия: {self.surname} \n
        Средняя оценка за лекции: {self.average_grade_lect()}"""
        return res



class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.course_attached = []
        
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def __str__(self):
        res = f"""Имя: {self.name} \n 
        Фамилия: {self.surname} \n """
        return res


 
student_1 = Student('Ruoy', 'Eman', 'male')
student_1.courses_in_progress += ['Python', 'Java']
student_2 = Student('Petr', 'Kozlov', 'male')
student_2.courses_in_progress += ['Python', 'Git']


 
lecturer_1 = Lecturer('Ivan', 'Ivanov')
lecturer_1.courses_attached += ['Git', 'Java', 'Python']
lecturer_2 = Lecturer('Alex', 'Sidorov')
lecturer_2.courses_attached += ['Python', 'Git', 'Java']


reviewer_1 = Reviewer('Petr', 'Petrov')
reviewer_1.courses_attached += ['Git', 'Java']
reviewer_2 = Reviewer('Maria', 'Antonova')
reviewer_2.courses_attached += ['Python']

student_1.add_courses('Git')
student_2.add_courses('Java')

student_1.rate_lect(lecturer_1, 'Java', 9)
student_1.rate_lect(lecturer_1, 'Python', 4)
student_1.rate_lect(lecturer_2, 'Python', 10)
student_1.rate_lect(lecturer_2, 'Java', 8)
student_2.rate_lect(lecturer_1, 'Python', 10)
student_2.rate_lect(lecturer_1, 'Git', 9)
student_2.rate_lect(lecturer_2, 'Python', 10)
student_2.rate_lect(lecturer_2, 'Git', 6)

reviewer_1.rate_hw(student_1, 'Java', 8)
reviewer_1.rate_hw(student_1, 'Java', 6)
reviewer_1.rate_hw(student_1, 'Java', 10)
reviewer_1.rate_hw(student_2, 'Git', 10)
reviewer_1.rate_hw(student_2, 'Git', 5)
reviewer_1.rate_hw(student_2, 'Git', 9)
reviewer_2.rate_hw(student_1, 'Python', 10)
reviewer_2.rate_hw(student_1, 'Python', 10)
reviewer_2.rate_hw(student_1, 'Python', 18)
reviewer_2.rate_hw(student_2, 'Python', 7)
reviewer_2.rate_hw(student_2, 'Python', 10)
reviewer_2.rate_hw(student_2, 'Python', 5)


print(student_1)
print("/" * 60)
print(student_2)
print("/" * 60)
print(lecturer_1)
print("/" * 60)
print(lecturer_2)
print("/" * 60)
print(reviewer_1)
print("/" * 60)
print(reviewer_2)
print("/" * 60)

student_1.__lt__(student_2)
lecturer_1.__lt__(lecturer_2)


student_list = [student_1, student_2]
lecturer_list = [lecturer_1, lecturer_2]

def average_students(student_list, course_name):
    res = 0
    count = 0
    for student in student_list:
        for key, value in student.items():
            if key == course_name:
                count += len(value)
                res += sum(value)
    average = res / count
    print(f'Средняя оценка студентов по курсу {course_name}: {round(average, 1)}')

average_students(student_list, 'Python')
average_students(student_list, 'Git')
average_students(student_list, 'Java')

def average_all_lecturers(lecturer_list, course_name):
    res = 0
    count = 0
    for lecture in lecturer_list:
        for key, value in lecture.items():
            if key == course_name:
                count += len(value)
                res += sum(value)
    average = res / count
    print(f'Средняя оценка лекторов по курсу {course_name}: {round(average, 1)}')

average_all_lecturers(lecturer_list, 'Git')
average_all_lecturers(lecturer_list, 'Java')
average_all_lecturers(lecturer_list, 'Python')
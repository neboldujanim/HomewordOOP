class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        print(f"Привет! Меня зовут {self.fullname}. Мне {self.age} лет. Женат/Замужем: {self.is_married}")

class Student(Person):
    def __init__(self, fullname, age, is_married, marks):
        super().__init__(fullname, age, is_married)
        self.marks = marks

    def calculate_average_mark(self):
        total_marks = sum(self.marks.values())
        average_mark = round(total_marks / len(self.marks))
        return average_mark

class Teacher(Person):
    base_salary = 10000

    def __init__(self, fullname, age, is_married, experience):
        super().__init__(fullname, age, is_married)
        self.experience = experience

    def calculate_salary(self):
        base = self.base_salary
        stop = self.experience - 3

        while stop > 0:
            bonus = base * 0.05
            base += bonus
            stop-=1
        return round(base, 1)

def create_students():
    student1 = Student("Тапчанов Актош", 17, False, {"Математика": 2, "Физика": 3, "Информатика": 4})
    student2 = Student("Канчыков Кокмэбек", 16, False, {"Математика": 3, "Физика": 4, "Информатика": 3})
    student3 = Student("Эщекова Шамалгуль", 18, False, {"Математика": 5, "Физика": 5, "Информатика": 5})
    return [student1, student2, student3]


teacher = Teacher("Чылапчинова Шыпыргуль", 35, True, 10)


print(f"Информация о учителе:")
teacher.introduce_myself()
print(f"Опыт работы: {teacher.experience} лет")
print(f"Базовая зарплата: {teacher.base_salary}")
print(f"Зарплата: {teacher.calculate_salary()}")


students = create_students()
print("\nИнформация о студентах:")
for student in students:
    student.introduce_myself()
    print(f"Оценки: {student.marks}")
    print(f"Средняя оценка: {student.calculate_average_mark()}")



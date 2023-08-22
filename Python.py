# 1. Создать класс Person с атрибутами fullname, age, is_married
class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    # 2. Добавить в класс Person метод introduce_myself, который бы распечатывал всю информацию о человеке
    def introduce_myself(self):
        print(f"Full Name: {self.fullname}")
        print(f"Age: {self.age}")
        print(f"Married: {'Yes' if self.is_married else 'No'}")
        print()

# 3. Создать класс Student наследовать его от класса Person и дополнить его атрибутом marks
class Student(Person):
    def __init__(self, fullname, age, is_married, marks):
        super().__init__(fullname, age, is_married)
        self.marks = marks

    # 4. Добавить метод в класс Student, который бы подсчитывал среднюю оценку ученика по всем предметам
    def calculate_average_mark(self):
        return sum(self.marks.values()) / len(self.marks)

# 5. Создать класс Teacher и наследовать его от класса Person, дополнить атрибутом experience.
class Teacher(Person):
    def __init__(self, fullname, age, is_married, experience, base_salary):
        super().__init__(fullname, age, is_married)
        self.experience = experience
        self.base_salary = base_salary

    # 7. Также добавить метод в класс Teacher, который бы считал зарплату
    def calculate_salary(self):
        bonus_percentage = max(0, self.experience - 3) * 0.05
        return self.base_salary * (1 + bonus_percentage)

# 8. Создать объект учителя и распечатать всю информацию о нем и высчитать зарплату
teacher = Teacher("John Doe", 35, True, 7, 50000)
teacher.introduce_myself()
print(f"Calculated Salary: ${teacher.calculate_salary():.2f}")
print()

# 9. Написать функцию create_students
def create_students():
    students = []
    # Создаем 3 объекта ученика и добавляем в список
    student1 = Student("Alice Johnson", 16, False, {"Math": 95, "History": 88, "Science": 92})
    student2 = Student("Bob Smith", 17, False, {"Math": 85, "History": 78, "Science": 80})
    student3 = Student("Eve Williams", 15, False, {"Math": 90, "History": 82, "Science": 88})
    students.extend([student1, student2, student3])
    return students

# 10. Вызвать функцию create_students и распечатать информацию о каждом ученике
students_list = create_students()
for student in students_list:
    student.introduce_myself()
    print(f"Average Mark: {student.calculate_average_mark():.2f}")
    print()
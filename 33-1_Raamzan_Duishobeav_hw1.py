
class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        print(f"Full Name: {self.fullname}")
        print(f"Age: {self.age}")
        print(f"Married: {'Yes' if self.is_married else 'No'}")
        print()

class Student(Person):
    def __init__(self, fullname, age, is_married, marks):
        super().__init__(fullname, age, is_married)
        self.marks = marks

    def calculate_average_mark(self):
        return sum(self.marks.values()) / len(self.marks)

class Teacher(Person):
    def __init__(self, fullname, age, is_married, experience, base_salary):
        super().__init__(fullname, age, is_married)
        self.experience = experience
        self.base_salary = base_salary

    def calculate_salary(self):
        bonus_percentage = max(0, self.experience - 3) * 0.05
        return self.base_salary * (1 + bonus_percentage)

teacher = Teacher("Sadyr Japarov", 35, True, 7, 50000)
teacher.introduce_myself()
print(f"Calculated Salary: ${teacher.calculate_salary():.2f}")
print()

def create_students():
    students = []
    # Создаем 3 объекта ученика и добавляем в список
    student1 = Student("Duishobaev Ramzan", 16, False, {"Math": 95, "History": 88, "Science": 92})
    student2 = Student("Cristiano Ronaldo", 17, False, {"Math": 85, "History": 78, "Science": 80})
    student3 = Student("Lebron James", 15, False, {"Math": 90, "History": 82, "Science": 88})
    students.extend([student1, student2, student3])
    return students

students_list = create_students()
for student in students_list:
    student.introduce_myself()
    print(f"Average Mark: {student.calculate_average_mark():.2f}")
    print()
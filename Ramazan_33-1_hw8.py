with open('results.txt', 'r')as file:
    file.readline()
    data = file.readlines()

students = {}

for i in data:
    name, grade = i.strip().split()
    students[name] = int(grade)


sorted_results = dict(sorted(students.items(), key=lambda x: x[1], reverse=True))


print("Top 3 the best students: ")

for name, grade in list(sorted_results.items())[:3]:
    print(f" {name} - {grade}")


with open('sorted_results.txt', 'w') as file:
    for name, grade in sorted_results.items():
        file.write(f"{name} - {grade}\n")













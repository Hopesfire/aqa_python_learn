from typing import List


class Student:

    def __init__(self, name: str, age: int, grades: List[float]):
        self.name = name
        self.age = age
        self.grades = grades

    # def get_avg_grades(self):
    #     return sum(self.grades) / len(self.grades)


def get_avg_grades(student):
    return sum(student.grades) / len(student.grades)


student1 = Student("Ivan", 20, [5, 4, 5, 3])
student2 = Student("Michael", 19, [4, 3, 5, 4])
student3 = Student("Alex", 21, [3, 2, 3, 3])

# print(student1.get_avg_grades())
# print(student2.get_avg_grades())
# print(student3.get_avg_grades())

print(get_avg_grades(student1))
print(get_avg_grades(student2))
print(get_avg_grades(student3))
print("\n")

student4 = Student("Olga", 22, [5, 5, 4, 5])
student5 = Student("Dmitry", 18, [3, 4, 2, 3])
student6 = Student("Elena", 20, [5, 2, 4, 3])
student7 = Student("Sergey", 21, [5, 3, 4, 4])
student8 = Student("Anna", 19, [5, 5, 5, 5])
student9 = Student("Nikita", 23, [3, 3, 4, 2])
student10 = Student("Victoria", 20, [5, 5, 3, 5])

students = [
    student1,
    student2,
    student3,
    student4,
    student5,
    student6,
    student7,
    student8,
    student9,
    student10,
]

for stud in students:
    avg = get_avg_grades(stud)
    if avg > 4.1:
        print(f"{stud.name}: {avg}")

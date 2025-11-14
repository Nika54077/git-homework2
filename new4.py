class Student:
    def __init__(self, name, age, subjects):
        self.name = name
        self.age = age
        self.subjects = subjects

    def add_subject(self, subject):
        self.subjects.append(subject)

    def get_info(self):
        return f"{self.name} is {self.age} and studies: {','.join(self.subjects)}"
students = []

a = Student("Alice", 15, ["Math", "Science"])
b = Student("Bob", 16, ["History", "Physics"])
c = Student("Carol", 14, ["English", "Biology"])
d = Student("Dave", 17, ["Chemistry", "Math"])
students.append(a)
students.append(b)
students.append(c)
students.append(d)

remove_student = input("Enter name: ")
for s in students:
    if s.name == remove_student:
        students.remove(s)
        print(remove_student, "has been deleted.")
        break
else:
    print("Student not found.")

print("Number of students:", len(students))






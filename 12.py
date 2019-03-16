class Students:
    #name = 'Zack'
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Students.count += 1

    def dispStudents(self):
        print("Name: ", self.name, " Age: ", self.age)


stu1 = Students("Zack", 28)
stu2 = Students("Bucky", 32)

stu1.dispStudents()
stu2.dispStudents()
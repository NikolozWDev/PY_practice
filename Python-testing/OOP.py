# OOP
class Server:
    def __init__(self, model, id, estimate):
        self.model = model
        self.id = id
        self.estimate = estimate
    def working(self):
        return f'{self.model} is working'
    def stoped(self):
        return f'{self.model} is stopped working'
    def describe(self):
        return f'{self.model}, {self.id}, {self.estimate}'


# create
ser1 = Server('server_python', 8, True)
ser2 = Server('server2_python', 10, False)


print(ser1.model, ser1.id, ser1.estimate)
print(ser2.model, ser2.id, ser2.estimate)

print(ser1.working())
print(ser2.describe())


print('__________________________________')
# class variables
class Student:
    learn_start = 2025
    students_amount = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.students_amount += 1
    def describe(self):
        return f'name: {self.name}, age: {self.age}'

student1 = Student('giorgi', 19)
student2 = Student('levani', 21)
student3 = Student('saba', 19)


print(f'learn started: {Student.learn_start}')
print(f'students amount: {Student.students_amount}')
print(student1.describe())
print(student2.describe())
print(student3.describe())
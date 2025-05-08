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



print('__________________________________')
# inheritance
class MainServer:
    def __init__(self, name, function):
        self.name = name
        self.function = function
    def server_region(self):
        return f'this server by [{self.name}][{self.function}]'

class ServerChild1(MainServer):
    def about(self):
        return f'{self.name} by new class 1'

class ServerChild2(MainServer):
    def about(self):
        return f'{self.name} by new class 2'    


ser3 = ServerChild1('python_server3', True)
ser4 = ServerChild2('python_server4', False)

print(ser3.server_region(), ser3.about())
print(ser4.server_region(), ser4.about())



print('__________________________________')
# multiple inheritance
class Animal:
    def __init__(self, name):
        self.name = name
    def description(self):
        return f'animal: {self.name}'

class Wild(Animal):
    def hunt(self):
        return f'{self.name} can hunting'

class UnWild(Animal):
    def un_hunt(self):
        return f'{self.name} cant hunting!'


class Rabbit(UnWild):
    pass
class Wolf(Wild):
    pass
class Fish(Wild, UnWild):
    pass


rabbit = Rabbit('rabbit')
wolf = Wolf('wolf')
fish = Fish('fish')


print(rabbit.description())
print(wolf.description())
print(fish.description())

print(rabbit.un_hunt())
print(wolf.hunt())
print(fish.hunt(), fish.un_hunt())



print('__________________________________')
# super()
class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius
    def describe(self):
        return f'color: {self.color}; is_filled: {self.is_filled}; radius: {self.radius}'

class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width
    def describe(self):
        return f'color: {self.color}; is_filled: {self.is_filled}; radius: {self.width}'

class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height
    def describe(self):
        return f'color: {self.color}; is_filled: {self.is_filled}; radius: {self.width}; height: {self.height}'


circle = Circle('red', True, 20)
square = Square('blue', False, 10)
triangle = Triangle('green', True, 10, 5)


print(circle.describe())
print(square.describe())
print(triangle.describe())



print('__________________________________')
# polymorphism
class MainArea:
    def area(self):
        pass

class Triangle(MainArea):
    def __init__(self, base, width):
        self.base = base
        self.width = width
    def area(self):
        return self.base * self.width * 0.5

class Square(MainArea):
    def __init__(self, width):
        self.width = width
    def area(self):
        return self.width ** 2

class Circle(MainArea):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2

class Piz(Circle):
    def __init__(self, radius, pepe):
        super().__init__(radius)
        self.pepe = pepe


shapes = [Triangle(5, 6), Square(4), Circle(8), Piz(10, 15)]
for i in shapes:
    print(f'area: {i.area()}cm²')



print('__________________________________')
# Duck typing
class MainLanguage:
    main = 'English'

class France(MainLanguage):
    def speak(self):
        return 'France'

class Georgia(MainLanguage):
    def speak(self):
        return 'Georgia'
    
class Car(MainLanguage):
    main = 'Car'
    def speak(self):
        return 'Horned car'
    
languages = [France(), Georgia(), Car()]
for i in languages:
    print(f'Language: {i.speak()}')
# this is my first python code
print('Hello World!')
print('I need python for back-end')


# this is strings
my_name = 'Nikoloz'
first_name = 'Jackson'
my_email = 'fake@gmail.com'
print(my_name)
print(f'Hello {first_name}' + ' world!')
print(f'your email is: {my_email}')


# integers and floats
my_age = 25
my_weight = 60.5
my_height = 1.75
print(f'my age is {my_age}, weight is {my_weight}, and my height is {my_height}')


# boolean
is_student = True
is_employed = False
print(f'you are student: {is_student} and you are employed: {is_employed}')


# typeCasting
name = 'ragaca'
age = 26
name_weight = 53.3
is_student = False
print(type(name), type(age), type(name_weight), type(is_student))


is_student = str(is_student)
print(type(is_student))
name_weight = int(name_weight)
print(name_weight)
age = float(age)
print(age)
name = bool(name)
print(name)


# if statements
age = int(input('Enter your age: '))
if age >= 18:
    print('you are adult')
elif age < 0:
    print('you are not born yet')
elif age > 100:
    print('you are too old')
else:
    print('you are not adult')


meal = input('do you like food ? (Y/N): ')
if meal == 'Y':
    print('good')
elif meal == 'N':
    print('bad')
else:
    print('wrong input. please write Y or N')


name_you = input('Enter your name: ')
if name_you == '':
    print('?')
else:
    print(f'hello {name_you}')



# arithmetic, Math
visitor = 0
visitor = visitor + 1
visitor = visitor - 2
visitor = visitor * (-3)
visitor = visitor / 2
visitor = int(visitor ** 4)
remainder = visitor % 2
print(visitor)
print(remainder)

x = 3.53
y = -4
z = 42
result1 = round(x)
result2 = abs(y)
result3 = pow(z, 2)
print(result1, result2, result3)
print(max(x, y, z), min(x, y, z))
import math
print(math.pi, math.e)
print(math.sqrt(64), math.ceil(3.2), math.floor(3.9))

# exercise
r = float(input('r: '))
l = 2 * math.pi * r
print(f'circle length is: {round(l)}')

# exercise
rr = float(input('r: '))
areaa = math.pi * (pow(rr, 2))
print(f'circle area is: {round(areaa)}')

# exercise
a = float(input('a: '))
b = float(input('b: '))
c = math.sqrt(pow(a, 2) + pow(b, 2))
print(f'c is: {c}')



# user input()
server = input('Enter your server: ')
code = int(input('select code: '))
code = round((code * 3) / 5)
print(f'your server is: {server} and your code is: {code}')

length = float(input('write length: '))
width = float(input('write width: '))
area = width * length
print(f'area is: {area}cm²')

food = input('order food: ')
price = float(input('price: '))
quantity = int(input('how many: '))
total_price = price * quantity
print(f'your order is: {food}, price is {price}, quantity is: {quantity}, and total price is: ${total_price}')


# little game (story game)
things1 = input('what do you want: ')
things2 = input('your table was: ')
human = input('who: ')
mood1 = input('how was he: ')
mood2 = input('how was I: ')
print(f'I want {things1}. but my table was {things2}. {human} was {mood1}. I was {mood2}')
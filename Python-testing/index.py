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


# user input()
server = input('Enter your server: ')
code = int(input('select code: '))
code = int((code * 3) / 5)
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
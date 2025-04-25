# format specifiers
num1 = 5.41233
num2 = -34.32
num3 = 23
print('👇')
print(f'{num1:.2f}')
print(f'{num2:.2f}')
print(f'{num3:.2f}')

print('👇')
print(f'{num1:<10}')
print(f'{num2:<10}')
print(f'{num3:<10}')

print('👇')
print(f'{num1:>10}')
print(f'{num2:>10}')
print(f'{num3:>10}')

print('👇')
print(f'{num1:^10}')
print(f'{num2:^10}')
print(f'{num3:^10}')

print('👇')
print(f'{num1:+}')
print(f'{num2:+}')
print(f'{num3:+}')

print('👇')
print(f'{num1:,}')
print(f'{num2:,}')
print(f'{num3:,}')

# task
num_pro = 5400.245223
variable = f'{num_pro:+,.2f}'
result = f'{variable:^20}'
print(result)



# while loop
i = 1
while i <= 10:
    print(i)
    i += 1
print('done')


name = input('Enter your name: ')
while name == "":
    print('please enter your name')
    name = input('Enter your name: ')
print(f'hello {name}')


age = input('( to quit write q ) tell us your age: ')
if age == 'q':
    print('goodbye')
else:
    while not age.isdigit() or int(age) < 0 or int(age) > 100:
        while age == 'q':
            print('goodbye')
            age = 's'
            break
    if age != 's':
        if len(age) == 0:
            age = input('(to quit write q) tell us your age: ')
        else:
            print(f'you are not {age} years old. write between (1 / 100)')
            age = input('(to quit write q) tell us your age: ')
    age = int(age)
    if age >= 18:
        print('you are adult. you can join our community')
    else:
        print('you are not adult. you can not join our community')




# compount interest calculator
while True:
    principal = input('Enter principal amount: ')
    if principal == '' or float(principal) <= 0:
        print('principal amount must be greater than 0')
    else:
        break
num_principal = float(principal)

while True:
    rate = input('Enter interest rate: ')
    if rate == '' or int(rate) <= 0:
        print('interest rate must be greater than 0')
    else:
        break
num_rate = int(rate)

while True:
    time = input('Enter time in years: ')
    if time == '' or int(time) <= 0:
        print('time must be greater than 0')
    else:
        break
num_time = int(time)

total = num_principal * pow((1 + (num_rate / 100)), num_time)
print(f'Total amount after {num_time} years is: {total}')
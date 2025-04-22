# mini calculator app
print('welcome mini calculator app')
operator = input('enter operator (+, -, x, :) ')

if operator == '+' or operator == '-' or operator == 'x' or operator == ':':
    num1 = float(input('enter number1: '))
    num2 = float(input('enter number2: '))

    if operator == '+':
        print(num1 + num2)
    elif operator == '-':
        print(num1 - num2)
    elif operator == 'x':
        print(num1 * num2)
    elif operator == ':':
        print(num1 / num2)
else:
    print(f'operator {operator} is not valid')



# weight app
print('welcome weight app')
weight = float(input('Enter your weight: '))
unit = input('Enter you unit (kg / lb): ')

if unit == 'kg':
    weight = weight * 2.2
    print(f'your weight is {weight} lbs')
elif unit == 'lb':
    weight = weight / 2.2
    print(f'your weight is {weight} lbs')
else:
    print(f'unit {unit} is not valid')